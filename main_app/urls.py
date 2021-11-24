from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('herbs/', views.herbs_index, name='herbs_index'),
  path('herbs/<int:herb_id>', views.herbs_detail, name='herbs_detail'),
]