from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

schema_urlpatterns = [
    path('api/messages/', include('api.urls')),
    path('api/', include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Dtest API",
        default_version='v1',
        description="Messages and Books",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_urlpatterns,
)

def home(request):
    return HttpResponse(
        """
        <div style='height: 100vh; background-color: #417690'>
        <h1 style='color: #f5dd5d; text-align: center; padding-top: 100px;'>Welcome!</h1>
        <br />
        <h2 style='color: #f5dd5d; text-align: center;'>/admin --- admin page</h2>
        <br />
        <h2 style='color: #f5dd5d; text-align: center;'>/swagger --- docs page</h2>
        <div>
    """)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/messages/', include('api.urls')),
    path('api/', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
