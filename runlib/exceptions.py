class NoActivityFound(Exception):
    """Exception raised when no activity is found in the database."""
    pass

class NoFitFileInZip(Exception):
    """Exception raised when no FIT file is found in the ZIP file."""
    pass