"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet
# from snippets.views import api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# Tutorial 6 | Binding ViewSets to URLs explicitly
# snippet_list = SnippetViewSet.as_view({
# 		'get': 'list',
# 		'post': 'create'
# 	})
# snippet_detail = SnippetViewSet.as_view({
# 		'get': 'retrieve',
# 		'put': 'update',
# 		'patch': 'partial_update',
# 		'delete': 'destroy'
# 	})
# snippet_highlight = SnippetViewSet.as_view({
# 		'get': 'highlight'
# 	}, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
# 		'get': 'list'
# 	})
# user_detail = UserViewSet.as_view({
# 		'get': 'retrieve'
# 	})

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     # url(r'^snippets/$', views.snippet_list),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#  #    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
# 	# url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
# 	# url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# 	# url(r'^users/$', views.UserList.as_view(), name='user-list'),
# 	# url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
#     url(r'^$', views.api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ]

# urlpatterns += [
# 	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# Tutorial 6 | Using Routers
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additioanlly, we include t he login URLs for the browsable API.
urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]