# -*- coding: UTF-8 -*-
'''
Created on 2020-01-13

@author: daizhaolin
'''

import os
import socketserver

from xmlrpc.server import (SimpleXMLRPCDispatcher,
                           SimpleXMLRPCRequestHandler)


class UnixStreamXMLRPCRequestHandler(SimpleXMLRPCRequestHandler):
    disable_nagle_algorithm = False

    def address_string(self):
        return self.client_address


class UnixStreamXMLRPCServer(socketserver.UnixStreamServer,
                             SimpleXMLRPCDispatcher):
    def __init__(self, addr, requestHandler=UnixStreamXMLRPCRequestHandler,
                 logRequests=True, allow_none=False, encoding=None,
                 bind_and_activate=True, use_builtin_types=False):
        self.logRequests = logRequests

        if os.path.exists(addr):
            os.remove(addr)

        SimpleXMLRPCDispatcher.__init__(self, allow_none, encoding, use_builtin_types)
        socketserver.UnixStreamServer.__init__(self, addr, requestHandler, bind_and_activate)


server = UnixStreamXMLRPCServer
