from django.urls import path
from shortener.views import (
    # home views
    HomeView, URLRedirectView,
    # auth views
    LoginView, SignupView, LogoutView,
    # about views
    AboutView,
    # analytics views
    AnalyticsView,
    # history views
    HistoryView
)


urlpatterns = [
    # home urls
    path(
        '', 
        HomeView.as_view(), 
        name='home'
    ),
    path(
        'shortify-url/<str:shortcode>/', 
        URLRedirectView.as_view(), 
        name='url_redirect'
    ),
    # auth urls
    path(
        'login/', 
        LoginView.as_view(), 
        name='login'
    ),
    path(
        'signup/', 
        SignupView.as_view(), 
        name='signup'
    ),
    path(
        'logout/', 
        LogoutView.as_view(), 
        name='logout'
    ),
    # about urls
    path(
        'about/', 
        AboutView.as_view(), 
        name='about'
    ),
    # analytics urls
    path(
        'analytics/', 
        AnalyticsView.as_view(), 
        name='analytics'
    ),
    # history urls
    path(
        'history/', 
        HistoryView.as_view(), 
        name='history'
    ),
]
