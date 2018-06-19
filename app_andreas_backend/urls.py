
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
# Users Structure - Views
from auth_users.views import AuthUserModelViewSet
from rates.views import RateModelViewSet
from tasks.views import TaskModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', AuthUserModelViewSet, base_name='users')
router.register(r'rates', RateModelViewSet, base_name='rates')
router.register(r'tasks', TaskModelViewSet, base_name='tasks')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
