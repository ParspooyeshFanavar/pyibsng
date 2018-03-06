"""IBSng main access file."""
from .connection.connection import Connection
IBSng = Connection
MAJOR_VERSION = '1'
MINOR_VERSION = '2'
MICRO_VERSION = '2'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)
