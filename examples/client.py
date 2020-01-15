# -*- coding: UTF-8 -*-
'''
Created on 2020-01-14

@author: daizhaolin
'''

from udsxmlrpc import Client

s = Client('/tmp/udsxmlprc.sock')

print(s.pow(2, 3))
print(s.add(2, 3))
print(s.mul(5, 2))

print(s.system.listMethods())
