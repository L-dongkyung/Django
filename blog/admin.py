from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'content')
    list_filter = ('id', 'title', 'modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)
