"""Initialize handler methods.

This class will not invoke by someone. It's just for inheritance.
"""
from abc import ABCMeta, abstractmethod


class Initiator(object, metaclass=ABCMeta):
    """Initialize handler method."""

    def __init__(self, *args, **kwargs):
        """Make headers ready."""
        self.setup(*args, **kwargs)

    @abstractmethod
    def setup(self, *args, **kwargs):
        """Set up passed arguments and update method headers."""
        raise NotImplementedError()
