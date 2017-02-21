import httplib
import os
import signal
import threading
import time

import bjoern

HOST = ('127.0.0.1', 9000)

request_completed = False

def application(environ, start_response):
    start_response('200 ok', [])
    yield "chunk1"
    os.kill(os.getpid(), signal.SIGINT)
    yield "chunk2"
    yield "chunk3"
    global request_completed
    request_completed = True


def requester():
    conn = httplib.HTTPConnection(*HOST)
    conn.request("GET", "/")
    conn.getresponse()


threading.Thread(target=requester).start()
try:
    bjoern.run(application, *HOST)
except KeyboardInterrupt:
    assert request_completed
else:
    raise RuntimeError("Didn't receive KeyboardInterrupt")
