"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import PostList, PostDetail,PostListView, PostAddView, PostEditView, PostListByAuthor, PostListByYear, PostListByMonth, PostListByDay
from home.views import HomeView
from about.views import AboutView
from contact.views import ContactAdd
from sitesetting.views import SiteSettingEdit
from djadmin.views import Dashboard
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('about/', AboutView.as_view(), name="about-page"),
    path('admin/', admin.site.urls),
    path('contact/', ContactAdd.as_view(), name="contact-page"),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/author/<username>/', PostListByAuthor.as_view(), name='post-author'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:year>/<int:month>/<int:day>/', PostListByDay.as_view(), name='post-detail'),
    path('posts/<int:year>/<int:month>/', PostListByMonth.as_view(), name='post-detail'),
    path('posts/<int:year>/', PostListByYear.as_view(), name='post-detail'),
    path('dj-admin/',login_required(Dashboard.as_view()),name='dj-admin-view'),
    path('dj-admin/posts/',login_required(PostListView.as_view()),name='dj-admin-posts-view'),
    path('dj-admin/posts/add/',login_required(PostAddView.as_view()),name='dj-admin-posts-add-view'),
    path('dj-admin/posts/<int:pk>/', login_required(PostEditView.as_view()),name='dj-admin-posts-update-view'),
    path('dj-admin/settings/',login_required(SiteSettingEdit.as_view()),name='dj-admin-sitesetting-view'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
