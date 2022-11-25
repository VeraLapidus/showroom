# CarShowroom

Stack: DRF, PostgreSQL, Celery, Redis, Docker-compose, JWT authorization


## Сommands 
docker-compose up -d --build


docker-compose up

---
http://127.0.0.1:8000/



### Comments 
Filter - look up via REST API (in swagger you can't use RangeFilter()) )

---
When forming the auto_show's wish_list - this TextField should include one or several dicts of the format {"brand": "None", "model": "None", "year": "None", "color": "None", "price" : "None"} separated by double " "
