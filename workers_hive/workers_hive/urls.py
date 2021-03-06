"""workers_hive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import workers_app.views as w_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', w_views.WorkersList.as_view(), name='workers-list'),
    path('add-worker/', w_views.WorkerCreate.as_view(), name='worker-create'),
    path('worker/<int:worker_pk>/', w_views.WorkerDetails.as_view(), name='worker-details'),
    path('worker/update/<int:worker_pk>/', w_views.WorkerUpdate.as_view(), name='worker-update'),
    path('worker/delete/<int:worker_pk>/', w_views.WorkerDelete.as_view(), name='worker-delete'),
    path('report/', w_views.OccupationAgeAvgReport.as_view(), name='age-report')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
