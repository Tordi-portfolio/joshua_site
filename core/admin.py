from django.contrib import admin
from .models import PasswordReset
from .models import Item

admin.site.register(Item)
admin.site.register(PasswordReset)