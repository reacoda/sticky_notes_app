# tests.py for Sticky Notes Application
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model"""
    
    def setUp(self):
        """
        This runs BEFORE each test.
        We create a test note that all our tests can use.
        """
        # Create a test note
        Note.objects.create(
            title='Test Note',
            content='This is test content.'
        )
    
    def test_note_has_title(self):
        """Test that a Note has the correct title"""
        # Get the note from database
        note = Note.objects.get(id=1)
        # Check if title matches
        self.assertEqual(note.title, 'Test Note')
    
    def test_note_has_content(self):
        """Test that a Note has the correct content"""
        # Get the note from database
        note = Note.objects.get(id=1)
        # Check if content matches
        self.assertEqual(note.content, 'This is test content.')
    
    def test_note_has_created_at(self):
        """Test that a Note has a created_at timestamp"""
        # Get the note from database
        note = Note.objects.get(id=1)
        # Check that created_at is not None
        self.assertIsNotNone(note.created_at)
        # Check that it's a datetime object
        self.assertIsInstance(note.created_at, type(timezone.now()))
    
    def test_note_has_updated_at(self):
        """Test that a Note has an updated_at timestamp"""
        # Get the note from database
        note = Note.objects.get(id=1)
        # Check that updated_at is not None
        self.assertIsNotNone(note.updated_at)
        # Check that it's a datetime object
        self.assertIsInstance(note.updated_at, type(timezone.now()))
    
    def test_note_string_representation(self):
        """Test that the string representation shows the title"""
        # Get the note from database
        note = Note.objects.get(id=1)
        # Check if str(note) returns the title
        self.assertEqual(str(note), 'Test Note')


class NoteViewTest(TestCase):
    """Tests for Note views"""
    
    def setUp(self):
        """
        This runs BEFORE each test.
        We create a test note for testing views.
        """
        # Create a test note
        Note.objects.create(
            title='Test Note',
            content='This is test content.'
        )
    
    def test_note_list_view(self):
        """Test that the notes list page loads and shows notes"""
        # Visit the notes list page
        response = self.client.get(reverse('note_list'))
        # Check if page loaded successfully (status code 200)
        self.assertEqual(response.status_code, 200)
        # Check if our test note appears on the page
        self.assertContains(response, 'Test Note')
    
    def test_note_detail_view(self):
        """Test that the note detail page shows all note information"""
        # Get our test note
        note = Note.objects.get(id=1)
        # Visit the note detail page
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        # Check if page loaded successfully
        self.assertEqual(response.status_code, 200)
        # Check if title appears
        self.assertContains(response, 'Test Note')
        # Check if content appears
        self.assertContains(response, 'This is test content.')
    
    def test_note_create_view_get(self):
        """Test that the create note page loads"""
        # Visit the create note page
        response = self.client.get(reverse('note_create'))
        # Check if page loaded successfully
        self.assertEqual(response.status_code, 200)
    
    def test_note_create_view_post(self):
        """Test that creating a new note works"""
        # Count notes before creating
        initial_count = Note.objects.count()
        # POST data to create a new note
        response = self.client.post(reverse('note_create'), {
            'title': 'New Test Note',
            'content': 'New test content.'
        })
        # Check if we were redirected (status code 302)
        self.assertEqual(response.status_code, 302)
        # Check if a new note was created
        self.assertEqual(Note.objects.count(), initial_count + 1)
        # Check if the new note has correct data
        new_note = Note.objects.latest('created_at')
        self.assertEqual(new_note.title, 'New Test Note')
        self.assertEqual(new_note.content, 'New test content.')
    
    def test_note_update_view_get(self):
        """Test that the update note page loads with existing data"""
        # Get our test note
        note = Note.objects.get(id=1)
        # Visit the update page
        response = self.client.get(reverse('note_update', args=[str(note.id)]))
        # Check if page loaded successfully
        self.assertEqual(response.status_code, 200)
        # Check if existing title appears in the form
        self.assertContains(response, 'Test Note')
    
    def test_note_update_view_post(self):
        """Test that updating a note works"""
        # Get our test note
        note = Note.objects.get(id=1)
        # POST updated data
        response = self.client.post(reverse('note_update', args=[str(note.id)]), {
            'title': 'Updated Test Note',
            'content': 'Updated test content.'
        })
        # Check if we were redirected
        self.assertEqual(response.status_code, 302)
        # Refresh the note from database
        note.refresh_from_db()
        # Check if note was updated
        self.assertEqual(note.title, 'Updated Test Note')
        self.assertEqual(note.content, 'Updated test content.')
    
    def test_note_delete_view(self):
        """Test that deleting a note works"""
        # Get our test note
        note = Note.objects.get(id=1)
        note_id = note.id
        # Count notes before deleting
        initial_count = Note.objects.count()
        # Visit/POST to delete URL
        response = self.client.post(reverse('note_delete', args=[str(note_id)]))
        # Check if we were redirected
        self.assertEqual(response.status_code, 302)
        # Check if note was deleted
        self.assertEqual(Note.objects.count(), initial_count - 1)
        # Check if note no longer exists
        self.assertFalse(Note.objects.filter(id=note_id).exists())

    def test_note_create_empty_title_fails(self):
        """Test that creating a note with empty title fails"""
        # Count notes before attempting to create
        initial_count = Note.objects.count()
        
        # Try to POST with empty title
        response = self.client.post(reverse('note_create'), {
            'title': '',  # Empty title
            'content': 'Some content here.'
        })
        
        # Should NOT create a new note
        self.assertEqual(Note.objects.count(), initial_count)
        
        # Should show the form again (status 200, not redirect 302)
        self.assertEqual(response.status_code, 200)
        
        # Should contain error message
        self.assertContains(response, 'Title cannot be empty')
    
    def test_note_create_empty_content_fails(self):
        """Test that creating a note with empty content fails"""
        # Count notes before attempting to create
        initial_count = Note.objects.count()
        
        # Try to POST with empty content
        response = self.client.post(reverse('note_create'), {
            'title': 'Test Title',
            'content': ''  # Empty content
        })
        
        # Should NOT create a new note
        self.assertEqual(Note.objects.count(), initial_count)
        
        # Should show the form again (status 200, not redirect 302)
        self.assertEqual(response.status_code, 200)
        
        # Should contain error message
        self.assertContains(response, 'Content cannot be empty')
    
    def test_note_create_whitespace_only_title_fails(self):
        """Test that creating a note with only whitespace in title fails"""
        initial_count = Note.objects.count()
        
        # Try to POST with whitespace-only title
        response = self.client.post(reverse('note_create'), {
            'title': '   ',  # Only spaces
            'content': 'Some content here.'
        })
        
        # Should NOT create a new note
        self.assertEqual(Note.objects.count(), initial_count)
        self.assertEqual(response.status_code, 200)
    
    def test_note_create_whitespace_only_content_fails(self):
        """Test that creating a note with only whitespace in content fails"""
        initial_count = Note.objects.count()
        
        # Try to POST with whitespace-only content
        response = self.client.post(reverse('note_create'), {
            'title': 'Test Title',
            'content': '   '  # Only spaces
        })
        
        # Should NOT create a new note
        self.assertEqual(Note.objects.count(), initial_count)
        self.assertEqual(response.status_code, 200)