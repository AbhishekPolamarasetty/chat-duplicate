from django.contrib import admin
from django.urls import path, include
from app1 import views
from app1.views import PostModelAPIView, PostModelAPIViewID, UserAPIView, UserAPIViewID
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from app1.views import edit_profilePage
from app1.views import profilePage
from app1.views import verifyPage
from app1.views import change_passwordPage
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app1.views import chat_view

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# from app1.views import signupPage, verify_email
from app1.Password import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexPage,name='index'),
    path('verify/',views.verifyPage,name='verify'),
    path('register/', views.registerPage, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login/',views.loginPage,name='login'),
    path('get-post/',views.getpostPage,name='get-post'),
    path('help/',views.helpPage,name='help'),
    # path('post/',views.postPage,name='post'),
    path('base/',views.basePage,name='base'),
    path('submit/', views.submit_form, name='submit_form'),
    # path('logout/',views.logoutPage,name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('post1/',views.Post,name='post'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('postAPI/',PostModelAPIView.as_view()),
    path('postAPI/<int:id>/',PostModelAPIViewID.as_view()),
    # path('chat/messages/<int:user_id>/', views.user_chat_list, name='user_chat_list'),
    # path('chat/messages/<int:user_id>/<int:other_user_id>/', views.chat_messages, name='chat_messages'),
    # path('chats/', chat_view, name='chat_view'),
    #  path('filter-posts/', filter_posts_view, name='filter_posts'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    #  path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profilePage, name='profile'),
    path('edit_profile/', views.edit_profilePage, name='edit_profile'),
    path('change/', views.change_passwordPage, name='change_password_page'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/<int:pk>/',UserAPIViewID.as_view()),
    path('users/',UserAPIView.as_view()),
    path('chats/', views.home, name='home'),
    path('<int:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
