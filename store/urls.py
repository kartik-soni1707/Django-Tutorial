from django.urls import path
from rest_framework_nested import routers
from . import views
from pprint import pprint
router=routers.SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

products_router=routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews',views.ReviewViewset, basename='product-reviews')
urlpatterns = router.urls+products_router.urls
