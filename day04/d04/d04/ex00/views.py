from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def render_index(request):
	context = {'title': "Ex00 : Markdown Cheatsheet."}
	return render(request, 'ex00/index.html', context)
