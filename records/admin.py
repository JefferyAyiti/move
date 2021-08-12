from django.contrib import admin
from .models import *

# Register your models here.
class Ministry_Admin(admin.ModelAdmin):
	list_display = ('mid', 'name', 'est')
admin.site.register(Ministry, Ministry_Admin)

class Minister_Admin(admin.ModelAdmin):
	list_display = ('persnr', 'last_name', 'first_name', 'appoint_year', 'rank', 'appointed', )
admin.site.register(Minister, Minister_Admin)

class Party_Admin(admin.ModelAdmin):
	list_display = ('abname', 'name', 'est',)
admin.site.register(Party, Party_Admin)

class Activity_Admin(admin.ModelAdmin):
	list_display =('act_id', 'act_name', 'category', 'start', 'status', 'end',)
admin.site.register(Activity, Activity_Admin)

class MP_Admin(admin.ModelAdmin):
	list_display = ('persnr', 'last_name', 'first_name', 'year_elect',)
admin.site.register(ParlMember, MP_Admin)

class Domain_Admin(admin.ModelAdmin):
	list_display = ('constituency','region', 'district', )
admin.site.register(Domain, Domain_Admin)




