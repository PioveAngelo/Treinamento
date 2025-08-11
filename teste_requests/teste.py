import requests

url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'

response = requests.get(url)


print(response.status_code)
