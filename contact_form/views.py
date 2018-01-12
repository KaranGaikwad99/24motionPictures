from django.views.generic import TemplateView
from django.shortcuts import render
from .models import UserData
from django.template.context_processors import csrf

from .forms import ContactForm
# Create your views here.'''


'''def Data_view(request):
    form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        name=form.cleaned_data.get('Name')
        surname=form.cleaned_data.get('Surname'),
        choice=form.cleaned_data.get('Choice'),
        email=form.cleaned_data.get('Email'),
        message=form.cleaned_data.get('Message'),

        return redirect('index.html')

    else:
        form=ContactForm()

    return rendeyr(request,'layout/new_contact.html',{'form':form}) '''



'''def Data_view(request):
    form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index.html')
    #   text=form.cleaned_data['Name',]

    else:
        form= ContactForm()

    args={'form':form }
    return render (request,'layout/new_contact.html',args)'''

def Data_view(request):
    form=ContactForm(request.POST or None   )
    if form.is_valid():
        query=form.save(commit=False)
        query.save()
        form = ContactForm
    context = {
        "form":form,

    }
    return render (request,'layout/new_contact.html', context)