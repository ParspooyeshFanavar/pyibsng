"""Initialize handler methods."""


class Initiator(object):
    """Initialize handler method."""

    def __init__(self, *args, **kwargs):
        """Make headers ready."""
        self.setup(*args, **kwargs)
        self.control()

    def setup(self, *args, **kwargs):
        """Set up passed arguments and update method headers."""
        raise NotImplementedError()