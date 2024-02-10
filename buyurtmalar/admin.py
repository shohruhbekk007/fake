from django.contrib import admin
from .models import Contact, User, Product
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin

@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


admin.site.register(User)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ExportMixin):
    list_display = ('cotegory','buyurtmalar', 'price')

class CustomUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'user_admin', 'first_name', 'last_name', 'country', 'photo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'password1', 'password2'),
            },
        ),
    )
    form = CustomUserCreationForm
    list_display = ('id', 'email', 'user_admin', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    ordering = ('id',)
