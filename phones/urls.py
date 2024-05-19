from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('phone/<int:phone_id>/', views.phone_details, name='phone_details'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    path('product-registration/', views.product_registration, name='product_registration'),
    # path('apply-for-loan/', views.loan_application_view, name='apply_for_loan'),
    # path('loan-application/<int:product_id>/', views.loan_application, name='loan_application'),
    path('loan-application-success/', views.loan_application_success, name='loan_application_success'),
    path('payment_application/<int:product_id>/',views.payment_application, name ='payment_application')
    # path('loan-application-success/', views.loan_application_success_view, name='loan_application_success'),
    # Additional paths can be added here for more views
]