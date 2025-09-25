from enum import IntEnum


class swSketchChamferType_e(IntEnum):
    """Chamfer types."""
    swSketchChamfer_DistanceAngle = 0
    swSketchChamfer_DistanceDistance = -1
    swSketchChamfer_DistanceEqual = 2

    def what(self):
        return {
            0: "Angle & Distance chamfer",
            -1: "Distance & Distance chamfer",
            2: "Two equal Distances chamfer",
        }[self.value]