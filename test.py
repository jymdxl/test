import urllib.request

url = "http://bin.entware.net/armv7sf-k2.6/"
req = urllib.request.Request(url)
req.add_header(
    'User-Agent',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
)
data = urllib.request.urlopen(req).read()
file = open("/home/jt/test/entware.html", "wb")
file.write(data)
file.close()