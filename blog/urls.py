from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',post_list,name='post_list'),
    # path('',PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',post_detail,name='post_detail'),
    path('<int:id>/share/',post_share,name='post_share'),
    path('<int:id>/comment/',post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/',post_list,name='post_list_by_tag'),
]