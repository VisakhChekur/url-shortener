# URL Shortener

A web-based application that shortens URLs. The backend is made using the Flask framework of Python.

# Working

The shortened URL's code that is appended to the base URL and the long URLs are stored in a MongoDB database collection. Using the database, the user is redirected to the webpage corresponding to the long URL.

## NOTE:
If you want to run this, please change the `MONGO_DB_CONNECTION_STRING` to the appropriate one for your database. The one used in this is deleted and no more in use since this was created simply for practice. Also ensure to change the `url_base` to the appropriate value for you. Both of these values are stored in `constants.py`.

## Steps Taken in Shortening URL

1. Check if the given long URL already exists in the database. If it does, return the corresponding short URL.
2. If the long URL is not present, a new URL code to add to the URL base is created. It is then checked to ensure that the created URL code is not already present in the database.
3. After this, the URL code and the corresponding long URL is added to the database.
4. Finally, the short URL is returned and displayed on the webpage to the user.
