from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_title(value):
    if len(str(value).split(' ')) < 3:
        raise ValidationError(
            _('Your title is not long enough')
        )
