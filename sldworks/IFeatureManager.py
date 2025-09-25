"""
Wrapper for IFeatureManager in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager.html?verRedirect=1

Allows you to create features.
"""

from swapy.sldworks import IFeature


class IFeatureManager:
    def __init__(self, comm_object):
        """
        Creates an instance of the IFeatureManager wrapper from the Solidworks API
        :param __comm_object: COM object representing IFeatureManager instance from Solidworks API\n
        """
        self.__comm_object = comm_object

    def FeatureExtrusion3(self, Sd: bool, Flip: bool, Dir: bool, T1: int, T2: int, D1: float, D2: float,
                          Dchk1: bool, Dchk2: bool, Ddir1: bool, Ddir2: bool, Dang1: float, Dang2: float,
                          OffsetReverse1: bool, OffsetReverse2: bool, TranslateSurface1: bool, TranslateSurface2: bool,
                          Merge: bool, UseFeatScope: bool, UseAutoSelect: bool, T0: int, StartOffset: float,
                          FlipStartOffset: bool):
        """
        Creates an extruded feature.\n

        The default direction for cut operations is opposite the sketch normal. The default direction for boss operations
        is along the sketch normal. Setting the Dir argument to True reverses the default direction.
        For double-ended extrusions, Direction 2 is always opposite to Direction 1.
        :param Sd: True for single ended, false for double ended
        :param Flip: True to flip the side to cut
        :param Dir: True to flip the direction of extrusion
        :param T1: Termination type for first end of the extrusion as defined in swEndConditions_e
        :param T2: Termination type for second end of the extrusion as defined in swEndConditions_e
        :param D1: Depth of extrusion for first end in meters; offset, if T1 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param D2: Depth of extrusion for second end in meters; offset, if T2 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param Dchk1: True to allow drafting in the first direction, false to not
        :param Dchk2: True to allow drafting in the second direction, false to not
        :param Ddir1: True for first draft angle to be inward, false to be outward; valid only if Dchk1 is true
        :param Ddir2: True for second draft angle to be inward, false to be outward; valid only if Dchk2 is true
        :param Dang1: Draft angle for first end; valid only if Dchk1 is true
        :param Dang2: Draft angle for second end; valid only if Dchk2 is true
        :param OffsetReverse1: True to offset the first end from another face or plane in a direction away from the sketch,
            false to offset in a direction toward the sketch; valid only if T1 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param OffsetReverse2: True to offset the second end from another face or plane in a direction away from the sketch,
            false to offset in a direction toward the sketch; valid only if T2 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param TranslateSurface1: True if the first end of the extrusion is a translation of the reference surface,
            false if it has a true offset; valid only if T1 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param TranslateSurface2: True if the second end of the extrusion is a translation of the reference surface,
            false if it has a true offset; valid only if T2 is set to swEndConditions_e.swEndCondOffsetFromSurface
        :param Merge: True to merge the results in a multibody part, false to not
        :param UseFeatScope: True if the feature only affects selected bodies, false if the feature affects all bodies
        :param UseAutoSelect: True to automatically select all bodies and have the feature affect those bodies,
            false to select the bodies that the feature affects
        :param T0: Start condition as defined in swStartConditions_e
        :param StartOffset: Distance from the sketch plane to start the extrude; valid only if T0 is set to swStartConditions_e.swStartOffset
        :param FlipStartOffset: True to flip the direction of the start offset, false to not; valid only if T0 is set to swStartConditions_e.swStartOffset
        :return:
        """
        return IFeature.IFeature(self.__comm_object.FeatureExtrusion3(Sd, Flip, Dir, T1, T2, D1, D2, Dchk1, Dchk2,
                                                                      Ddir1, Ddir2, Dang1, Dang2, OffsetReverse1,
                                                                      OffsetReverse2, TranslateSurface1, TranslateSurface2,
                                                                      Merge, UseFeatScope, UseAutoSelect, T0,
                                                                      StartOffset, FlipStartOffset))

    def FeatureRevolve2(self, SingleDir: bool, IsSolid: bool, IsThin: bool, IsCut: bool, ReverseDir: bool,
                        BothDirectionUpToSameEntity: bool, Dir1Type: int, Dir2Type: int, Dir1Angle: float,
                        Dir2Angle: float, OffsetReverse1: bool, OffsetReverse2: bool, OffsetDistance1: float,
                        OffsetDistance2: float, ThinType: int, ThinThickness1: float, ThinThickness2: float,
                        Merge: bool, UseFeatScope: bool, UseAutoSelect: bool):
        """
        Creates a base-, boss-, or cut-revolve feature.\n

        Before calling this method, call IModelDocExtension::SelectByID2 to select:\n

        - the sketch to revolve, using Mark = 0.\n
        - the axis of revolution, using Mark = 4 or 16.\n
        - the up-to surface, up-to vertex, or offset-from surface, using Mark = 32.\n
        - one or more affected bodies or components (only if UseFeatScope is set to true and UseAutoSel is set to false),
        using Mark = 1 for each.\n
        :param SingleDir: True if the revolve is in one direction, false if in two directions
        :param IsSolid: True if this is a solid revolve feature, false if not
        :param IsThin: True if this is a thin revolve feature, false if not
        :param IsCut: True if this is a cut revolve feature, false if not
        :param ReverseDir: True reverses the angle of the revolution, false does not; only applies if Dir1Type is not swEndConditions_e.swEndCondMidPlane
        :param BothDirectionUpToSameEntity: True if the revolve is up to the same entity in both directions, false if not;
            only applies if SingleDir is false and Dir1Type and Dir2Type are swEndConditions_e.swEndCondUpToVertex,
            swEndConditions_e.swEndCondUpToSurface, or swEndConditions_e.swEndCondOffsetFromSurface)
        :param Dir1Type: Revolve end condition as defined in swEndConditions_e
        :param Dir2Type: Revolve end condition in direction 2; as defined in swEndConditions_e and only applies if
            Dir1Type is not swEndConditions_e.swEndCondMidPlane
        :param Dir1Angle: Angle in radians of revolution in direction 1; only applies if Dir1Type is swEndConditions_e.swEndCondBlind
        :param Dir2Angle: Angle in radians of revolution in direction 2; only applies if Dir2Type is swEndConditions_e.swEndCondBlind
        :param OffsetReverse1: True to reverse the offset direction in direction 1, false to not; only applies if
            Dir1Type is swEndConditions_e.swEndCondOffsetFromSurface
        :param OffsetReverse2: True to reverse the offset direction in direction 2, false to not; only applies if
            Dir2Type is swEndConditions_e.swEndCondOffsetFromSurface
        :param OffsetDistance1: Offset distance in direction 1; only applies if Dir1Type is swEndConditions_e.swEndCondOffsetFromSurface
        :param OffsetDistance2: Offset distance in direction 2; only applies if Dir2Type is swEndConditions_e.swEndCondOffsetFromSurface
        :param ThinType: Type and direction as defined in swThinWallType_e
        :param ThinThickness1: Wall thickness in direction 1 (if ThinType is swThinWallType_e.swThinWallMidPlane,
            (ThinThickness1)/2 is used for each direction)
        :param ThinThickness2: Wall thickness in direction 2 (only applies if ThinType is swThinWallType_e.swThinWallTwoDirection)
        :param Merge: True to merge the results into a multi-body part, false to not
        :param UseFeatScope: True if the feature only affects selected bodies, false if the feature affects all bodies
        :param UseAutoSelect: True to automatically select all bodies and have the feature affect those bodies,
            false to select the bodies or components that the feature affects
        :return: IFeature object
        """
        return IFeature.IFeature(self.__comm_object.FeatureRevolve2(SingleDir, IsSolid, IsThin, IsCut, ReverseDir,
                                                                    BothDirectionUpToSameEntity, Dir1Type, Dir2Type,
                                                                    Dir1Angle, Dir2Angle, OffsetReverse1, OffsetReverse2,
                                                                    OffsetDistance1, OffsetDistance2, ThinType,
                                                                    ThinThickness1, ThinThickness2, Merge, UseFeatScope,
                                                                    UseAutoSelect))
