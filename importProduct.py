import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_lims.settings")

from orga_run.models import Product


with open('product.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
  for row in reader:
    
    name=row['Nom du produit'] 
    #print( name)
    ref=row['Référence'] 
    #print( ref)
    real_cost=row['Prix (Catalogue)'] 
    #print( real_cost)
    reduce_cost=row['Prix (Remisé)'] 
    #print( reduce_cost)
    nb_react_by_samples = row['Nb de réactions / échantillon'] 
    #print( nb_react_by_samples)
    conditionement_nombre=row['Conditionnement'] 
    #print( conditionement_nombre )
    conditionement_type = row['ConditionnementType'] 
    #print( conditionement_type) 
    comment=row['Commentaires']
    #print( comment)
    
    product = Product(
      name = name,
      ref = ref,
      real_cost = real_cost,
      reduce_cost = reduce_cost,
      nb_react_by_samples = nb_react_by_samples,
      conditionement_nombre = conditionement_nombre,
      conditionement_type = conditionement_type,
      comment = comment
    )

    product.save()


