import re
from rest_framework.exceptions import  ValidationError


email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
phone_regex = re.compile("^9\d{12}$")
def chack_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = "email"
    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = "phone"
    else:
        data = {
            "success": False,
            "massage":"Email yoki telfon raqamoingiz notogri"
        }
        raise ValidationError(data)
    return email_or_phone