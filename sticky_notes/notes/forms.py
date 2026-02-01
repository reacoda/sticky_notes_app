from django import forms 
from .models import Note 


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects

    This form automatically generates fields based on the Note Model
    and handles validation 
    """

    class Meta:
        model = Note
        fields = ['title', 'content']

        # Custom labels for form fields 
        labels = {
            'title': 'Note Title',
            'content': 'Note Content',
        }

        # help text that appears below each field
        help_texts = {
            'title': 'Enter a short descriptive title for your note (max 200 characters)',
            'content': 'Write your note content here (optional)',
        }

        # customise the HTML widgets 
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your note here...',
                'rows': 5,
            })
        }