import os
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_lims.settings")
from django.core.wsgi import get_wsgi_application

from orga_run.models import Product, Lot


application = get_wsgi_application()


with open('product.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t', quotechar='"')
    for row in reader:

        name = row['Nom du produit']
        # print( name)
        ref = row['Référence']
        supplier = row['Fournisseur']
        # print( ref)
        real_cost = row['Prix (Catalogue)']
        # print( real_cost)
        reduce_cost = row['Prix (Remisé)']
        # print( reduce_cost)
        nb_react_by_samples = row['Nb de réactions / échantillon']
        # print( nb_react_by_samples)
        conditionement_nombre = row['Conditionnement']
        # print( conditionement_nombre )
        conditionement_type = row['ConditionnementType']
        # print( conditionement_type)
        comment = row['Commentaires']
        # print( comment)

        product, created = Product.objects.get_or_create(name=name)

        print (product.name)
        product.ref = ref
        product.supplier = supplier
        product.real_cost = real_cost
        product.reduce_cost = reduce_cost
        product.nb_react_by_samples = nb_react_by_samples
        product.conditionement_nombre = conditionement_nombre
        product.conditionement_type = conditionement_type
        product.comment = comment
        product.real_cost_by_sample = round(float(real_cost)/float(conditionement_nombre), 2)
        product.reduce_cost_by_sample = round(float(reduce_cost)/float(conditionement_nombre), 2)
        product.save()

        lot, created_lot = Lot.objects.get_or_create(product=product, current=True)
        if created_lot:
            lot.current_stock = product.conditionement_nombre
            lot.code_fabricant = product.ref
            lot.save()
            print("Nouveau lot")
