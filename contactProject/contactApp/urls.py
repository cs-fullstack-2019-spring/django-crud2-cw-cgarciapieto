from django.urls import path

from . import views

# paths to contacts page and delete page
urlpatterns = [
    path('', views.index, name='contacts'),
    path('contacts/edit/<int:id>/', views.editcontacts, name='edit'),
    path('contacts/delete/<int:id>/', views.deletecontact, name='delete'),

]