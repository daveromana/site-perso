from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^index$', TemplateView.as_view(template_name='index.html')),
	url(r'^motivation$', TemplateView.as_view(template_name='motivation.html')),
	url(r'^examens$', TemplateView.as_view(template_name='examens.html')),
	url(r'^stages$', TemplateView.as_view(template_name='stages.html')),
	url(r'^actualite$', TemplateView.as_view(template_name='actualite.html')),
	url(r'^notes$', TemplateView.as_view(template_name='notes.html')),
	url(r'^cv$', TemplateView.as_view(template_name='cv.html')),
	url(r'^BRI$', TemplateView.as_view(template_name='BRI.html')),
	url(r'^RAC$', TemplateView.as_view(template_name='RAC.html')),
	url(r'^multi-check$', TemplateView.as_view(template_name='multi-check.html')),
	url(r'^GYMNASE$', TemplateView.as_view(template_name='GYMNASE.html')),
	url(r'^404$', TemplateView.as_view(template_name='404.html')),
	url(r'^merci$', TemplateView.as_view(template_name='merci.html')),
	url(r'^contact$', 'sammy.views.contact'),




    # Examples:
    # url(r'^$', 'sammy.views.home', name='home'),
    # url(r'^sammy/', include('sammy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
