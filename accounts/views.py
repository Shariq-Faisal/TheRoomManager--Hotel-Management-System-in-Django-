from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'auth/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



User = get_user_model()
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Password do not match')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'User already taken')
            return redirect('register')
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password1
        )
        messages.success(request, 'Account Created Successfully')
        return redirect('login')
    
    return render(request, 'auth/register.html')

