import requests
import datetime
from decouple import config
import json
from urllib import parse
from bs4 import BeautifulSoup
from pprint import pprint 

## load data
# 장르.json -> dictionary
with open('genres.json', 'r', encoding = 'utf-8', newline= '') as f:
    genres_list = json.load(f)

temp_genre_list = {}
for genre in genres_list:
    temp_genre_list[genre['fields']['genreNm']] = genre['pk'] 

# 영화.json -> dictionary
with open('movies.json', 'r', encoding = 'utf-8', newline= '') as f:
    movies_list = json.load(f)

origin_movies = {}
for movie in movies_list:
    origin_movies[movie['pk']] = movie


# actors.json -> dictionary
temp_actors_list = dict()
with open('actors.json', 'r', encoding = 'utf-8', newline= '') as f:
    data = json.load(f)

for d in data:
    temp_actors_list[d['pk']] = d

# directors.json -> dictionary
temp_directors_list = dict()
with open('directors.json', 'r', encoding = 'utf-8', newline= '') as f:
    data = json.load(f)

for d in data:
    temp_directors_list[d['pk']] = d



# 영화 주말 박스오피스 
API_KEY = config('MOVIE_API_KEY')
MOVIE_DETAIL_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key='
temp_movies_name = {}

# DATE = datetime.date(2019, 11, 15)
DATE = datetime.datetime.now()
for i in range(20, 30):
    print(i)
    DATE -= datetime.timedelta(weeks=i)
    DATE_in = DATE.strftime('%Y%m%d')
    response = requests.get(f'{MOVIE_DETAIL_URL}{API_KEY}&targetDt={DATE_in}').json()
    for movie in response.get('boxOfficeResult').get('weeklyBoxOfficeList'):
        if origin_movies.get(movie.get('movieCd')): continue
        temp_movies_name[movie.get('movieCd')] = movie.get('movieNm')
# print(temp_movies_name)

# naver 에서 title, link, subtitle, pubDate, userRating 받아오기
NAVER_DETAIL_URL = 'https://openapi.naver.com/v1/search/movie.json'
headers = {
    "X-Naver-Client-Id" : config('NAVER_ID'),
    "X-Naver-Client-Secret" : config('NAVER_SECRET')
}
temp_movies = dict()
for k, v in temp_movies_name.items():
    url = f'{NAVER_DETAIL_URL}?query={v}'
    res = requests.get(url, headers=headers).json()
    if res.get('items') and len(res.get('items')) > 0:
        res1 = res.get('items')[0]
    temp_movies[k] = {
            "pk": k,
            "model":"movies.Movie",
            "fields":{
                "title": v,
                "link":res1.get('link'),
                "subtitle":res1.get('subtitle'),
                "pubDate":res1.get('pubDate'),
                "userRating":res1.get('userRating'),
                "actors": [],
                "directors":[],
            }
        }

# 네이버 link에서 image link, description, genres, acotrs, directors crawling 해오기
img_url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
for k, v in temp_movies.items():
    res = requests.get(v['fields']['link']).text
    code = str(v['fields']['link']).replace('https://movie.naver.com/movie/bi/mi/basic.nhn?code=', '')
    soup = BeautifulSoup(res, 'html.parser')
    # 장르
    genres = soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a')
    temp = []
    for g in genres:
        if temp_genre_list.get(g.text) == None:
            temp_genre_list[g.text] = len(temp_genre_list) + 1
        temp.append(temp_genre_list[g.text])
    temp_movies[k]['fields']['genres'] = temp   
    
    # description
    des = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p')
    des_temp = ''
    for d in des:
        des_temp += d.text
    temp_movies[k]['fields']['description'] = des_temp   
    
    # image
    temp_movies[k]['fields']['image']=img_url+code
    
    # 배우들
    res_detail = requests.get('https://movie.naver.com/movie/bi/mi/detail.nhn?code='+code).text
    soup_detail = BeautifulSoup(res_detail, 'html.parser')
    
    temp_actors = soup_detail.select('#content > div.article > div.section_group.section_group_frst > div.obj_section.noline > div > div.lst_people_area.height100 > ul > li')
    # print(temp_actors)
    for actor in temp_actors:
        actor_code = str(actor.select('div > a')[0].get('href')).replace('/movie/bi/pi/basic.nhn?code=','')
        temp_movies[k]['fields']['actors'].append(actor_code)
        if temp_actors_list.get(actor_code): continue
        temp_actors_list[actor_code] = {
            "pk": actor_code,
            "model": "movies.Actor",
            "fields":{
                "peopleNm": actor.select('div > a')[0].text,
            }
        } 
    # pprint(temp_movies)

    # 감독들
    temp_director = soup_detail.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(2)')
    for director in temp_director:
        for d in director.select('div > .k_name'):
            director_code = d.get('href').replace('/movie/bi/pi/basic.nhn?code=','')
            temp_movies[k]['fields']['directors'].append(director_code)
            if temp_directors_list.get(director_code) == None:
                temp_directors_list[director_code] = {
                "pk": director_code,
                "model": "movies.Director",
                "fields":{
                    "peopleNm": d.text,
                }
            }

# pprint(temp_movies)
# pprint(temp_actors_list)
# pprint(temp_directors_list)

# update
origin_movies.update(temp_movies)

Wtemp_genre_list = []
Wtemp_movies = []
Wtemp_actors_list = []
Wtemp_directors_list = []

for k, v in temp_genre_list.items():
    Wtemp_genre_list.append(
    {
        "pk": v,
        "model": "movies.genre",
        "fields": {
            "genreNm": k
        }
    }
    )
    
for k, v in temp_movies.items():
    Wtemp_movies.append(v)

for k, v in temp_actors_list.items():
    Wtemp_actors_list.append(v)

for k, v in temp_directors_list.items():
    Wtemp_directors_list.append(v)

# 저장
with open('genres.json', 'w', encoding='UTF-8') as fp:
    json.dump(Wtemp_genre_list, fp, ensure_ascii=False, indent=4)

with open('movies.json', 'w', encoding='UTF-8') as fp:
    json.dump(Wtemp_movies, fp, ensure_ascii=False, indent=4)

with open('actors.json', 'w', encoding='UTF-8') as fp:
    json.dump(Wtemp_actors_list, fp, ensure_ascii=False, indent=4)

with open('directors.json', 'w', encoding='UTF-8') as fp:
    json.dump(Wtemp_directors_list, fp, ensure_ascii=False, indent=4)
