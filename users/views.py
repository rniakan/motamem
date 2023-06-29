from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView

from users.models import Account


def login_user(request):
    if request.method == "POST":
        username = request.POST['log']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.add_message(request, messages.SUCCESS, "مشخصات وارد شده استباه می باشد")
            return redirect('main_page')
    else:
        return render(request, 'acc/login.html', {})


class UsersTemplateView(TemplateView):
    template_name = 'base/base_bootstrap.html'


class AccountTemplateView(TemplateView):
    template_name = 'base/base_bootstrap.html'

    def get_context_data(self, **kwargs):
        account_list = Account.objects.all()
        kwargs.update({'accounts': account_list})
        return super(AccountTemplateView, self).get_context_data(**kwargs)


class AccountSaveTemplateView(CreateView):
    model = Account


class AccountListTemplateView(ListView):
    model = Account

class profile_tamplateview(TemplateView):
    template_name = 'acc/user_profile.html'


