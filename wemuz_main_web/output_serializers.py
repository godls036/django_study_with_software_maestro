from rest_framework import serializers

from django.contrib.auth.models import User


class UserOutputSerializer(serializers.ModelSerializer):

    """
    1. 서버가 전달하려고하는 데이터 덩어리들을 HTTP 프로토콜에서 사용가능한 json 객체로 변환한다. 
        # 통신을 하는 클라이언트가 어떤 언어로 구현되어진 프로그램인지 어떠한 프레임 워크를 쓰는지와 상관없이 
        # Django 서버는 HTTP 프로토콜만 지키면 어떠한 클라이언트와도 소통이 가능하다.
        # 여기서 말하는 프로토클을 지키기 위해서 모든 응답은 HttpResponse를 반환한다.
        # HttpResponse body 에는 HTTP 프로토콜이 허용하는 형식으로만 Data를 실어서 전달한다. (대표적으로 json형식)
    """

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

        