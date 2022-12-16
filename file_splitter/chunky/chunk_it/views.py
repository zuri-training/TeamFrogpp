from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# from rest_framework import status
from .test_split import fileSplitter
from django.http import HttpResponse, HttpResponseRedirect
import zipfile
from .forms import ChunkFileForm
from .models import File_result, Chunk_file, convert_bytes
from .validators import compare_size

# User authentication 
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def landingpage(request):
    if request.method == 'GET':
        return render(request, 'chunk_it/landingpg.html')
 
def signup(request):
 
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('chunk_it:dashboard'))
     
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
 
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username = username,password = password)
            # login(request, user)
            return HttpResponseRedirect(reverse_lazy('chunk_it:dashboard'))
         
        else:
            return render(request,'chunk_it/signup.html',{'form':form})
     
    else:
        form = CustomUserCreationForm()
        return render(request,'chunk_it/signup.html',{'form':form})
 
 
def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('chunk_it:dashboard'))
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse_lazy('chunk_it:dashboard'))
        else:
            messages.error(request,"Your Username and  Password didn't match. Please try again")
            form = AuthenticationForm()
            return render(request,'registration/login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})
 
 
# def signout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse_lazy('chunk_it:login'))

# User authentication End

class Dashboard(LoginRequiredMixin, View):  
    def get(self, request):
        return render(request, 'chunk_it/dashboard.html')


class ChunkFile( LoginRequiredMixin, View):

    template = 'chunk_it/chunkpg.html'

    def get(self, request):
        form = ChunkFileForm()
        ctx = {"form": form}
        
        return render(request, self.template, ctx)


    def post(self, request):
        form = ChunkFileForm(request.POST, request.FILES)

        def form_valid(self, form):
            
            totalfilesize = form.file.size
            userdefinedsize = convert_bytes(form.size_num, form.size_string)
            compare_size( totalfilesize, userdefinedsize)
            return super().form_valid(form)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        mainform = form.save()
        mainform.user = request.user
        mainform.save()
        global ID
        ID = form.instance.id


def download(request):
        zip_folder = "filesplit.zip"
        filenames = fileSplitter(ID)
        response = HttpResponse(request, content_type='application/zip')
        with zipfile.ZipFile(zip_folder, 'a') as zip_file:
            for filename in filenames:
                zip_file.write(filename)
        response['Content-Disposition'] = 'attachment; filename={}'.format(zip_folder)
        return response

            



class ContactUs(View):
    def get(self, request):
        return render(request, 'chunk_it/contactus.html')

class Privacy(View):
    def get(self, request):
        return render(request, 'chunk_it/privacy.html')

class Forget(View):
    def get(self, request):
        return render(request, 'chunk_it/forget.html')