from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from main.models import Employee
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
# Create your views here.


class MainView(TemplateView):
	template_name = "main_entry.html"

	def get(self, request):
		if request.user.is_authenticated:
			users = User.objects.all()
			ctx = {}
			ctx['users'] = users
			return render(request, self.template_name, ctx)
		else:
			return render(request, self.template_name, {})


class LoginFormView(FormView):
	form_class = AuthenticationForm

	template_name = "login.html"

	success_url = "../../main"

	def form_valid(self, form):

		self.user = form.get_user()

		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)
		


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/entry/")

class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "../"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)