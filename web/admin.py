from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Blog, Categories, Contact

# To remove user,groups from admin panel
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Categories)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # actions = [mark_active, mark_inactive]
    list_display = ("title", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "content")
    list_filter = ("title", "content")
    # ordering = "timestamp"
    exclude = None
    # readonly_fields = ("auto_id",)
    # autocomplete_fields = ("content",)
    search_fields = (
        "title",
        "content__name",
    )


admin.site.register(Contact)
