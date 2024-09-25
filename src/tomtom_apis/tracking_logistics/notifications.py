"""Notifications API."""

from typing import Self

from ..api import BaseApi


class NotificationsApi(BaseApi):
    """Notifications API.

    The Notifications API and its services provides the ability to read and clear the history of sent notifications. If you wish to stop receiving
    any notifications from the Notifications API services, please contact our Support and provide the address you wish to unsubscribe. See the
    Contact Groups documentation page for further information on the Contact Groups API. TomTom's Notifications service is intended to manage
    communication from Maps APIs to users. The following means of contact are supported:

    For more information, see: https://developer.tomtom.com/notifications-api/documentation/product-information/introduction
    """

    def __init__(self: Self) -> None:  # pylint: disable=super-init-not-called
        """Not implemented.

        Raises:
            NotImplementedError: Always.
        """
        raise NotImplementedError
