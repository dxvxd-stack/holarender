import web
import os
from controllers.index import index

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    port = os.environ.get('PORT', '8080')
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', int(port)))