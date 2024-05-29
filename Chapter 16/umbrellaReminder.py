import requests, bs4
from twilio.rest import Client

accountSID = 'xxxx'
authToken = 'xxxx'
myNumber = '+xxxx'
twilioNumber = '+xxxxx'

def rain_check():
    url = 'https://weather.com/nl-NL'
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    weather_elem = soup.select('.CurrentConditions--phraseValue--mZC_p')
    weather = weather_elem[0].getText()
    
    if 'regen' in weather.lower():
        return True

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

if rain_check():
    textmyself('Remember to take an umbrella.')