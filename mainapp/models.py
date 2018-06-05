from django.db import models
from datetime import datetime
# Create your models here.
class code_model(models.Model):
	custom_Key = models.CharField(max_length=100, primary_key=True)
	time_stamp = models.DateTimeField(default = datetime.now)
	HTML_code = models.CharField(max_length=100000)
	def __str__(self):
		return self.HTML_code