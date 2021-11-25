from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Herb, Remedy

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def herbs_index(request):
  herbs = Herb.objects.all()
  return render(request, 'herbs/index.html', { 'herbs': herbs })

@login_required
def herbs_detail(request, herb_id):
  herb = Herb.objects.get(id=herb_id)
  return render(request, 'herbs/detail.html', { 'herb': herb })

@login_required
def remedies_index(request):
  remedies = Remedy.objects.all()
  return render(request, 'remedies/index.html', { 'remedies': remedies })

@login_required
def remedy_detail(request, remedy_id):
  remedy = Remedy.objects.get(id=remedy_id)
  return render(request, 'remedies/detail.html', { 'remedy': remedy })

class RemedyCreate(LoginRequiredMixin, CreateView):
  model = Remedy
  fields = ['name', 'herbs', 'type', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class RemedyUpdate(LoginRequiredMixin, UpdateView):
  model = Remedy
  fields = ['name', 'herbs', 'type', 'description']

class RemedyDelete(LoginRequiredMixin, DeleteView):
  model = Remedy
  success_url = '/remedies/'

@login_required
def assoc_Remedy(request, herb_id, remedy_id):
  Remedy.objects.get(id=remedy_id).herbs.add(herb_id)
  return redirect('remedy_detail', remedy_id=remedy_id)

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
