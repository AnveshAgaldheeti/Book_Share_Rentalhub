from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Sell_model(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    date=models.DateField(auto_now_add=True)
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE, editable=False)
    categories=models.ForeignKey(Category,on_delete=models.CASCADE,default=7)
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def total_cost(self):
        return sum(item.total_price() for item in self.cartitems.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cartitems', on_delete=models.CASCADE)
    sell = models.ForeignKey(Sell_model, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.sell.title}'

    def total_price(self):
        return self.quantity * self.sell.price
    



    





