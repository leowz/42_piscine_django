from django.shortcuts import render
import datetime
import os.path
from ex02.form import MyForm
from django.conf import settings

filename = getattr(settings, "HISTORY_FILE", None)
if not filename:
	filename = 'form.log'

def read_file():
	hist = [];
	if os.path.isfile(filename):
		try:
			with open(filename) as f:
				hist = f.readlines()
		except Exception as e:
			print(e);
			exit(1);
	return hist;

def add_an_entry(msg):
	try:
		with open(filename, 'a') as f:
			f.write(msg + '\n');
	except Exception as e:
		print(e);
		exit(1);

def render_form(request):
	msgs = read_file()
	if request.method == 'POST':
		form = MyForm (request.POST)
		if form.is_valid():
			date = datetime.datetime.now()
			msg = form.cleaned_data['message']
			msg += '; ' + str(date)
			add_an_entry(msg)
			msgs.append(msg)
	else:
		form = MyForm ()

	return render ( request , 'form.html', {'form': form, 'msgs': msgs})