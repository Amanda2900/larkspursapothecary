from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from main_app.models import Remedy

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# class RemedyCreate(LoginRequiredMixin, CreateView):
#   def form_valid(self, form):
#     form.instance.user = self.request.user 
#     return super().form_valid(form)

# @login_required
# def cats_index(request):
#   remedies = Remedy.objects.filter(user=request.user)
#   return render(request, 'cats/index.html', { 'remedies': remedies })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('herbs_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
