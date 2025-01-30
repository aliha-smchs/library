from django.db.models import Field
from django.utils.translation import gettext_lazy as _

class EncryptedTextField(Field):
    description = _("Encrypted text field")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255  # Adjust based on your encryption needs
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'BYTEA'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.decrypt(value)

    def to_python(self, value):
        if value is None:
            return value
        return self.decrypt(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return self.encrypt(value)

    def encrypt(self, value):
        # Use pgcrypto's pgp_sym_encrypt function
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT pgp_sym_encrypt(%s, 'encryption_key')", [value])
            row = cursor.fetchone()
            return row[0]

    def decrypt(self, value):
        # Use pgcrypto's pgp_sym_decrypt function
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT pgp_sym_decrypt(%s, 'encryption_key')", [value])
            row = cursor.fetchone()
            return row[0].tobytes().decode('utf-8')