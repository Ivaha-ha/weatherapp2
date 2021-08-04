"""
weather app progect!!!
"""
ACCU_URL = 'https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561'
import html
from urllib.request import urlopen, Request

#getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
accu_request = Request(ACCU_URL, headers=headers)
accu_page = urlopen(accu_request).read()
accu_page = str(accu_page)

ACCU_TEMP_TAG = '<div class="temp">'
print(accu_page.find(ACCU_TEMP_TAG))
"""
accu_temp_start = accu_page.find(ACCU_TEMP_TAG)+len(ACCU_TEMP_TAG)
accu_temp_finish = accu_temp_start + 4
print(accu_page[accu_temp_start : accu_temp_finish])
"""
accu_temp_tag_size = len(ACCU_TEMP_TAG)
accu_temp_tad_index = accu_page.find(ACCU_TEMP_TAG)
accu_temp_value_start = accu_temp_tad_index + accu_temp_tag_size
accu_temp = ''
for char in accu_page[accu_temp_value_start:]:
    if char != '<':
        accu_temp += char
    else:
        break
print('ACCUWEATHER:\n')
print(f'Temperature: {html.unescape(accu_temp)}')

#print(accu_page)








