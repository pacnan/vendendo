from django.conf.urls import url
from . import views

app_name = 'crm'

urlpatterns = [

    url(r'^organization/(?P<pk>[0-9]+)/delete/$', views.OrganizationDelete.as_view(), name='organization-delete'),
    url(r'^organization/(?P<pk>[0-9]+)/activate/$', views.OrganizationActivate.as_view(), name='organization-activate'),
    url(r'^organization/(?P<pk>\d+)/$', views.OrganizationUpdate.as_view(), name='organization-update'),
    url(r'^organization/add/$', views.OrganizationCreate.as_view(), name='organization-add'),
    url(r'^organizations/$', views.OrganizationIndex.as_view(), name='organization-index'),

    url(r'^member/(?P<pk>[0-9]+)/deactivate/$', views.MemberDeactivate.as_view(), name='member-deactivate'),
    url(r'^member/(?P<pk>[0-9]+)/activate/$', views.MemberActivate.as_view(), name='member-activate'),
    url(r'^member/(?P<pk>[0-9]+)/delete/$', views.MemberDelete.as_view(), name='member-delete'),
    url(r'^member/(?P<pk>[0-9]+)/toinvite/$', views.MemberInvite.as_view(), name='member-invite'),
    url(r'^member/(?P<pk>[0-9]+)/altertype/$', views.MemberAlterType.as_view(), name='member-alter-type'),
    url(r'^invite/activate/$', views.MemberInviteActivate.as_view(), name='member-invite-activate'),
    url(r'^member/find/$', views.MemberFind.as_view(), name='member-find'),
    url(r'^member/add/$', views.MemberCreate.as_view(), name='member-add'),
    url(r'^member/join/$', views.MemberJoin.as_view(), name='member-join'),
    url(r'^members/$', views.MemberIndex.as_view(), name='member-index'),

    url(r'^occupationarea/(?P<pk>[0-9]+)/delete/$', views.OccupationAreaDelete.as_view(), name='occupationarea-delete'),
    url(r'^occupationarea/(?P<pk>[0-9]+)/$', views.OccupationAreaUpdate.as_view(), name='occupationarea-update'),
    url(r'^occupationarea/add/$', views.OccupationAreaCreate.as_view(), name='occupationarea-add'),
    url(r'^occupationarea/$', views.OccupationAreaIndex.as_view(), name='occupationarea-index'),

    url(r'^customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer-delete'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerUpdate.as_view(), name='customer-update'),
    url(r'^customer/add/$', views.CustomerCreate.as_view(), name='customer-add'),
    url(r'^customer/import/$', views.CustomerImport.as_view(), name='customer-import'),
    url(r'^customer/$', views.CustomerIndex.as_view(), name='customer-index'),

    url(r'^salestage/(?P<pk>[0-9]+)/up/$', views.SaleStageUp.as_view(), name='salestage-up'),
    url(r'^salestage/(?P<pk>[0-9]+)/down/$', views.SaleStageDown.as_view(), name='salestage-down'),
    url(r'^salestage/(?P<pk>[0-9]+)/delete/$', views.SaleStageDelete.as_view(), name='salestage-delete'),
    url(r'^salestage/(?P<pk>[0-9]+)/$', views.SaleStageUpdate.as_view(), name='salestage-update'),
    url(r'^salestage/add/$', views.SaleStageCreate.as_view(), name='salestage-add'),
    url(r'^salestage/$', views.SaleStageIndex.as_view(), name='salestage-index'),

    url(r'^customerservice/(?P<pk>[0-9]+)/$',
        views.CustomerServiceUpdate.as_view(),
        name='customerservice-update'),
    url(r'^customerservice/(?P<pk>[0-9]+)/delete/$',
        views.CustomerServiceDelete.as_view(),
        name='customerservice-delete'),
    url(r'^customerservice/add/$', views.CustomerServiceCreate.as_view(), name='customerservice-add'),
    url(r'^customerservice/$', views.CustomerServiceIndex.as_view(), name='customerservice-index'),

    url(r'^opportunity/(?P<pk>[0-9]+)/$', views.OpportunityUpdate.as_view(), name='opportunity-update'),
    url(r'^opportunity/(?P<pk>[0-9]+)/delete/$', views.OpportunityDelete.as_view(), name='opportunity-delete'),
    url(r'^opportunity/add/$', views.OpportunityCreate.as_view(), name='opportunity-add'),
    url(r'^opportunity/$', views.OpportunityIndex.as_view(), name='opportunity-index'),


    url(r'^activity/(?P<pk>[0-9]+)/delete/$', views.ActivityDelete.as_view(), name='activity-delete'),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ActivityUpdate.as_view(), name='activity-update'),
    url(r'^activity/add/$', views.ActivityCreate.as_view(), name='activity-add'),
    url(r'^activity/$', views.ActivityIndex.as_view(), name='activity-index'),

    url(r'^invitemessage/$', views.InviteMessageIndex.as_view(), name='invitemessage-index'),
    url(r'^invitemessage/(?P<pk>\w+)/activate/$', views.InviteMessageActivate.as_view(), name='invitemessage-activate'),
    url(r'^invitemessage/(?P<pk>\w+)/leave/$', views.InviteMessageLeave.as_view(), name='invitemessage-leave'),

    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard-index'),

    url(r'^help/$', views.Help.as_view(), name='help-index'),

    url(r'^success/$', views.SuccessPage.as_view(), name='success-index'),
    url(r'^error/$', views.ErrorPage.as_view(), name='error-index'),
]
