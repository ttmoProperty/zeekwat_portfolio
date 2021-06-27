from django.db import models
from django.urls import reverse

class Navbar(models.Model):
	logo = models.ImageField(upload_to='images/logo/%Y/%m/%d/')
	title = models.TextField()
	tab1 = models.TextField()
	tab2 = models.TextField()
	tab3 = models.TextField()
	tab4 = models.TextField()

	def __str__(self):
		return self.title

class Landing(models.Model):
	pre_text = models.TextField()
	main_text = models.TextField()
	line_text = models.TextField()
	download_link = models.FileField(upload_to='files/download_links/%Y/%m/%d/')
	background = models.ImageField(upload_to='files/background/%Y/%m/%d/', default='image.jpeg')

	def __str__(self):
		return self.main_text

class About(models.Model):
	profile = models.ImageField(upload_to='images/profiles/%Y/%m/%d/')
	title = models.TextField()
	subtitle = models.TextField()
	content = models.TextField()

	def __str__(self):
		return self.title

class Service(models.Model):
	service_title = models.TextField()
	service_content = models.TextField()

	def __str__(self):
		return self.service_title

class Category(models.Model):
	category_name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('category_name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('art_list_by_category', args=[self.slug])

class Art(models.Model):
	category = models.ForeignKey(Category, related_name='arts', on_delete=models.CASCADE)
	caption = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	artmage = models.ImageField(upload_to='images/artmages/%Y/%m/%d/')

	class Meta:
		ordering = ('caption',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.caption

	def get_absolute_url(self):
		return reverse('detail', args=[self.id, self.slug])

