from rest_framework import exceptions, status


class TokenDoesNotExist(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Token is not valid anymore."


class UserHasNoHotel(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User does not have a hotel."
