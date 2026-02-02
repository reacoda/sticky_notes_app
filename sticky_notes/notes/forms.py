# notes/forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.
    
    Includes validation to ensure title and content are not empty.
    """
    
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title',
                'required': True
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note content',
                'rows': 5,
                'required': True
            })
        }
        labels = {
            'title': 'Title',
            'content': 'Content'
        }
    
    def clean_title(self):
        """
        Validate that title is not empty or just whitespace.
        
        Returns:
            str: The cleaned and stripped title
            
        Raises:
            ValidationError: If title is empty or only whitespace
        """
        title = self.cleaned_data.get('title')
        
        # Check if title exists and is not just whitespace
        if not title or not title.strip():
            raise forms.ValidationError('Title cannot be empty.')
        
        return title.strip()
    
    def clean_content(self):
        """
        Validate that content is not empty or just whitespace.
        
        Returns:
            str: The cleaned and stripped content
            
        Raises:
            ValidationError: If content is empty or only whitespace
        """
        content = self.cleaned_data.get('content')
        
        # Check if content exists and is not just whitespace
        if not content or not content.strip():
            raise forms.ValidationError('Content cannot be empty.')
        
        return content.strip()
        