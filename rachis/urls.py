from django.urls import path, include
                      
urlpatterns = [
    path('api/', include(('rachis.apps.authentication.urls'), namespace='auth')),
    path('api/', include(('rachis.apps.resource.urls'), namespace='resources')),
]