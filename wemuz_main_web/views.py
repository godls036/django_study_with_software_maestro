from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from .input_serialziers import UserInputSerializer
from .output_serializers import UserOutputSerializer

class UserHTTPAPI(APIView):

    """
    url: host/user/
    위 url을 통해서 해당 서버로 접근 했을때 호출되는 view 객체
    [get, post] 해당 http method 요청을 처리할 수 있는 로직이 구현되어있다.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        # 모든 유저를 db로부터 select 해서 id 순서대로 정렬한다.
        order_by = request.GET.get("order_by", "id")
        user_qs = User.objects.all().order_by(order_by)
        # 해당 유저들을 Serializer 객체를 통해서 json 객체로 serializing 한다
        serialzier = UserOutputSerializer(user_qs, many=True)
        # 만들어진 json 객체를 HttpResponse 객체를 통해서 요청이온 클라이언트로 전송한다.
        return Response(serialzier.data, status=HTTP_200_OK)
        

    def post(self, request):
        try:
            # 클라이언트로 부터 받은 HttpRequest 객체 body에 있는 json 데이터를 python의 원시 객체들로 deserializing 한다
            serializer = UserInputSerializer(data=request.data)
            # 이때 사용되는 Serializer 객체가 데이터 body로 부터 전달된 데이터들을 검사, 검증한다.
            serializer.is_valid(raise_exception=True)
            # Serializer 객체에 구현되어진 create 메서드가 호출되어진다.
            # 해당 메서드에는 입력받은 데이터들을 사용해 User를 생성하고 DB에 저장하는 로직이 있다.
            serializer.save()
            # 생성되어진 User객체의 정보와, 생성 성공했음을 의미하는 201 status code를 클라이언트로 전송한다.
            return Response(serializer.validated_data, status=HTTP_201_CREATED)
        # 유저를 생성하는 로직 중에 필요 데이터가 없거나, 데이터가 잘못되었을 경우 에러가 발생한다면
        # status code 400과 에러 메세지를 반환한다.
        except Exception as e:
            return Response(e.args[0], status=HTTP_400_BAD_REQUEST)



# 필요한 view들은 여기 구현하시면 되요

"""
1. Musician 을 생성하는 api
2. Musician 정보를 수정하는 api
3. Musician 정보를 읽는(select) api
"""

"""
1. Article 을 생성하는 api
2. Article 을 읽는(select) api
"""