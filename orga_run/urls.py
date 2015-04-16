from django.conf.urls import patterns, url
from orga_run.views import ProjectCreate, ProjectList, ProjectEdit, ProjectDetail, ProductCreate, ProductList, ProductDetail, ProductEdit, LotCreate

urlpatterns = patterns('orga_run.views',
  url(r'^new_project$',  ProjectCreate.as_view(), name='project_new'),
  url(r'^list_project$', ProjectList.as_view(), name='project_list'),
  url(r'^edit_project/(?P<pk>\d+)$', ProjectEdit.as_view(), name='project_edit'),
  url(r'^detail_project/(?P<pk>\d+)$', ProjectDetail.as_view(), name='project_detail'),
 # url(r'^connexion$', 'django.contrib.auth.views.login'),
  url(r'^destockage$','destockage', name='destockage'),
  url(r'^acceuil$','acceuil', name='acceuil'),

  url(r'^new_product', ProductCreate.as_view(), name='product_new'),
  url(r'^list_product$', ProductList.as_view(), name='product_list'),
  url(r'^edit_product/(?P<pk>\d+)$', ProductEdit.as_view(), name='product_edit'),
  url(r'^detail_product/(?P<pk>\d+)$', ProductDetail.as_view(), name='product_detail'),
  
  url(r'^new_lot$',  LotCreate.as_view(), name='lot_new'),

)
