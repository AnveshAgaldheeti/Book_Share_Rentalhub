from django.contrib import admin
from .models import Sell_model,Category


admin.site.register(Category)

class sell_admin(admin.ModelAdmin):
    list_display=['title','author','price','uploaded_by','categories']
    list_filter=['categories','price']
    search_fields=['title','author','price']
admin.site.register(Sell_model,sell_admin)
