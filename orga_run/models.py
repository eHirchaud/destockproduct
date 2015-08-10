from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    acro = models.CharField(max_length=30)
    code = models.CharField(max_length=8)
    client = models.CharField(max_length=50)
    date_start = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de création")

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length=100)
    ref = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50, default="divers")
#  conditionement =
    real_cost = models.FloatField(default=0.0)
    reduce_cost = models.FloatField(default=0.0)
    nb_react_by_samples = models.FloatField(default=0.0)
    conditionement_nombre = models.FloatField(default=0.0)
    conditionement_type = models.CharField(max_length=15)
#  reac_by_sample = models.DecimalField(decimal_places=2, max_digits = 5)
    real_cost_by_sample = models.FloatField(default=0)
    reduce_cost_by_sample = models.FloatField(default=0)
    comment = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Manip(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Sample(models.Model):
    code = models.CharField(max_length=20)
    project = models.ForeignKey(to=Project, related_name="samples")
    manips = models.ManyToManyField(Manip)

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code


class Run(models.Model):
    code = models.CharField(max_length=20)
    projects = models.ManyToManyField(Project)
    samples = models.ManyToManyField(Sample)

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code


class StepProto(models.Model):
    manip = models.ForeignKey(Manip, related_name="steps_proto")
    product = models.ForeignKey(Product, related_name="steps_proto")
    reac_by_sample = models.FloatField(default=0)
    reac_by_manip = models.FloatField(default=0)


class Lot(models.Model):
    product = models.ForeignKey(Product, related_name='lots', null=True)
    current_stock = models.FloatField(verbose_name="Nombre de réactions restantes", null=True)
    samples = models.ManyToManyField(Sample, null=True)
    code_fabricant = models.CharField(max_length=15)
    code_tmpi = models.CharField(max_length=10, null=True)
    n_lot = models.CharField(max_length=20, null=True)
    manip = models.ManyToManyField(Manip, null=True)
    open_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Date d'ouverture")
    peremption_date = models.DateTimeField(verbose_name="Date de péremption", null=True)
    current = models.BooleanField(default=True)


# class Application(models.Model):
#    lot = models.ForeignKey(Product)
#    protocole = models.ForeignKey(StepProto)

class EntryDestock(models.Model):
    manip = models.ForeignKey(Manip, related_name='entries_destock', null=True)
    product = models.ForeignKey(Product, related_name='entries_destock', null=True)
    project = models.ForeignKey(Project, related_name='entries_destock', null=True)
    count_react = models.FloatField(default=0)
    cost_real = models.FloatField(default=0)
    cost_reduce = models.FloatField(default=0)
    run = models.ForeignKey(Run, related_name='entries_destock', null=True)


class ActionProject(models.Model):
    date_start = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'action")
    action_description = models.TextField()
    # user = models.ForeignKey(User)
    project = models.ForeignKey(Project)


class Profil(models.Model):
    user = models.OneToOneField(User)
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatar/")
    signature = models.TextField(blank=True)
    inscrit_newlette = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
