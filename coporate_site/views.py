from .form import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .form import ContactForm


def toppage(request):
    return render(request, 'top.html')


class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context
