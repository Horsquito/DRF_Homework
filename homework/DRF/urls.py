from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('performer', views.PerformerView)
router.register('task', views.TaskView)

urlpatterns = [
    path('', include(router.urls))
]
