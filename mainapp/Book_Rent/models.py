from django.db import models
from django.contrib.auth.models import User

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
    



    





