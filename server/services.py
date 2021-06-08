from googleapiclient.discovery import build
import datetime
import asyncio
import threading
import time
from rake_nltk import Rake
from . import models

def get_key():
    file = open('./keys.txt')
    keys = file.read().split('\n')

    return keys

def select_key(keys):
    SERVICE = 'youtube'
    VERSION = 'v3'
    DATE = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)).isoformat()
    MAX = 1
    for key in keys:
        try:
            youtube_object = build(SERVICE, VERSION, developerKey = keys[0])
            search_keyword = youtube_object.search().list(q='cricket', part="id, snippet", publishedAfter= DATE, maxResults=MAX).execute()

            results = search_keyword.get("items", [])
            return key
        except:
            pass

    ## if we reach here, then no valid key
    return ''

        

def youtube_query(query):
    keys = get_key()
    key = select_key(keys)
    if(key == ''):
        print('No valid key')
        return {}
    SERVICE = 'youtube'
    VERSION = 'v3'
    DATE = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)).isoformat()
    MAX = 100
    try:
        youtube_object = build(SERVICE, VERSION, developerKey = keys[0])
        search_keyword = youtube_object.search().list(q=query, part="id, snippet", publishedAfter= DATE, maxResults=MAX).execute()

        results = search_keyword.get("items", [])
    except:
        print('Key exhausted')  # TODO
        keys.pop(0)
        results = {}

    # print(results)
    return results

def get_keywords(title):
    # rake nltk
    rake_obj = Rake()
    rake_obj.extract_keywords_from_text(title)
    phrases = rake_obj.get_ranked_phrases()
    return ' '.join(phrases)


def extract_info(result):
    info = {
        'video_id': result['id']['videoId'],
        'title' : result['snippet']['title'],
        'description': result['snippet']['description'],
        'thumbnail_url': result['snippet']['thumbnails']['default']['url'],
        'published_at': result['snippet']['publishedAt'],
        'keywords': get_keywords(result['snippet']['title'])
    }
    return info

def store_in_db(result):
    info = extract_info(result)
    model_obj = models.Video(video_id=info['video_id'], video_title=info['title'], description=info['description'], thumbnail_url=info['thumbnail_url'], published_at=info['published_at'], keywords=info['keywords'])
    model_obj.save()

async def start_service():
    while True:
        search_results = youtube_query('cricket')
        # print(search_results)
        if search_results == {}:
            return

        for result in search_results:
            print(result)
            store_in_db(result=result)

        await asyncio.sleep(10)

def start():
    while True:
        api_keys = get_key()
        if len(api_keys):
            asyncio.run(start_service())
        time.sleep(10)

THREAD = threading.Thread(target=start)







