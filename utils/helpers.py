import string, random


def generate_short_code(length=6):
    """Generate a random short code."""
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return short_code


def get_short_url(request, short_code):
    """Get the short URL."""
    url = request.build_absolute_uri(f"/shortify-url/{short_code}/")
    return url