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