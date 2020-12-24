from bs4 import BeautifulSoup
import requests

def charToInt(character):
    if character == '0':
        return 0
    elif character == '1':
        return 1
    elif character == '2':
        return 2
    elif character == '3':
        return 3
    elif character == '4':
        return 4
    elif character == '5':
        return 5
    elif character == '6':
        return 6
    elif character == '7':
        return 7
    elif character == '8':
        return 8
    elif character == '9':
        return 9
    

def stringToDouble(string):
    negative = False
    isDouble = False
    retVal = 0

    for cur in string:
        if cur == '-':
            negative = True
        elif cur == '.':
            isDouble = True
        else:
            retVal = retVal * 10
            retVal = retVal + charToInt(cur)

    if negative:
        retVal = -retVal

    exponent = len(string) - string.find('.') - 1
    for i in range(0, exponent):
        retVal = retVal / 10

    return retVal

tails = ["GSPC", "DJI", "IXIC", "RUT"]
values = {}

for tail in tails:

    req = requests.get("https://finance.yahoo.com/quote/%5E" + tail + "?p=^" + tail)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    change = soup.find_all("span", {"data-reactid": "34"})[1].text

    while True:
        if change[-1] != ' ':
            change = change[:-1]
        else:
            change = change[:-1]
            break

    if change[0] == '+':
        change = change[1:]

    values[tail] = stringToDouble(change)

print(values)