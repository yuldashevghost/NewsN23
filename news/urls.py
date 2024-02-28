from django.urls import path

from news.views import home_page, contact_page, t_page, single_page, contact_create, advertise_page

app_name = 'news'

urlpatterns = [
    path('', home_page, name="home_page"),
    path('contact', contact_page, name='contact_page'),
    path('404-page', t_page, name='404_page'),
    path('new/<int:new_id>/', single_page, name='single_page'),
    path('contact-create', contact_create, name='contact_create'),
    path('advertise/', advertise_page, name='advertise')
]