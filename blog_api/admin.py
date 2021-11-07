from django.contrib import admin
from .models import Posts, Comments, Tags

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Tags)