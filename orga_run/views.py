from django.shortcuts import render
import csv
from orga_run.models import Project , Product
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy

def load_project(file_path):
  reader = csv.DictReader(open(file_path))
  for row in reader:
    project = Project(name = row['Name'], client = ['Client'])
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
  template_name="orga_run/project_detail.html"
  success_url = reverse_lazy('project_list')


class ProductCreate(CreateView):
  model = Product
  success_url = reverse_lazy('product_list')


class ProductList(ListView):
  model = Product

