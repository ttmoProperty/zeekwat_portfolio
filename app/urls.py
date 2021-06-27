from django.urls import path 
from .import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('<slug:category_slug>/', views.index, name='art_list_by_category'),
	# path('<slug:category_slug>/<int:id>/<slug:slug>/', views.detail, name='detail'),
]