from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.utils import duration_in_days, time_difference_in_hours

User = get_user_model()


class Project(models.Model):
    name = models.CharField(
        _("Project Name"),
        max_length=120,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='project_creator',
        null=True
    )

    project_admin = models.ManyToManyField(
        "accounts.User",
        related_name="project_admin",
    )

    team = models.ManyToManyField(
        User,
        related_name="project_team",
        blank=True
    )

    is_archived = models.BooleanField(
        _("Project is Archived or Not"),
        default=False,
    )

    created = models.DateTimeField(
        _("Project Create time"),
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        _('Project Update Time'),
        auto_now=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.name

    @property
    def sys_id(self):
        return f'PRJ-{str(self.id).zfill(6)}'


class Task(models.Model):
    # Task Status Variables
    NEW = "new"
    IN_PROGRESS = "in_progress"
    TO_BE_REVIEWED = "to_be_reviewed"
    TESTED = "tested"
    PENDING = "pending"
    DONE = "done"

    # Task Priority Variables
    NORMAL = "normal"
    LOWEST = "lowest"
    LOW = "low"
    HIGH = 'high'
    HIGHEST = 'highest'

    # Status Choices
    STATUS_CHOICES = (
        (NEW, _("New")),
        (IN_PROGRESS, _("In Progress")),
        (TO_BE_REVIEWED, _("To Be Reviewed")),
        (TESTED, _("Tested")),
        (PENDING, _("Pending")),
        (DONE, _("Done"))
    )

    # Priority Choices
    PRIORITY_CHOICES = (
        (NORMAL, _("Normal")),
        (LOWEST, _("Lowest")),
        (LOW, _("Low")),
        (HIGH, _("High")),
        (HIGHEST, _("Highest"))
    )

    name = models.CharField(
        _("Task Name"),
        max_length=150,
    )

    due_date = models.DateTimeField(
        _("Task Due Date"),
        blank=True,
        null=True
    )

    assigned_to = models.ManyToManyField(
        "accounts.User",
        related_name="task",
    )

    task_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="NEW"
    )

    task_priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default="NORMAL"
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name='task_creator',
        null=True
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="task",
        null=True,
        default=1
    )

    is_archived = models.BooleanField(
        _("Task is Archived or Not"),
        default=False,
    )

    created = models.DateTimeField(
        _('Task Create Date'),
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        _("Task Update Date"),
        auto_now=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Task'

    def __str__(self):
        return self.name

    @property
    def sys_id(self):
        return f'TSK-{str(self.id).zfill(6)}'

    @property
    def total_task_time(self):
        duration_in_seconds = sum([i.duration_in_seconds for i in self.time_sheet.all()])
        duration = duration_in_days(duration_in_seconds)
        return duration


class TimeSheet(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="time_sheet",
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name='created_by_user',
        null=True
    )

    start_time = models.DateTimeField(
        _("Task Start Time"),
        blank=True,
        null=True
    )

    end_time = models.DateTimeField(
        _("Task End Date"),
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _('Task Create Date'),
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Task Time Sheet'

    def __str__(self):
        return f'{self.id} | {self.task.name}'

    @property
    def sys_id(self):
        return f'TSH-{str(self.id).zfill(6)}'

    @property
    def duration(self):
        difference = self.end_time - self.start_time
        duration = time_difference_in_hours(difference)
        return duration

    @property
    def duration_in_seconds(self):
        difference = self.end_time - self.start_time
        seconds = difference.total_seconds()
        return seconds
