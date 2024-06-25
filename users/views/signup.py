from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View  # Import Django's base View class
from users.signup_form import SignupForm  # Import your signup form


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()  # Save the new user
            user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
        return render(request, 'users/signup.html', {'form': form})
