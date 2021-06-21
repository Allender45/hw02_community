from django.contrib import admin
from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'description', )
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group', 'published', )
    list_filter = ('group', 'pub_date', 'author', )
    search_fields = ('text', )
    list_editable = ('group', 'published', )
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
