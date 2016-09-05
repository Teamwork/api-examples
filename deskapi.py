#!/usr/bin/env python
# encoding: utf-8

''' These are a few examples on how to use the Teamwork Desk API.

These examples are not comprehensive, but they should show how to use the API
for some of the most common tasks.

The full API documentation is available at http://developer.teamwork.com/desk/

For support email desk@teamwork.com

It is recommended that you run this with Python 3; but Python 2 should also
work.

To test this, start a Python console in the directory this file is located:

    $ python

And then use:

    import deskapi
    deskapi.install = 'https://your-url.teamwork.com'
    deskapi.key = 'your-key'

And you can now run the functions.

'''

from __future__ import print_function
import sys

try:
    import requests
except ImportError:
    print("It looks like you don't have the requests module installed.")
    print()
    print('This can be installed with:')
    print()
    print('  $ pip install requests')
    print()
    print('Also see the requests documentation:')
    print("  http://docs.python-requests.org/en/master/user/install/")
    print()
    sys.exit(1)

# Your installation URL
install = 'https://___.teamwork.com'

# Your API key
# You can get one at https://<your-install>/desk/#myprofile/apikeys
key = '___'


# Helper methods so we don't have to add the installation & authentication
def _get(u, **p):    return requests.get(    install + u, auth=(key, ''), **p)
def _post(u, **p):   return requests.post(   install + u, auth=(key, ''), **p)
def _delete(u, **p): return requests.delete( install + u, auth=(key, ''), **p)
def _put(u, **p):    return requests.put(    install + u, auth=(key, ''), **p)

def get_ticket(ticket_id):
    ''' Get one ticket by ID.

    >>> get_ticket(84405978)['ticket']['id']
    84405978
    '''

    r = _get('/desk/v1/tickets/{}.json'.format(ticket_id))
    if r.status_code != 200:
        print('error: status code is', r.status_code)
    return r.json()

def add_note(ticket_id, body, status='', assigned_to=''):
    ''' Add a note to an existing ticket.

    Args:
        status:       'active', 'closed', etc.
        assigned_to:  ID of the user.
    Returns:
        Decoded JSON from the server.

    >>> add_note(84405978, 'Hello')['result']
    'ok'
    '''

    r = _post('/desk/v1/tickets/{}.json'.format(ticket_id), data={
        'isDraft': 'false',
        'type': 'note',
        'body': body,
        'status': status,
        'assignedTo': assigned_to,
    })
    if r.status_code != 200:
        print('error: status code is', r.status_code)
    return r.json()

def add_customer(email, first_name, last_name):
    ''' Add a new customer. '''

    r = _post('/desk/v1/customers.json', data={
        'email': email,
        'firstName': first_name,
        'lastName': last_name,
    })
    if r.status_code != 200:
        print('error: status code is', r.status_code)
    return r.json()

if __name__ == '__main__':
    print(help(__name__))


# The MIT License (MIT)
# Copyright © 2016 Teamwork.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# vim:et
