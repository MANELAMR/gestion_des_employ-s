from django.contrib import admin
from django.contrib.auth.models import User
from .models import Employer , Administrateur
# Register your models here.
admin.site.register(Employer),
admin.site.register(Administrateur)