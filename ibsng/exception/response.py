"""IBSng 'response exception' exceptions handler."""
from . import auth, unknown


def throw_exception(server_error):
    """Throw exception based on server error.

    :param server_error: sever error body
    :type server_error: str

    :return: exception class
    :rtype: object
    """
    error_code = 'UNKNOWN'

    # Check error content contains error code
    if server_error.find('|') >= 0:
        error_code = server_error.split('|')[0]

    # Find matched exception
    e = {
        'INVALID_ADMIN_NAME': auth.InvalidAuthentication,
        'INCORRECT_PASSWORD': auth.InvalidAuthentication,
        'INVALID_SESSION_ID': auth.InvalidSessionId,
        'UNKNOWN': unknown.UnknownError,
    }.get(error_code, unknown.UnknownError)

    if error_code == 'UNKNOWN' or e == unknown.UnknownError:
        return e(server_error)
    return e()
