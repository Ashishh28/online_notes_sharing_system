from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm, NoteForm
from .models import Note
from django.contrib import messages


# -------------------------------
# Public Views
# -------------------------------

def home(request):
    # Fetch public notes, including those uploaded by any user
    notes = Note.objects.filter(public=True).order_by('-uploaded_at')
    return render(request, 'home.html', {'notes': notes})


# -------------------------------
# Authenticated Views
# -------------------------------

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('dashboard')  # Redirect to dashboard after registration
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout


@login_required
def dashboard(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(user=request.user, title__icontains=query)
    else:
        notes = Note.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'notes': notes, 'query': query})


@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note uploaded successfully.")
            return redirect('home')  # Redirect to home after note upload (instead of dashboard)
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {'form': form})


@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect('dashboard')  # Redirect to dashboard after note update
    else:
        form = NoteForm(instance=note)
    return render(request, 'upload_note.html', {'form': form})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    messages.success(request, "Note deleted successfully.")
    return redirect('dashboard')  # Redirect to dashboard after note deletion


def public_notes(request):
    notes = Note.objects.filter(public=True).order_by('-uploaded_at')
    return render(request, 'public_notes.html', {'notes': notes})

