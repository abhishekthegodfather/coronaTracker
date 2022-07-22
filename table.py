# # Developing the API for Tracking Active Corona Virus Cases

# from cgitb import text
import requests
from bs4 import BeautifulSoup
from flask import jsonify, Flask

# from collections import deque

app = Flask(__name__)
@app.route('/')

def coronaAPI():
    url = "https://www.worldometers.info/coronavirus/"

    res = requests.get(url)
    HtmlData = res.text
    # print(res.content);


    soup = BeautifulSoup(res.text, "html.parser")
    PreHtml = soup.prettify()
    # print(PreHtml);

    CaseDom = soup.find_all('div', id="maincounter-wrap")
    arr = []
    inidArr = []

    for i in CaseDom:
        textEle = i.text
        textEle = textEle.strip()
        arr.append(textEle)

    # print(arr)

    for i in arr:
        tex = i.split('\n\n')
        inidArr.append(tex)

    # print(inidArr)

    itemDict = {item[0] : "".join(item[1:]) for item in inidArr}

    # corrected_dict = { k.replace(':', ''): v for k, v in itemDict.items() }
    final_dict = { k.replace(':', ''): int(v.replace(",", "")) for k, v in itemDict.items() }

    jData = jsonify(final_dict)
    # print(corrected_dict)
    # print(jData)
    return jData

if __name__ == '__main__':
    app.run(debug= True)


# # randomArry = []
# # for i in itemDict:
# #     i = i.split(':')
# #     # print(type(i[0]))
# #     randomArry.append(i[0]);
# #     # print(i)

# print(len(randomArry))


# for j in itemDict:
#     for i in randomArry:
#         itemDict[randomArry[i]] = itemDict.pop(i)

# # print(inidArr)










# arr = []
# inidArr = []

# for i in CaseDom:
#     textEle = i.text
#     textEle = textEle.strip()
#     arr.append(textEle)

#     # print(arr)

# for i in arr:
#     tex = i.split('\n\n')
#     inidArr.append(tex)

#     # print(inidArr)

# itemDict = {item[0] : "".join(item[1:]) for item in inidArr}

#     # corrected_dict = { k.replace(':', ''): v for k, v in itemDict.items() }
# final_dict = { k.replace(':', ''): int(v.replace(",", "")) for k, v in itemDict.items() }


    # print(corrected_dict)
    # print(jData)
  





