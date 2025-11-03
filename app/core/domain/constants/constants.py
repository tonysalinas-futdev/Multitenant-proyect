from enum import Enum 

class Status(str,Enum):
    ACTIVE="active"
    ON_VACATION="on vacation"
    INACTIVE="inactive"

class UserRole(str,Enum):
    ADMIN="admin"
    MANAGER="manager"
    VIEWER="viewer"
