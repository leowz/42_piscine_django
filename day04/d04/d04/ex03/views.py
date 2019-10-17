from django.shortcuts import render

# Create your views here.
def show_table(request):
	range_list = [i for i in range(0, 51, 1) ];
	col_list = [0, 1, 2, 3];
	header = ['noir', 'rouge', 'bleu', 'vert'];
	context ={ 'title': "ex03: list", 'range_list': range_list, 'col_list': col_list, 'header': header };
	return render(request, 'list.html', context)
