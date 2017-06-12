from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class EmailNullField(models.EmailField):
    description = "EmailField that stores NULL"

    def get_db_prep_value(self, value, connection=None, prepared=False):
        value = super(EmailNullField, self).get_db_prep_value(value, connection, prepared)
        if value == "":
            return None
        else:
            return value


class PhoneNumberNullField(PhoneNumberField):
    description = "PhoneNumberField that stores NULL when empty"

    def get_db_prep_value(self, value, connection=None, prepared=False):
        value = super(PhoneNumberNullField, self).get_db_prep_value(value, connection, prepared)
        if value == "":
            return None
        else:
            return value
