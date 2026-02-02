from django.db import models

class Note(models.Model):
    """
    Model representing a sticky note

    Fields:
        title: short description of the note (max 200 characters)
        content: The note content (can be a long text)
        created_at: datetime when note was created(auto-generated)
        updated_at: datetime when note was last modified (auto-generated)
    """

    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the note title when the object is printed"""
        return self.title
    
    class Meta:
        # newest note first
        ordering = ['-created_at']