import json,requests
def placesByStates(place):
    lan, lon = place[2], place[3]
    gl = json.dumps([{"type":"CIRCLE","position":"{0},{1}".format(lan,lon),"radius":1000000}])
    key = "iB4D6jntYlOdin6qwWqjJpGndY8Dqnbp"
    url = "https://api.tomtom.com/search/2/geometrySearch/IMPORTANT_TOURIST_ATTRACTION.json?key={0}&geometryList={1}&categorySet=9457,7339005,7376003,9927003,9927004,9927005,7376".format(key,gl)
    res = json.loads(requests.get(url).text)['results']
    places = []
    for i in res:
        places.append([i['poi']['name'],i['address'],imageUrl(i['poi']['name'])])
        print(places[-1])
    return places

def imageUrl(name):
    url = "https://rapidapi.p.rapidapi.com/images/search"
    querystring = {"q":name,"count":"1"}
    headers = {
        'x-rapidapi-key': "b7950242dbmsh896e4e949798a68p1a4a56jsn6aa4653dbb2b",
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    kk = json.loads(response.text)
    try:
        result = kk['value'][0]['thumbnailUrl']
    except:
        result = ""
    #print(result)
    return result