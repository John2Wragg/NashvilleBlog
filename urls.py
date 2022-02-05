from django.urls import path
from django.conf.urls import url
from . import views

#

urlpatterns = [
    path('postlist',views.PostListView.as_view(),name='post_list'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comments/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comments/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]

# URLs for views both template and function based. Also include the primary
# keys to denote the correct comment to load in a detail view etc.
