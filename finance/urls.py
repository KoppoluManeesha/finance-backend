from django.urls import path
from .views import FinancialRecordListCreateView, FinancialRecordDetailView, DashboardView

urlpatterns = [
    path('records/', FinancialRecordListCreateView.as_view(), name='record-list'),
    path('records/<int:pk>/', FinancialRecordDetailView.as_view(), name='record-detail'),
    path('dashboard/', DashboardView.as_view()),
]