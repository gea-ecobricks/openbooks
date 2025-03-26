import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html']))
    message = """<!DOCTYPE html><html><head><title>OpenBooks Accounting</title></head><body><div style="font-family: Arial, sans-serif; text-align:center; padding: 20px;"><h1>Welcome to the Global Ecobrick Alliance OpenBooks accounting app</h1><h2>Beta Version</h2><p This is a beta app. The live version remains public at <a href="https://ecobricks.org/en/openbooks" target="_blank">ecobricks.org/openbooks</a></p><br><a href="https://github.com/gea-ecobricks/openbooks/" style="margin-right: 5px; padding: 10px 20px; font-size: 18px; background-color: #444; color: white; text-decoration: none; padding: 5px; border: none; cursor: pointer;">View GitHub Repository</a><br><a href="https://ecobricks.org/en/openbooks/" style="margin-right: 5px; padding: 10px 20px; font-size: 18px; background-color: #444; color: white; text-decoration: none; padding: 5px; border: none; cursor: pointer;">View current OpenBooks</a></div></body></html>"""
    return [message.encode()]
