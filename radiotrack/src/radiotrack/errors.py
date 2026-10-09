class RadioException(Exception):
    """Base class for exceptions for Radios."""
    pass

class RadioNotFoundException(RadioException):
    """Exception raised when a radio is not found in the database."""
    pass

class RadioSerialNumberAlreadyExistsException(RadioException):
    """Exception raised when a radio serial number already exists in the database."""
    pass


class ManufacturerException(Exception):
    """ Base class for exception for Manufacturer """
    pass

class ManufacturerNotFoundException(ManufacturerException):
    """ Exception raised when the manufacturer is not found in the database. """
    pass

class AccessoryException(Exception):
    """ Base classs for exception for Accessories. """
    pass

class AccessoryNotFound(AccessoryException):
    """ Exception raised when Accessory is not found. """
    pass
