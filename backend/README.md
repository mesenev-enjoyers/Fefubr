# API endpoints
## Registration
- auth/users/ (POST)
  - username
  - email
  - password
## Login/Logout
Returns token
- auth/token/login (POST)
  - username
  - password

Destroy Current token
- auth/logout (POST) - add token in header

## Get users
  - auth/users/ - all users
  - auth/users/{id} - current user

## Subscriptions, Tags
Returns user's tags
- users/tags/?user={int}  - if ?user is null - returns current user's tags
  - user(id) - who is subscribed
  - tag(id) - who this user subscribed to(tag)


Returns user's subscribtions
- users/subscribe/?user={int}  - if ?user is null - returns current user's subscribtions
  - user(id) - who is subscribed
  - subscribe(id) - who this user subscribed to(user)