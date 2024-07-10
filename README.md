### Project discription
This project is a simple bullen boerd systhem based on class in python. Users can create accounts, write posts, view posts, search posts and delete posts.


### Skills
* Python 3.10
* hashlib
* logging
* tabualte
* time


### Installation
pip install tabualte


### Main features
* Create account: Users can create new accounts with name, id and password.
  * Uses hashlib module to hash passwords
  * Uses logging module to log message "The password has been hashed"
* User list: Users can view user list.
  * Use tabulate module to display user list in table.
* Post list: Users can view post list.
  * Use tabulate module to displat post list in table.
* Write post: Users can write a new post with id, password
  * Verify input password with hashed password
* Delete post : Users can delete a post with title, id, password
  * Verify input password with hashed password
