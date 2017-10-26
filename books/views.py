from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import ModelFormMixin

from .models import Book, Category, Author, Comment, Rating
from django.template import loader
from django.views.generic import View, ListView, CreateView, DetailView, FormView, UpdateView, DeleteView
from django.utils import timezone
from .forms import CategoryForm, AuthorForm, BookForm,  CommentForm
from django.urls import reverse_lazy
import json

# list view --------------------------------------------------
class CategoryListView(ListView):
    template_name = 'books/category_list.html'
    model = Category
    context_object_name = 'categories'


class AuthorListView(ListView):
    template_name = 'books/authors_list.html'
    model = Author
    context_object_name = 'authors'


class BookListView(ListView):
    template_name = 'books/books_list.html'
    model = Book
    context_object_name = 'all_books'
# end list view --------------------------------------------------


# delete --------------------------------------------------
class BookDelete(DeleteView):
    model = Book
    fields = ['title']
    template_name = 'books/book_confirm_delete.html'
    # success_url = reverse_lazy('/books/category/')
    success_url = '/books/all_books/'


class CategoryDelete(DeleteView):
    model = Category
    fields = ['title']
    template_name = 'books/category_confirm_delete.html'
    # success_url = reverse_lazy('/books/category/')
    success_url = '/books/categories/'


class AuthorDelete(DeleteView):
    model = Author
    fields = ['name']
    template_name = 'books/author_confirm_delete.html'
    # success_url = reverse_lazy('/books/category/')
    success_url = '/books/authors/'
# end delete --------------------------------------------------


# detail view --------------------------------------------------
class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    '''
    model = Book
    context_object_name = 'books'
    pk_url_kwarg = 'pk'''
    model = Book
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'category_id'
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AuthorDetailView(DetailView):
    template_name = 'books/author_detail.html'
    model = Author
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CategoryDetailView(DetailView):
    template_name = 'books/category_detail.html'
    model = Category
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
# end detail view --------------------------------------------------

# create view ??--------------------------------------------------
class CategoryCreateView(ListView):
    model = Category
    fields = ['title']
# ---------------------------------


# create view --------------------------------------------------
class CategoryFormView(CreateView):
    form_class = CategoryForm
    template_name = 'books/category_form.html'
    success_url = '/books/categories/'


class BookFormView(CreateView):
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = '/books/all_books/'


class AuthorFormView(CreateView):
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = '/books/authors/'


class CommentFormView(CreateView):
    form_class = CommentForm
    template_name = 'books/comment_form.html'
    success_url = '/'
# end create view --------------------------------------------------


# update view --------------------------------------------------
class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    # template_name_suffix = '_update_form'
    template_name = 'books/category_update_form.html'
    success_url = '/books/categories/'


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    # template_name_suffix = '_update_form'
    template_name = 'books/book_update_form.html'
    success_url = '/books/all_books/'


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    # template_name_suffix = '_update_form'
    template_name = 'books/author_update_form.html'
    success_url = '/books/authors/'
# end update view --------------------------------------------------

# -----------------------------------------------------------------------------------------


def index(request):
    # return HttpResponse("Hello, world!")
    books = Book.objects.all()
    for b in books:
        id = b.id
        print(id)
        get_r = Rating.objects.filter(book_id=id).exists()
        print(get_r)
        if get_r == False:
            Rating.objects.create(like=0, dislike=0, book_id=id)

    return render(request, 'books/index.html',
                  {'books': books})


def set_like(request):
    id = request.GET.get('id', None)
    print(id)
    old_like = Rating.objects.get(book_id=id)
    old_like_value = old_like.like
    new_like = int(old_like_value) + 1
    Rating.objects.filter(book_id=id).update(like=new_like)
    return HttpResponse(json.dumps(str(new_like)))

def set_dislike(request):
    id = request.GET.get('id', None)
    print(id)
    old_dislike = Rating.objects.get(book_id=id)
    old_dislike_value = old_dislike.dislike
    new_dislike = int(old_dislike_value) + 1
    Rating.objects.filter(book_id=id).update(dislike=new_dislike)

    return HttpResponse(json.dumps(str(new_dislike)))

        #
#
# def create_cat(request):
#     # return HttpResponse("Hello, world!")
#     if request.method == "POST":
#         Category.objects.create(title=request.POST['title'], description=request.POST['description'])
#     cat = Category.objects.all()
#     return render(request, 'books/form_author.html', {'cats': cat})
#
#
# def info_book(request):
#     # book_info = Book.objects.get(pk=1)
#     # return render(request, 'books/books.html', {'book_info': book_info})
#     t = loader.get_template('books/info_books.html')
#     c = {'books': Book.objects.all().prefetch_related('authors')}
#     return HttpResponse(t.render(c, request))
#
#
# def category(request):
#     # return HttpResponse("Hello, world!")
#     categories = Category.objects.all()
#     return render(request, 'books/category.html',
#                   {'categories': categories})
#
#
# def authors(request):
#     # return HttpResponse("Hello, world!")
#     authors = Author.objects.all()
#     return render(request, 'books/authors.html',
#                   {'authors': authors})
#
#
# def books(request):
#     # return HttpResponse("Hello, world!")
#     books = Book.objects.all()
#     return render(request, 'books/books.html',
#                   {'books': books})