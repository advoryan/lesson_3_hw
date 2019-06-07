from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from cart.models import User
from django.urls import reverse_lazy
from .forms import CreateUserForm, UpdateUserForm, UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin


class LoginView(auth_views.LoginView):
    template_name = 'alog/login.html'


class LogoutView(auth_views.LogoutView):
    extra_context = 'none'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'alog/password_templates/password_reset_form.html'
    email_template_name = 'alog/password_templates/password_reset_email.html'
    subject_template_name = 'alog/password_templates/password_reset_subject.txt'
    success_url = '/'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'alog/password_templates/password_reset_confirm.html'
    success_url = '/'


class CreateUser(CreateView):
    model = User
    template_name = 'alog/registration/create_user.html'
    form_class = CreateUserForm
    # form_class = UserCreationForm
    # success_url = reverse_lazy('log-in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return self.request.POST.get('next', '/')


class UpdateUser(UserPassesTestMixin, UpdateView):
    model = User
    template_name = "alog/registration/update_user.html"
    form_class = UpdateUserForm

    def get_success_url(self):
        print(self.object)
        return reverse_lazy('view-user', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class ViewUser(UserPassesTestMixin, DetailView):
    model = User
    template_name = "alog/registration/view_user.html"

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'alog/registration/password_change_form.html'
    success_url = reverse_lazy('change-password-done')


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = 'alog/registration/password_change_done.html'