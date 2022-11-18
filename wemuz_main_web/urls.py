from django.urls import path
from .views import UserHTTPAPI


urlpatterns = [
    # host/user/ 로 온 요청을 UserHTTPAPI 로 전달한다.
    path("user/", UserHTTPAPI.as_view(), name="user_api"),
    # path("...", View, name="url name 리버스 기능을 사용힉 위해서"),
    # ...
]