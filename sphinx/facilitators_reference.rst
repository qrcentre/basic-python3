Facilitator's Reference
=======================

Part 3
------
- ``telegram_*`` methods raise ``urllib.error.HTTPError: HTTP Error 401:
  Unauthorized``: check that the HTTP API token was copied correctly.
- ``telegram_send`` method raises ``urllib.error.HTTPError: HTTP Error 400: Bad
  Request``: check that the ``/start`` command has been sent to the bot through
  telegram.
