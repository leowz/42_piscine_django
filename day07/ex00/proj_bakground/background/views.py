from django.shortcuts import render
from .forms import FileForm
from .models import File
from django.views.generic import View

# Create your views here.
def home(request):
	files = File.objects.all()
	if request.method == 'POST' :
		form = FileForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save()
		else:
			print('formulaire invalide')
	else:
		form = FileForm()
	return render(request, "base.html" , {'form' : form,   'files' : files})