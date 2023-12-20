from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_home', views.user_home, name='user_home'),
    path('user_profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('SignOut', views.SignOut, name='SignOut'),
    path('company_register', views.company_register, name='company_register'),
    path('company_login', views.company_login, name='company_login'),
    path('company_home', views.company_home, name='company_home'),
    path('company_profile/<int:pk>/', views.company_profile, name='company_profile'),
    path('add_job_vacancy', views.add_job_vacancy, name='add_job_vacancy'),
    path('view_my_job_postings', views.view_my_job_postings, name='view_my_job_postings'),
    path('SignOut2', views.SignOut2, name='SignOut2'),
    path('mainhome', views.mainhome, name='mainhome'),
    path('mainlogin', views.mainlogin, name='mainlogin'),
    path('admin_register', views.admin_register, name='admin_register'),
    path('SignOut3', views.SignOut3, name='SignOut3'),
    path('job_providers', views.job_providers, name='job_providers'),
    path('job_seekers', views.job_seekers, name='job_seekers'),
    path('job_postings', views.job_postings, name='job_postings'),
    path('posting_prediction/<int:pk>/', views.posting_prediction, name='posting_prediction'),
    path('view_jobposting', views.view_jobposting, name='view_jobposting'),
    path('view_posting_single/<int:pk>/', views.view_posting_single, name='view_posting_single'),
    path('view_company_profile/<int:companyid>/', views.view_company_profile, name='view_company_profile'),
    path('apply/<int:pk>/', views.apply, name='apply'),
    path('my_applications', views.my_applications, name='my_applications'),
    path('applications', views.applications, name='applications'),
    path('update_application/<int:pk>/', views.update_application, name='update_application'),
    path('accept_application/<int:pk>/', views.accept_application, name='accept_application'),
    path('reject_application/<int:pk>/', views.reject_application, name='reject_application'),
    path('view_applicant/<int:pk>/', views.view_applicant, name='view_applicant'),
    path('remove_company/<int:pk>/', views.remove_company, name='remove_company'),


]