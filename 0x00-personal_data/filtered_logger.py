#!/usr/bin/env python3
""" Handling personal data"""

from typing import List
import re
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ('name', 'password', 'phone', 'ssn', 'email')


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str
        ) -> str:
    """returns the log message obfuscated"""

    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)
