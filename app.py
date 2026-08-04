import web
from controllers.index import index

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()