from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hi, name='hi'),
    path('details/<int:id>', views.details, name='details'),
    path('about/' ,views.about, name='about'),
    path('ptraining/' ,views.ptraining, name='ptraining'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)