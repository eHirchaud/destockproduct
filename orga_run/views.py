from django.shortcuts import render
from decimal import *
import csv
from orga_run.models import Project, Product, Lot, Run, Sample, StepProto, Manip, EntryDestock
from django.core.urlresolvers import reverse_lazy
from orga_run.forms import ConnexionForm, DestockageForm, UploadRunForm, UploadStepForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth import authenticate, login
import chardet
import io
import codecs
import math


def load_project(file_path):
    reader = csv.DictReader(open(file_path))
    for row in reader:
        project = Project(name=row['Name'], client=['Client'])
        project.save()


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
    fields = ['product', 'current_stock', 'code_fabricant', 'code_tmpi', 'n_lot', 'peremption_date']


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


class EntryDestockCreate(CreateView):
    model = EntryDestock


class EntryDestockList(ListView):
    model = EntryDestock


class EntryDestockEdit(UpdateView):
    model = EntryDestock
    success_url = reverse_lazy('entrydestock_edit')


class EntryDestockDetail(DetailView):
    model = EntryDestock
    success_url = reverse_lazy('entrydestock_list')


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


def uploadStep(request):
    to_upload = True
    if request.method == 'POST':
        form = UploadStepForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            populateStep(f)
            to_upload = False
    else:
        form = UploadStepForm()
    return render(request, 'orga_run/uploadstep.html', locals())


def populateStep(csvfile):

    reader = csv.DictReader(codecs.iterdecode(csvfile, 'utf-8'), delimiter=',', quotechar='"')
    for row in reader:
        quoi = row['Quoi']
        produit = row['Nom du produit']
        ech = row['echantillon']
        if ech == '':
            ech = 0.0
        else:
            ech = float(ech)
        manip = row['manip']
        if manip == '':
            manip = 0.0
        else:
            manip = float(manip)

        manip_object, created_manip = Manip.objects.get_or_create(name=quoi)
        product, product_created = Product.objects.get_or_create(name=produit)
        step, step_created = StepProto.objects.get_or_create(
            manip=manip_object,
            product=product,
            reac_by_sample=ech,
            reac_by_manip=manip
            )


def uploadRun(request):
    to_upload = True

    if request.method == 'POST':
        form = UploadRunForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            manips = form.cleaned_data['manips']
            run = populateRun(f)
            destockage_run(manips, run)
            # calcul_cout_run(manips,run)
            entries = EntryDestock.objects.filter(run=run)
        to_upload = False
    else:
            form = UploadRunForm()
    return render(request, 'orga_run/uploadrun.html', locals())


def destockage_run(manips, run):
    for project in run.projects.all():
        samples = project.samples.filter(run=run)
        for manip in manips:
            for step in manip.steps_proto.all():
                # pour les produits par echantillons
                if step.reac_by_sample != 0.0:
                    # Calcul du nombre de réactions pour cette étape
                    reac_utilise_sample = step.reac_by_sample * samples.count()
                    # Calcul du cout pour tous les échantillons du projet (real et reduit)
                    cost_real = step.product.real_cost_by_sample * samples.count()
                    cost_reduce = step.product.reduce_cost_by_sample * samples.count()
                    # On reccupere le lot en cours
                    lot_current = Lot.objects.all().filter(product=step.product, current=True)[0]
                    # lots utilisés pour cette étape
                    lot_used = []
                    # on ajoute le lot en cours d'utilisation
                    lot_used.append(lot_current)
                    # Si dans le stock on ce qu'il faut, facile on retranche ce qu'on utilise au stock
                    # Et on sauvegarde
                    if lot_current.current_stock > reac_utilise_sample:
                        lot_current.current_stock = lot_current.current_stock - reac_utilise_sample
                        lot_current.save()
                    # Sinon c'est chaud patate
                    else:
                        # on compte le nombre de réactifs restant aprés l'utilisation du lot en cours
                        reac_utilise_sample = reac_utilise_sample - lot_current.current_stock
                        # on archive le lot en cours en changeant les parametres qu'il faut
                        # le status current à False et le nombre de réactif restant à 0
                        lot_current.current = False
                        lot_current.current_stock = 0
                        lot_current.save()
                        # On regarde combien de lot supplémentaires qu'il va nous falloir
                        nb_lots = reac_utilise_sample / lot_current.product.nb_react_by_samples
                        # Plusieurs cas de figure. Si il nous faut plus d'un lot
                        # Creer le nombre de supplémentaire complétement utilisé que l'on archive directement
                        if nb_lots > 1:
                            for n in range(1, math.ceil(nb_lots)):
                                tmp_lot = Lot(current=False, product=step.product, current_stock=0)
                                tmp_lot.save()
                                lot_used.append(tmp_lot)

                        # Puis ce qu'il va rester dans le dernier lot.
                        reac_restant = (nb_lots * step.product.conditionement_nombre) - reac_utilise_sample
                        # On créer un dernier lot courrant avec en réactif restant le nombre de réactif initial
                        # dans le lot
                        # moins le nombre de réactif que l'on a utilisé
                        tmp_lot = Lot(current=True, product=step.product, current_stock=reac_restant)
                        lot_used.append(tmp_lot)
                        tmp_lot.save()
                else:
                    reac_utilise_sample = 0.0
                    cost_real = step.product.real_cost_by_sample * (samples.count() / run.samples.count())
                    cost_reduce = 0.0

                reac_utilise_sample = step.reac_by_sample * samples.count()
                entrydestock, created_entry = EntryDestock.objects.get_or_create(
                    manip=manip,
                    project=project,
                    run=run,
                    product=step.product
                    )

                entrydestock.count_react = entrydestock.count_react + reac_utilise_sample
                entrydestock.cost_real = entrydestock.cost_real + cost_real
                entrydestock.cost_reduce = entrydestock.cost_reduce + cost_reduce
                entrydestock.save()
    return("TODO")
#
# def calcul_cout_run(manips,run):
#    for project in run.projects:
#        calcul_cout_project(run, project)
#    return("TODO")
#
# def destockage_project(run,project,manips)


def populateRun(csvfile):
    reader = csv.DictReader(codecs.iterdecode(csvfile, 'utf-8'), delimiter=',', quotechar='"')
    for row in reader:
        run_text = row['Run']
        project_text = row['Projet']
        sample_text = row['Echantillon']
        run, created = Run.objects.get_or_create(code=run_text)
        project, created = Project.objects.get_or_create(acro=project_text, code=project_text)
        sample, created_sample = Sample.objects.get_or_create(code=sample_text, project=project)
        run.projects.add(project)
        run.samples.add(sample)
    return(run)


class ManipCreate(CreateView):
    model = Manip


class ManipList(ListView):
    model = Manip


class ManipEdit(UpdateView):
    model = Manip
    success_url = reverse_lazy('manip_view_edit')


class ManipDetail(DetailView):
    model = Manip
    success_url = reverse_lazy('manip_view_list')
