from django.contrib import admin
from .models import RegularUser
from .forms import RegularUserChangeForm, RegularUserCreationForm


# Низкоуровневый админский интерфейс
from django.contrib.auth.admin import UserAdmin 
# Register your models here.


# Создаем свой интерфейс по взаимодействию с моделью на основе UserAdmin
class RegularUserAdmin(UserAdmin):
    add_form = RegularUserCreationForm
    form = RegularUserChangeForm
    model = RegularUser


# Регистрируем интерфейс в панель
admin.site.register(RegularUser, RegularUserAdmin)

