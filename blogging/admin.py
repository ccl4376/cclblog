from django.contrib import admin
from models import blog,Upload

class BlogAdmin(admin.ModelAdmin):
    model = blog
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class UploadAdmin(admin.ModelAdmin):
    list_display = ('bupimg',)
    list_display_links = ('bupimg',)

admin.site.register(blog, BlogAdmin)
admin.site.register(Upload, UploadAdmin)
