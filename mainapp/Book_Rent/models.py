from django.db import models

class Sell_model(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    





