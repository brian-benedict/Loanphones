from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('phone/<int:phone_id>/', views.phone_details, name='phone_details'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    # path('product-registration/', views.product_registration, name='product_registration'),
    # path('apply-for-loan/', views.loan_application_view, name='apply_for_loan'),
    # path('loan-application/<int:product_id>/', views.loan_application, name='loan_application'),
    path('loan-application-success/', views.loan_application_success, name='loan_application_success'),
    path('payment_application/<int:product_id>/',views.payment_application, name ='payment_application'),
    # path('loan-application-success/', views.loan_application_success_view, name='loan_application_success'),
    # Additional paths can be added here for more views
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admins/', views.admin_home, name='admin_home'),
    path('admins/product-registration/', views.product_registration, name='product_registration'),
    path('admins/download-data/', views.download_data, name='download_data'),
    path('products/', views.product_list, name='product_list'),
    # Other URL patterns
    path('product_edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('product_delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('product_image_delete/<int:image_id>/', views.product_image_delete, name='product_image_delete'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),

]