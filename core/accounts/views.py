from django.shortcuts import render ,redirect 
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from .forms import  LoginForm , UserRegisterForm , ProfileUpdateForm , UserDocumentForm 
from .models import Profile , UserDocument , Mostanadat 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout 



def custom_404(request, exception):
    return render(request, 'accounts/404.html', status=404)


class MostanadatView(View):
    template_name = 'accounts/mostanadat_list.html'
    
    def get(self,request):
        documents = Mostanadat.objects.all()

        
        
        context = {
            'documents':documents
        }
        
        return render(request,self.template_name,context)

class UserDocumentView(LoginRequiredMixin, View):
    template_name = 'accounts/documents.html'
    form_class = UserDocumentForm

    def get(self, request):
        document, created = UserDocument.objects.get_or_create(user=request.user)
        form = self.form_class(instance=document)
        return render(request, self.template_name, {'form': form, 'document': document})

    def post(self, request):
        document, created = UserDocument.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('accounts:documents')  
        return render(request, self.template_name, {'form': form, 'document': document})


class ProfileView(View):
    
    
    template_name = "accounts/profile.html"
    
    def get(self,request):
        user_found = User.objects.get(username = request.user )
        user_profile = Profile.objects.get(user=user_found)
        
        context = {
            'profile':user_profile
        }
        return render(request,self.template_name,context)


class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm  

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:profile')
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username_input = form.cleaned_data["username"]
            password_input = form.cleaned_data['password']
            user = authenticate(request, username=username_input, password=password_input)
            print(f"**** user : {user} ****")
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    
    def get(self,request):
        logout(request)
        return redirect('accounts:login')

            
class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:profile')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('accounts:profile')

        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile') 
        return render(request, self.template_name, {'form': form})
    

class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/profile_edit.html'
    form_class = ProfileUpdateForm

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')  # بازگشت به صفحه پروفایل
        return render(request, self.template_name, {'form': form})