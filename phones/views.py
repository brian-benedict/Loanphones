from Loanphones import settings
from .forms import ProductForm, CustomerForm
from django.shortcuts import render, redirect
from .models import Phone, Customer, Product, PaymentApplication
from django.contrib import messages


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def phone_details(request, phone_id):
    products = Product.objects.get(id=phone_id)
    return render(request, 'phone_details.html', {'products': products})

def contact_us(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'contact.html', {'form': form})

def about_us(request):
    return render(request, 'about.html')



def product_registration(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = ProductForm()
    return render(request, 'product_registration.html', {'form': form})




# In views.py
# from django.shortcuts import render, redirect
from .forms import LoanApplicationForm

# def loan_application_view(request):
#     if request.method == 'POST':
#         form = LoanApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('loan_application_success')  # Redirect to a success page
#     else:
#         form = LoanApplicationForm()
#     return render(request, 'loan_application_form.html', {'form': form})


# from django.shortcuts import render
# from .models import Product

# def loan_application(request, product_id):
#     # Retrieve the product object
#     product = Product.objects.get(pk=product_id)
#     if request.method == 'POST':
#         form = LoanApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('loan_application_success')  # Redirect to a success page
#     else:
#         form = LoanApplicationForm()
#     # Pass the product and its initial loan amount to the template
#     context = {
#         'form': form,
#         'product': product,
#         'initial_loan_amount': product.initial_loan_amount,
#     }

#     return render(request, 'loan_application.html', context)


def loan_application_success(request):
    return render(request, 'loan_application_success.html')






# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Product
from .forms import LoanApplicationForm

def payment_application(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            # Get cleaned form data
            cleaned_data = form.cleaned_data

            # Format form data into email message
            email_message = f"Product: {product.name}\n\n"
            for field_name, field_value in cleaned_data.items():
                email_message += f"{field_name.capitalize()}: {field_value}\n"

            # Send email
            subject = 'New Payment Application Submission'
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_email = 'gorasha6@gmail.com'
            send_mail(subject, email_message, sender_email, [recipient_email])

            try:
                send_mail(subject, email_message, sender_email, recipient_email)
                messages.success(request, 'Email sent successfully!')
            except Exception as e:
                messages.error(request, 'Failed to send email: {}'.format(str(e)))

            return redirect('loan_application_success')  # Redirect to a success page

    else:
        form = LoanApplicationForm()

    context = {
        'form': form,
        'product': product,
        'initial_loan_amount': product.initial_loan_amount,
    }    
    return render(request, 'payment_application.html', context)

