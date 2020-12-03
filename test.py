import sys
import json
import time
import logging
import winerror
import win32api
import win32event
import threading
import http.server
from logging import handlers
from urllib.parse import urlparse, parse_qs

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global logger
        logger.info('do_GET: ++')
        uri = urlparse(self.path)
        if uri.path.startswith(r'/api'):
            self.handle_api(uri)
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Hello, world')
        logger.info('do_GET: --')

    def handle_api(self, uri):
        global logger
        logger.info('handle_api: ++')
        input_data = parse_qs(uri.query)
        data = {'error':0, 'message': 'error message', 'start_detection': str(int(time.time())), 'path': uri.path, 'input_data': input_data}
        self.send_response(200)
        self.send_header("Content-type", "applicatin/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        logger.info('handle_api: --')


def run():
    global logger
    logger.info('run: ++')
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', 20330), MyHandler)
    httpd.serve_forever()
    logger.info('run: --')

def prepare_log():
    global logger
    logger = logging.getLogger('test')
    logger.setLevel(logging.INFO)
    fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(fmt))
    th = handlers.TimedRotatingFileHandler('test.log',when='D',backupCount=3, encoding='utf-8')
    th.setFormatter(logging.Formatter(fmt))
    logger.addHandler(sh)
    logger.addHandler(th)
    return logger


def start_service():
    global logger
    logger.info('start_service: ++')
    evt = win32event.CreateEvent(None, False, False, "test")
    err = win32api.GetLastError()
    if err == winerror.ERROR_ALREADY_EXISTS:
        logger.info('Instance already running.')
    else:
        t=threading.Thread(target=run, daemon=True)
        t.start()
        win32event.WaitForSingleObject(evt, win32event.INFINITE)
    win32api.CloseHandle(evt)
    logger.info('start_service: --')


if __name__ == '__main__':
    global logger
    if len(sys.argv) > 1:
        if sys.argv[1] == '-kill-service':
            evt = win32event.CreateEvent(None, False, False, "test")
            win32event.SetEvent(evt)
            win32api.CloseHandle(evt)
    else:
        logger = prepare_log()
        logger.info("Start:")
        start_service()
        logger.info("End:")
    sys.exit(0)