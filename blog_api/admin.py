from django.contrib import admin
from .models import Posts, Comments, Tags

# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'id', 'slug', 'created_by')


admin.site.register(Comments)
admin.site.register(Tags)
