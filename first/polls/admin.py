from django.contrib import admin
from polls.models import Choice

admin.site.register(Choice)

from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
	# Change order of fields:
	# fields = ['question', 'pub_date']

	# Create fieldsets with customized titles
	fieldsets = [
		('Bombe', 				{'fields': ['question']}),
		('Date Information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
admin.site.register(Poll, PollAdmin)