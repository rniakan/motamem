from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView



class AccountTemplateView(TemplateView):
    template_name = 'base/base_bootstrap.html'

    def get_context_data(self, **kwargs):
        account_list = Account.objects.all()
        kwargs.update({'accounts':account_list})
        return super(AccountTemplateView, self).get_context_data(**kwargs)

class AccountSaveTemplateView(CreateView):
    model = Account

class AccountListTemplateView(ListView):
    model = Account