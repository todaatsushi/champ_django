from django.shortcuts import render
from django.core.mail import EmailMessage
from django.utils import timezone

import os

from home.forms import ContactForm


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', 'None')
            email = request.POST.get('email', 'None')
            content = request.POST.get('content', 'None')
            sentiment = request.POST.get('sentiment', 'None')

            # Draft email & send to admin
            mail = EmailMessage(
                subject=f'Champ: {sentiment} Contact Email from {name} - {timezone.now()}',
                body=content,
                from_email=email,
                to=[os.environ.get('EMAIL_ADDRESS')],
            )

            mail.send()
            return render(request, 'home/thanks.html')

    context = {
        'form': form_class
    }

    return render(request, 'home/contact.html', context)
