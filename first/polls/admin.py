from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# Change order of fields:
	# fields = ['question', 'pub_date']

	# Create fieldsets with customized titles
	fieldsets = [
		('Bombe', 				{'fields': ['question']}),
		('Date Information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)