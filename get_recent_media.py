import requests
import urllib
from get_user_id import get_user_username, get_user_id
from const import BASE_URL, APP_ACCESS_TOKEN


def get_recent_media(user_id):

    if user_id != 0:
        req_url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + APP_ACCESS_TOKEN
    else:
        print "User does not exist."
        exit()
    #   fetching recent media's data.
    data = requests.get(req_url).json()
    #   fetched
    query = raw_input("Get post by searching for keyword in caption: ")
    if not query:
        print data['data'][0]['id']
        img_url = data['data'][0]['images']['standard_resolution']['url']
        urllib.urlretrieve(img_url, 'hey.jpg')
        return data['data'][0]['id']
    else:
        count = 0
        for temp in data['data']:
            if temp['caption']['text'].find(query) > 0:
                break
        else:
            count += 1
        print data['data'][count]['id']
        img_url = data['data'][count]['images']['standard_resolution']['url']
        urllib.urlretrieve(img_url, 'hey.jpg')
        return data['data'][count]['id']

    #   Downloading the image.