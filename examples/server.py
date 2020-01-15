# -*- coding: UTF-8 -*-
'''
Created on 2020-01-14

@author: daizhaolin
'''

from udsxmlrpc import Server

s = Server('/tmp/udsxmlprc.sock')

s.register_introspection_functions()
s.register_function(pow)

def adder_function(x, y):
    return x + y

s.register_function(adder_function, 'add')


class MyFuncs:
    def mul(self, x, y):
        return x * y


s.register_instance(MyFuncs())
s.serve_forever()
