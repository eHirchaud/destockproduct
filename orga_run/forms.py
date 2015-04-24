from django import forms
from orga_run.models import Project


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class DestockageForm(forms.Form):
    PROJECT_CHOICES = [[x.id, x.code] for x in Project.objects.all()]
    date = forms.DateField()
    projects = forms.MultipleChoiceField(choices=PROJECT_CHOICES, required=False, widget=forms.CheckboxSelectMultiple())
    eGel = forms.FloatField(label="E-Gel")
    puce_bio_adn = forms.FloatField(label="Puce BioA ADN")
    puce_bioA_arn_nano = forms.FloatField(label="Puce BioA ARN Nano")
    puce_bioA_arn_pico = forms.FloatField(label="Puce BioA ARN Pico")

class UploadRunForm(forms.Form):
	file = forms.FileField(label="Fichier de run")