from django.urls import path 
from . import views

# URL patterns for the notes app 
urlpatterns = [
    # Homepage - shows list of all notes
    # Example: http://locahost:8000
    path('', views.note_list, name='note_list'),

    # View a single note's details
    # Example: http://localhost:8000/note/5/
    path('note/<int:pk>/', views.note_detail, name='note_detail'),

    # Create a new note 
    # Example: http://localhost:8000/note/new
    path('note/new/', views.note_create, name='note_create'),

    # Edit an existing note
    # Example: http://localhost:8000/note/6/edit
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),

    # Delete a note
    # Example: http://localhost:8000/note/6/delete/
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
