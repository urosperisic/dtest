from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet
from shop.views import ProductViewSet, CategoryViewSet
from simpleauth.views import SignupView, LogoutView, RoleBasedView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

schema_urlpatterns = [
    path('api/messages/', include('api.urls')),
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/role-based/', RoleBasedView.as_view(), name='role_based'),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Dtest API",
        default_version='v1',
        description="Messages and Books, and Shop",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_urlpatterns,
)

def home(request):
    return HttpResponse(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Admin Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                main {
                    min-height: 100vh;
                    background-color: #0C4B33;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                h1, h2, p {
                    color: #fff;
                    text-align: center;
                }
                h1 {
                    padding-top: 100px;
                }
            </style>
        </head>
        <body>
            <main>
                <div>
                    <h1>Welcome!</h1>
                    <br />
                    <h2>/admin --- admin page</h2>
                    <br />
                    <h2>/swagger --- docs page</h2>
                    <br />
                    <p>/api/messages --- messages page</p>
                    <br />
                    <p>/api/books --- books page</p>
                    <br />
                    <p>/api/categories --- categories page</p>
                    <br />
                    <p>/api/products --- products page</p>
                    <br />
                    <p>/api/signup --- signup page</p>
                    <br />
                    <p>/api/login --- login page</p>
                    <br />
                    <p>/api/logout --- logout page</p>
                    <br />
                    <p>/api/token/refresh --- refresh token page</p>
                    <br />
                    <p>/api/role-based --- role-based page</p>
                </div>
            </main>
        </body>
        </html>
        """
    )

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/messages/', include('api.urls')),
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/role-based/', RoleBasedView.as_view(), name='role_based'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
