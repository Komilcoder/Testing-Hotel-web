from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from .models import *
from rooms.forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, CreateUserForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user


class HomeList(ListView):
    model = ToursitBlog
    template_name = 'rooms/index.html'
    context_object_name = 'object_list'

class IndexDetailView(DetailView):
    model = ToursitBlog
    template_name = 'rooms/index_detail.html'

    def get_context_data(self , *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = ToursitBlog.objects.all()
        return context



class AboutPage(ListView):
    model = About
    template_name = 'rooms/about.html'
    context_object_name = 'object_list'


class AboutDetailView(DetailView):
    model = About
    template_name = 'rooms/about_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        return context



class Secondabout(ListView):
    model = LocalGuest
    template_name = 'rooms/about.html' 
    context_object_name = 'object_list'

 

class SecondAboutDetail(DetailView):
    model = LocalGuest
    template_name = 'rooms/secondabout.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['secondary'] = LocalGuest.objects.all()
        return context           
   

@method_decorator(login_required, name='dispatch')
class PackageListView(ListView):
    model = Package
    template_name = 'rooms/packages.html'
    context_object_name='object_list'


class PackageDetailView(DetailView):
    model = Package
    template_name = 'rooms/pack_detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['package'] = Package.objects.all()
        return context


class PostList(ListView):
    model = Blog
    template_name = 'rooms/blog.html'
    context_object_name = 'object_list'




class PostDetailView(DetailView):
    model = Blog
    template_name = 'rooms/single-blog.html'

    def get_context_data(self , *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Blog.objects.all()
        return context


    

# !---  start forms here ---!

# created form
def contact_create(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()
    return render(request, 'rooms/contact.html',{'form':form})   


# edit form here

def contact_edit(request, pk=None):
    contact = get_object_or_404(Contact,pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm(instance=contact)
    return render(request,'rooms/contact_edit.html',{'form':form,'contact':contact})            
# ! ---- end form ---!



@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)     # this is authenticate login line 8
            return redirect('home')
            messages.info(request, 'Username Or Password is incorrect')
           

    context={}

    return render(request , 'registration/login.html',context)



def logoutuser(request):
    logout(request)                      # this  logout is authenticate line 8
    return redirect('login')   
    
     

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'registration/register.html',context)              
         