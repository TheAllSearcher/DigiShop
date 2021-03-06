from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from .models import User, Shop, Address, Email
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'mobile','is_staff')
    fieldsets = [('Users', {'fields': ['first_name', 'last_name', 'email', 'mobile', 'image']}),
                 ('Permissions',{'fields':['is_staff','is_active','is_superuser','groups','user_permissions']})]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'mobile', 'password1', 'password2')
        }),
    )
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page = 5
    ordering = ('first_name',)

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d User was successfully Entered.',
            '%d User was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected User as Entered"
    actions = [make_published]


# Register your models here.
@admin.register(Shop)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'slug', 'description', 'image']}),
                 ('Related Table Information', {'fields': ['user'], 'classes': ['collapse']}),
                 ]
    list_display = ('name', 'slug', 'user', 'description')
    list_filter = ['name', 'slug']
    search_fields = ['name', 'slug', 'user']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Shop was successfully Entered.',
            '%d Shop was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Shop as Entered"
    actions = [make_published]


@admin.register(Address)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['city', 'street', 'alley', 'zip_code']}),
                 ('Related Table Information', {'fields': ['user'], 'classes': ['collapse']}),
                 ]
    list_display = ('user', 'city', 'street', 'alley', 'zip_code')
    list_filter = ['city', 'street', 'alley', 'zip_code']
    search_fields = ['city', 'street', 'alley', 'zip_code']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Address was successfully Entered.',
            '%d Address was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Address as Entered"
    actions = [make_published]


@admin.register(Email)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['subject', 'body']}),
                 ('Related Table Information', {'fields': ['user'], 'classes': ['collapse']}),
                 ]
    list_display = ('user', 'subject')
    list_filter = ['subject']
    search_fields = ['subject']
    list_per_page = 5

    def make_published(self, request, queryset):
        updated = queryset.update(draft=False)
        self.message_user(request, ngettext(
            '%d Email was successfully Entered.',
            '%d Email was successfully Entered.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected Email as Entered"
    actions = [make_published]
