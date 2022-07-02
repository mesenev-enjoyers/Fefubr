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
- users/tags/
  - user(id) - who is subscribed
  - tag(id) - who this user subscribed to(tag)
    - Get parameters:
      - ?user(id) if ?user is null - returns current user's tags


Delete user's tags
- users/tags/{subs_id} - id of tag subscribtion
  

Returns user's subscribtions
- users/subscribe/ 
  - user(id) - who is subscribed
  - subscribe(id) - who this user subscribed to(user)
    - Get parameters:
      - ?user(id) if ?user is null - returns current user's subscribtions

Delete user's subscribtion
- users/tags/{subs_id} - id of subscribtion


## Article
Returns article
- content/article
    - Get parameters:
      - ?tag(id) filtering by tag
      - ?user(id) filtering by user