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
  - users - all users (id, username, rating)
    - Get parameters:
      - ?top(int) -returns top users(sorted by rating)
  - users/{id} - current user (id, username, rating)

## Subscriptions, Tags
Returns user's tags
- users/tags/ (GET, POST)
  - user(id) - who is subscribed
  - tag(id) - who this user subscribed to(tag)
    - Get parameters:
      - ?user(id) if ?user is null - returns current user's tags


Delete user's tags
- users/tags/{subs_id} - id of tag subscribtion
  

Returns user's subscribtions
- users/subscribe/  (GET,POST)
  - user(id) - who is subscribed
  - subscribe(id) - who this user subscribed to(user)
    - Get parameters:
      - ?user(id) if ?user is null - returns current user's subscribtions

Delete user's subscribtion
- users/tags/{subs_id} - id of subscribtion


## Article
Returns articles
- content/article  (GET, POST)
  - creator(id)
  - name
  - content
  - tags(id..)
  - picture
  - Get parameters:
    - ?tag(id) filtering by tag
    - ?user(id) filtering by user
    - ?rating | if **True** sorting by rating

Returns concrete article

- content/article/{id}
  - Get parameters:
    - ?like=True - sets like
    - ?unlike=True - removes like


## Comment
- content/comment  (GET,POST)
  - creator(id)
  - article(id)
  - content
  - -reply(id on comment)
  - Get parameners:
    - ?article(id) - returns comment of concrete article

Returns concrete comment
- content/comment/{id}
  - Get parameters:
    - ?like=True - sets like
    - ?unlike=True - removes like
