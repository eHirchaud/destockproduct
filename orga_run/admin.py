from django.contrib import admin
from orga_run.models import Project, Product, Sample, Run, Manip, Lot

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('acro', 'code', 'client', 'date_start',)
	list_filter = ('client',)
	date_hierarchy = 'date_start'


class ProductAdmin(admin.ModelAdmin):
  list_display =('name','ref','comment', )


class RunAdmin(admin.ModelAdmin):
	list_display = ('code', )


class SampleAdmin(admin.ModelAdmin): 
	list_display = ('code', 'project', )


class ManipAdmin(admin.ModelAdmin):
	liste_display = ('name',)


class LotAdmin(admin.ModelAdmin):
	list_display = ('product','current_stock','current', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Run, RunAdmin)
admin.site.register(Manip, ManipAdmin)
admin.site.register(Lot, LotAdmin)
