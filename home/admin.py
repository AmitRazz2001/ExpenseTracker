from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile,Expense)
class ExpenseAdmin(admin.ModelAdmin):
    class Meta:
        models = Profile, Expense
        fields = '__all__'