from django.contrib import admin
from .models import POST, Tag, Profile

@admin.register(POST)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # auto fills slug
    filter_horizontal = ('tags', 'mentions')    # nice UI for M2M fields

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)