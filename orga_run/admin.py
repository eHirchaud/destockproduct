from django.contrib import admin
from orga_run.models import Project, Product

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('acro', 'code', 'client', 'date_start')
  list_filter = ('client',)
  date_hierarchy = 'date_start'
  
class ProductAdmin(admin.ModelAdmin):
  list_display =('name','ref','comment')
  
admin.site.register(Project, ProjectAdmin)
admin.site.register(Product,ProductAdmin)
