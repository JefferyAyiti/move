from django.db import models
from datetime import date

# Create your models here.
class Ministry(models.Model):
	mid = models.SmallAutoField(verbose_name='MinID', primary_key=True,)
	name = models.CharField(max_length=64)
	est = models.DateField(blank=True, default=date.today)

	def __str__(self):
		return "%s" %(self.name)
	class Meta:
		verbose_name = 'Ministry'
		verbose_name_plural = 'Ministries'
		ordering = ('name', 'est',)

class Minister(models.Model):
	persnr = models.SmallAutoField(verbose_name="PersNr", primary_key=True,)
	last_name = models.CharField(max_length=30,)
	first_name = models.CharField(max_length =30,)
	appoint_year = models.DateField(blank=True, default=date.today, verbose_name='YearOfAppointment')
	POST = [('MIN', 'Minister'),
	('DEP', 'Deputy Minister',)]
	rank = models.CharField(max_length=3,choices=POST,)
	appointed = models.ForeignKey('Ministry', on_delete= models.PROTECT,)

	def __str__(self):
		return "%s, %s" % (self.last_name, self.first_name)

	class Meta:
		verbose_name = 'Minister'
		verbose_name_plural = 'Ministers'
		ordering = ('rank','last_name','first_name',)

class Activity(models.Model):
	act_id = models.SmallAutoField(verbose_name = "ActivityID", primary_key=True)
	act_name= models.CharField(max_length=64)
	CAT = [('PROJ', 'Project'), ('INIT', 'Initiative'),]
	STAT = [('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Halted','Halted'), ('Abandoned', 'Abandoned')]
	category = models.CharField(max_length=4, choices=CAT,)
	start = models.DateField(blank=True,default=date.today)
	status = models.CharField(max_length=9,choices=STAT,)
	end = models.DateField(blank=True,default=date.today)

	def __str__(self):
		return "%s" % (self.act_name)

	class Meta: 
		verbose_name = 'Activity'
		verbose_name_plural = 'Activities'
		ordering = ('act_name', 'status',)

class Party(models.Model):
	abname = models.CharField(max_length=4, primary_key=True)
	name = models.CharField(max_length=30)
	est  =models.DateField(blank=True,default=date.today)

	def __str__(self):
		return "%s" % (self.abname)

	class Meta:
		verbose_name= 'Party'
		verbose_name_plural = 'Parties'
		ordering = ('est',)

class ParlMember(models.Model):
	persnr = models.SmallAutoField(verbose_name='PersNr', primary_key=True)
	last_name = models.CharField(max_length=30)
	first_name= models.CharField(max_length =30)
	year_elect = models.DateField(blank=True,default=date.today)
	no_terms = models.PositiveIntegerField(default=1)
	party = models.ForeignKey('Party', on_delete = models.PROTECT, default='NPP')
	elected_to = models.OneToOneField('Domain', on_delete=models.PROTECT)

	def __str__(self):
		return "%s, %s" % (self.last_name, self.first_name)

	class Meta:
		verbose_name = 'MP'
		verbose_name_plural = 'MPs'
		ordering = ('last_name','first_name', 'elected_to',)


class Domain(models.Model):
	region = models.CharField(max_length=32)
	district = models.CharField(max_length=32)
	constituency = models.CharField(max_length=64, primary_key=True)

	def __str__(self):
		return "%s, %s" % (self.region, self.constituency)

	class Meta:
		verbose_name = 'Domain'
		verbose_name_plural = 'Domains'
		ordering = ('region','constituency',)


# class Education(models.Model):
# 	persnr = models.ForeignKey()
# 	max_level = models.CharField()