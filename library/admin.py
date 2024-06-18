from django.contrib import admin

from library.models import Author, AuthorsBooks, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # This will raise an error
    #     ERRORS:
    # <class 'library.admin.BookAdmin'>: (admin.E013) The value of 'fields' cannot include the ManyToManyField 'authors', because that field manually specifies a relationship model.
    fields = ['name', 'authors'] 

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(AuthorsBooks)    
class AuthorsBooksAdmin(admin.ModelAdmin):
    fields = ['author', 'book']
