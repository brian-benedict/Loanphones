from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone_number', 'address']



from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'camera', 'storage_ram', 'battery', 'android_version', 'sim_type', 'screen']


# In forms.py
# from django import forms
# from .models import LoanApplication

# class LoanApplicationForm(forms.ModelForm):
#     class Meta:
#         model = LoanApplication
#         fields = ['full_name', 'email', 'phone_number']  # Add more fields as needed

from django import forms
from .models import PaymentApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = PaymentApplication
        fields = ['firstname', 'lastname', 'id_number', 'phone1', 'phone2', 'region', 'district', 'street', 'gender', 'age_range', 'payment_choice']

