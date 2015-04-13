import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_lims.settings")

from orga_run.models import Product


with open('product.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
  for row in reader:
    print(row['Nom du produit'])
