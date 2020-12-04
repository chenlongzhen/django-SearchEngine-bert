# django search basic demo 

## usage 

1. python3 manage.py runserver 

2. python manage.py makemigrations 
3. python manage.py migrate

4. upload search data
- data file should be in csv type, has two rows, key and value
- key is used to autocomplete
- value is used to get result by search key 

like this:

<img width="250" height="150" src="https://github.com/chenlongzhen/DjangoProject-SearchDemo/blob/master/readmepic/3.png"/>
upload website:
http://127.0.0.1:8000/upload/

---

main page：

http://127.0.0.1:8000/search_cxbc

<img width="300" height="200" src="https://github.com/chenlongzhen/DjangoProject-SearchDemo/blob/master/readmepic/1.png"/>

<img width="300" height="200" src="https://github.com/chenlongzhen/DjangoProject-SearchDemo/blob/master/readmepic/2.png"/>
