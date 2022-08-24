from django.urls import path
from admissions.views import addAdmission
from admissions.views import admissionReport

urlpatterns = [

    path('newadm/', addAdmission),
    path('admreport/', admissionReport),

]
