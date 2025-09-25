from enum import IntEnum


class swMoveCopyOptions_e(IntEnum):
    """SOLIDWORKS Move/Copy document options (bitmask), SolidWorks swMoveCopyOptions_e."""

    swMoveCopyOptionsOverwriteExistingDocs = 1
    swMoveCopyOptionsCreateNewFolder = 2

    def what(self):
        """Returns a human-readable description of this move/copy option."""
        return {
            1: "Overwrite existing documents",
            2: "Create a new folder for the copied documents",
        }[self.value]