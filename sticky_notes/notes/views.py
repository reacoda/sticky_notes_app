from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    View to display a list of all notes.
    
    GET request: Shows all notes ordered by creation date (newest first).
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered template with list of all notes
    """
    # Get all notes from database (newest first due to model's Meta ordering)
    notes = Note.objects.all()
    
    # Create context dictionary to pass to template
    context = {
        'notes': notes,
        'page_title': 'My Sticky Notes',
    }
    
    # Render the template with context
    return render(request, 'notes/note_list.html', context)


def note_detail(request, pk):
    """
    View to display details of a single note.
    
    GET request: Shows the full details of one specific note.
    
    Args:
        request: HTTP request object
        pk: Primary key (ID) of the note to display
        
    Returns:
        Rendered template with note details
    """
    # Get the note with this ID, or show 404 error if not found
    note = get_object_or_404(Note, pk=pk)
    
    # Create context dictionary
    context = {
        'note': note,
    }
    
    # Render the template with context
    return render(request, 'notes/note_detail.html', context)


def note_create(request):
    """
    View to create a new note.
    
    GET request: Shows empty form
    POST request: Processes form submission, saves note if valid
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered template with form, or redirect to note list after save
    """
    # Check if form was submitted (POST) or just viewing (GET)
    if request.method == 'POST':
        # User submitted the form - create form with submitted data
        form = NoteForm(request.POST)
        
        # Validate the form
        if form.is_valid():
            # Save the new note to database
            note = form.save()
            
            # Redirect to the list of all notes
            return redirect('note_list')
    else:
        # User is just viewing the page - show empty form
        form = NoteForm()
    
    # Create context dictionary with form
    context = {
        'form': form,
        'form_title': 'Create New Note',
    }
    
    # Render the template with form
    return render(request, 'notes/note_form.html', context)


def note_update(request, pk):
    """
    View to update an existing note.
    
    GET request: Shows form pre-filled with existing note data
    POST request: Processes form submission, updates note if valid
    
    Args:
        request: HTTP request object
        pk: Primary key (ID) of the note to update
        
    Returns:
        Rendered template with form, or redirect to note list after update
    """
    # Get the existing note, or show 404 if not found
    note = get_object_or_404(Note, pk=pk)
    
    # Check if form was submitted (POST) or just viewing (GET)
    if request.method == 'POST':
        # User submitted the form - create form with submitted data AND existing note
        form = NoteForm(request.POST, instance=note)
        
        # Validate the form
        if form.is_valid():
            # Save the updated note to database
            form.save()
            
            # Redirect to the list of all notes
            return redirect('note_list')
    else:
        # User is just viewing - show form pre-filled with existing note data
        form = NoteForm(instance=note)
    
    # Create context dictionary with form and note
    context = {
        'form': form,
        'note': note,
        'form_title': 'Edit Note',
    }
    
    # Render the template with form
    return render(request, 'notes/note_form.html', context)


def note_delete(request, pk):
    """
    View to delete an existing note.
    
    Any request: Deletes the note and redirects to note list
    
    Args:
        request: HTTP request object
        pk: Primary key (ID) of the note to delete
        
    Returns:
        Redirect to note list after deletion
    """
    # Get the note to delete, or show 404 if not found
    note = get_object_or_404(Note, pk=pk)
    
    # Delete the note from database
    note.delete()
    
    # Redirect to the list of all notes
    return redirect('note_list')