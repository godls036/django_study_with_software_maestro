from rest_framework import serializers

from django.contrib.auth.models import User


class UserInputSerializer(serializers.ModelSerializer):

    """
    1. 클라이언트로부터 json 객체로 전달되어진 데이터들을 python의 원시 데이터들로 변환한다. 
    2. (클라이언트로부터) HttpRequest 객체를 통해서 UserHTTPAPI로 전달되어진 데이터들을 검증(검사)한다.
    3. 해당 Serializer의 save() 메서드가 호출되면 아래 create() 메서드가 호출된다.
    """

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
        )
        user.save()
        return user
