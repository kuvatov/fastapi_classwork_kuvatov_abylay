class NotFoundException(Exception):
   """Raises when get fails"""


class CreateException(Exception):
   """Raises when creation fails"""


class UpdateException(Exception):
   """Raises when update fails"""


class DeleteException(Exception):
   """Raises when deletion fails"""
   