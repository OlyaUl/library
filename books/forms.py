from django import forms
from .models import Book, Category, Author, Comment


class CategoryForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Category
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Comment
        fields = '__all__'