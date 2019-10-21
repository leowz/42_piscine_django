from django.shortcuts import render, HttpResponse
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
			CREATE TABLE IF NOT EXISTS ex00_movies (
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
