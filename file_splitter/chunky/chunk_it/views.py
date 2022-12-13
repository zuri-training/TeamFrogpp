from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import Chunk_fileSerializer, File_resultSerializer
# from rest_framework import status
from rest_framework.response import Response
from .test_split import fileSplitter
from django.http import HttpResponse, HttpResponseRedirect
import zipfile
from .forms import ChunkFileForm
from .models import File_result, Chunk_file

# User authentication 
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
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
            form = AuthenticationForm()
            return render(request,'chunk_it/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'chunk_it/signin.html', {'form':form})
 
 
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('chunk_it:login'))

# User authentication End



class ChunkFile(APIView, LoginRequiredMixin):
    template = 'chunk_it/dashboard1.html'

    def get(self, request):
        form = ChunkFileForm()
        ctx = {"form": form}
        
        return render(request, self.template, ctx)


    def post(self, request):
        global form
        form = ChunkFileForm(request.POST, request.FILES)

        # def form_valid(self, form):
        #     form.instance.user = self.request.user
        #     return super().form_valid(form)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect('download/')

def download(request):
    if request.method == 'POST':
            ID = form.instance.id
            filenames = fileSplitter(ID)
            response = HttpResponse(content_type='application/zip')
            zip_file = zipfile.ZipFile(response, 'w')
            for filename in filenames:
                zip_file.write(filename)
            response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
            return response
            
    if request.method == 'GET':
        return render('download.html')


