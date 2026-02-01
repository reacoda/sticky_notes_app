from django.contrib import admin
from .models import Note

# Customise how Notes appear in admin panel


class NoteAdmin(admin.ModelAdmin):
    """
    Customises the admin interface for Note model
    """
    # Show these fields in the list view 
    list_display = ('title', 'created_at', 'updated_at')

    # Add filters in the sidebar
    list_filter = ('created_at', 'updated_at')

    # add search functionality 
    search_fields = ('title', 'content')

    # Make these fields read-only 
    readonly_fields = ('created_at', 'updated_at')

# Register the Note model with the custom admin class


admin.site.register(Note, NoteAdmin)
