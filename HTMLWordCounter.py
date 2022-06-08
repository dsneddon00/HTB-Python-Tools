import requests

PAGE_URL = 'http://138.68.162.48:31994/' # change the target and the port to what suits you

resp = requests.get(PAGE_URL)
html_str = resp.content.decode()
print(html_str)
