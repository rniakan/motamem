from django.urls import path
from . import views
from users.views import UsersTemplateView, AccountTemplateView

urlpatterns = [
    path('login_user',views.login_user, name="fast_login"),
    path('', UsersTemplateView.as_view(),name='user_list'),
    path('accout/', AccountTemplateView.as_view(),name='users_account'),
    path('user_profile/',views.profile_tamplateview.as_view(), name="user_profile"),
    # path('account/',include([
        # '',ListView,
        # '<slug:pk>/update',updateview,
        # 'create/',createview
    # ]))
]
