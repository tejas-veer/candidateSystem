
from django.urls import path,include
# from .views import candidate_details, candidate_list
# from .views import CandidateList,CandidateDetails
from .views import CandidateModelViewSet,UserModelViewSet,index
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('candi' , CandidateModelViewSet , basename='candi')
router.register('user' , UserModelViewSet , basename='user')

urlpatterns = [
    path("", index , name="index"),
    path('api/', include(router.urls) , name='candi' ),
    path('api/', include(router.urls) , name='candi' ),
    path('api/auth/', obtain_auth_token  , name='auth_token' ),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

