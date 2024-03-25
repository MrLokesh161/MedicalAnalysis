from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import patient_view, patientdisplay_view

urlpatterns = [
    path('patient/', patient_view, name="Patient Details Form"),
    path('patientdetails/', patientdisplay_view, name="Patient Details")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
