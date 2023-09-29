from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Customer

def home(request):
    customers = Customer.objects.all()
    
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, Please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered, WELCOME!!!!")
            return redirect('home')
    else:
        form = SignUpForm() 
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer(request, pk):
    if request.user.is_authenticated:
        # Look up customer
        customer = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer': customer})
    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()  
        messages.success(request, "Customer Record Deleted")
        return redirect('home')    
    else:
        messages.success(request, "You must be logged in to do that...!")
        return redirect('home')
        

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Customer Added...")
                return redirect("home")
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect("home")
    

def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been updated...")
            return redirect("home")
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, "You must be logged in...")
        return redirect("home")
        
        
                    