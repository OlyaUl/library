from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
from django.views.generic import CreateView
from .forms import UserForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/books/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'my_auth/login.html', {})


class UserFormView(CreateView):
    form_class = UserForm
    template_name = 'my_auth/register.html'
    success_url = '/books/'

    def form_valid(self, form):
        response = super(UserFormView, self).form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return response

    def get_context_data(self, **kwargs):
        return super(UserFormView, self).get_context_data(**kwargs)












'''if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/books/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'books/login.html', {})'''