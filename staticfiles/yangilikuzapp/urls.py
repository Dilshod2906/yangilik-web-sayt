from django.urls import path
from .views import IndexView,natija1,CategoryView,contactpageview,PostDetail,newslist,successcontact,search_venues,Newscreatview,Newsupdateview,Newsdelateview,UserRegistr
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('news/', newslist, name='newslist' ),
    path('', IndexView, name='home'),
    path('404', natija1, name='404'),
    path('mahalliy',CategoryView , name='mahalliy'),
    path('aloqa', contactpageview, name='aloqa'),
    path('news/<int:id>/', PostDetail, name='single'),
    path('contact_done', successcontact, name='contact_done'),
    path('search_venues', search_venues, name='search_venues'),
    path('news/create/', Newscreatview.as_view(), name='news_create'),
    path('news/<int:pk>/update/', Newsupdateview.as_view(), name='news_update'),
    path('news/<int:pk>/delate/', Newsdelateview.as_view(), name='news_delate'),
    path("register/", UserRegistr, name="register"),
]
