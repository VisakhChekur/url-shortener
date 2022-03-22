import pymongo
import random
import string
import dns.resolver
from constants import url_base, MONGO_DB_CONNECTION_STRING

# fixes dns no nameserver error
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

# retrieving the collection
client = pymongo.MongoClient(MONGO_DB_CONNECTION_STRING)
url_db = client['url_shortener']
url_collection = url_db['urls']


def url_shortener(url):
    """Shortens the url."""

    # check if url already in db
    if long_url_exists(url):
        url_code = get_short_url_code(url)
        return generate_short_url(url_code)

    url_code = ""
    # generate valid url_code to append to url_base
    while not valid_url_code(url_code):
        url_code = generate_url_code()

    # creating short url and updating it to mongodb
    short_url = generate_short_url(url_code)
    update_url_collection(url, url_code)

    return short_url

def generate_url_code():
    """Generates a random url code."""
    
    url_code = [random.choice(string.ascii_letters) for _ in range(5)]
    return "".join(url_code)

def valid_url_code(url_code):
    """Checks if the generated url code is valid or not."""

    if not url_code:
        return False

    if url_code_exists(url_code):
        return False
    
    return True


def url_code_exists(url_code):
    """Checks if give url code exists in the database."""

    result = url_collection.count_documents({"url_code": url_code})
    if result:
        return True
    return False

def long_url_exists(url):
    """Checks if there is a shortened url for the given url already. Returns True if it exists."""

    result = url_collection.count_documents({"long_url": url})
    if result:
        return True
    return False

def get_short_url_code(url):
    """Returns the url code of the shortened url of a long url that is already in the database."""

    result = url_collection.find_one({"long_url": url})
    return result['url_code']

def get_long_url(url_code):
    """Returns the long url if it exists in the database, else it returns None."""

    if not url_code_exists(url_code):
        return None
    result = url_collection.find_one({"url_code": url_code})
    return result['long_url']

def generate_short_url(url_code):
    """Generates the shortened url."""
    return url_base + url_code

def update_url_collection(long_url, url_code):
    """Updates the MongoDB collection."""

    new_entry = {
        "_id": url_collection.count_documents({}) + 1,
        "url_code": url_code,
        "long_url": long_url,
    }
    url_collection.insert_one(new_entry)

"""
SCHEMA OF THE URL COLLECTION
----------------------------

_id: id of document
long_url: the long url that is shortened
url_code: part that is appended to the url base

"""
