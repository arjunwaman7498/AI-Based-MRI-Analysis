from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("brain/", views.brain_analysis),
    path("history/", views.history),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("clear-history/",views.clear_history,name="clear_history"),
    path("download-report/<int:patient_id>/",views.download_report,name="download_report"),
    path("doctor-login/",views.doctor_login,name="doctor_login"),

]