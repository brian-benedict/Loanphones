from django.db import models

# Create your models here.
from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phone_images/')
    
    def __str__(self):
        return f"{self.brand} {self.model_name}"

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.full_name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='phones/static/product_images/')
#     camera = models.CharField(max_length=100)
#     storage_ram = models.CharField(max_length=100)
#     battery = models.CharField(max_length=100)
#     android_version = models.CharField(max_length=100)
#     sim_type = models.CharField(max_length=100)
#     screen = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Add price field
#     initial_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Initial amount for loan

#     def __str__(self):
#         return self.name



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/product_images/')
    camera = models.CharField(max_length=100)
    storage_ram = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    android_version = models.CharField(max_length=100)
    sim_type = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"





# In models.py
# from django.db import models

# class LoanApplication(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     # amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # Add more fields as needed

#     def __str__(self):
#         return self.full_name

from django.db import models

class PaymentApplication(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    AGE_RANGE_CHOICES = [
        ('18-25', '18-25'),
        ('26-35', '26-35'),
        ('36+', '36+'),
    ]
    age_range = models.CharField(max_length=10, choices=AGE_RANGE_CHOICES)
    PAYMENT_CHOICES = [
        ('cash', 'Cash Payment'),
        ('loan', 'Loan'),
    ]
    payment_choice = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
