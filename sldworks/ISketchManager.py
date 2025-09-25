"""
Wrapper for ISketchManager in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html?_gl=1*y35905*_up*MQ..*_ga*MTQ0MTc5NDI2MS4xNzUyNjcxODgw*_ga_XQJPQWHZHH*czE3NTI2NzE4NzkkbzEkZzEkdDE3NTI2NzI1OTkkajYwJGwwJGgw

Gets the sketch manager, which allows access to sketch-creation routines.
"""

from swapy.sldworks import ISketch, ISketchArc, ISketchSegment, IModelDoc2


class ISketchManager:
    def __init__(self, comm_object, Document):
        """
        Creates an instance of the ISketchManager wrapper from the Solidworks API
        :param comm_object: COM object representing IEdmFile5 instance from Solidworks API
        """
        self.__comm_object = comm_object
        self.AddToDB = self.__comm_object.AddToDB
        self.AutoSolve = self.__comm_object.AutoSolve
        self.CurvatureDensity = self.__comm_object.CurvatureDensity
        self.CurvatureScale = self.__comm_object.CurvatureScale
        self.DisplayWhenAdded = self.__comm_object.DisplayWhenAdded
        self.Document = Document

    def Create3PointArc(self, X1: float, Y1: float, Z1: float,
                              X2: float, Y2: float, Z2: float,
                              X3: float, Y3: float, Z3: float):
        """
        Creates a 3-point arc.
        :param X1: X coordinate of point 1
        :param Y1: Y coordinate of point 1
        :param Z1: Z coordinate of point 1
        :param X2: X coordinate of point 2
        :param Y2: Y coordinate of point 2
        :param Z2: Z coordinate of point 2
        :param X3: X coordinate of point 3
        :param Y3: Y coordinate of point 3
        :param Z3: Z coordinate of point 3
        :return: Sketch segment for the 3-point arc
        """
        return ISketchSegment.ISketchSegment(self.__comm_object.Create3PointArc(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3))

    def Create3PointCenterRectangle(self, X1: float, Y1: float, Z1: float,
                                          X2: float, Y2: float, Z2: float,
                                          X3: float, Y3: float, Z3: float):
        """
        Creates a 3-point center rectangle at any angle.
        :param X1: X coordinate of point 1
        :param Y1: Y coordinate of point 1
        :param Z1: Z coordinate of point 1
        :param X2: X coordinate of point 2
        :param Y2: Y coordinate of point 2
        :param Z2: Z coordinate of point 2
        :param X3: X coordinate of point 3
        :param Y3: Y coordinate of point 3
        :param Z3: Z coordinate of point 3
        :return: Array of sketch segments that represent the edges and diagonals created for this center rectangle
        """
        segment_array = self.__comm_object.Create3PointCenterRectangle(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
        res = []
        for segment in segment_array:
            res.append(ISketchSegment.ISketchSegment(segment))

        return res

    def Create3PointCornerRectangle(self, X1: float, Y1: float, Z1: float,
                                          X2: float, Y2: float, Z2: float,
                                          X3: float, Y3: float, Z3: float):
        """
        Creates a 3-point corner rectangle at any angle.
        :param X1: X coordinate of point 1
        :param Y1: Y coordinate of point 1
        :param Z1: Z coordinate of point 1
        :param X2: X coordinate of point 2
        :param Y2: Y coordinate of point 2
        :param Z2: Z coordinate of point 2
        :param X3: X coordinate of point 3
        :param Y3: Y coordinate of point 3
        :param Z3: Z coordinate of point 3
        :return: Array of sketch segments that represent the edges created for this corner rectangle
        """
        segment_array = self.__comm_object.Create3PointCornerRectangle(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3)
        res = []
        for segment in segment_array:  # Convert every segment in the array to a wrapper class
            res.append(ISketchSegment.ISketchSegment(segment))

        return res

    def CreateArc(self, XC: float, YC: float, ZC: float,
                        X1: float, Y1: float, Z1: float,
                        X2: float, Y2: float, Z2: float,
                        Direction: int):
        """
        Creates an arc based on a center point, a start point, an end point, and a direction.
        :param XC: X coordinate of the circle center point in meters
        :param YC: Y coordinate of the circle center point in meters
        :param ZC: Z coordinate of the circle center point in meters
        :param X1: X coordinate of the start point of the arc in meters
        :param Y1: Y coordinate of the start point of the arc in meters
        :param Z1: Z coordinate of the start point of the arc in meters
        :param X2: X coordinate of the end point of the arc in meters
        :param Y2: Y coordinate of the end point of the arc in meters
        :param Z2: Z coordinate of the end point of the arc in meters
        :param Direction: +1 : Go from the start point to the end point in a counter-clockwise direction,
                          -1 : Go from the start point to the end point in a clockwise direction
        :return: ISketchArc
        """
        return ISketchArc.ISketchArc(self.__comm_object.CreateArc(XC, YC, ZC, X1, Y1, Z1, X2, Y2, Z2, Direction))

    def CreateCircleByRadius(self, XC: float, YC: float, ZC: float, Radius: float):
        """
        Creates a circle based on a center point and a specified radius.\n

        This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch is created.
        You can check for an active sketch using ISketchManager::ActiveSketch.
        :param XC: X coordinate of the circle center point in meters
        :param YC: Y coordinate of the circle center point in meters
        :param ZC: Z coordinate of the circle center point in meters
        :param Radius: Radius of the circle in meters
        :return: Sketch segment for the circle
        """
        return ISketchSegment.ISketchSegment(self.__comm_object.CreateCircleByRadius(XC, YC, ZC, Radius))

    def CreateCenterLine(self, X1: float, Y1: float, Z1: float,
                               X2: float, Y2: float, Z2: float):
        """
        Creates a center line between the specified points.
        :param X1: X coordinate of first end point, in meters
        :param Y1: Y coordinate of first end point, in meters
        :param Z1: Z coordinate of first end point, in meters
        :param X2: X coordinate of second end point, in meters
        :param Y2: Y coordinate of second end point, in meters
        :param Z2: Z coordinate of second end point, in meters
        :return: Sketch segment for the center line
        """
        return self.__comm_object.CreateCenterLine(X1, Y1, Z1, X2, Y2, Z2)

    def CreateCenterRectangle(self, X1: float, Y1: float, Z1: float,
                                    X2: float, Y2: float, Z2: float):
        """
        Creates a center rectangle.
        :param X1: X coordinate for point 1
        :param Y1: Y coordinate for point 1
        :param Z1: Z coordinate for point 1
        :param X2: X coordinate for point 2
        :param Y2: Y coordinate for point 2
        :param Z2: Z coordinate for point 2
        :return: Array of sketch segments that represent the edges and diagonals created for this center rectangle
        """
        segment_array = self.__comm_object.Create3PointCornerRectangle(X1, Y1, Z1, X2, Y2, Z2)
        res = []
        for segment in segment_array:  # Convert every segment in the array to a wrapper class
            res.append(ISketchSegment.ISketchSegment(segment))

        return res

    def CreateChamfer(self, Type: int, Distance: float, AngleORDist: float):
        f"""
        Creates a chamfer between two selected sketch entities.
        :param Type: Type of chamfer as defined in swSketchChamferType_e
        :param Distance: Distance of the chamfer
        :param AngleORDist: If Type = swSketchChamfer_DistanceDistance, then the second chamfer distance.
            If Type = swSketchChamfer_DistanceAngle, then the second chamfer angle. 
            If Type = swSketchChamfer_DistanceEqual, then this argument is ignored because Distance is used for both edges
        :return: Sketch segment for the chamfer
        """
        return self.__comm_object.CreateChamfer(Type, Distance, AngleORDist)

    def CreateCircle(self, XC: float, YC: float, ZC: float,
                           Xp: float, Yp: float, Zp: float):
        """
        Creates a circle based on a center point and a point on the circle.
        :param XC:
        :param YC:
        :param ZC:
        :param Xp:
        :param Yp:
        :param Zp:
        :return: Sketch segment for the circle
        """
        return self.__comm_object.CreateCircle(XC, YC, ZC, Xp, Yp, Zp)

    def CreateFillet(self, Radius: float, ConstrainedCorners):
        """
        Creates a sketch fillet using the selected sketch entities.
        :param Radius: Radius of the fillet in meters
        :param ConstrainedCorners: Action to take if the corner to fillet is constrained or dimensioned. If the corner
            is not constrained or dimensioned, then this parameter is ignored. Defined in swConstrainedCornerAction_e
        :return: Sketch segment for the fillet
        """
        return ISketchSegment.ISketchSegment(self.__comm_object.CreateFillet(Radius, ConstrainedCorners))

    def CreateLine(self, X1: float, Y1: float, Z1: float,
                   X2: float, Y2: float, Z2: float):
        """
        Creates a sketch line in the currently active 2D or 3D sketch.\n

        If a sketch is not active, then the line is not created and NULL is returned. You can check for an active sketch
        using the ISketchManager::ActiveSketch function.
        :param X1: X coordinate of the line start point
        :param Y1: Y coordinate of the line start point
        :param Z1: Z coordinate of the line start point
        :param X2: X coordinate of the line end point
        :param Y2: Y coordinate of the line end point
        :param Z2: Z coordinate of the line end point
        :return: ISketchSegment instance
        """
        return ISketchSegment.ISketchSegment(self.__comm_object.CreateLine(X1, Y1, Z1, X2, Y2, Z2))

    def FullyDefineSketch(self, EntitiesToFullyDefine: bool, UseRelations: bool, RelationsToApply: int,
                          UseDimensions: bool, HorizontalDimScheme: int, HorizontalDatumDisp,
                          VerticalDimScheme: int, VerticalDatumDisp, HorizontalDimPlacement: int,
                          VerticalDimPlacement: int):
        """
        Fully defines a sketch.
        :param EntitiesToFullyDefine: True to fully define all entities, false to fully define only the entities selected
        :param UseRelations: True to use relations, false to not
        :param RelationsToApply: Relations to apply as defined in swSketchFullyDefineRelationType_e
        :param UseDimensions: True to use dimensions, false to not
        :param HorizontalDimScheme: 0 - chain; 1 - baseline; 2 - ordinate
        :param HorizontalDatumDisp: Horizontal datum (model edge, model vertex, sketch line, sketch point), or, if Nothing or null, use entity with selection mark = 6
        :param VerticalDimScheme: 0 - chain; 1 - baseline; 2 - ordinate
        :param VerticalDatumDisp: Vertical datum (model edge, model vertex, sketch line, sketch point), or, if Nothing or null, use entity with selection mark = 6
        :param HorizontalDimPlacement: 0 - Above sketch; 1 - Below sketch
        :param VerticalDimPlacement: 0 - Above sketch; 1 - Below sketch
        :return:
        """
        return self.__comm_object.FullyDefineSketch(EntitiesToFullyDefine, UseRelations, RelationsToApply,
                                                    UseDimensions, HorizontalDimScheme, HorizontalDatumDisp,
                                                    VerticalDimScheme, VerticalDatumDisp, HorizontalDimPlacement,
                                                    VerticalDimPlacement)

    def GetActiveSketch(self):
        """
        Getter for the ActiveSketch, to wrap it into a ISketch class
        :return: ISketch instance of the COM ActiveSketch
        """
        return ISketch.ISketch(self.__comm_object.ActiveSketch)

    def InsertSketch(self, UpdateEditRebuild: bool):
        """
        Inserts a new sketch in the current part or assembly document.
        :param UpdateEditRebuild: True to rebuild the part with any changes made to the sketch and exit sketch mode, false to not
        :return:
        """
        return self.__comm_object.InsertSketch(UpdateEditRebuild)
