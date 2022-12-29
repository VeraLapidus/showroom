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


### Celery
showroom -> deals -> tasks.py


### JWT 
**create new jwt for existing user**  <http://127.0.0.1:8000/auth/jwt/create> 
-> send JSON format {"username": "...", "password": "..."}


**get jwt refresh for existing user**  <http://127.0.0.1:8000/auth/jwt/refresh/> 

### Djoser
**All users**  <http://127.0.0.1:8000/auth/users/>


**User create**  <http://127.0.0.1:8000/auth/users/>
-> POST  Body  form-data -> send 'username', 'password', 'email'

**User Activate**  <http://127.0.0.1:8000/auth/users/activation/>
-> POST  Body  form-data -> send 'uid', 'token', which are in the link from the letter of user's email

**Reset Username**  <http://127.0.0.1:8000/auth/users/reset_username/>
-> POST  Body  form-data -> send 'email'

**Reset Username Confirmation**  <http://127.0.0.1:8000/auth/users/reset_username_confirm/>
-> POST  Body  form-data -> send 'uid', 'token' (which are in the link from the letter of user's email); AND 'new_username'

**Reset Password**  <http://127.0.0.1:8000/auth/users/reset_password/>
-> POST  Body  form-data -> send 'email'

**Reset Password Confirmation**  <http://127.0.0.1:8000/auth/users/reset_password_confirm/>
-> POST  Body  form-data -> send 'uid', 'token' (which are in the link from the letter of user's email); AND 'new_password'
