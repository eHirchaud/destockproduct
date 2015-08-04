from django.shortcuts import render
import csv
from orga_run.models import Project, Product, Lot, Run, Sample
from orga_run.forms import ConnexionForm, DestockageForm, UploadRunForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
import chardet
import io
import codecs

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

class LotList(ListView):
    model = Lot

class LotEdit(UpdateView):
    model = Lot
    success_url = reverse_lazy('lot_edit')

class LotDetail(DetailView):
    model = Lot
    success_url = reverse_lazy('lot_list')

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


class SampleCreate(CreateView):
    model = Sample

class SampleList(ListView):
    model = Sample


class SampleEdit(UpdateView):
    model = Sample
    success_url = reverse_lazy('sample_edit')

class SampleDetail(DetailView):
    model = Sample
    success_url = reverse_lazy('sample_list')
   

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

def uploadRun(request):
    to_upload = True
    if request.method == 'POST':
        form = UploadRunForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']

            
            rows = populateRun(f)

        to_upload = False
    else:
            form = UploadRunForm()
    return render(request,'orga_run/uploadrun.html', locals())

def populateRun(csvfile):
    
    #csv = open(csvfile)
    #reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    reader = csv.DictReader(codecs.iterdecode(csvfile,'utf-8'), delimiter=',', quotechar='"')
    

    #reader = csv.reader(csvfile)
    
    
    
    #print(reader)
    #res = ""
    
    for row in reader:
       #print (',' .join(row))
       #print(row['Run'])
    # run = row['P']
        #res = res + row +"<br/>"
        run_text = row['Run']
        project_text = row['Projet']
        sample_text = row['sample']
    #    barcode = row['Barcode']
        
        
        run, created = Run.objects.get_or_create(code=run_text)
        project, created = Project.objects.get_or_create(acro=project_text, code=project_text)
        sample, created_sample = Sample.objects.get_or_create(code=sample_text, project= Project(id = project.id))
        
        run.projects.add(project)
        run.samples.add(sample)

    #print(res)
    
    
    return(run.code)     
