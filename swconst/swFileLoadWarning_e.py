from enum import IntEnum

class swFileLoadWarning_e(IntEnum):
    """SOLIDWORKS file load warnings (bitmask), SolidWorks swFileLoadWarning_e (2025)."""

    swFileLoadWarning_IdMismatch = 1
    swFileLoadWarning_ReadOnly = 2
    swFileLoadWarning_SharingViolation = 4
    swFileLoadWarning_DrawingANSIUpdate = 8
    swFileLoadWarning_SheetScaleUpdate = 16
    swFileLoadWarning_NeedsRegen = 32
    swFileLoadWarning_BasePartNotLoaded = 64
    swFileLoadWarning_AlreadyOpen = 128
    swFileLoadWarning_DrawingsOnlyRapidDraft = 256
    swFileLoadWarning_ViewOnlyRestrictions = 512
    swFileLoadWarning_ViewMissingReferencedConfig = 1024
    swFileLoadWarning_DrawingSFSymbolConvert = 2048
    swFileLoadWarning_RevolveDimTolerance = 4096
    swFileLoadWarning_ModelOutOfDate = 8192
    swFileLoadWarning_ComponentMissingReferencedConfig = 16384
    swFileLoadWarning_AutomaticRepair = 262144
    swFileLoadWarning_CriticalDataRepair = 524288
    swFileLoadWarning_MissingDesignTable = 131072
    swFileLoadWarning_InvisibleDoc_LinkedDesignTableUpdateFail = 65536
    swFileLoadWarning_MissingExternalReferences = 1048576

    def what(self):
        """Returns a human-readable description of this warning."""
        return {
            1: "Internal document ID does not match referenced document",
            2: "Document is read-only",
            4: "Document is in use by another process",
            8: "ANSI dimension arrow update in drawing",
            16: "Sheet scale applied to sketch entities",
            32: "Document needs to be rebuilt",
            64: "Base part not loaded",
            128: "Document already open",
            256: "RapidDraft only applies to drawings",
            512: "View-only document with restricted configuration",
            1024: "View references missing configuration",
            2048: "Converted surface finish symbols in drawing",
            4096: "Revolved dimension tolerance legacy mismatch",
            8192: "Model is out of date with drawing views",
            16384: "Component missing referenced configuration",
            65536: "Invisible document with linked design table failed to update",
            131072: "Missing design table",
            262144: "Non-critical custom property data automatically repaired",
            524288: "Critical data in document automatically repaired",
            1048576: "External references missing when loading",
        }[self.value]