Reproduce and experiment with bug [12203](https://code.djangoproject.com/ticket/12203)


Commit [81ff35f1cea63f6c9d6bf8a914196de04fa37515](https://github.com/RosanaRufer/django_issue_12203/commit/81ff35f1cea63f6c9d6bf8a914196de04fa37515)

* Replicates ticket instruction.
* Unable to see the specified bug as runserver can't be executed with: Error <class 'library.admin.BookAdmin'>: (admin.E013) The value of 'fields' cannot include the ManyToManyField 'authors', because that field manually specifies a relationship model.


Commit [130bd4f6529e22aa724107ebd52aa281ca36b23d](https://github.com/RosanaRufer/django_issue_12203/commit/130bd4f6529e22aa724107ebd52aa281ca36b23d)

* Removes "through='AuthorsBooks' as suggested in description.
* Able to add Authors and Books but of course AuthorBooks isn't updated
