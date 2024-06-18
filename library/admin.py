from django.contrib import admin

from library.models import Book

class BookAdmin(admin.ModelAdmin):
    # This will raise an error
    #     ERRORS:
    # <class 'library.admin.BookAdmin'>: (admin.E013) The value of 'fields' cannot include the ManyToManyField 'authors', because that field manually specifies a relationship model.
    fields = ['authors'] 

admin.site.register(Book, BookAdmin)