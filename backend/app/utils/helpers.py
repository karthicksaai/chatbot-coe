from datetime import datetime
from bson import ObjectId

def serialize_id(id):
    """Convert ObjectId to string for JSON serialization"""
    if isinstance(id, ObjectId):
        return str(id)
    return id

def format_datetime(dt):
    """Format datetime object to string"""
    if isinstance(dt, datetime):
        return dt.isoformat()
    return dt
