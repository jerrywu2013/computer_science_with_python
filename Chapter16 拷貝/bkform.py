# L-16 MCS 260 : books
"""
This module defines the formats in which we
store the information of a book on file, e.g.:

'1:2:Making Use of Python:'
The format of a book is a string of 3 fields:
(1) availability, (2) key, (3) title.
"""

def pack(key, status, title):
    """
    Returns the string with book information
    where key is the book identification number,
    status is True or False for availability,
    title is the title of the book.
    """
    if status:
        result = '1:'
    else:
        result = '0:'
    result += '%d:' % key
    result += title + ':\n'
    return result

def get_status(book):
    """
    Given a string with book information,
    returns True or False for the availability.
    """
    splitted = book.split(':')
    return int(splitted[0]) == 1

def get_key(book):
    """
    Given a string with book information,
    returns the identification number of the book.
    """
    splitted = book.split(':')
    return int(splitted[1])

def get_title(book):
    """
    Given a string with book information,
    returns the title of the book.
    """
    splitted = book.split(':')
    return splitted[2]
