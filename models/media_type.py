from enum import Enum


class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"

    @property
    def lower(self):
        return self.value

    @property
    def upper(self):
        return self.name
