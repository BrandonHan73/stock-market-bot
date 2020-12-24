from bs4 import BeautifulSoup
import requests


########################################################################################################################

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
        elif cur == '+':
            negative = False
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


########################################################################################################################

tails = ["GSPC", "DJI", "IXIC", "RUT"] \
    # tails = ["GSPC"]
values = {}

for tail in tails:
    print(tail)
    req = requests.get("https://finance.yahoo.com/quote/%5E" + tail + "?p=^" + tail)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    data = soup.find("div", {"id": "YDC-Lead-Stack-Composite", "data-reactid": "24"})
    data = data.find("div", {"id": "Lead-3-QuoteHeader-Proxy"})
    positive = data.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
    negative = data.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"})

    if positive == None:
        data = negative.text
    if negative == None:
        data = positive.text

    for i in range(0, len(data)):
        if data[i] == ' ':
            data = data[:i]
            break;

    values[tail] = stringToDouble(data)

print(values)
