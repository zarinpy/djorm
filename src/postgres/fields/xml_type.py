from xml.etree.ElementTree import ParseError
from xml.etree import ElementTree as xml

from django.core import exceptions
from django.db.models import Field
from django.db.models.fields.mixins import CheckFieldDefaultMixin
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


class XMLField(CheckFieldDefaultMixin, Field):
    empty_strings_allowed = False
    default_error_messages = {
        'invalid': _("'%(value)s' value must be a valid XML string."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'xml'

    def cast_db_type(self, connection):
        return 'xml'

    def to_python(self, value):
        if value is None:
            return None

        return value

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value is None:
            return

        if not isinstance(value, str):
            raise exceptions.ValidationError(
                self.error_messages['invalid'],
                code='invalid',
                params={'value': value},
            )

        try:
            xml.fromstring(value)
        except ParseError:
            raise exceptions.ValidationError(
                self.error_messages['invalid'],
                code='invalid',
                params={'value': value},
            )

    def formfield(self, form_class=None, choices_form_class=None, **kwargs):
        kwargs["widget"] = Textarea
        return super().formfield(form_class, choices_form_class, **kwargs)