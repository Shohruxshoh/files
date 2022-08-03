from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from .models import Files
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
# Create your views here.
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'files/signup.html'



def logout_view(request):
    logout(request)
    return redirect('home')
def home(request):

    context = {}
    return render(request, "files/home.html", context)

class FilesDetailView(DetailView):
    model = Files
    template_name = "files/detail.html"

class FilesUpdateView(UpdateView):
    model = Files
    template_name = 'files/edit.html'
    fields = ['file_name', 'files', 'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy('view')


class FilesDeleteView(DeleteView):
    model = Files
    template_name = 'files/delete.html'
    success_url = reverse_lazy('view')


class FilesListView(ListView):
    model = Files
    template_name = 'files/view.html'


class FilesCreateVeiw(CreateView):
    model = Files
    template_name = 'files/create.html'
    fields = ['user', 'file_name', 'files', 'image_one', 'image_two', 'image_three']
    success_url = reverse_lazy('home')
    