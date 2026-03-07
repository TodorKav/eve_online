from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from eve.accounts.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
UserModel = get_user_model()

class UserCreateView(UserPassesTestMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    model = UserModel
    form_class = CustomUserCreationForm

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        return True


class UserEditView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'accounts/profile_edit.html'
    model = UserModel
    form_class = CustomUserChangeForm
    success_message = "Your profile was successfully updated."

    def get_success_url(self):
        return reverse_lazy('accounts:profile_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView,):
    template_name = 'accounts/profile_detail.html'
    model = UserModel

    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False