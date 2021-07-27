# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView

from projects.forms import ProjectCreateForm, TaskCreateForm, TimeSheetCreateForm
from projects.models import Project, Task, TimeSheet


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """
    Project Create View
    """
    form_class = ProjectCreateForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:project_dashboard')

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """
    Project Create View
    """
    queryset = Project.objects.all()
    form_class = ProjectCreateForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:project_dashboard')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """
    Task Delete View
    """

    model = Project
    success_url = reverse_lazy('projects:project_dashboard')

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Task Create View
    """
    form_class = TaskCreateForm
    template_name = 'projects/task_create.html'
    success_url = reverse_lazy('projects:task_dashboard')

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Task Create View
    """
    queryset = Task.objects.all()
    form_class = TaskCreateForm
    template_name = 'projects/task_create.html'
    success_url = reverse_lazy('projects:task_dashboard')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Task Delete View
    """

    model = Task
    success_url = reverse_lazy('projects:task_dashboard')

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)


class TimeSheetCreateView(LoginRequiredMixin, CreateView):
    """
    Task Create View
    """
    form_class = TimeSheetCreateForm
    template_name = 'projects/time_sheet_create.html'
    success_url = reverse_lazy('projects:time_sheet_dashboard')

    def get_form_kwargs(self):
        kwargs = super(TimeSheetCreateView, self).get_form_kwargs()
        kwargs['request_user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()
        return super(TimeSheetCreateView, self).form_valid(form)


class TimeSheetUpdateView(LoginRequiredMixin, UpdateView):
    """
    Task Create View
    """
    queryset = TimeSheet.objects.all()
    form_class = TimeSheetCreateForm
    template_name = 'projects/time_sheet_create.html'
    success_url = reverse_lazy('projects:time_sheet_dashboard')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super(TimeSheetUpdateView, self).form_valid(form)


class ProjectDashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'projects/project_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser:
            context['project_list'] = Project.objects.all()
        elif user.is_employee:
            context['project_list'] = Project.objects.filter(team__in=[user])
        elif user.is_admin:
            context['project_list'] = Project.objects.filter(project_admin__in=[user])
        else:
            pass

        return context


class TaskDashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'projects/task_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser:
            context['task_list'] = Task.objects.all()
        elif user.is_employee:
            context['task_list'] = Task.objects.filter(assigned_to=user)
        elif user.is_admin:
            context['task_list'] = Task.objects.filter(project__project_admin__in=[user])
        else:
            pass

        return context


class TimeSheetDashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'projects/time_sheet_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser:
            context['time_sheet_list'] = TimeSheet.objects.all()
        elif self.request.user.is_employee:
            context['time_sheet_list'] = TimeSheet.objects.filter(created_by=user)
        else:
            pass

        return context
