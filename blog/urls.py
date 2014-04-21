__author__ = 'Daniel'
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, Project
from blog import views
urlpatterns = patterns('',
                      url(r'^$',ListView.as_view(
                          queryset = Post.objects.all().order_by("-date")[:25],
                          template_name="blog.html")),
                      url(r'^(?P<pk>\d+)$',DetailView.as_view(
                          model = Post,
                          template_name="post.html")),
                      url(r'^archives/$',ListView.as_view(
                          queryset = Post.objects.all().order_by("-date"),
                          template_name="archives.html")),
                      url(r'^latestnews/$',ListView.as_view(
                          queryset = Post.objects.all().order_by("-date")[:5],
                          template_name="archives.html")),
                      url(r'^projects/$',ListView.as_view(
                          queryset = Project.objects.all().order_by("-date")[:5],
                          template_name="projects.html")),
)
