"""IBSng main access file."""
from .connection.connection import Connection as IBSng
MAJOR_VERSION = '1'
MINOR_VERSION = '2'
MICRO_VERSION = '0'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)
