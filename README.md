Finance Data Processing & Access Control Backend

📌 Project Overview

This project is a backend system for managing financial records with role-based access control. It allows users to create, view, update, and analyze financial data through secure APIs.
The system is designed to demonstrate backend architecture, API design, authentication, authorization, and data processing logic.

🚀 Features

  🔐 Authentication
      JWT-based authentication
      Access & Refresh tokens
      Secure API access
      
  👥 User Roles & Permissions
  
      Admin
        Full access (Create, Update, Delete)
      Analyst
        View records & dashboard insights
      Viewer
        View-only access
        
  💰 Financial Records Management
  
        Create financial records
        View all records
        Retrieve single record
        Update records
        Delete records

  Each record includes:

      Amount
      Type (Income / Expense)
      Category
      Date
      Notes
      
  🔍 Filtering Support
  
        Filter by type (income / expense)
        Filter by category
        Filter by date range

        Example:
        
            /api/finance/records/?type=income
            /api/finance/records/?category=Food
            /api/finance/records/?start_date=2026-04-01&end_date=2026-04-30
            
  📊 Dashboard Analytics
      Provides aggregated financial insights:

      Total Income
      Total Expense
      Net Balance
      Category-wise breakdown
      Recent transactions
      
  🛠 Tech Stack
  
      Python
      Django
      Django REST Framework
      Simple JWT
      SQLite3 
      
🌐 API Endpoints

    🔐 Auth APIs
    
          Method	Endpoint
          POST	/api/token/
          POST	/api/token/refresh/
          
    💰 Finance APIs
    
          Method	Endpoint	                  Description
          POST	  /api/finance/records/	      Create record (Admin)
          GET	    /api/finance/records/	      Get all records
          GET	    /api/finance/records/<id>/	Get single record
          PUT	    /api/finance/records/<id>/	Update record (Admin)
          DELETE	/api/finance/records/<id>/	Delete record (Admin)
          
    📊 Dashboard API
    
          Method	Endpoint
          GET	    /api/finance/dashboard/
          
🔧 Setup Instructions

# Clone repository
git clone <your-repo-link>

# Navigate to project
cd finance_backend

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

  🔐 Authentication Usage

        Get token: POST /api/token/
        Use in headers:
        Authorization: Bearer <access_token>
        
  🧠 Assumptions
  
        Each user can access only their own financial records
        Categories are user-defined (no fixed list)
        Admin role is required for modifying data
        SQLite is used for simplicity
        
  ⚠️ Error Handling
  
        400 → Bad Request
        401 → Unauthorized
        403 → Forbidden
        404 → Not Found
        
  ✨ Future Enhancements
  
      Pagination support
      Export data to CSV
      Advanced analytics (monthly trends)
      Role management UI
      API documentation
      
📌 Conclusion

This project demonstrates backend development skills including API design, authentication, role-based access control, data filtering, and aggregation. It reflects a real-world approach to building scalable and maintainable backend systems.
