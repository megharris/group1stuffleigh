from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'sis'
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    #re_path(r'^home/$', views.home, name='home'),
    path('tutor_list', views.tutor_list, name='tutor_list'),
    path('course_list', views.course_list, name='course_list'),
    path('schedule_list', views.schedule_list, name='schedule_list'),
    path('register/', views.register, name='register'),

    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('student_home', views.student_home, name='student_home'),

    path('tutor_dashboard', views.tutor_dashboard, name='tutor_dashboard'),
    path('tutor_home', views.tutor_home, name='tutor_home'),
    path('tutor_profile', views.tutor_profile, name='tutor_profile'),
    path('tutor_courses', views.tutor_courses, name='tutor_courses'),
    path('tutor_rosters', views.tutor_rosters, name='tutor_rosters'),
    path('tutor_wage', views.tutor_wage, name='tutor_wage'),

]