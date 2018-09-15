from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url

from django.contrib import admin
from . import views

# app_name="limaye"

urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls",)),
    # other urls
    path("blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    path("ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    path("about/", views.about, name="about"),
    # path("gallery/", views.ObjectCreateView, name="about")
    # path('booking/', include('booking.urls', namespace="booking")),
    url(r'^booking/', include('booking.urls')),

    #Publications
    path('publications/list', views.PublicationListView.as_view(), name='publications-list'),
    path('publications/create', views.PublicationCreateView.as_view(), name='publications-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
