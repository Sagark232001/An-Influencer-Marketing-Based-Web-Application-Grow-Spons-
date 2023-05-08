from . import views
from django.urls import path

urlpatterns = [
    path('',views.dashboardCmp, name='dashboardCmp'),
	path('creation/',views.creation,name="creation"),
	path('dashboard/filter', views.dashboardFilter, name="dashboardFilterCmp"),
	path('dashboard/save_post/', views.saved_post_view, name='cmp_save_post'),
	path('payment/<int:post_id>/', views.payment, name="payment"),
	path('transaction/', views.transaction, name="transaction"),
	path('sponsored/', views.sponsored, name="sponsored"),
	path('accept_mail/<int:id>/', views.accept_mail, name="accept_mail"),
 
 	path('profile/<int:id>/', views.profile_cmp, name='profile_cmp'),
	path('personal_post/<int:id>/', views.personal_post_cmp, name='personal_post_cmp'),
]