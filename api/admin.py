from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Carts)
admin.site.register(PayMethod)
admin.site.register(Adress)
admin.site.register(Categories)
admin.site.register(Colors)
admin.site.register(Sizes)
admin.site.register(Images)
admin.site.register(Product)
admin.site.register(Reviews)