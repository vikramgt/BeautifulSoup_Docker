from django.db import models

class Data(models.Model):
	job_title = models.CharField(max_length=250)
	company = models.CharField(max_length=250)
	loc = models.CharField(max_length=250)
	
	class Meta:
		app_label = "bsdjango"
		
	def __str__(self):
		return self.job_title
