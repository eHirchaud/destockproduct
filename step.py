import os
import csv


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_lims.settings")

from orga_run.models import Product, Manip, StepProto

with open('step2.csv', 'r') as csvfile:

    reader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
    for row in reader:
      #print("-------")
      quoi = row['Quoi']
      #print(quoi)
      produit = row['Nom du produit']
      print(produit)
      ech = row['echantillon']
      #print(ech)
      manip = row['manip']
      #print(manip)
      print("_______")

      #manip_object = Manip.objects.get_or_create(name=quoi)
      product = Product.objects.get(name="Ion Xpress Plus Fragment Library Kit")
     # print(product.name)

