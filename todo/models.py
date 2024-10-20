from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """
    Represents a task "Todo" item with a name and a status.
    """
    todo_name = models.CharField(
        max_length=60,
        blank=False,
        help_text="The name of the task (max 60 characters)"
    )
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)