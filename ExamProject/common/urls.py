from django.urls import path

from ExamProject.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]
