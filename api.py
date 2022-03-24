from flask_restful import Resource, abort, reqparse
import url_shortener as us

# arguments for a GET request
url_get_args = reqparse.RequestParser()
url_get_args.add_argument("short_url", type=str, help="The shortened URL.")
url_get_args.add_argument("long_url", type=str, help="The long URL.")

# arguments for a POST request
url_post_args = reqparse.RequestParser()
url_post_args.add_argument("long_url", type=str, help="The long URL is required.", required=True)

class URL(Resource):
    
    def get(self):
        """Returns both the short and long URL based on GET request."""

        short_url, long_url = self.get_args()
        if short_url:
            return self.get_from_short_url(short_url)
        elif long_url:
            return self.get_from_long_url(long_url)
        # neither short or long URL is provided
        abort(400, message="Please provide a short URL or a long URL.")

    def post(self):
        """Creates and returns a shortened URL for a new long URL."""

        args = url_post_args.parse_args(strict=True)
        long_url = args['long_url']
        if us.long_url_exists(long_url):
            abort(400, message="A shortened URL for that long URL already exists. Please try a GET request.")
        short_url = us.url_shortener(long_url)
        response = {
            "short_url": short_url,
            "long_url": long_url
        }
        return response, 201

    def get_args(self):
        """Returns the arguments for each GET request."""

        args = url_get_args.parse_args()
        # getting short url
        try:
            short_url = args['short_url']
        except KeyError:
            short_url = None
        # getting long url
        try:
            long_url = args['long_url']
        except KeyError:
            long_url = None

        return short_url, long_url

    def get_from_short_url(self, short_url):
        """Handles the GET request when the short URL is given."""

        url_code = us.get_url_code_from_short_url(short_url)
        long_url = us.get_long_url(url_code)
        if not long_url:
            abort(404, message="That shortened URL doesn't exist...")
        response = {
            "short_url": us.generate_short_url(url_code),
            "long_url": long_url, 
        }
        return response, 200
    
    def get_from_long_url(self, long_url):
        """Handles the GET request when the long URL is given."""

        if not us.long_url_exists(long_url):
                abort(404, message="That long URL doesn't exist.")
        url_code = us.get_short_url_code(long_url)
        response = {
            "short_url": us.generate_short_url(url_code),
            "long_url": long_url
        }
        return response, 200