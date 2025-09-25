from enum import IntEnum


class swStartConditions_e(IntEnum):
    """Feature start conditions."""

    swStartSketchPlane = 0
    swStartSurface = 1
    swStartVertex = 2
    swStartOffset = 3

    def what(self):
        return {
            0: "Start from sketch plane",
            1: "Start from surface",
            2: "Start from vertex",
            3: "Start from offset",
        }[self.value]