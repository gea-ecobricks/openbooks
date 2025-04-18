import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It really gotta gotta work!\n'
    version = 'Python v' + sys.version.split()[0] + '\n'
    response = '\n'.join([message, version])
    return [response.encode()]
