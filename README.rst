IBSng Python Driver
===================
This library provides access on IBSng JSON-RPC API.

Support
=======
* Python 2.7.x
* Python 3.x.x

Install
=======
Pyibsng is accessible by `pip`.

.. code-block:: shell

    $ pip install pyibsng

Get Started
===========
Getting started document_.

.. _document: https://github.com/ParspooyeshFanavar/pyibsng/blob/master/docs/get-started.rst

To start using this library we need to import `IBSng` package:

.. code-block:: python

    from ibsng import IBSng


Test Authentication:

.. code-block:: python

    con = IBSng("user:password@http://ip:port")
    con.auth()

Get all charge info:

.. code-block:: python

    charges = con.charge.getChargeInfo("sample1")
    print(charges.result)
    print(charges.json)


To have list of all handlers and methods, checkout handlers.xml_.

.. _handlers.xml: https://github.com/ParspooyeshFanavar/pyibsng/blob/master/docs/handlers.xml


Current Handler Support
=======================

+--------------------------+----------+--------+
| Description              | Methods  | Status |
+==========================+==========+========+
| admin                    | 11       | Stable |
+--------------------------+----------+--------+
| appnama                  | 2        | Stable |
+--------------------------+----------+--------+
| bw                       | 25       | Stable |
+--------------------------+----------+--------+
| charge                   | 10       | Stable |
+--------------------------+----------+--------+
| extra_charge             | 6        | Stable |
+--------------------------+----------+--------+
| group                    | 11       | Stable |
+--------------------------+----------+--------+
| invoice                  | 24       | Stable |
+--------------------------+----------+--------+
| ippool                   | 11       | Stable |
+--------------------------+----------+--------+
| isp                      | 14       | Stable |
+--------------------------+----------+--------+
| ldap                     | 9        | Stable |
+--------------------------+----------+--------+
| log_console              | 1        | Stable |
+--------------------------+----------+--------+
| login                    | 3        | Stable |
+--------------------------+----------+--------+
| perm                     | 14       | Stable |
+--------------------------+----------+--------+
| ras                      | 16       | Stable |
+--------------------------+----------+--------+
| session                  | 3        | Stable |
+--------------------------+----------+--------+
| stat                     | 3        | Stable |
+--------------------------+----------+--------+
| system_notification      | 2        | Stable |
+--------------------------+----------+--------+
| user                     | 39       | Stable |
+--------------------------+----------+--------+
| user_custom_field        | 4        | Stable |
+--------------------------+----------+--------+
| util                     | 22       | Stable |
+--------------------------+----------+--------+
| voip_provider            | 2        | Stable |
+--------------------------+----------+--------+
| voucher                  | 10       | Stable |
+--------------------------+----------+--------+

Under Development
=================
Incompleted handlers:

* telephony_support
* mc
* online_payment
* notification
* snapshot
* report

Incompleted sections:

* tests

Contribute
==========
If you find a bug or have an update, kindly create an issue in github page and send us a pull request.

To write new module, checkout write-module_ document.

.. _write-module: https://github.com/ParspooyeshFanavar/pyibsng/blob/master/docs/write-module.rst
