udsxmlrpc
=========

Unix domain socket XML-RPC

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install -U udsxmlrpc

Server Simple Example
---------------------

.. code-block:: python

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

.. code-block:: text

    $ python server.py

Client Simple Example
---------------------

.. code-block:: python

    from udsxmlrpc import Client

    s = Client('/tmp/udsxmlprc.sock')

    print(s.pow(2, 3))
    print(s.add(2, 3))
    print(s.mul(5, 2))

    print(s.system.listMethods())

.. code-block:: text

    $ python client.py
    8
    5
    10
    ['add', 'mul', 'pow', 'system.listMethods', 'system.methodHelp', 'system.methodSignature']

.. _pip: https://pip.pypa.io/en/stable/quickstart/
