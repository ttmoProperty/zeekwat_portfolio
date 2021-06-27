from django.shortcuts import render, get_object_or_404
from .models import Navbar, Landing, About, Service, Category, Art
from django.core.paginator import Paginator 

def index(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	arts = Art.objects.all()
	
	art_paginator = Paginator(arts, 6)

	page_num = request.GET.get('page')

	page = art_paginator.get_page(page_num)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		arts = arts.filter(category=category)
	context = {
		'navs' : Navbar.objects.all(),
		'landings' : Landing.objects.all(),
		'abouts' : About.objects.all(),
		'services' : Service.objects.all(),
		'category' : category,
		'categories' : categories,
		# 'arts' : arts,
		'page' : page
	}
	return render(request, 'app/index.html', context)

# def detail(request, id, slug):
# 	art = get_object_or_404(Art, id=id, slug=slug)
# 	return render(request, 'app/index.html', {'art':art})