from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from db.models import Author,Books
# Create your views here.

class MainView(TemplateView):
    template_name = 'main.html'

    def get(self , request):
        if request.user.is_authenticated:
            author  = Author.objects.order_by('id')
            books = Books.objects.all()
            ctx = {}
            ctx['author'] = author
            ctx['books'] = books

            return render(request , self.template_name , ctx)
        else:
            return render(request , self.template_name , {})

    def post(self,request):
        if request.user.is_authenticated:
            query_a = request.POST['search_a']

            result = Author.objects.filter(surname=query_a)
            if result.count() != 0 :
                ctx = {
                    'result' : result,
                    'query' : query_a,
                }
            else:
                ctx = {
                    'empty': "Ничего не найдено",
                    'query': query_a,
                }
            return render(request,'result.html',ctx)


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "login/"

    template_name = "register.html"

    def form_valid(self , form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")



