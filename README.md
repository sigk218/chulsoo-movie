# Final Project 

[일자별 업무 진행](#일자별-업무-진행), [규칙](#규칙), [극복](#극복)

## 목표 

- 영화정보 검색, 추천 사이트 만들기 

- 다시보기 플랫폼 가격 별로 표시

- 좋아요 기반의 영화 추천 알고리즘 적용

  *실제 구현 정도는 50%* 



## 개발 환경

|           | Languaes   | FrameWork                                                    |
| --------- | ---------- | ------------------------------------------------------------ |
| Front-end | Python     | [Django (djangorestframework)](https://www.django-rest-framework.org/) |
| Back-end  | Javascript | [Vue.JS](https://kr.vuejs.org/v2/guide/index.html) , [Vutify](https://vuetifyjs.com/ko/) |

- 웹 Django REST API 서버를 구축. 

## 배포환경

|           | 배포 환경 | 링크                                                         |
| --------- | --------- | ------------------------------------------------------------ |
| Front-end | FireBase  | https://stark-garden-07113.herokuapp.com/                    |
| Back-end  | Heroku    | [https://chulsoo-front.firebaseapp.com](https://chulsoo-front.firebaseapp.com/) |



## 구조도

### A. ERD

![ERD](ERD.png)

### B. Data Base

94개의 seed data

### C. mockup

![home](home.png)


![mousehover](mousehover.png)

## 규칙

- 데이터베이스는 gitignore 할 것. (fixtures만 업로드 하도록)

  

## 일자별 업무 진행

|       | 김병철                             | 이수진                                              |
| ----- | --------------------------------- | -------------------------------------------------- |
| 11.21 | Youtube 영화 다시보기 정보 크롤링 | naver Series 에서 영화 다시보기 정보 (가격) 크롤링 |
| 11.22 | Youtube 영화 다시보기 정보(제목, 링크, 가격) 크롤링<br />Model 빌드(ERD로 표현) <br />DRF를 이용해 API 서버 만들기Create, Read, Delete<br /> | naver Series 에서 영화 다시보기 정보 (제목, 링크) 크롤링, <br />영진위에서 [영화정보 크롤링](#영화정보-크롤링)<br />Seed data인 ixtures/movies.json, genres.json 만들기\|
|11.25 | Login, Logout 기능 구현,<br />회원가입 기능 구현 실패,       | [django 서버로 API요청](#django-서버로-API요청), 영화 리스트 응답 받아서 vue에 띄우기(`MovieList.vue`) |
| 11.26 | Login Page를 Main으로 설정.<br />Navbar, MovieList의 하위 컴포넌트 및 버튼 수정 | Toolbar 만들기([md-icons 설치](#md-icons-설치))<br />새로운 fixture(movie,genre,director,actor) 추가 |
| 11.27 | 회원 가입 기능 구현.<br />검색, LIKE, 댓글, 영화 추천 백엔드 구성 | 영화 가격 크롤링 한 후 정보 movies.json에 추가<br />이미지 고화질 링크로 변경. |
| 11.28 | back-end 마무리<br />VIew 컴포넌트 구조 정리. | Detail, LIKE, 댓글 기능 구현. |



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



### md-icons 설치

In `bash`,

```bash
npm install material-design-icons-iconfont --save
```

In `main.js`

```javascript
import 'material-design-icons-iconfont/dist/material-design-icons.css'
```




### 유저정보 뽑아내기

```
npm install vue-jwt-decode
```



## 느낀점

1. 크롤링  

   - 영진위 API와 네이버 영화검색 API를 사용했는데 정확한 데이터를 선별하는 것이 힘들었다.  (영화 제목은 같은데 띄어쓰기 외래어 등 표기법이 다를때, 같은 제목의 영화가 여러개일 때, 감독이면서 배우인 경우등)   

     네이버 영화 검색 API로 정보를 크롤링 해 올때,   제목에 키워드가 들어가기만 하면 결과가 나와서 비교해서 데이터를 가져와야했음.(안함)   

   - 가격 정보를 크롤링 해올 때,  뷰에서(내 프론트 서버) 에서 요청을 보내면 cors에러가 난다는것을 몰랐음.    

   - 크롤링을 selector로 한다면, 나중에 유지 보수를 어떻게 해야하는 것인지 의문이 들었다. 생각해보면 웹페이지를 크롤링해서 또 다른 웹페이지를 만든다는 건 좀 이상하긴하다. 제대로된 서비스를 만들 때에는 정식으로 API를 요청해서 사용하는 것이 이치에 맞는 것 같다.   

   - 실제로 영화별로 구조가 완전히 다 같지는 않았다.    

   - 자바스크립트로 렌더된 페이지를 크롤링할 때, 비동기 처리때문에 페이지가 로드되기 전에 데이터를 받아와지는 경우가 있음. 그런경우 어떻게 해야할지 해결책을 완전히 찾지는 못했지만 임시적으로는 원하는 정보가 나올 때까지 재요청을 보내서 크롤링하는 방식을 사용했음.

2. vue (front-end)   

   - back-end 와의 요청/응답      
     - props로 movie data를 받으면, 자식 컴포넌트에서 (댓글, 좋아요) 등리 변해도 업데이트 할수가 없었다.  정보가 바뀔때마다 업데이트하는 방식을 택했지만 속도가 너무 느리다.   헤로쿠의 요청/응답 문제인지, 우리조 코드의 구조의 문제인지 잘 모르겠다. 더 좋은 방식이 있을 것 같다.    
   - vuetify 사용     
     - 공부를 전혀 안하고 써야해서 복붙을 벗어나지 못했다. 처음 html할 때 보단 예제 코드를 잘 읽을 수 있었지만, 여전히 내 마음대로 컴포넌트 배치를 하기에는 지식이 부족했다.   
   - Vue App 구조를 먼저 설계하는 작업이 꼭 필요하다.     
     - 우리조의 경우 컴포넌트 구조를 탄탄탄히 하지 않아서  중간에 고치고, 각가 수정을 해버려서 conflict 가 날 때가 있었다.  django의 모델, API구조 와 더불어 실제 개발전 가장 공들여서 계획을 세워야하는 부분 같다.

3. Django(Back-end)   

   - API서버에서 최대한 많은 정보를 줄 수 있도록 설계해야한다. 안그러면 VM이 너무 무거워져서 오히려 속도가 많이 느려지는 것 같다.   
   - Serializer, data 유효성 검사, JWT 등에 대한 이해가 부족했다.    
   - rest API      
     - back-end를 단단히 한다면, 서로 코드를 잘 몰라도 협업하기 굉장히 용이하다.

4. 깃(협업)   

   - 마이그레이션 에러      
     - 가장 많이 발생한 conflict이다. 마이그레이션은 실제 배포 전까지는, 한사람이 정해서 makemigrations 하고, 각자 local에서 migrate해야할 것같다.   
   - vue npm     
     - 이용시 생각보다 많은 파일들이 설치되기 때문에 설정을 변경할 수도 있는 설치라면 유의 해야한다. 시간을 가장 많이 썻고 보람도 없었다.    
   - 각자 몫을 나누기 전에 모델, API 구조, 컴포넌트 구조 이거 세개는 모든 팀원이 잘 알고 있으면 좋을 것같다. 실제로 문제에 너무 빠져 오랜시간 고민해서 답이 안나오는 것을 다른 팀원 들이 보면 생각보다 쉽게 찾을 수 도 있기 때문 (물론 이번에는 내가 해결하지 못한 문제가 너무 많았다 ㅜㅜ)   
   - git merge는 함부로 하는 것이 아니고 진짜 웬만해서는 같은 파일 작업도 절대 하면 안된다는것 + 복구가 힘들 것 같으면 과감히 git reset을 하자. 시간을 너무 뺏김.      
     - master 브랜치는 한명이 권한을 가지고 머지를 해주는게 효율적으로도 좋고, 그렇게 하는게 깃이 덜 꼬이게 할 방법인거 같음. 한명이 계속해서 전체적인 맥락을 알고 있어야 나머지가 편하게 코딩할 수 있다. 그리고 서로 건드리면 안되는 부분들을 명확히 하고 고치고 싶은데 건드릴 수 없는 부분들은 이슈를 내서 해결 해달라고 해야한다. 괜히 건드렸다가 conflict가 생기면 찝찝해진다.

5. 그 외의 것   

   - 프로젝트를 하면서 새로 배운것들은 바로바로 문서화를 하자.     
     - 하다보니 점점 귀찮아서 안하게 되었는데 똑같은 것을 또 찾고 있는 상황이 자주 발생함. 미리 문서화를 해놓으면 그 당시에는 좀 귀찮지만 다시 찾아야 될 때 빠르게 찾을 수도 있고 정리하는 과정에서 스스로 다시 복습하는 효과도 있어서 머리속에 잘들어가게 된다.   
   - 가상환경의 중요성을 알게되었다.
     - 가상환경 안깔고 코딩을 해보니까 먼저, 배포할 때 내가 딱 필요한 모듈만 설치해서 쓰고 싶은데 그걸 일일히 적어줘야 되서 불편했고, 두 번째로는 라이브러리를 잘못깔아서 오류가 났을 때 어떤 라이브러리가 잘못된 건지 쉽게 파악할 수 없었던 점이 불편했다.

