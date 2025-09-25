"""Actions to take if the corner to be filleted is constrained or has a dimension."""
from enum import IntEnum


class swConstrainedCornerAction_e(IntEnum):
    """Options for handling constrained corners when adding fillets in SOLIDWORKS."""

    swConstrainedCornerInteract = 0
    swConstrainedCornerKeepGeometry = 1
    swConstrainedCornerDeleteGeometry = 2
    swConstrainedCornerStopProcessing = 3

    def what(self):
        return {
            0: "Ask the user whether to delete the geometry or stop processing",
            1: "Keep the constraint or dimension by creating a virtual intersection point before adding the fillet",
            2: "Delete the constraint or dimension and add the fillet",
            3: "Do not delete the constraint or dimension and do not create the fillet",
        }[self.value]
