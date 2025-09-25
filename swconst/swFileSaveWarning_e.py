from enum import IntEnum


class swFileSaveWarning_e(IntEnum):
    """File Save warning codes."""

    swFileSaveWarning_RebuildError = 1
    swFileSaveWarning_NeedsRebuild = 2
    swFileSaveWarning_ViewsNeedUpdate = 4
    swFileSaveWarning_AnimatorNeedToSolve = 8
    swFileSaveWarning_AnimatorFeatureEdits = 16
    swFileSaveWarning_EdrwingsBadSelection = 32
    swFileSaveWarning_AnimatorLightEdits = 64
    swFileSaveWarning_AnimatorCameraViews = 128
    swFileSaveWarning_AnimatorSectionViews = 256
    swFileSaveWarning_MissingOLEObjects = 512
    swFileSaveWarning_OpenedViewOnly = 1024
    swFileSaveWarning_XmlInvalid = 2048

    def what(self):
        return {
            1: "Rebuild error occurred during save.",
            2: "Document needs rebuild before save.",
            4: "Some views need to be updated.",
            8: "Animator: model needs to be solved.",
            16: "Animator: feature edits detected.",
            32: "eDrawings: bad selection.",
            64: "Animator: light edits detected.",
            128: "Animator: camera views included.",
            256: "Animator: section views included.",
            512: "OLE objects are missing.",
            1024: "Drawing is opened in view-only mode.",
            2048: "Invalid XML detected in the document.",
        }[self.value]
