from django.contrib import admin
from django.utils.html import format_html
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Complete admin configuration for Blog model with advanced features
    """
    
    # Display fields in the blog list view
    list_display = ('title', 'user', 'get_text_preview', 'get_image_preview', 'created_at', 'updated_at')
    
    # Fields to filter by in the sidebar
    list_filter = ('created_at', 'updated_at', 'user')
    
    # Fields to search
    search_fields = ('title', 'text', 'user__username')
    
    # Read-only fields that cannot be edited
    readonly_fields = ('get_image_preview', 'created_at', 'updated_at')
    
    # Default ordering
    ordering = ('-created_at',)
    
    # Pagination
    list_per_page = 20
    
    # Field organization in the detail view
    fieldsets = (
        ('Blog Information', {
            'fields': ('title', 'text', 'user')
        }),
        ('Media', {
            'fields': ('image', 'get_image_preview'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Add fields for creation form
    add_fieldsets = (
        ('Blog Information', {
            'fields': ('title', 'text', 'user', 'image'),
            'classes': ('wide',)
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        """Override form based on add or change"""
        form = super().get_form(request, obj, **kwargs)
        if obj is None:  # Adding a new blog
            self.fields = self.add_fieldsets[0][1]['fields']
        return form
    
    def get_text_preview(self, obj):
        """Display preview of text field"""
        preview = obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
        return preview
    get_text_preview.short_description = 'Text Preview'
    
    def get_image_preview(self, obj):
        """Display image preview in admin"""
        if obj.image:
            return format_html(
                '<img src="{}" width="200" height="auto" style="max-width: 100%; height: auto;" />',
                obj.image.url
            )
        return 'No image'
    get_image_preview.short_description = 'Image Preview'
    
    def save_model(self, request, obj, form, change):
        """Save model and set user automatically"""
        if not change:  # If creating new blog
            obj.user = request.user
        super().save_model(request, obj, form, change)
    
    # Custom actions
    actions = ['mark_as_updated']
    
    def mark_as_updated(self, request, queryset):
        """Custom action to update selected blogs"""
        updated_count = queryset.count()
        for blog in queryset:
            blog.save()  # This will trigger updated_at
        self.message_user(request, f'{updated_count} blog(s) marked as updated.')
    mark_as_updated.short_description = 'Mark selected blogs as updated'

