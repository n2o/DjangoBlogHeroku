from django.contrib import admin
from blogengine.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
