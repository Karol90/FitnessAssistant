from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fitness.views.home', name='home'),
    # url(r'^fitness/', include('fitness.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loguj/', 'uzytkownicy.views.login'),
    url(r'^rejestracja/', 'uzytkownicy.views.register_view'),
    url(r'^uzytkownik', 'uzytkownicy.views.user_view'),
    url(r'^profil', 'uzytkownicy.views.profile_view'),
    url(r'^edytuj-profil', 'uzytkownicy.views.edit_profile_view'),
    url(r'^dodaj-produkt', 'posilki.views.add_product'),
    url(r'^dodaj-posilek', 'posilki.views.add_meal'),
    url(r'^wyloguj', 'uzytkownicy.views.logout_view'),
    url(r'^blad-logowania/', 'uzytkownicy.views.blad_logowania'),
    url(r'^main/', 'glowna.views.display')
)
