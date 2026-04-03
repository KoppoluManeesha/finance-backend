from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from django.db.models import Sum

from .models import FinancialRecord
from .serializers import FinancialRecordSerializer

from users.permissions import IsAdmin
from django.utils.decorators import method_decorator


# =========================
# LIST + CREATE VIEW
# =========================
class FinancialRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = FinancialRecord.objects.filter(
            user=self.request.user
        ).order_by('-date')

        # Filters
        record_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if record_type:
            queryset = queryset.filter(type=record_type)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

    def perform_create(self, serializer):
        # Only admin can create
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admin can create records")

        serializer.save(user=self.request.user)


# =========================
# DETAIL VIEW
# =========================
class FinancialRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure user only accesses their own records
        return FinancialRecord.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  # all roles can view
        return [IsAuthenticated(), IsAdmin()]  # only admin can modify/delete


# =========================
# DASHBOARD VIEW
# =========================
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        records = FinancialRecord.objects.filter(user=user)

        # Total Income
        total_income = records.filter(type='income').aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Total Expense
        total_expense = records.filter(type='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0

        # Net Balance
        net_balance = total_income - total_expense

        # Category Breakdown
        category_data = records.values('category').annotate(
            total=Sum('amount')
        )

        # Recent Transactions
        recent_transactions = records.order_by('-date')[:5]

        return Response({
            "total_income": float(total_income),
            "total_expense": float(total_expense),
            "net_balance": float(net_balance),
            "category_breakdown": list(category_data),
            "recent_transactions": [
                {
                    "id": r.id,
                    "amount": float(r.amount),
                    "type": r.type,
                    "category": r.category,
                    "date": r.date,
                    "notes": r.notes
                } for r in recent_transactions
            ]
        })