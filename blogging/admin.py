from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from blogging.models import Post, Category


class PostInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [PostInline,
               ]


#  exclude  the ‘posts’ field from the form in your  Category  admin
class CategoryInline(admin.TabularInline):
    model = Category


class CategoryAdmin(admin.ModelAdmin):
    # form = CategoryInline
    list_display = ('name', 'description')
    exclude = ['posts']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# admin.site.register(Post)
# admin.site.register(Category)


# include inline, category inline, tells admin you need to add fields from this other table
# variable called inlines which will be a list, and that list will be pointing to
# another class called categoryInline
# outside of this class, categoryInline, inhertiing from tabular
# define a model for it, category table.posts and a pass through,
# that's what you're doing with your inlines. Will make category show up in blog admin
# then exclude , create another class called CategoryAdmin inherit from admin.modeladmin
# then exclude, pass a tuple to exclude the posts, called a string, bc I don't want this field
# to show up in the category admin
