from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('create_at','update_at',)
    readonly_fields = ('create_at','update_at',)
    list_display = ('title','create_at','update_at',)
    search_fields = ('title','content','tag','category',)
    # prepopulated_fields = {'slug':('title','tag',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)