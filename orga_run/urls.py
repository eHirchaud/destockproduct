from django.conf.urls import patterns, url
from orga_run.views import *

urlpatterns = patterns('orga_run.views',
                       url(r'^new_project$',  ProjectCreate.as_view(), name='project_new'),
                       url(r'^list_project$', ProjectList.as_view(), name='project_list'),
                       url(r'^edit_project/(?P<pk>\d+)$', ProjectEdit.as_view(), name='project_edit'),
                       url(r'^detail_project/(?P<pk>\d+)$', ProjectDetail.as_view(), name='project_detail'),
                       # url(r'^connexion$', 'django.contrib.auth.views.login'),
                       url(r'^destockage$', 'destockage', name='destockage'),
                       url(r'^acceuil$', 'acceuil', name='acceuil'),
                       url(r'^uploadrun$', 'uploadRun', name='uploadRun'),

                       url(r'^new_product', ProductCreate.as_view(), name='product_new'),
                       url(r'^list_product$', ProductList.as_view(), name='product_list'),
                       url(r'^edit_product/(?P<pk>\d+)$', ProductEdit.as_view(), name='product_edit'),
                       url(r'^detail_product/(?P<pk>\d+)$', ProductDetail.as_view(), name='product_detail'),

                       url(r'^new_lot', LotCreate.as_view(), name='lot_new'),
                       url(r'^list_lot$', LotList.as_view(), name='lot_list'),
                       url(r'^edit_lot/(?P<pk>\d+)$', LotEdit.as_view(), name='lot_edit'),
                       url(r'^detail_lot/(?P<pk>\d+)$', LotDetail.as_view(), name='lot_detail'),

                       url(r'^new_run', RunCreate.as_view(), name='run_new'),
                       url(r'^list_run$', RunList.as_view(), name='run_list'),
                       url(r'^edit_run/(?P<pk>\d+)$', RunEdit.as_view(), name='run_edit'),
                       url(r'^detail_run/(?P<pk>\d+)$', RunDetail.as_view(), name='run_detail'),
                       
                       url(r'^new_sample', SampleCreate.as_view(), name='sample_new'),
                       url(r'^list_sample$', SampleList.as_view(), name='sample_list'),
                       url(r'^edit_sample/(?P<pk>\d+)$', SampleEdit.as_view(), name='sample_edit'),
                       url(r'^detail_sample/(?P<pk>\d+)$', SampleDetail.as_view(), name='sample_detail'),
                       )
