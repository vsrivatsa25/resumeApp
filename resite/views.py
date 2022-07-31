from django.shortcuts import render,redirect
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
import random
from datetime import datetime

class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    form = ContactForm

    def get_context_data(self, **kwargs):
        context = {}
        context["img"] = str(random.randint(1, 10))
        start_date = datetime(year=2020, month=12, day=7)
        today = datetime.today()
        context["internship_experience"] = abs(start_date.year - today.year) * 12 + today.month - start_date.month
        return context

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = ContactForm(self.request.POST, self.request.FILES)

            if form.is_valid():
                newform = form.save(commit=False)
                newform.save()
                messages.success(
                    self.request, _('Thank you for getting in touch! Will get back to you shortly.'))
                return redirect('index')
        else:
            form = UserDetails()
            return render(request, 'index.html', {'form': form})
