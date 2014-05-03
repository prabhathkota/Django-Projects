from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

#This is just for dispaly order of columns for Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    ordering = ('-first_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'publisher', 'authors', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin) #AuthorAdmin is just for disply in Admin page
admin.site.register(Book, BookAdmin) #BookAdmin is just for display in Admin page