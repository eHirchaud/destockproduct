from django.shortcuts import render
import csv
from orga_run.models import Project, Product, Lot, Run
from orga_run.forms import ConnexionForm, DestockageForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login


def load_project(file_path):
    reader = csv.DictReader(open(file_path))
    for row in reader:
        project = Project(name=row['Name'], client=['Client'])
        project.save()
# Create your views here.



class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project_list')


class ProjectList(ListView):
    model = Project


class ProjectEdit(UpdateView):
    model = Project
    success_url = reverse_lazy('project_list')


class ProjectDetail(DetailView):
    model = Project
    template_name = "orga_run/project_detail.html"
    success_url = reverse_lazy('project_list')



class ProductEdit(UpdateView):
    model = Product
    success_url = reverse_lazy('product_edit')


class ProductDetail(DetailView):
    model = Product
    template_name = "orga_run/product_detail.html"
    success_url = reverse_lazy('product_list')


class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('product_list')


class ProductList(ListView):
    model = Product


class LotCreate(CreateView):
    model = Lot


class RunCreate(CreateView):
    model = Run

class RunList(ListView):
    model = Run

class RunEdit(UpdateView):
    model = Run
    success_url = reverse_lazy('run_edit')

class RunDetail(DetailView):
    model = Run
    success_url = reverse_lazy('run_list')


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def destockage(request):
    if request.method == "POST":
        form = DestockageForm(request.POST)
        if form.is_valid():
            envoi = True
    else:
        form = DestockageForm()
    return render(request, 'orga_run/destockage.html', locals())


def acceuil(request):
    return render(request, 'orga_run/acceuil.html', locals())
