class InvalidPayloadException(Exception):
    """
    Custom exception class for specific error handling.
    """
    def __init__(self, message, error_code=None):
        """
        Initialize the exception with an error message and optional error code.
        """
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        """
        Return a string representation of the exception.
        """
        if self.error_code:
            return f"[Error {self.error_code}] {super().__str__()}"
        return super().__str__()
