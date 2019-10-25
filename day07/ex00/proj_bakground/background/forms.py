from django import forms
from .models import File

class FileForm(forms.ModelForm):
	""" formulaire pour la classe File """
	class Meta:
		model = File
		fields = ['name', 'file']