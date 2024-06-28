from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View  # Import Django's base View class

from users.models import Profile
from users.signup_form import SignupForm  # Import your signup form


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'users/templates/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()  # Save the new user
            user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                Profile.objects.create(user=request.user)
                messages.success(request, 'Signup successful')
                return redirect('home')  # Redirect to the home page after successful login
        messages.error(request, 'Signup error, please try again')
        return render(request, 'users/templates/signup.html', {'form': form})
