from rest_framework import exceptions, status


class TokenDoesNotExist(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Token is not valid anymore."


class UserHasNoHotel(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User does not have a hotel."


class CheckWithNoParam(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Must provide email to check."


class GuestDoesNotExist(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Guest does not exist."


class GuestAlreadyExists(exceptions.APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Guest already exists in database."
