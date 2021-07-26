from django import forms
from django.contrib.auth import get_user_model

from projects.models import Project, Task, TimeSheet

User = get_user_model()


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = (
            'name',
            'team',
            'is_archived',
        )

    def clean(self):
        cleaned_data = super(ProjectCreateForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        project = super().save(commit=False)
        if commit:
            project.save()
            self.save_m2m()
        return project


class TaskCreateForm(forms.ModelForm):
    due_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Task
        fields = (
            'name',
            'project',
            'due_date',
            'assigned_to',
            'task_status',
            'task_priority',
            'is_archived',
        )

    def clean(self):
        cleaned_data = super(TaskCreateForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        task = super().save(commit=False)
        if commit:
            task.save()
            self.save_m2m()
        return task


class TimeSheetCreateForm(forms.ModelForm):
    start_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    end_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = TimeSheet
        fields = (
            'task',
            'start_time',
            'end_time',
        )

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user", None)
        super(TimeSheetCreateForm, self).__init__(*args, **kwargs)
        self.fields["task"].queryset = Task.objects.filter(assigned_to=self.request_user)

    def clean(self):
        cleaned_data = super(TimeSheetCreateForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        time_sheet = super().save(commit=False)
        if commit:
            time_sheet.save()
        return time_sheet
