from django.conf.urls import patterns, url
from orga_run.views import *

urlpatterns = patterns('orga_run.views',
                       url(r'^project_new$',  ProjectCreate.as_view(), name='project_new'),
                       url(r'^project_list$', ProjectList.as_view(), name='project_list'),
                       url(r'^project_edit/(?P<pk>\d+)$', ProjectEdit.as_view(), name='project_edit'),
                       url(r'^project_detail/(?P<pk>\d+)$', ProjectDetail.as_view(), name='project_detail'),
                       # url(r'^connexion$', 'django.contrib.auth.views.login'),
                       url(r'^destockage$', 'destockage', name='destockage'),
                       url(r'^acceuil$', 'acceuil', name='acceuil'),
                       url(r'^uploadrun$', 'uploadRun', name='uploadRun'),

                       url(r'^product_new', ProductCreate.as_view(), name='product_new'),
                       url(r'^product_list$', ProductList.as_view(), name='product_list'),
                       url(r'^product_edit/(?P<pk>\d+)$', ProductEdit.as_view(), name='product_edit'),
                       url(r'^product_detail/(?P<pk>\d+)$', ProductDetail.as_view(), name='product_detail'),

                       url(r'^lot_new', LotCreate.as_view(), name='lot_new'),
                       url(r'^lot_list$', LotList.as_view(), name='lot_list'),
                       url(r'^lot_edit/(?P<pk>\d+)$', LotEdit.as_view(), name='lot_edit'),
                       url(r'^lot_detail/(?P<pk>\d+)$', LotDetail.as_view(), name='lot_detail'),

                       url(r'^run_new', RunCreate.as_view(), name='run_new'),
                       url(r'^run_list$', RunList.as_view(), name='run_list'),
                       url(r'^run_edit/(?P<pk>\d+)$', RunEdit.as_view(), name='run_edit'),
                       url(r'^run_detail/(?P<pk>\d+)$', RunDetail.as_view(), name='run_detail'),
                       
                       url(r'^sample_new', SampleCreate.as_view(), name='sample_new'),
                       url(r'^sample_list$', SampleList.as_view(), name='sample_list'),
                       url(r'^sample_edit/(?P<pk>\d+)$', SampleEdit.as_view(), name='sample_edit'),
                       url(r'^sample_detail/(?P<pk>\d+)$', SampleDetail.as_view(), name='sample_detail'),

                       url(r'^uploadstep$', 'uploadStep', name='uploadStep'),
                       
                       url(r'^manip_new', ManipCreate.as_view(), name='manip_new'),
                       url(r'^manip_list$', ManipList.as_view(), name='manip_list'),
                       url(r'^manip_edit/(?P<pk>\d+)$', ManipEdit.as_view(), name='manip_edit'),
                       url(r'^manip_detail/(?P<pk>\d+)$', ManipDetail.as_view(), name='manip_detail'),

                       
                       url(r'^entrydestock_new', EntryDestockCreate.as_view(), name='entrydestock_new'),
                       url(r'^entrydestock_list$', EntryDestockList.as_view(), name='entrydestock_list'),
                       url(r'^entrydestock_edit/(?P<pk>\d+)$', EntryDestockEdit.as_view(), name='entrydestock_edit'),
                       url(r'^entrydestock_detail/(?P<pk>\d+)$', EntryDestockDetail.as_view(), name='entrydestock_detail'),
                       
                       )
