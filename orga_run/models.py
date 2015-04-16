from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
  acro = models.CharField(max_length=30)
  code = models.CharField(max_length=8)
  client = models.CharField(max_length=50)
  date_start = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
  


class Product(models.Model):
  name = models.CharField(max_length = 100)
  ref = models.CharField(max_length = 50)
#  conditionement = 
  real_cost = models.FloatField()
  reduce_cost = models.FloatField()
  nb_react_by_samples = models.FloatField()
  conditionement_nombre = models.FloatField()
  conditionement_type = models.CharField(max_length=15)
#  reac_by_sample = models.DecimalField(decimal_places=2, max_digits = 5)  
  comment = models.TextField()
  

class Manip(models.Model):
  name = models.CharField(max_length = 100)

class Sample(models.Model):
  code = models.CharField(max_length=20)
  project = models.ForeignKey(Project)
  manips = models.ManyToManyField(Manip)

class Run(models.Model):
  code = models.CharField(max_length=20)  
  projects = models.ManyToManyField(Project)
  samples = models.ManyToManyField(Sample)

class StepProto(models.Model):
  manip = models.ForeignKey(Manip)
  products = models.ForeignKey(Product)
  manip = models.ForeignKey(Manip)
  reac_by_samples = models.DecimalField(decimal_places=2, max_digits = 5) #Double
  reac_by_manip = models.DecimalField(decimal_places=2, max_digits = 5) #Double


class Lot(Product):
  current_stock = models.IntegerField(verbose_name="Nombre de réactions restantes")
  samples = models.ManyToManyField(Sample)
  code_fabricant = models.CharField(max_length = 15)
  code_tmpi = models.CharField(max_length = 10)
  n_lot = models.CharField(max_length = 20,null=True )
  manip = models.ManyToManyField(Manip)
  open_date = models.DateTimeField(auto_now=True, auto_now_add = False,verbose_name="Date d'ouverture", )
  peremption_date = models.DateTimeField(verbose_name="Date de péremption", null=True)

class Application(models.Model):
  lot = models.ForeignKey(Product)
  protocole = models.ForeignKey(StepProto)

class ActionProject(models.Model):
  date_start = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'action")
  action_description = models.TextField() 
  #user = models.ForeignKey(User)
  project = models.ForeignKey(Project)

class Profil(models.Model):
  user = models.OneToOneField(User)
  site_web = models.URLField(blank=True)
  avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")
  signature = models.TextField(blank = True)
  inscrit_newlette = models.BooleanField(default=False)

  def __str__(self):
    return "Profil de {0}".format(self.user.username)
