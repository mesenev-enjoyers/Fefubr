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
