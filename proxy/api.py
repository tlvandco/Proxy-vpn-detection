import requests

def getinfo(ip):
    response = requests.get("https://ipqualityscore.com/api/json/ip/ZbVWRTqaxPzptPaNVoSTfklEjKK6TRCr/"+ip)
    return response.json()