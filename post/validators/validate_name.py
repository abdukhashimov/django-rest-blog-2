from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_name(value):
    if len(str(value)) < 3:
        raise ValidationError(
            _('You name is not long enough')
        )
