from django.contrib import admin

# Register your models here.

from .models import post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "update", "puplish"]
	list_filter = ["puplish"]
	search_fields = ["title", "content"]
	class Meta:
		model = post

admin.site.register(post, PostModelAdmin)
