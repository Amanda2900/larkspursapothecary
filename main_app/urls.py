from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('herbs/', views.herbs_index, name='herbs_index'),
  path('herbs/<int:herb_id>', views.herbs_detail, name='herbs_detail'),
  path('remedies/', views.remedies_index, name='remedies_index'),
  path('myremedies/', views.myremedies, name='myremedies'),
  path('remedies/<int:remedy_id>/', views.remedy_detail, name='remedy_detail'),
  path('remedies/create/', views.RemedyCreate.as_view(), name='remedy_create'),
  path('remedies/<int:pk>/update/', views.RemedyUpdate.as_view(), name='remedy_update'),
  path('remedies/<int:pk>/delete/', views.RemedyDelete.as_view(), name='remedy_delete'),
  path('remedies/<int:remedy_id>/add_photo/', views.add_photo, name='add_photo'),
]