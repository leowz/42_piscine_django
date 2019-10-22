from django.shortcuts import render, HttpResponse
from ex04.form import MyForm
import psycopg2

# Create your views here.
def init(request):
	try:
		conn = psycopg2.connect(
			database='formationdjango',
			user='djangouser',
			password='secret',
			host='localhost',
			)

		cur = conn.cursor();

		cur.execute(
			"""
			CREATE TABLE IF NOT EXISTS ex04_movies (
			episode_nb serial PRIMARY KEY,
			title varchar(64) NOT NULL,
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL
			)
			"""
			)

		conn.commit();
		conn.close();
	except psycopg2.Error as e:
		return HttpResponse(str(e));
	return HttpResponse('OK');

def populate(request):
	try:
		conn = psycopg2.connect(
			database='formationdjango',
			user='djangouser',
			password='secret',
			host='localhost',
			)

		cur = conn.cursor();

		retStr = "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'1',
			'The Phantom Menace',
			'George Lucas',
			'Rick McCallum',
			'1999-05-19'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'2',
			'Attack of the Clones',
			'George Lucas',
			'Rick McCallum',
			'2002-05-16'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'3',
			'Revenge of the Sith',
			'George Lucas',
			'Rick McCallum',
			'2005-05-19'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'4',
			'A New Hope',
			'George Lucas',
			'Gary Kurtz, Rick McCallum',
			'1977-05-25'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'5',
			'The Empire Strikes Back',
			'Irvin Kershner',
			'Gary Kurtz, Rick McCallum',
			'1980-05-17'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'6',
			'Return of the Jedi',
			'Richard Marquand',
			'Howard G. Kazanjian, George Lucas, Rick McCallum',
			'1983-05-25'
			)
			"""
			);

		retStr += "OK <br />"
		cur.execute(
			"""
			INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
			VALUES(
			'7',
			'The Force Awakens',
			'J. J. Abrams',
			'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
			'2015-12-11'
			)
			"""
			);

		conn.commit();
		conn.close();
	except psycopg2.Error as e:
		return HttpResponse(str(e));
	return HttpResponse(retStr);

def display(request):
	try:
		conn = psycopg2.connect(
			database='formationdjango',
			user='djangouser',
			password='secret',
			host='localhost',
			)

		cur = conn.cursor();

		cur.execute(""" SELECT * FROM ex04_movies """);
		responses = cur.fetchall();
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
			for response in responses:
				retString += "<tr>"
				for col in response:
					retString += '<td>' + str(col) + '</td>'
				retString += "</tr>"
			retString += "</table>"
		else: 
			retString = "No data Available"
		conn.commit();
		conn.close();
	except psycopg2.Error as e:
		return HttpResponse(str(e));
	return HttpResponse(retString);

def remove(request):
	try:
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)
		
		curr = conn.cursor()

		if request.method == 'POST':
			form = MyForm(request.POST)
			curr.execute("DELETE FROM ex04_movies WHERE title LIKE '{0}'".format(request.POST['titleChoice']))
			conn.commit()
			curr.execute(""" SELECT title FROM ex04_movies """)
			response = curr.fetchall();

			retString = ""
			if response:
				data = []
				for r in response:
					data.append(str(r[0]))
				#form = MyForm(initial = data)
				form = MyForm(titleChoices = data)
				conn.close()
				return render ( request , 'form.html', {'form': form})

			else: 
				retString = "No data Available"
				conn.close()
				return HttpResponse(retString)

			conn.close()
			return HttpResponse('reussi')

		else:
			curr.execute(""" SELECT title FROM ex04_movies """)
			response = curr.fetchall()

			retString = ""
			if response:
				data = []
				for r in response:
					data.append(str(r[0]))
				form = MyForm(titleChoices = data)
				# print(form);
				conn.close()
				return render ( request , 'form.html', {'form': form})

			else: 
				retString = "No data Available"
				conn.close()
				return HttpResponse(retString)

	except psycopg2.Error as e:
		return HttpResponse(str(e));













