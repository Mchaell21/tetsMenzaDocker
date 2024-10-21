from django.contrib import admin
from .models import ImageServ, Post, PostImage, LogoImg

# Register your models here.
admin.site.register(ImageServ)
admin.site.register(LogoImg)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass