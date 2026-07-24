from django.contrib import admin
from .models import User, UserProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'user_type', 'is_active', 'created_at']
    list_filter = ['user_type', 'is_active', 'created_at']
    search_fields = ['email', 'username']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'city']
    search_fields = ['user__email']
