from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from core.forms import SignUpForm
from django.http import HttpResponse
from core.models import Appointment


# Create your views here.





class Signup(View):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)

        customer_group, created = Group.objects.get_or_create(name='Customer')

        # print(SignUpForm)
        # print(form.fields)
        # print(form.errors.as_json)
        # print(form.errors.as_data())


        if form.is_valid():
            user = form.save(commit=False)
            user.active = False
            user.save()
            customer_group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('core/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # form = SignUpForm()
            return render(request, 'core/signup.html', {'form': form})

class ActivateURL(View):

    def get(self, request, uidb, token):
        try:
            uid = urlsafe_base64_decode(uidb).decode()
            user = get_user_model()._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')










class Base(View):
    def get(self,request):
        return render(request, 'core/base.html')

class About(View):
    def get(self,request):
        return render(request, 'core/about.html')

class Blog(View):
    def get(self,request):
        return render(request, 'core/blog.html')

class Contact(View):
    def get(self,request):
        return render(request, 'core/contact.html')

class Dep(View):
    def get(self,request):
        return render(request, 'core/dep.html')

class Doctor(View):
    def get(self,request):
        return render(request, 'core/doctor.html')

class Elements(View):
    def get(self,request):
        return render(request, 'core/elements.html')

class Index(View):
    def get(self,request):
        return render(request, 'core/index.html')

class Services(View):
    def get(self,request):
        return render(request, 'core/services.html')

class Single_blog(View):
    def get(self,request):
        return render(request, 'core/single_blog.html')

class Appoinment(View):
    def get(self,request):
        return render(request, 'core/appointment.html')

    def post(self, request):
        date=request.POST["date"]
        name=request.POST["name"]
        age=request.POST["age"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        p_doctor=request.POST["p_doctor"]
        gender=request.POST["gender"]

        # print(date,name,age,phone,email,p_doctor,gender)

        data=Appointment(date=date, name=name, age=age, phone=phone, email=email, p_doctor=p_doctor, gender=gender)

        data.save()
        return render(request,'core/appointment.html')
