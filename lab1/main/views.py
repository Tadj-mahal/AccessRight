from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Employee
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View

class List(TemplateView):
    template_name = "employees.html"

    def get(self, request):
        all_employees = Employee.objects.all()
        ctx = {
            'all_employees': all_employees,
        }
        return render(request, self.template_name, ctx)
        
    def post(self, request):
       template = "employees.html" 
       if 'search' in request.POST:
           template = "result.html"  
           query = request.POST['search']
           result_list = Employee.objects.filter(id = query)
           if result_list.count() != 0:
    	       	context = {
    	       		'result_list': result_list,
    	       		'query': query,
    	       	}
           else:
           		context = {
           			'empty': "Nothing founded. 404!",
           			'query': query,
           		}
       

       if 'deluser' in request.POST:
           query = request.POST['deluser']
           Employee.objects.get(id = query).delete()
           all_employees = Employee.objects.all()
           context = {
                    'all_employees': all_employees,
                } 


       if 'adduser' in request.POST:
           print(request.POST)
           emp = Employee()
           emp.name = request.POST.get("name")
           emp.surname = request.POST.get("surname")
           emp.position = request.POST.get("position")
           emp.address = request.POST.get("address")
           emp.phone  = request.POST.get("phone")
           emp.save()
           all_employees = Employee.objects.all()
           context = {
            'all_employees': all_employees,
            }
       return render(request, template, context)
       
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "employees.html"

    template_name = "employees.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)