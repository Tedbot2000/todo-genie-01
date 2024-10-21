
# ToDo Genie: The user-friendly to-do list application

Do more with the Django application that is your daily manager for things you need to get done. 


## Key Features:

1. **User Authentication and Authorisation:** ToDo Genie uses AllAuth for user authentication and authorisation, providing a secure way for users to create accounts and log in to access their personalised to-do lists.

2. **CRUD Operations:** The application supports Create, Read, Update, and Delete (CRUD) operations, enabling users to add, view, edit, and delete tasks as needed.

3. **Intuitive User Interface:** ToDo Genie features a user-friendly interface that makes it easy to navigate and manage tasks, with a clean design and minimal clutter.

4. **Task Status Toggle:** Users can easily toggle the status of their tasks between Not Started, In Progress, and Completed, helping them track their progress and stay organised.

5. **Task Deletion:** Users can delete tasks that are no longer relevant or completed, keeping their task list up-to-date and clutter-free.

6. **Responsive Design:** The application is designed to be responsive, ensuring a seamless user experience across various devices and screen sizes.

![Responsive Design](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/Responsive.png)


## User Experience (UX)


ToDo Genie is designed as a simple yet powerful task management tool that caters to individuals who value efficiency, organisation, and ease of use. The app's UX design emphasises simplicity and clarity, providing users with an intuitive interface that helps them manage their daily tasks effectively. With a clean and minimalistic aesthetic, ToDo Genie ensures that users can focus on what matters most — getting things done.


### Site User

The primary users of ToDo Genie are individuals from various backgrounds who seek a straightforward and reliable solution for task management. These users may include students, professionals, or anyone looking to keep track of their daily responsibilities. They appreciate the app's user-friendly design, which allows them to quickly add, organise, and complete tasks without unnecessary complexity. These users value productivity, clarity, and a tool that adapts to their needs, helping them stay on top of their to-do lists.


### Goal

ToDo Genie aims to provide users with a streamlined and efficient way to manage their tasks, ensuring they stay on top of their commitments and goals. By offering essential features such as task creation, (and, in a future version, prioritisation, and tracking), the app helps users organise their day-to-day activities with ease. The goal is to create a minimalist, user-focused experience that simplifies task management, making it easier for users to achieve their personal and professional objectives without distraction.


### ToDo List ERD

I intentionally kept the Entity Relationship Diagram straightforward to maintain a clear focus on the Minimum Viable Product (MVP). This approach ensured that I had a clear vision from the outset, with the flexibility to create a new ERD for any significant additions or changes in the future.

![ToDo List ERD](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/ToDo_ListERDDiagram.png)

During development, I decided to modify the Status variable from a simple Boolean toggle to a String/CharField. This change was made when I decided there should be more status options beyond just "Not Started" and "Complete."

```python
status = models.CharField(
        max_length=20,
        default="Not Started",
        choices=[
            ("Not Started", "Not Started"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        help_text="The status of the task "
        "(choices: Not Started, In Progress, Completed)"
    )
```


### Agile Development: Creating a Kanban Board on GitHub

