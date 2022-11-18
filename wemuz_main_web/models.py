from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    """
    초코뮤직 기사가 저장되는 테이블
    """

    title = models.CharField(max_length=256)
    content = models.TextField()
    link = models.URLField(max_length=512)
    publisher = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Musician(models.Model):

    """
    초코뮤직에 가입한 회원이 생성한 뮤지션
    """

    alias = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    sns = models.URLField(max_length=512, blank=True)


"""
공연에 대한 model을 정의하기
DB 테이블에 생성될 attribute는 아래와 같습니다.
1. 공연 제목
2. 공연 사진
3. 공연 내용
4. 공연한 뮤지션
"""