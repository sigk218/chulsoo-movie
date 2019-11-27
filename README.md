# Final Project 

[일자별 업무 진행](#일자별-업무-진행), [규칙](#규칙), [극복](#극복)

## 목표 

- 영화 배우 기반 영화 추천.

- 다시보기 플랫폼 추천.



## 개발 환경

|           | Languaes   | FrameWork                                                    |
| --------- | ---------- | ------------------------------------------------------------ |
| Front-end | Python     | [Django (djangorestframework)](https://www.django-rest-framework.org/) |
| Back-end  | Javascript | [Vue.JS](https://kr.vuejs.org/v2/guide/index.html) , [Vutify](https://vuetifyjs.com/ko/) |

- 웹 Django REST API 서버를 구축. 



## 구조도

### A. ERD

![ERD](ERD.png)



### B. Data Base

400개의 seed data



## 규칙

- 데이터베이스는 gitignore 할 것. (fixtures만 업로드 하도록)

  

## 일자별 업무 진행

|       | 병철                              | 수진                                               |
| ----- | --------------------------------- | -------------------------------------------------- |
| 11.21 | Youtube 영화 다시보기 정보 크롤링 | naver Series 에서 영화 다시보기 정보 (가격) 크롤링 |
| 11.22 | Youtube 영화 다시보기 정보(제목, 링크, 가격) 크롤링<br />Model 빌드(ERD로 표현) <br />DRF를 이용해 API 서버 만들기Create, Read, Delete<br /> | naver Series 에서 영화 다시보기 정보 (제목, 링크) 크롤링, <br />영진위에서 [영화정보 크롤링](#영화정보-크롤링)<br />Seed data인 ixtures/movies.json, genres.json 만들기\|
|11.25 | Login, Logout 기능 구현,<br />회원가입 기능 구현 실패,       | [django 서버로 API요청](#django-서버로-API요청), 영화 리스트 응답 받아서 vue에 띄우기(`MovieList.vue`) |
| 11.26 |                                                              | Toolbar 만들기([md-icons 설치](#md-icons-설치))<br />새로운 fixture(movie,genre,director,actor) 추가 |



## 극복



### 영화정보 크롤링

[영진위](http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do)에서 지금부터 52주간의 영화 이름을 받아오는중, 

dictionary를 json으로 저장하는 과정에서 인코딩 문제가 발생.

```python
with open('movies_name.json', 'w', encoding='UTF-8') as fp:
    json.dump(movies_name, fp, ensure_ascii=False)
```

`encoding='UTF-8'` , `ensure_ascii=False`  추가로 해결. 



### django 서버로 API요청

첫 번째, URL 오류

```javascript
const MOVIE_URL = 'localhost:8000/api/v1/movies/' //(x)
const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/' //(O)
```



두  번째, 인증 오류 (401 (Unauthorized))

django에서 로그인 된 사용자만 영화 리스트를 제공하도록 설계 했기 때문.

=> API 요청시 세션에서 로그인 정보를 찾아 (jwt 형식으로) 함께 보내준다. 

```javascript
const token = this.$session.get('jwt')
const options = {
    headers: {
        Authorization: 'JWT ' + token
    }
}    
axios.get(MOVIE_URL, options)
    .then(res=>{
    this.movies = res.data 
})
```



### `bash` 창에서 no such table error 

```bash
'C:\Users\student\FINAL2\final-back\movies\fixtures\movies\genres.json': Could not load movies.Genre(pk=1): no such table: movies_genre
```

=> migrate 하면 해결됨.


### NavigationDuplicated Error

vue Router에서 현재페이지와 같은 페이지로 router.push를 하게 되면 콘솔창에 NavigationDuplicated Error가 발생한다. 

```javascript
router.push({name: 'login'})
```

이 코드에서 에러가 발생하는데

```javascript
router.push({name: 'login'}, () => {})
```

이렇게 noop callback fucntion(아무것도 하지 않는 함수)을 추가해 주면 err를 catch 할 수 있다. 또는

```javascript
router.push({name: 'login'}).catch(err => {})
```

와 같이 .catch 메소드를 사용해서 에러를 핸들링 할 수 있다.



### 로그인 하지 않은 유저에 대한 접근제한

로그인 하지 않은 유저는 로그인이나 회원가입을 먼저 하도록 접근 제한을 하고 싶었다. 모든 url에 대해서 같은 조건을 적용하고 싶어서 App.vue에 mounted 시점에 loggedIn() 이라는 함수를 이용해 session에 JWT 정보가 없을 때는 Login 페이지로 리다이렉트 하는 방식을 이용했다.



### 로그인과 회원가입 페이지 하나로 합치기

처음에 로그인 페이지와 회원가입 페이지를 나눠서 만들었다. 하지만 위에 작성한 것 처럼 접근제한을 하려다 보니 로그인 되지 않은 유저는 회원가입 페이지로 이동할 수 없는 문제가 발생했다.

그래서 url을 하나로 합치고 조건부 렌더링을 이용해 login과 register를 둘 다 할 수 있는 하나의 페이지를 만드는 방식으로 문제를 해결했다. 



=======
### md-icons 설치

In `bash`,

```bash
npm install material-design-icons-iconfont --save
```

In `main.js`

```javascript
import 'material-design-icons-iconfont/dist/material-design-icons.css'
```

<<<<<<< HEAD


### 유저정보 뽑아내기

```
npm install vue-jwt-decode
```

=======
>>>>>>> master
