from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import localtime
from django.views.generic import FormView, RedirectView, TemplateView

from accounts.forms import UserCreateForm, UserLoginForm
from projects.models import Task
from utils.messages import SYSTEM_ERR_MSG

User = get_user_model()


class UserDashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user_dashboard.html'

    def get_context_data(self, **kwargs):
        # import ipdb; ipdb.set_trace()
        context = super().get_context_data(**kwargs)

        user = self.request.user
        if user.is_superuser:
            context['task_due_today'] = Task.objects.filter(due_date__date=localtime().date()).exclude(task_status='done')
            context['upcoming_task'] = Task.objects.filter(due_date__date__gte=localtime().date()).exclude(task_status='done')
        elif user.is_admin:
            context['task_due_today'] = Task.objects.filter(project__project_admin__in=[user], due_date__date=localtime().date()).exclude(task_status='done')
            context['upcoming_task'] = Task.objects.filter(project__project_admin__in=[user], due_date__date__gte=localtime().date()).exclude(task_status='done')
        elif user.is_employee:
            context['task_due_today'] = Task.objects.filter(project__team__in=[user], due_date__date=localtime().date()).exclude(task_status='done')
            context['upcoming_task'] = Task.objects.filter(project__team__in=[user], due_date__date__gte=localtime().date()).exclude(task_status='done')
        return context


class UserSignUpView(FormView):
    """Customer SignUp View"""
    form_class = UserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:user_dashboard')

    def form_valid(self, form):
        self.object = form.save()
        return super(UserSignUpView, self).form_valid(form)


class UserLoginView(FormView):
    """Customer login view"""
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:user_dashboard')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(self.request, user)
            return super(UserLoginView, self).form_valid(form)
        messages.error(self.request, SYSTEM_ERR_MSG['INVALID_CREDENTIALS'])
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UserLogoutView(RedirectView):
    pattern_name = 'pages:homepage'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)
