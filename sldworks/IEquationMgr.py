"""
Wrapper for IEquationMgr in Solidworks API. For more information: https://help.solidworks.com/2020/English/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEquationMgr.html

Maintains a list of all of the existing equations in a model.
"""


class IEquationMgr:
    def __init__(self, comm_object):
        """
        Creates an instance of the IEquationMgr wrapper from the Solidworks API
        :param comm_object: COM object representing IEquationMgr instance from Solidworks API\n
        """
        self.__comm_object = comm_object

    def Add2(self, Index: int, Equation: str, Solve: bool):
        """
        Adds an equation at the specified index.\n

        To add an equation using this method, you must specify Equation with the names of dimensions and global
        variables in double double quotes and the entire equation in double quotes\n

        If you call this method to add an equation whose left-hand side already exists in another equation, this method
        returns an error.
        :param Index: 0-based index of the new equation (-1 places it at the end of the list)
        :param Equation: String containing the equation
        :param Solve: True to solve the equation immediately; false otherwise
        :return:
        """
        return self.__comm_object.Add2(Index, Equation, Solve)