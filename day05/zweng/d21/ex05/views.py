from django.shortcuts import render, HttpResponse
from ex05.form import MyForm
from ex05.models import Movies
import psycopg2

# Create your views here.

def populate(request):
	try:
		retStr = 'OK<br />'
		m = models.Movies(
			episode_nb='1',
			title = 'The Phantom Menace', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '1999-05-19'
			) 
		m.save()

		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='2',
			title = 'Attack of the Clones', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '2002-05-16'
			) 
		m.save()		
		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='3',
			title = 'Revenge of the Sith', 
			director = 'George Lucas', 
			producer = 'Rick McCallum', 
			release_date = '2005-05-19'
			) 
		m.save()		
		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='4',
			title = 'A New Hope', 
			director = 'George Lucas', 
			producer = 'Gary Kurtz, Rick McCallum', 
			release_date = '1977-05-25'
			) 
		m.save()		
		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='5',
			title = 'The Empire Strikes Back', 
			director = 'Irvin Kershner', 
			producer = 'Gary Kurtz, Rick McCallum', 
			release_date = '1980-05-17'
			) 
		m.save()		
		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='6',
			title = 'Return of the Jedi', 
			director = 'Richard Marquand', 
			producer = 'Howard G. Kazanjian, George Lucas, Rick McCallum', 
			release_date = '1983-05-25'
			) 
		m.save()		
		retStr += 'OK<br />'
		m = models.Movies(
			episode_nb='7',
			title = 'The Force Awakens', 
			director = 'J. J. Abrams', 
			producer = 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 
			release_date = '2015-12-11'
			) 
		m.save()	
	except Exception as e:
		return HttpResponse(str(e));
	return HttpResponse(retStr);

def display(request):
	try:
		responses  = models.Movies.objects.all()
		retString = ""
		if responses:
			retString = "<table border='1'>"
			retString += """<tr>
			<th>episode_nb</th>
			<th>title</th>
			<th>opening_crawl</th>
			<th>director</th>
			<th>producer</th>
			<th>release_date</th>
			</tr>
			"""
			for r in responses:
				retString += '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr><br />'.format(r.episode_nb, 
					r.title, r.opening_crawl, r.director, r.producer, r.release_date)
			retString += "</table>"
		else: 
			retString = "No data Available"
	except psycopg2.Error as e:
		return HttpResponse(str(e));
	return HttpResponse(retString);

def remove(request):
	try:
		if request.method == 'POST':
			form = MyForm(request.POST)
			r = Movies.objects.filter(title = request.POST['films'])
			r.delete()
			r = Movies.objects.all()

			listTitles = []
			for val in r:
				listTitles.append(val.title)
			if len(listTitles) > 0:
				form = MyForm(listTitles)
				return render ( request , 'form.html', {'form': form})
			else: 
				retString = "No data Available"
				return HttpResponse(retString)

		else:
			r = Movies.objects.all()
			listTitles = []
			for val in r:
				listTitles.append(val.title)
			if len(listTitles) > 0:
				form = MyForm(listTitles)
				return render ( request , 'form.html', {'form': form})
			else: 
				retString = "No data Available"
				return HttpResponse(retString)

	except psycopg2.Error as e:
		return HttpResponse(str(e));
















