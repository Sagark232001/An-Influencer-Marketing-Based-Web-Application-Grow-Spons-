from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
	path('view/<int:pk>', viewinf, name='viewinf'),
    path('influencer_details/', influencer_details, name="influencer_details"),
    path('dashboard/', dashboardInf, name="dashboardInf"),
	path('dashboard/filter', dashboardFilter, name="dashboardFilter"),
    path('add_post/', influencerPost, name="influencerPost"),
	path('save_post/', save_post, name='save_post'),
	path('saved_post_view/', saved_post_view, name='saved_post_view'),
	path('remove_saved_post/', remove_saved_post, name='remove_saved_post'),
	path('profile/', profile, name='profile'),
	path('edit_profile/', edit_profile, name='edit_profile'),
	path('personal_post/', personal_post, name='personal_post'),
	path('delete_post/<int:id>/', delete_post, name='delete_post'),
	path('notification/', notification, name='notification'),
	path('accept_request/<int:post_id>/<int:spon_id>/', accept_request, name='accept_request'),
	path('display_modal/<int:work_id>', display_modal, name='display_modal'),
	path('transaction/', transaction, name='transactioninf'),


    path('login/', loginHandle, name='login'),
    path('register/', signupHandle, name='signUp'),
    path('logout/', handleLogout, name='logout'),
    path('company_register/', companySignupHandle, name='companySignupHandle'),



    path('reset_password/',
	 auth_views.PasswordResetView.as_view(template_name = 'authentication/password_reset.html'),
	  name='reset_password'), #submit email form
	path('reset_password_sent/',
	 auth_views.PasswordResetDoneView.as_view(template_name = 'authentication/password_reset_sent.html'),
	  name='password_reset_done'), #Email send and reset
	path('reset/<uidb64>/<token>',
	 auth_views.PasswordResetConfirmView.as_view(template_name = 'authentication/password_reset_form.html'),
	  name='password_reset_confirm'), #link to reset and email
	path('reset_password_complete/',
	 auth_views.PasswordResetCompleteView.as_view(template_name = 'authentication/password_reset_done.html'),
	  name='password_reset_complete'), #password successfully send
]