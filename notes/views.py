from  django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, NoteForm
from .models import Note, Profile

def home(request):
    return render(request, 'notes/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Your account has been created! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'notes/register.html', {'form': form})

@login_required
def dashboard(request):
    notes_count = Note.objects.filter(user=request.user).count()
    return render(request, 'notes/dashboard.html', {'notes_count': notes_count})

@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/notes_list.html', {'notes': notes})

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Your note has been added!')
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Add Note'})

@login_required
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your note has been updated!')
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Update Note'})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Your note has been deleted!')
        return redirect('notes_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'notes/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'notes/change_password.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | Q(subject__icontains=query),
            user=request.user
        )
    else:
        notes = Note.objects.filter(user=request.user)
    
    return render(request, 'notes/search_results.html', {'notes': notes, 'query': query})
 