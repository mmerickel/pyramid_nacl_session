def _export(thing):
    """ No-op; document that ``thing`` is an API.

    Also, shuts pyflakes up about unused import.
    """

from .serializer import EncryptingPickleSerializer
_export(EncryptingPickleSerializer)
from .scripts import generate_secret
_export(generate_secret)
