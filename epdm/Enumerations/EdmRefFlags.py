from enum import IntEnum


class EdmRefFlags(IntEnum):
    """Types of item reference."""
    EdmRef_Dynamic = 4
    EdmRef_File = 1
    EdmRef_Item = 2
    EdmRed_Static = 8

    def what(self):
        return {
            4: "Auto-update item to file reference",
            1: "Item to file reference",
            2: "Item to item reference",
            8: "Attachment-type item to file reference"
        }[self.value]
