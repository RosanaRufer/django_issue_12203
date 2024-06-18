from django.contrib import admin

from library.models import Author, AuthorsBooks, Book


class AuthorsBooksInline(admin.TabularInline):
    model = AuthorsBooks
    extra = 1
    fields = ['author', 'book']
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # This will raise an error
    #     ERRORS:
    # <class 'library.admin.BookAdmin'>: (admin.E013) The value of 'fields' cannot include the ManyToManyField 'authors', because that field manually specifies a relationship model.
    fields = ['name']
    list_display = ['name', 'get_authors'] 
    inlines = [AuthorsBooksInline]
    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name'] 
    inlines = [AuthorsBooksInline]

