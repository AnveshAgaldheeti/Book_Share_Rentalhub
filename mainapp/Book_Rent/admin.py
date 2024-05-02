from django.contrib import admin
from .models import Sell_model

# admin.site.register(Sell_model)

class sell_admin(admin.ModelAdmin):
    list_display='__all__'
admin.site.register(Sell_model,)
