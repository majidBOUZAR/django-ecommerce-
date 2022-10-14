from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (
    ('FL', 'Farine_Semoul'),
    ('P', 'Pates'),
    ('G', 'Gateaux'),
    ('S', 'Sucrerie'),
    ('OF', 'Graines'),
    ('L', 'Laitiers'),
    ('B', 'Boisson'),
    ('PFM', 'Produit_Fait_Maison'),
   
    ('CM', 'Compliment Alimentaire'),
)

FEATURED_CATEGORY_CHOICES = (
    
    ('FL', 'Farine_Semoul'),
    ('P', 'Pates'),
    ('G', 'Gateaux'),
    ('S', 'Sucrerie'),
    ('OF', 'Graines'),
    ('L', 'Laitiers'),
    ('B', 'Boisson'),
    ('PFM', 'Produit_Fait_Maison'),
   
    ('CM', 'Compliment_Alimentaire'),
)

CATEGORY_CHOICES_MAP = {
    'Farine_Semoul': 'FL',
    'Pates': 'P',
    'Gateaux': 'G',
    'Sucrerie': 'S',
    'Graines': 'OF',
    'Laitiers': 'L',
    'Boisson': 'B',
    'Produit_Fait_Maison': 'PFM',
  
    'Compliment_Alimentaire': 'CM',
}

class Product(models.Model):
    test={('available','available'),
       ('sold','sold')  }
    title = models.CharField(max_length=200)

    image1 = models.ImageField(upload_to="app/images/")
    image2 = models.ImageField(upload_to="app/images/", null=True, blank=True)
    image3 = models.ImageField(upload_to="app/images/", null=True, blank=True)
    image4 = models.ImageField(upload_to="app/images/", null=True, blank=True)
    image5 = models.ImageField(upload_to="app/images/", null=True, blank=True)

    shortinfo = models.TextField(default='NA')
    description = models.TextField(default='NA')
    weight = models.CharField(blank=True,null=True, max_length=10)
    price = models.FloatField()
    discounted_price = models.FloatField(null=True, blank=True)
    fav_count = models.IntegerField(null=True, blank=True)
    latest = models.DateField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    quantity1= models.CharField(choices=test,max_length=10,default='available') 

    def __str__(self):
        return self.title
        


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = 'customer' ,null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        total_with_shipping = total + 200.0
        dinars_total= total_with_shipping/145.632
        return total, total_with_shipping,dinars_total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

  


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        if self.product.discounted_price is not None:
            total = (self.product.price - self.product.discounted_price) * self.quantity
        else:
            total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=17)

    def __str__(self):
        return str(self.address)


