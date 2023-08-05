from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.site_header = "Blog Admin Panal"
admin.site.site_title = "Blog Admin Panal"


class TopicAdmin(admin.ModelAdmin):
    fields= ("title","content")
    list_display=["id",  'title' , 'active']
    list_editable = ('title',)
    search_fields=['title','content']
    list_filter = ('created_at',)
    date_hierarchy='created_at'
    

    




admin.site.register(Post , TopicAdmin)


