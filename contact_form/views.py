from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact_form.forms import ContactForm
from django.views.generic.base import TemplateView
from django.template.loader import get_template
from MotionPictures.settings import production
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form=form_class(data=request.POST)
        if form.is_valid():
            Name=request.POST.get('first_name','')
            Surname=request.POST.get('last_name','')
            CHOICES=request.POST.get('CHOICES','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            template = get_template('contact_template.txt')
            context =Context({
            "form":form
                })
            content=template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "24MotionPictures" +'',
                ['ajaymundhe21@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, "contact.html",Context)






      #  subject= 'site contact form'
       # from_email= base.EMAIL_HOST_USER
        #to_email=[save_it.email,'ajaymundhe21@gmail.com'] 
        #send_mail(subject,
         #       message, 
          #      from_email, 
           #     to_email,
            #    fail_silently=False)



