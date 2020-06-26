from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from graphene_django.views import GraphQLView
from rest_framework.urlpatterns import format_suffix_patterns
from api.schema import schema
from django.urls import include, path
from rest_framework import routers
from api import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'topics', views.TopicViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True,schema = schema))),

]
