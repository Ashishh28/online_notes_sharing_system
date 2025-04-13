from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/<int:pk>/update/', views.update_note, name='update_note'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('search/', views.search, name='search'),
]
 