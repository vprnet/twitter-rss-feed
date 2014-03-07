from flask import Flask, render_template
from config import NPR_API_KEY
import requests
app = Flask(__name__)

DEBUG = True

@app.route('/')
def rss_feed():
    r = requests.get('http://api.npr.org/query?id=176665462,161419865,175255325' +
        '&orgid=692&action=or&output=RSS&apiKey=%s' % (NPR_API_KEY))
    return r.text

if __name__ == '__main__':
    app.run()