For the development of ToDo Genie, I adopted an Agile approach to ensure continuous progress and adaptability throughout the project. Central to this methodology was the use of a Kanban board on GitHub Projects, which allowed for clear visualisation and efficient management of the development process. View the [project board here](https://github.com/users/Tedbot2000/projects/3).

The Kanban board acted as the cornerstone of project management, providing a real-time snapshot of task progression. The board was divided into the following sections:

![User Stories](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/UserStories.png)

**To Do:** This column was where tasks and user stories that were identified but not yet prioritised for development were listed.

**In Progress:** Tasks actively being worked on were tracked in this column. This provided transparency on ongoing development efforts and helped maintain focus on current objectives.

**Complete:** Successfully completed tasks were shifted to this section for review or testing. This column highlighted the progress made and served as a record of what had been accomplished.

**Future Implementation:** Potential features and ideas for future releases were kept in this column. It allowed for long-term planning while keeping immediate priorities clear.


### User Stories

User stories were integral to the development of ToDo Genie, ensuring that each feature was designed to meet the needs of the end-users. These stories were mapped onto the Kanban board, guiding the development process from concept to completion.

some example user stories were:

    As a logged-in user I can add a new to-do item so that I can keep track of my tasks.

        Given a form for adding a new to-do item, when a user submits a valid item, 
        the item is added to the list and displayed on the main page.

        When a user submits an empty or invalid item, an error message is displayed.

        The newly added item appears at the top of the list or in a designated order.

and:

    As a user I can view responsive content so that I can access and use it easily on 
    different devices (desktop, tablet, mobile).

        When a user opens the application on different devices, the layout adjusts appropriately to the
        screen size.

        The to-do list is readable and usable on all device sizes without requiring horizontal scrolling.

        Buttons, forms, and interactive elements are appropriately sized for touch interaction on
        mobile devices.



## User Interface (UI)

- The application features a clean and minimalistic design, with a focus on usability and accessibility.
- The task list is displayed in a table format, with columns for task name, status, and actions. These move to two columns on mobile devices.
- The UI is controlled by simple buttons. These seemed to be particularly appropriate for users with touch screens without making the application unduly difficult for users with large screens.
- The application uses a responsive design, ensuring that it is usable on various devices and screen sizes.


### Wireframes

To visualise the user interface and user experience of the application, two wireframes were created: one for mobile screens and one for desktops. These wireframes provide a low-fidelity representation of the application's layout, navigation, and key features.

**Mobile Wireframe**

The mobile wireframe is designed to accommodate the smaller screen size and touch-based interaction of mobile devices. The layout is optimised for portrait mode, with a focus on simplicity and ease of use.

![Mobile Wireframe](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/wireframes/MobileWireframe.png)

Key features of the mobile wireframe include:

- A clean and simple nav bar at the top of the screen, allowing users easy access to login/logout features
- A card-based layout for displaying content, with clear typography and minimal clutter
- A focus on vertical scrolling, with clear section headers and dividers to guide the user's attention
- A simple and clear footer

**Desktop Wireframe**

The desktop wireframe takes advantage of the larger screen size and mouse-based interaction to provide a more detailed and feature-rich experience. The layout is optimized for a wider range of screen resolutions and aspect ratios.

![Desktop Wireframe](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/wireframes/DesktopWireframe.png)

Key features of the desktop wireframe include:

- A more comprehensive top navigation bar, with clear menu items and the current login status of the user
- A multi-column layout for displaying content, with clear headings and subheadings
- A focus on verticle scrolling, with clear section headers and dividers to guide the user's attention
- A simple and clear footer

**Design Principles**

Both wireframes are guided by the following design principles:

- Simplicity: A clean and minimalistic design that avoids clutter and focuses on the most important features and content.
- Consistency: A consistent layout and design language across both mobile and desktop versions, to provide a seamless user experience.
- Accessibility: A design that is accessible and usable for a wide range of users, with clear typography, high contrast colours, and intuitive navigation.

These wireframes provide a solid foundation for the application's user interface and user experience, and will serve as a guide for further design and development iterations.


### Colour Scheme

The colour scheme for the application is a combination of three distinct colours that work together to create a unique and engaging visual identity.


### Primary colour:

- **#Gun Metal (#0f242b):** A dark, rich grey tone with a hint of blue undertones, evoking a sense of sophistication and modernity. This colour is used as the primary brand colour and is prominent in the logo, text, and footer background.


### Secondary colours:

- **Goldenrod (#dfad38):** A warm, vibrant yellow-orange tone that adds a touch of energy and optimism to the design. This colour is used in the logo and main background image to add visual interest to the design.
- **#Baby Powder (#fdfdfb):** A soft, calming white tone with a hint of warmth, providing a clean and gentle contrast to the other colours. This colour is used as a card background colour to provide a clean but subtle and understated approach.

![Colours](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/coolors.png)


### Colour Rationale:

The chosen colour scheme is designed to:

- Create contrast: The dark gun metal tone provides a striking contrast to the bright goldenrod tone, while the baby powder tone provides a subtle background that allows other design elements to stand out.
- Evoke emotions: The goldenrod tone adds a sense of excitement and energy, while the gun metal tone conveys a sense of sophistication and modernity.
- Be unique: The combination of these three colours creates a distinctive visual identity that sets the application apart from others.
- Be accessible: The colour scheme is designed to be accessible to users with colour vision deficiency, with sufficient contrast and clear colour differentiation.

Overall, the chosen colour scheme provides a visually appealing and consistent design language that enhances the user experience and reinforces the brand's identity.


## Templates


### Base Template (`base.html`)

The base template provides a foundation for the application's layout and design, including the navigation bar, footer, and main content area. It uses Bootstrap for styling and layout, and includes custom CSS for additional design elements.


#### Meta Content:

- **Bootstrap Framework:** This is a widely-used CSS framework for building responsive and mobile-first interfaces.
- **Custom CSS:** The custom CSS stylesheet ('static/css/style.css') is used to visualy expand and enhance beyond bootstrap.
- **Character Encoding:** The character encoding standard used in the template is set to UTF-8 to support a wide range of characters and languages.
- **Fonts:** The font families used in the template are the Google fonts Roboto and Konkhmer Sleokchher, providing a clean and modern typography.


#### Navigation Bar:

The navigation bar is a critical component of the base template, providing links to essential pages and features of the application. It includes:

- **Login and Register Links:** When a user is not logged in links to the login and register pages are available, allowing users to access their accounts or create new ones.
- **Logout Link:** A link to logout of the application is available only when the user is logged in.
- **Username Display:** The navigation bar displays the username of the logged-in user, providing a personalised experience.


#### Main Content:

The main content area displays:

- **Alert Messages:** Alert messages are displayed to provide feedback to the user. These messages are shown near the top of the card, ensuring they are visible without the need for scrolling too far. They are automatically dismissed after five seconds.
- **Primary UI Content:** Primary content from other HTML files is served below this.


#### Script References:

The base template includes references to the following scripts:

- **Bootstrap JavaScript Files:** The template includes references to Bootstrap's JavaScript files, which provide functionality for components such as buttons, modals, and tooltips.
- **Custom JavaScript Code:** The template also includes custom JavaScript code, which provides functionality for task management features, such as toggling task statuses and updating the task list.


### Main Page Template (todo_list.html)

The todo_list.html template serves as the main page of the application, displaying the user's task list and providing features for task management.


#### Meta Content:

- Extends the `base.html` template to ensure a consistent layout and styling across the entire application.
- Utilises `{% load static %}` to load static files.


#### Content:

The todo_list.html template displays the following content:

- **Task Form:** The template includes a form for adding new tasks, allowing users to create new tasks and add them to their task list.
- **Task List:** The template displays the user's task list, including task names, statuses, and actions (edit and delete).
- **Task Status Toggle:** The template provides a button for toggling task statuses, allowing users to easily update the status of their tasks.
    - If a task is not started the button will appear grey
    - If a task is in progress the button will appear orange
    - When a task is completed the button will appear green
- **Task Actions:** The template includes a button for editing tasks, allowing users to update them, and for deleting tasks, allowing users to remove them.

![Task List Widescreen](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/TaskListWide.png)
![Task List Widescreen](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/TaskListNarrow.png)

### Edit Task Page Template (edit_task.html)

The edit_task.html template is accessed via the 'Edit' button alongside a task on the todo_list.html page. It displays a textbox populated with the task the user wishes to edit and a submit button for when they have finished editing.


#### Meta Content:

- Extends the `base.html` template to ensure a consistent layout and styling across the entire application.
- Utilises `{% load static %}` to load static files.


#### Content:

The edit_tas.html template displays the following content:

- **Task Form:** The template includes a form for editing the selected task, allowing users to update exisitng tasks in their task list.


## ToDo Model

The toDo model is used to represent the tasks within the ToDo Genie Django application. Below is an outline of the model's primary attributes and features:


### Fields:

The ToDo model includes the following fields to store and manage tasks, while associating them with a user:

- **id:** A unique identifier for each task, automatically generated by Django as a primary key.
- **todo_name:** A character field to store the title or name of the task, with a maximum length of 60 characters.
- **status:** A choice field to store the status of the task, with options including "not started", "in progress", and "completed".
- **user:** A foreign key field to store the user who created the task, linking the task to the User model.


## ToDo Views

The ToDo Views are responsible for handling the logic for each task-related action in the application. These views are defined in the **views.py** file and are called when a user interacts with the application.

Here are the Task Views defined in the **views.py** file:

**1. todo_list**

- This view retrieves a list of all to-do list tasks from the database and renders the todo_list.html template, passing the task list as a context variable.
- The todo_list view is called when the, logged in, user visits the root URL of the application ('').

**2. toggle_status**

- This view takes an id parameter, which identifies the task to be updated.
- The view toggles the completed status of the task and saves the changes to the database.
- The toggle_status view is called when the user clicks the "Toggle Status" button for a task.

**3. delete_task**

- This view takes an id parameter, which identifies the task to be deleted.
- The view deletes the task from the database.
- The delete_task view is called when the user clicks the "Delete" button for a task.

**4. update_task**

- This view takes an id parameter, which identifies the task to be updated.
- The view retrieves the task from the database, updates its details, and saves the changes to the database.
- The update_task view is called when the user submits the 'Edit' form for a task.


**URL Routing**

The URL Routing system in Django maps URLs to views, which handle the logic for each page or action in the application. In the ToDo Genie application, the URL patterns are defined in the **urls.py** file.

The **urls.py** file defines four URL patterns:

**Todo List Page:**
- URL: '/'
- View: 'todo_list'
- Name: 'todo_list'
- Function: Displays the list of tasks

**Toggle Task Status:**
- URL: '/toggle_status/<int:id>/'
- View: 'toggle_status'
- Name: 'toggle_status'
- Function: Toggles the status of a task

**Delete Task:**
- URL: '/delete/<int:id>/'
- View: 'delete_task'
- Name: 'delete'
- Function: Deletes a task

**Update Task:**
- URL: '/update/<int:id>/'
- View: 'update_task'
- Name: 'update'
- Function: Updates a task

By using URL Routing, the ToDo Genie application can decouple the URL structure from the view logic, making it easier to maintain and extend the application.


# Testing and Validation

## HTML Validation

All HTML pages were validated using the W3C Markup Validation Service

signup.html Validation

![signup.html Validation](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/signupGood.png)

login.html Validation

![login.html Validation](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/loginGood.png)

logout.html Validation

![logout.html Validation](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/logoutGood.png)

edit_task.html Validation

![edit_task.html Validation](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/edit_taskGood.png)


## CSS Validation

The style.css file was validated using the W3C CSS Validation Service

![CSS Validtation](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/cssGood.png)

## Javascript Validation

The javascript.js file was validate using the validator at JSLint.com

![Testing with JSLint](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/JSLint.png)

## Python Validation

All python files were validated using the Code Institute Python Linter

Those with the error "E501 line too long" are all files which were automatically created by Django. All custom files have been corrected and validate with no errors. 

![Python vaidation app_adapters.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_adapters_py.png)
![Python vaidation app_admin.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_admin_py.png)
![Python vaidation app_apps_py.png](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_apps_py.png)
![Python vaidation app_models_py.png](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_models_py.png)
![Python vaidation app_urls.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_urls_py.png)
![Python vaidation app_views.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/app_views_py.png)
![Python vaidation proj_asgi.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/proj_asgi_py.png)
![Python vaidation proj_setting.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/proj_settings_py.png)
![Python vaidation proj_urls.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/proj_urls_py.png)
![Python vaidation proj_wsgi.py](https://github.com/Tedbot2000/todo-genie-01/blob/main/docs/images/proj_wsgi_py.png)


## Tests

# Testing

## Automated Testing

The application was thoroughly tested using Django's automated testing framework. A comprehensive test suite was created to verify all core functionalities of the application.

### Test Statistics
- Total number of tests: 12
- All tests passed successfully
- Test coverage includes models, views, and user interactions
- Tests run time: ~2.5 seconds

### Technical Implementation

The test suite uses Django's `TestCase` class which provides:
- Automatic database setup and teardown for each test
- A test client for simulating HTTP requests
- Authentication helpers
- Assertion methods for verifying responses and database states

Example of the test setup:
```python
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
```

### Authentication Tests
| Test Description | Result |
|-----------------|--------|
| User can create an account | Pass |
| User can log in | Pass |
| User can log out | Pass |
| Unauthorized users are redirected to login | Pass |
| Users cannot access other users' todo lists | Pass |

Example of authentication test:
```python
def test_todo_list_view_unauthenticated(self):
    """Test todo list view redirects for unauthenticated user"""
    response = self.client.get(reverse('todo_list'))
    self.assertEqual(response.status_code, 302)  # Redirects to login
```

### Task Management Tests
| Test Description | Result |
|-----------------|--------|
| Create new task | Pass |
| Prevent creation of tasks > 60 characters | Pass |
| Prevent creation of empty tasks | Pass |
| Edit existing task | Pass |
| Delete existing task | Pass |
| View task list | Pass |

Example of task creation test:
```python
def test_create_todo(self):
    """Test creating a new todo item"""
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(reverse('todo_list'), {'task': 'New Task'})
    self.assertEqual(response.status_code, 302)  # Redirects after creation
    self.assertTrue(Todo.objects.filter(todo_name='New Task').exists())
    messages = list(get_messages(response.wsgi_request))
    self.assertIn('Task "New Task" added successfully!', 
                 str(messages[0]))
```

### Task Status Tests
Example of status toggle test:
```python
def test_toggle_status(self):
    """Test toggling todo status"""
    self.client.login(username='testuser', password='testpass123')
    response = self.client.get(
        reverse('toggle_status', kwargs={'id': self.todo.id})
    )
    updated_todo = Todo.objects.get(id=self.todo.id)
    self.assertEqual(updated_todo.status, 'In Progress')
```

### Test Coverage Details

#### Model Tests
The `Todo` model is tested for:
- Field validations
- Default values
- User relationships
- Maximum length constraints

Example of model test:
```python
def test_todo_model(self):
    """Test Todo model creation and fields"""
    self.assertEqual(self.todo.todo_name, 'Test Task')
    self.assertEqual(self.todo.status, 'Not Started')
    self.assertEqual(self.todo.user, self.user)
```

#### View Tests
Views are tested for:
- HTTP response codes
- Template rendering
- Context data
- Form processing
- Message generation

Example of view test with message verification:
```python
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
```

#### Security Testing
Security tests verify:
- User isolation
- Authentication requirements
- Authorization checks
- CSRF protection

Example of security test:
```python
def test_user_cannot_edit_others_todos(self):
    """Test that users cannot edit other users' todo lists"""
    other_user = User.objects.create_user(
        username='otheruser',
        password='otherpass123'
    )
    other_todo = Todo.objects.create(
        todo_name='Other Task',
        status='Not Started',
        user=other_user
    )
    
    self.client.login(username='testuser', password='testpass123')
    response = self.client.post(
        reverse('edit', kwargs={'id': other_todo.id}),
        {'task': 'Hacked Task'}
    )
    self.assertEqual(response.status_code, 404)
```

## Manual Testing

While automated tests cover the core functionality, manual testing verified:

### Responsiveness Testing
- Testing performed using Firefox with Accessibility Properties
- Verified layout and functionality across different screen sizes:
  - Mobile: 320px, 375px, 425px
  - Tablet: 768px
  - Laptop: 1024px, 1440px
  - Desktop: 2560px

### Browser Compatibility
The application was manually tested on:
- Firefox (Version 122.0)
- Chrome (Version 121.0)
- Safari (Version 17.0)
- Edge (Version 120.0)

### User Interface Testing
- Verified all buttons and links are working
- Confirmed proper display of success/error messages
- Tested form submissions and validation feedback
- Checked accessibility features and ARIA labels

## Testing Tools Used
- Django TestCase framework
- Firefox Developer Tools
- Django Debug Toolbar
- Browser Developer Tools

## Test Execution
To run the automated test suite:
```bash
# Run all tests
python manage.py test

# Run tests with detailed output
python manage.py test -v 2

# Run a specific test
python manage.py test todo.tests.TodoTests.test_create_todo
```

All tests are located in the `tests.py` file within the todo app directory.


# Deployment

The repo was created in Github. Code was created and update updated in Gitpod.

The app was deployed on [Heroku here](https://todo-genie-65081f96d293.herokuapp.com/)

Secret Keys were connected to config vars in Heroku.

The Code Institute PostGres database was connected in Heroku.


#Future Features

Some features which were planned but left for future versions were:

- **Due dates:** To keep track of deadlines.
- **Reminders:** To prompt users of impending due dates.
- **Task Prioritisation:** And sorting.
- **Categories and Tags:** To organise and filter tasks.
- **Collaboration:** The ability to have multiple users sharing and accessing a task list.



# Credits and Thanks

Some of the basic coding principles came from the Code Institute's module "I Think Therefore I blog" and some of the views.py code came from watching Dennis Ivy's YouTube "To Do App" video: https://www.youtube.com/watch?v=4RWFvXDUmjo

Other resources used during troubleshooting were Stack Overflow, and W3CSchools.

The KonKhmer SleokChher Google Font used in the ToDo Genie logo text and Favicon is Copyright 2022 The Konkhmer Sleokchher Project Authors and licensed under the SIL Open Font License, Version 1.1. available with a FAQ at: http://scripts.sil.org/OFL

Thanks go to the entire bootcamp cohort I studied with at the Code Institute in summer 2024 and to the staff who have brought me a long way in such a short period of time.
