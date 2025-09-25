from enum import IntEnum


class swSelectOption_e(IntEnum):
    """Selection options for SOLIDWORKS objects."""

    swSelectOptionDefault = 0
    swSelectOptionExtensive = 1

    def what(self):
        return {
            0: "Default selection option",
            1: "Extensive selection option",
        }[self.value]