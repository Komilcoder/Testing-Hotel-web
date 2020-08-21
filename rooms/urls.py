from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeList.as_view() , name="home"),
    path('index_detail/<int:pk>/', views.IndexDetailView.as_view(),name="Index-detail"),
    
    path('package/' , views.PackageListView.as_view() , name="package"),
    path('package/<int:pk>/', views.PackageDetailView.as_view(), name="package-detail"),
    
    path('post/', views.PostList.as_view(), name="blog"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('about/' , views.AboutPage.as_view(), name="about"),
    path('abouts/<int:pk>/', views.AboutDetailView.as_view(), name="about-datail"),
    
    path('abouts/' , views.Secondabout.as_view(), name="aboutsecond"),
    path('aboutsecond/<int:pk>/', views.SecondAboutDetail.as_view(), name="seconds"),

    # forms
    path('contact/',views.contact_create, name="contact"),    
    path('contact/edit/<int:pk>/' , views.contact_edit, name="contact-edit"),
    
    path('register/', views.register, name="register"),
    path('login/', views.loginPage ,name="login"),
    path('logout/' , views.logoutuser , name="logout"),
    
]
