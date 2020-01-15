# -*- coding: UTF-8 -*-
'''
Created on 2020-01-13

@author: daizhaolin
'''

import socket

try:
    import httplib
except ImportError:
    import http.client as httplib

try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib


class UnixStreamHTTPConnection(httplib.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.host)


class UnixStreamTransport(xmlrpclib.Transport, object):
    def __init__(self, socketfile):
        self.socketfile = socketfile
        super(UnixStreamTransport, self).__init__()

    def make_connection(self, host):
        if self._connection and host == self._connection[0]:
            return self._connection[1]
        self._connection = host, UnixStreamHTTPConnection(self.socketfile)
        return self._connection[1]


class UnixStreamXMLRPCClient(xmlrpclib.ServerProxy, object):
    def __init__(self, socketfile):
        super(UnixStreamXMLRPCClient,
              self).__init__('http://',
                             transport=UnixStreamTransport(socketfile))


Client = UnixStreamXMLRPCClient
