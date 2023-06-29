# Register your models here.
from django.contrib import admin
from .models import Post, UserType, UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher_name', 'publish_date')
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('مجوزها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخچه', {'fields': ('date_joined', 'last_login')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_staff')
    list_filter = ('is_staff', 'role', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

User = settings.AUTH_USER_MODEL
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
