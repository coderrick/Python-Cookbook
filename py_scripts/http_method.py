#http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
import urllib.request

urllib.request.urlopen("http://google.com").read()