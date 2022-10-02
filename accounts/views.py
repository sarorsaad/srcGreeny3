
from.models import Profile
from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from .forms import SingupForm,UserActivateForm



def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request, 'registration/profile.html',{'profile':profile})

def generate_code():
    length=8
    numbers='0123456789'
    code= ''.join(random.choice(numbers)for x in range (length))
    return code
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SingupForm(request.POST)
        if form.is_valid():
            username=form.cleaned.data['username']
            email=form.cleaned.data['email']
            myform=form.save()
            profile=Profile.objects.get(user__username=username)
            profile.active=False
            profile.save()

            send_mail(
              subject='Activate Your Account',
              message = f'use this code {profile.code} to avtivate your account', 
              from_email='sarorsaad@gmail.com',
              recipient_list=[email],
              fail_silently=False
              )
            return redirect(f'accounts/{username}/activate')

    else:
        form=SingupForm()
    return render(request, 'registration/signup.html',{'form':form})

def user_activate(request,username):
        profile=Profile.objects.get(user__username=username)
        if request.method=='POST':
            form=UserActivateForm(request.POST)
            if form.is_valid():
                code=form.cleaned_data['code']
                if profile.code==code:
                    profile.active=True
                    profile.code=''
                    profile.code_used=True 
                    return redirect('/accounts/login')
        else:
            form=UserActivateForm()
        return render(request, 'registration/activation.html',{'form':form})