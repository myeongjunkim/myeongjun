from django.urls import path, include

import myeongjun.views


urlpatterns = [
    path('', myeongjun.views.myeongjun_main, name='myeongjun_main'),
    path('hometown/', myeongjun.views.hometown, name='hometown'),
    path('gallery/', myeongjun.views.gallery, name='gallery'),
    path('load_map/', myeongjun.views.load_map, name='load_map'),
    path('cafe/', myeongjun.views.cafe, name='cafe'),
    path('introduceme/', myeongjun.views.introduceme, name='introduceme'),
]
