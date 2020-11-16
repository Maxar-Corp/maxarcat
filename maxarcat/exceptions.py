#
# exceptions.py
#


class CatalogError(Exception):
    def __init__(self, message, status=None, response=None, request_id=None):
        """
        An exception from the STAC catalog web service

        :param message: User-friendly error message
        :param status: Optional HTTP status
        :param response: Optional response object for request that caused error
        :param request_id: Optional request ID
        """
        self.message = message
        self.status = status
        self.response = response
        self.request_id = request_id

    def __str__(self):
        options = ['message={!r}'.format(self.message)]
        if self.status:
            options.append('status={!r}'.format(self.status))
        if self.request_id:
            options.append('request_id={!r}'.format(self.request_id))
        return 'CatalogError({})'.format(', '.join(options))
