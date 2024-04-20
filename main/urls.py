from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ProductAPIView, UserRegistrationView, ProductImageAPIView, CommentAPIView, EditorViewSet, \
    RatingAPIView

urlpatterns = [path('api/v1/product_list/', ProductAPIView.as_view(), name='main'),
               path('api/v1/product_image_list/', ProductImageAPIView.as_view(), name='product_image'),
               path('api/v1/comment_list/', CommentAPIView.as_view(), name='comment'),
               path('editor_list/<int:pk>/', EditorViewSet.as_view(), name='editor'),
               path('api/v1/rating_list/', RatingAPIView.as_view(), name='rating'),
               path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               path('api/registration/', UserRegistrationView.as_view(), name='registration'),
               ]
