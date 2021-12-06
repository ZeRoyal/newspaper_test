from django.contrib import admin
from .models import Article
from .models import Comment

# class CommentInline(admin.StackedInline):
# 	model = Comment

class CommentInline(admin.TabularInline): # new
	model = Comment


class ArticleAdmin(admin.ModelAdmin):
	inlines = [
	CommentInline,
	]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment) 

