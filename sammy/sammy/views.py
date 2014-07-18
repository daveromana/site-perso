#-*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label=u"Votre adresse mail")
    #renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    
from django.shortcuts import render
from django.http import HttpResponseRedirect

def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            
            from django.core.mail import send_mail
            send_mail(sujet, message, envoyeur, ['sa56@hotmail.ch'], fail_silently=False)
            
            return HttpResponseRedirect('/merci')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'toto':3.1415})