from django.conf.urls import patterns, url
from orga_run.views import ProjectCreate, ProjectList, ProjectEdit, ProjectDetail, ProductCreate, ProductList

urlpatterns = patterns('orga_run.views',
  url(r'^new_project$',  ProjectCreate.as_view(), name='project_new'),
  url(r'^list_project$', ProjectList.as_view(), name='project_list'),
  url(r'^edit_project/(?P<pk>\d+)$', ProjectEdit.as_view(), name='project_edit'),
  url(r'^detail_project/(?P<pk>\d+)$', ProjectDetail.as_view(), name='project_detail'),

  url(r'^new_product', ProductCreate.as_view(), name='product_new'),
  url(r'^list_product$', ProductList.as_view(), name='product_list'),
  

)
