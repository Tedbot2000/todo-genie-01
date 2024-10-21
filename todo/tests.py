from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create a test todo
        self.todo = Todo.objects.create(
            todo_name='Test Task',
            status='Not Started',
            user=self.user
        )
        # Create a second user for authorization tests
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123'
        )

    def test_todo_model(self):
        """Test Todo model creation and fields"""
        self.assertEqual(self.todo.todo_name, 'Test Task')
        self.assertEqual(self.todo.status, 'Not Started')
        self.assertEqual(self.todo.user, self.user)

    def test_todo_list_view_authenticated(self):
        """Test todo list view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'Not Started')

    def test_todo_list_view_unauthenticated(self):
        """Test todo list view redirects for unauthenticated user"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_create_todo(self):
        """Test creating a new todo item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('todo_list'), {'task': 'New Task'})
        self.assertEqual(response.status_code, 302)  # Redirects after creation
        self.assertTrue(Todo.objects.filter(todo_name='New Task').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task "New Task" added successfully!', 
                     str(messages[0]))

    def test_create_todo_too_long(self):
        """Test creating a todo with name longer than 60 characters"""
        self.client.login(username='testuser', password='testpass123')
        long_task = 'x' * 61
        response = self.client.post(reverse('todo_list'), {'task': long_task})
        self.assertFalse(Todo.objects.filter(todo_name=long_task).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task name cannot be more than 60 characters long.', 
                     str(messages[0]))

    def test_create_todo_empty(self):
        """Test creating a todo with empty name"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('todo_list'), {'task': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task cannot be empty.', str(messages[0]))

    def test_toggle_status(self):
        """Test toggling todo status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('toggle_status', kwargs={'id': self.todo.id})
        )
        updated_todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.status, 'In Progress')
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Status of "Test Task" updated to In Progress.', 
                     str(messages[0]))

    def test_delete_task(self):
        """Test deleting a todo item"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('delete', kwargs={'id': self.todo.id})
        )
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task "Test Task" deleted successfully.', 
                     str(messages[0]))

    def test_edit_task(self):
        """Test editing a todo item"""
        self.client.login(username='testuser', password='testpass123')
        # First get the edit page
        response = self.client.get(
            reverse('edit', kwargs={'id': self.todo.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_task.html')
        
        # Then test the update
        response = self.client.post(
            reverse('edit', kwargs={'id': self.todo.id}),
            {'task': 'Updated Task'}
        )
        updated_todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.todo_name, 'Updated Task')
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task "Updated Task" updated successfully.', 
                     str(messages[0]))

    def test_edit_task_too_long(self):
        """Test editing a todo with name longer than 60 characters"""
        self.client.login(username='testuser', password='testpass123')
        long_task = 'x' * 61
        response = self.client.post(
            reverse('edit', kwargs={'id': self.todo.id}),
            {'task': long_task}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Task name cannot be more than 60 characters long.', 
                     str(messages[0]))

    def test_user_can_only_see_own_todos(self):
        """Test that users can only see their own todos"""
        # Create a todo for other_user
        other_todo = Todo.objects.create(
            todo_name='Other Task',
            status='Not Started',
            user=self.other_user
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('todo_list'))
        
        # Should see own todo but not other user's todo
        self.assertContains(response, 'Test Task')
        self.assertNotContains(response, 'Other Task')

    def test_user_cannot_edit_others_todos(self):
        """Test that users cannot edit other users' todos"""
        other_todo = Todo.objects.create(
            todo_name='Other Task',
            status='Not Started',
            user=self.other_user
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('edit', kwargs={'id': other_todo.id}),
            {'task': 'Hacked Task'}
        )
        self.assertEqual(response.status_code, 404)