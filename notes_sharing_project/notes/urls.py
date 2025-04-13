from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_note, name='upload_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('public/', views.public_notes, name='public_notes'),


]
