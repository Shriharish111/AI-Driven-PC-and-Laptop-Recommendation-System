import urllib.parse

def amazon_link(product_name):
    base_url = "https://www.amazon.in/s?k="
    query = urllib.parse.quote_plus(product_name)
    return base_url + query