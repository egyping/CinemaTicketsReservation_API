from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    #2 
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),
    
    #3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.FBV_List),

    #3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_pk),

    #4.1 GET POST from rest framework class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),

    #4.2 GET PUT DELETE from rest framework class based view APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    #5.1 GET POST from rest framework class based view mixins
    path('rest/mixins/', views.mixins_list.as_view()),

    #5.2 GET PUT DELETE from rest framework class based view mixins
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

    #6.1 GET POST from rest framework class based view generics
    path('rest/generics/', views.generics_list.as_view()),

    #6.2 GET PUT DELETE from rest framework class based view generics
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

    #7 Viewsets
    path('rest/viewsets/', include(router.urls)),

    #8 find movie 
    path('fbv/findmovie', views.find_movie),

    #9 new reservation
    path('fbv/newreservation',views.new_reservation),

    #10 rest auth url 
    path('api-auth', include('rest_framework.urls')),

    #11 Token authentication
    path('api-token-auth', obtain_auth_token),


    #12 Post pk generics Post_pk
    #path('post/generics/', views.Post_list.as_view()),
    path('post/generics/<int:pk>', views.Post_pk.as_view()),

]
