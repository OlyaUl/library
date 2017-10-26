from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^create_cat/$', views.create_cat, name='create_cat'),
    # url(r'^info_book/$', views.info_book, name='info_book'),
    # url(r'^books/$', views.books, name='books'),
    # url(r'^authors/$', views.authors, name='authors'),
    # url(r'^category/$', views.category, name='category'),
    ##url(r'^books/$', views.BookListView.as_view(), name='books'),
    # url(r'^detail_books/$', views.BookDetailView.as_view(), name='detail_books'),
    #     url(r'category/add/$', views.CategoryCreateView.as_view(), name='category_add'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    url(r'^all_books/$', views.BookListView.as_view(), name='all_books'),

    url(r'^detail_book/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='detail_book'),
    url(r'^detail_author/(?P<pk>\d)/$', views.AuthorDetailView.as_view(), name='detail_author'),
    url(r'^detail_category/(?P<pk>\d)/$', views.CategoryDetailView.as_view(), name='detail_category'),

    url(r'^category_update/(?P<pk>\d)/$', views.CategoryUpdate.as_view(), name='category_update'),
    url(r'^book_update/(?P<pk>\d)/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^author_update/(?P<pk>\d)/$', views.AuthorUpdate.as_view(), name='author_update'),

    url(r'^category_delete/(?P<pk>\d)/$', views.CategoryDelete.as_view(), name='category_delete'),
    url(r'^book_delete/(?P<pk>\d)/$', views.BookDelete.as_view(), name='book_delete'),
    url(r'^author_delete/(?P<pk>\d)/$', views.AuthorDelete.as_view(), name='author_delete'),

    url(r'^category_create/$', views.CategoryFormView.as_view(), name='category_create'),
    url(r'^book_create/$', views.BookFormView.as_view(), name='book_create'),
    url(r'^author_create/$', views.AuthorFormView.as_view(), name='author_create'),
    url(r'^comment_create/$', views.CommentFormView.as_view(), name='comment_create'),

    url(r'^set_like/$', views.set_like, name='set_like'),
    url(r'^set_dislike/$', views.set_dislike, name='set_dislike'),

]