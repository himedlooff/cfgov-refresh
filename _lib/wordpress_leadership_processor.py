import sys
import json
import os.path
import requests
from string import Template

import dateutil.parser

def posts_at_url(url):

    url = os.path.expandvars(url)
    resp = requests.get(url)
    results = json.loads(resp.content)
    total = 0
    for p in results['leaders']:
        total += 1
        yield p

def documents(name, url, **kwargs):
    
    for post in posts_at_url(url):
        yield post
