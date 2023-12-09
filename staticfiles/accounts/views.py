from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.

def User_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, 
                                username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("Muvoffaqqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Sizning profilingiz aktiv emas")
            else:
                return HttpResponse("Login yoki parolda xatolik bor!")
    else:
        form = LoginForm
        context = {
            'form': form
        }
    return render(request,"registration/login.html",context)






def dashboard_view(request):
    user = request.user

    return render(request, 'registration/view_profile.html', {'user_profile': user})

# def edit_profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile', username=user_profile.username)
#     else:
#         form = UserProfileForm(instance=user_profile)

#     return render(request, 'registration/edit_profile.html', {'form': form})
