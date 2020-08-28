from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# def register_view(request, *args, **kwargs):
#     if request.user.is_authenticated:
#         return redirect('blog-home')
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}, now you can log in.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, template_name='users/register.html', context={'form': form})


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')
#
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, template_name='users/profile.html', context=context)


class RegisterView(DetailView):

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog-home')
        form = UserRegisterForm()
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog-home')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, now you can log in.')
            return redirect('login')


class ProfileOverview(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, template_name=self.template_name, context=context)


class CustomProfileView(LoginRequiredMixin, ListView):
    model = User
    # context_object_name = 'custom'

    def get(self, request, *args, **kwargs):
        # def get_queryset(self):
        if self.request.user.username != self.kwargs.get('username'):
            # TODO kwargs.get() takes arguments from urls.py
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            return render(request, template_name=self.template_name, context={'custom': user})
            # return User.objects.filter(username=user.username).first()
        return redirect('profile')
