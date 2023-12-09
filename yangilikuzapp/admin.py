from django.contrib import admin
from .models import Category,News,contact,ViewCount,Comment
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status']
    list_filter = ['status','publish_time','creatid_time']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'publish_time'
    search_fields=['title','body']
    ordering=['status','publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']   

admin.site.register(contact) 
        
admin.site.register(ViewCount)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
