import sys
import json
import os.path
import requests
from string import Template

import dateutil.parser

def posts_at_url(url):

    static_files = [ "leadership.json", "something-else.json" ]
    for static_file in static_files:
        static_file_path = os.path.join(url, static_file)
        resp = requests.get(static_file_path)
        results = json.loads(resp.content)
        for p in results:
            yield p

def documents(name, url, **kwargs):
    
    for post in posts_at_url(url):
        yield post
