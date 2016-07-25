from django.conf.urls import url
from .views import (
	Home,
	NewPost,
	NewUser,
	Login,
	Article,
	Logout,
	NewComment,
	Delete,
	Update,
	Profile
	)


urlpatterns = [
	url(r'^home$',Home.as_view(),name="home"),
	url(r'^new_post$',NewPost.as_view(),name="new_post"),
	url(r'^new_user$',NewUser.as_view(),name="new_user"),
	url(r'^new_comment/(?P<pk>[0-9]+)$',NewComment.as_view(),name="new_comment"),
	url(r'^article/(?P<pk>[0-9]+)$',Article.as_view(),name="article"),
	url(r'^delete/(?P<pk>[0-9]+)$',Delete.as_view(),name="delete"),
	url(r'^update/(?P<pk>[0-9]+)$',Update.as_view(),name="update"),
	url(r'^profile$',Profile.as_view(),name='profile'),
	url(r'^logout$',Logout.as_view(),name="logout"),
    url(r'^',Login.as_view(),name='login')
]
