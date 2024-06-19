from Loanphones import settings
from .forms import ProductForm, CustomerForm
from django.shortcuts import render, redirect
from .models import Phone, Customer, Product, PaymentApplication
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import ProductForm, ProductImageFormSet
from .models import Product


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect




from django.http import HttpResponse
import csv

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



# def product_registration(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Redirect to home page after successful registration
#     else:
#         form = ProductForm()
#     return render(request, 'product_registration.html', {'form': form})





# @login_required
# def product_registration(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_home')  # Redirect to admin home after successful registration
#     else:
#         form = ProductForm()
#     return render(request, 'product_registration.html', {'form': form})

# from django.contrib.auth.decorators import login_required
# from .forms import ProductForm, ProductImageFormSet
# from .models import Product

# @login_required
# def product_registration(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         formset = ProductImageFormSet(request.POST, request.FILES, instance=Product())
#         if form.is_valid() and formset.is_valid():
#             product = form.save()
#             formset.instance = product
#             formset.save()
#             return redirect('admin_home')  # Redirect to admin home after successful registration
#     else:
#         form = ProductForm()
#         formset = ProductImageFormSet(instance=Product())
#     return render(request, 'admin/product_registration.html', {'form': form, 'formset': formset})




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, ProductImageFormSet
from .models import Product, ProductImage

@login_required
def product_registration(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Handle additional images
            additional_images = request.FILES.getlist('additional_images')
            for image in additional_images:
                ProductImage.objects.create(product=product, image=image)
            return redirect('admin_home')  # Redirect to admin home after successful registration
    else:
        form = ProductForm()
    return render(request, 'admin/product_registration.html', {'form': form})






@login_required
def download_data(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="payment_applications.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow([
        'First Name', 'Last Name', 'ID Number', 'Phone 1', 'Phone 2', 
        'Region', 'District', 'Street', 'Gender', 'Age Range', 'Payment Choice'
    ])

    # Write data rows
    applications = PaymentApplication.objects.all().values_list(
        'firstname', 'lastname', 'id_number', 'phone1', 'phone2', 
        'region', 'district', 'street', 'gender', 'age_range', 'payment_choice'
    )
    for application in applications:
        writer.writerow(application)

    return response





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






from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Product, PaymentApplication
from .forms import LoanApplicationForm

def payment_application(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            # Save the form data to the PaymentApplication model
            # payment_application = form.save()
            form.save()

            # Format form data into email message
            email_message = f"Product: {product.name}\n\n"
            for field_name, field_value in form.cleaned_data.items():
                email_message += f"{field_name.capitalize()}: {field_value}\n"

            # Send email
            subject = 'New Payment Application Submission'
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_email = 'brian.benedict@gretsauniversity.ac.ke'
            try:
                send_mail(subject, email_message, sender_email, [recipient_email])
                messages.success(request, 'Email sent successfully!')
            except Exception as e:
                messages.error(request, 'Failed to send email: {}'.format(str(e)))

            return redirect('home')  # Redirect to a success page

    else:
        form = LoanApplicationForm()

    context = {
        'form': form,
        'product': product,
        'initial_loan_amount': product.initial_loan_amount,
    }    
    return render(request, 'payment_application.html', context)







# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from .models import Product
# from .forms import LoanApplicationForm

# def payment_application(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     if request.method == 'POST':
#         form = LoanApplicationForm(request.POST)
#         if form.is_valid():
#             # Get cleaned form data
#             cleaned_data = form.cleaned_data
#             payment_application = form.save()

#             # Format form data into email message
#             email_message = f"Product: {product.name}\n\n"
#             for field_name, field_value in cleaned_data.items():
#                 email_message += f"{field_name.capitalize()}: {field_value}\n"

#             # Send email
#             subject = 'New Payment Application Submission'
#             sender_email = settings.DEFAULT_FROM_EMAIL
#             recipient_email = 'brian.benedict@gretsauniversity.ac.ke'
#             send_mail(subject, email_message, sender_email, [recipient_email])

#             try:
#                 send_mail(subject, email_message, sender_email, recipient_email)
#                 messages.success(request, 'Email sent successfully!')
#             except Exception as e:
#                 messages.error(request, 'Failed to send email: {}'.format(str(e)))

#             return redirect('loan_application_success')  # Redirect to a success page

#     else:
#         form = LoanApplicationForm()

#     context = {
#         'form': form,
#         'product': product,
#         'initial_loan_amount': product.initial_loan_amount,
#     }    
#     return render(request, 'payment_application.html', context)




@login_required
def admin_home(request):
    products = Product.objects.all()
    return render(request, 'admin/admin_home.html', {'products': products})






def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, ProductImage
from .forms import ProductForm, ProductImageFormSet

@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductImageFormSet(request.POST, request.FILES, instance=product)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_home')  # Redirect to admin home after successful edit
    else:
        form = ProductForm(instance=product)
        formset = ProductImageFormSet(instance=product)
    return render(request, 'admin/product_edit.html', {'form': form, 'formset': formset, 'product': product})

@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_home')
    return render(request, 'admin/product_delete.html', {'product': product})











from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
