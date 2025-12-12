from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # auth urls : 
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),         # Login, logout, password reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Signup

    #card urls : 
     path('cards/', DailyPositiveCardListCreateView.as_view(), name='cards-list-create'),
    path('cards/<int:pk>/', DailyPositiveCardRetrieveUpdateDestroyView.as_view(), name='cards-detail'),

    # Profile urls :
    path('profile/', StudentProfileView.as_view(), name='student-profile'),

    # journal urls :
    path('journal/', JournalListCreateView.as_view(), name='journal-list-create'),
    path('journal/<int:pk>/', JournalRetrieveUpdateDeleteView.as_view(), name='journal-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

