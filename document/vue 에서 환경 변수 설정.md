VUE 에서 환경 변수 설정 

[Vue CLI](https://cli.vuejs.org/guide/mode-and-env.html#modes) 링크 참고.

```shell
.env # loaded in all cases
.env.local  # loaded in all cases, ignored by git
```



0. `.env.local` 파일 생성

​		VUE_APP prefix를 붙이면 client 환경에서 해당 값 사용 가능.

1. In `scripts`

   ```javascript
   const MOVIE_URL = process.env.VUE_APP_BASE_URL
   ```

   

가상환경 설치하기

Window PowerShell 에서는 Active 파일을 실행함.

```python
python -m venv [name]
source ~/[name]/3.7.3/Scripts/activate
```



Window에서 alias 명령어 사용하기

`.barsh`



*설치 해야 할 파일들*

```shell
pip install django 
pip install python-decouple
pip install django-heroku
pip install django-rest-auth
pip install django-cors-headers
pip install django-allauth
pip install gunicorn
```



migrate 후 data load 해주기



## Django 배포하기

Paas인 Heroku를 이용해서 배포하기.

1. Pipelining

In `settings.py`

```python
...
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
...
```

In  `shell`

```
python manage.py collectstatic
```

In `ignore`

```
venv
*.sqlite3
.env
*.bak
```



2. 내 원격 저장소에 저장하기

   ```
   git remote add origin [URL]
   ```

3.  

   ```shell
   pip istall django-heroku
   ```

   In `settings`

   ```python
   import django_heroku
   django_heroku.settings(locals())
   ```

   In `runtime.txt`

   ```
   python-3.7.4
   ```

   in `Procfile`

   gunicorn 설치 후,

   ```python
   web: gunicorn [app_name].wsgi --log-file -
   ```

   ```
   pip freeze > requirements.txt
   ```

   

   In `settings.py`

   ```python
   ALLOWED_HOSTS = [
       '[app_name].herokuapp.com'
   ]
   ```

4.  migration 해주고, 서버를 켰을때 404 페이지가 나오면 성공!

5.  배포 후, heroku 서버에서 

     

## Vue 배포하기 

[FireBase](https://console.firebase.google.com/?hl=ko&pli=1) 서버에 Vue 코드를 배포해보자 !

1. 프로젝트 생성 (사진)

2. 애널리틱스 허용 (사진)

3. Fire Base Cli 설치

   ```powershell
   npm install -g firebase-tools
   ```

 4. 

   ```
   firebase init 
   ```

   - 옵션 -> 'Hosting'
   - `dist` 입력

   5.

   ```
npm run build
firebase deploy
   ```

   



http 400 에러 

-> 백엔드 서버가 켜져있지 않을 때 주로 발생 

주소, 메서드 등이 틀렸을 때 



## 무한 스크롤 

사용자가 필요한 만큼만 리소스를 요청 -> 한번에 리소스를 로드하는 것보다 속도가 빠름. 





### back-end

#### pagination 

전체 자료를 적절히 나눌 때 `pagination` 을 사용. 

 [공식 문서](https://www.django-rest-framework.org/api-guide/pagination/), [stackoverflow](https://stackoverflow.com/questions/38173984/using-infinite-scroll-with-django-rest-framework)

Django는 `Privious/Next` 링크를 통한 `pagination` 을 제공.

마찬가지로 REST framework도 이를 지원하며, 한 페이지당 몇 개의 데이터를 넣을 것인지 정할 수 있다.  



이 부분은 공식 문서에 class로 정의되어 있었다. 

따라서, [클래스 기반 뷰](https://wayhome25.github.io/django/2017/05/02/CBV/) 을 기반으로 url과 view class를 정의했다.



In `urls.py` 

```
path('movies/list/', views.MovieListView.as_view()), # as_view() 클래스 함수를 통해 함수뷰 생성
```



In `movies > views.py`

```python
class MoviePagination(pagination.PageNumberPagination):
    page_size = 20


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
```

class 는 데코레이터를 달 수 없고, return 값이 없어도 된다 ! (class와 함수의 차이는 ? )



Postman을 통해 `http://127.0.0.1:8000/api/v1/movies/list/?page=[page_num]` 에 GET 요청을 보내면 

page_size 만큼 결과를 받을 수 있다.





### front-end



https://github.com/ElemeFE/vue-infinite-scroll



고쳐야 할 것 

- [ ] data 크롤링 (최신 정보로, 제목 맞춰서)
- [x] url 바꾸기 
- [ ] 반응형 
- [ ] 유투브, 인스타그램 로고 넣기 
- [ ] admin page 만들기 
- [ ]  깃 리모트  추가해주기
- [ ] git ignore 정리 
- [x] 헤로쿠 쉘에서 마이그레이션 해주기
- [ ] 깃랩에 있는 커밋 옮기기 
- [ ] http 오류 
- [ ] 무한 스크롤 로드 
- [ ] 웹 크롤러 만들기



**정리 해야할 것**

- [ ] 깃 협업 모델 