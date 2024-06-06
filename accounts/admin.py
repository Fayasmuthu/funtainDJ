from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from import_export.admin import ImportExportActionModelAdmin

from accounts.models import User

# Register your models here.
# admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username",'first_name','email', "is_active","is_staff"]
#     list_filter = ["email", "username"]
#     # search_fields = ["order_id", "user__username"]
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Username already exists")


class MyUserAdmin(UserAdmin, ImportExportActionModelAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    ordering = ("username",)
    list_display = ("username", "is_active", "last_login", "date_joined", "is_staff", "is_superuser")
    list_display_links = ("username",)
    readonly_fields = ("last_login", "date_joined", "pk")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined", "last_login")
    fieldsets = (
        ("Basic Info", {"fields": ("username", "password", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Groups", {"fields": ("groups",)}),
        ("other", {"fields": ("is_customer","phone_number","photo","first_name")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, MyUserAdmin)
