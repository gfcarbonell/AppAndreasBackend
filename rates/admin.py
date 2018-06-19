# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
	list_display = ('lot', 'location', 'rate', 'description', 'observation')
	search_fields  = ['lot', 'location', 'rate', 'description', 'observation']
	fieldsets = (
        ('Rate Info', {'fields':('lot', 'location', 'rate')}),

        ('Extra info', {'fields':('description', 'observation')}),
    )

	class Meta:
		model = Rate