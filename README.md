# drf를 활용해서 Django API를 만들어 보아요.<br/>
## 과제 내용<br/>
#### 1. 공연 Table 생성
> 테이블 명: Performance<br/>
> 테이블 속성: title(공연 제목), photo(공연 사진), description(공연 내용), musician(공연한 뮤지션[ForeignKey 사용해보기])

#### 2. Musician을 생성하는 api 구현
> models.py 에 뮤지션을 위한 테이블을 생성하는 Musician 객체가 정의되어 있어요.<br/>
> 해당 객체를 사용해서 뮤지션을 생성하는 POST api를 정의해 보세요.<br/>
> 제가 위쪽에 user를 생성하는 api를 정의해 두었습니다. 참고해서 해보시면되요.<br/>

#### 3. Musician을 수정하는 api 구현
> Musician 정보를 수정하는 patch api를 정의해 보세요.

#### 4. Musiican을 읽는 api 구현
> 모든 뮤시젼을 읽어서 alias순으로 정렬한 결과를 리턴하는 get api를 정의해 보세요.

#### 5. Article을 생성하는 api와 읽는 api를 각각 정의해 보세요.

#### 6. 참고사항
> 위에서 설명한 모든 api들은 urls.py 에서 매핑해줘야 됩니다.<br/>
> http 요청이 들어오면 해당 요청을 처리하는 view를 django가 호출 합니다.<br/>
> 이때 필요한 view를 호출할수있게 routing 해주는 모듈이 urls 모듈이구요.<br/>
> ##### 해당 repo를 fork하셔서 1번주터 5번까지의 과제가 완료된 후 해당 repo로 pull request 요청해주시면되요.<br/><br/>
### 아래와 같은 순서대로 과제 진행해 주시면 됩니다.<br/>
fork 하는 방법은 google링 해서 공부해보셔요 어렵지 않아요.<br/>
프로젝트폴더를 ide로 open하시고 다음 순서대로 명령 입력해주시면됩니다.<br/><br/>
1. 가상환경 생셩 및 실행<br/>
2. pip install -r requirements.txt<br/>
3. python manage.py migrate (제가 구현 해놓은 migrations file들로 django 에서 기본적으로 제공해주는 sqlite db 초기화)<br/>
4. python manage.py runserver (서버 실행)<br/>
5. 과제 진행해주시면 됩니다.<br/>
6. models.py 에 새로운 model을 정의 했으면 python manage.py makemigrations 명령을 사용해서 변경된 부분을 db에적용하는 mirations 파일을 생성해주셔야 됩니다.<br/>
7. 그리고 python manage.py migrate 명령으로 해당 변경사항을 db에 적용 시켜주셔야되요.
