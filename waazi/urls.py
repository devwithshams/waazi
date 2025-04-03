from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from waazi.views import ScholarViewSet, CategoryViewSet, WaaziViewSet, home, scholar_profile, scholars

router = DefaultRouter()
router.register(r'scholars', ScholarViewSet, basename='scholar')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'waazi', WaaziViewSet, basename='waazi')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('scholar/<int:scholar_id>/', scholar_profile, name='scholar_profile'),
    path('scholars/', scholars, name='scholars'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
