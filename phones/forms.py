from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone_number', 'address']



from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'camera', 'storage_ram', 'battery', 'android_version', 'sim_type', 'screen', 'price', 'initial_loan_amount']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

ProductImageFormSet = forms.inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=3, can_delete=True)


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

    widgets = {
        'phone2': forms.TextInput(attrs={'required': False}),
    }

    def __init__(self, *args, **kwargs):
        super(LoanApplicationForm, self).__init__(*args, **kwargs)
        self.fields['phone2'].required = False

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 4}))

from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'aria-label': 'Your Email',
            'required': 'required'
        })
    )
