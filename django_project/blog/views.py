from django.shortcuts import render
#7. when come to fuction home(), it simply return a <h1> Blog Home </h1>
def home(request):
	return render(request, 'blog/home.html')

def about(request):
	return render(request, 'blog/about.html')
# Create your views here.

#load templates

