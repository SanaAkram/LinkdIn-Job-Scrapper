
import requests
from urllib.parse import urlparse, urlencode


def parse_cookies(cookie_str):
    cookies = {}
    if cookie_str:
        cookie_list = cookie_str.split("; ")
        for cookie in cookie_list:
            key, value = cookie.split("=")
            cookies[key] = value
    return cookies

def redirect_to_https(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == "http":
        return "https://" + url[len("http://"):]

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain not in ["www.linkedin.com", "www.linkedin.cn"]:
        subdomain_index = domain.find(".linkedin")
        if subdomain_index != -1:
            domain = "www" + domain[subdomain_index:]
    return domain


def redirect_to_authwall(url, trk, trk_info, original_referer):
    domain = get_domain(url)
    params = {
        "trk": trk,
        "trkInfo": trk_info,
        "original_referer": original_referer[:200],
        "sessionRedirect": url
    }
    authwall_url = f"https://{domain}/authwall?{urlencode(params)}"
    return authwall_url


# Example usage:
url = "http://www.linkedin.com"
cookie_str = "trkCode=xyz; trkInfo=abc; sl=123"
referer = "https://www.example.com"
trk = "xyz"
trk_info = "abc"

cookies = parse_cookies(cookie_str)
https_url = redirect_to_https(url)
authwall_url = redirect_to_authwall(https_url, trk, trk_info, referer)
print("Redirect to Authwall URL:", authwall_url)
