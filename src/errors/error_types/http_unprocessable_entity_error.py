class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = "Unprocessabl Entity"
        self.status_code = 422
