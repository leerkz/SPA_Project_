from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def youtube_only_validator(value):
    parsed_url = urlparse(value)
    if 'youtube.com' not in parsed_url.netloc:
        raise ValidationError("Разрешены только ссылки на youtube.com")
