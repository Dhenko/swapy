from enum import IntEnum


class swMoveCopyError_e(IntEnum):
    """SOLIDWORKS Move/Copy document errors (2025), excluding obsoletes."""

    swMoveCopyErrorNone = 0
    swMoveCopyErrorSourceDoesNotExist = 1
    swMoveCopyErrorFail = 2

    def what(self):
        """Returns a human-readable description of this error."""
        return {
            0: "Successful",
            1: "Source file does not exist",
            2: "Failed to create destination directories or copy operation failed (possibly permissions issue)",
        }[self.value]