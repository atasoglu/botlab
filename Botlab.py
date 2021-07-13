from types import FunctionType
from typing import List, Union
import Rotations
import numpy as np

np.set_printoptions(suppress=True)

class Botlab:
    RADIAN = lambda angle: angle
    DEGREE = lambda angle: np.deg2rad(angle)

    def __init__(self, angle_unit:FunctionType) -> None:
        self.__angle_translator = angle_unit

    def multiply(self, matrixes:list) -> np.ndarray:
        res = np.identity(3)
        for matrix in matrixes:
            res = res.dot(matrix)
        return res

    def pos_vector(self, x:Union[float, int], y:Union[float, int], z:Union[float, int]) -> np.ndarray:
        """(3,1) boyutunda konum vektörü döndürür!"""
        return np.array([[x, y, z]]).T

    def cos_to_rotmatrix(self, cos_matrix:np.ndarray):
        vfunc = np.vectorize( lambda angle: np.cos( self.__angle_translator(angle) ) )
        return vfunc(cos_matrix)

    def rotmatrix_to_pos(self, rot_matrix:np.ndarray, posB:np.ndarray) -> np.ndarray:
        return np.matmul(rot_matrix, posB)

    def rot_global(self, Axis:str, Rot_Angle:Union[int, float, list]) -> np.ndarray:
        if len(Axis) > 1 and type(Rot_Angle) is list:
            rot = np.identity(3)
            for _axis, _angle in zip(Axis, Rot_Angle):
                rot = rot.dot( self.rot_global(_axis, _angle) )
            return rot
        elif type(Axis) is str and (type(Rot_Angle) is float or type(Rot_Angle) is int):
            angle = self.__angle_translator(Rot_Angle)
            axis_str = Axis.lower()
            if axis_str == 'x': return Rotations.ROT_X(angle)
            elif axis_str == 'y': return Rotations.ROT_Y(angle)
            elif axis_str == 'z': return Rotations.ROT_Z(angle)
            else: raise ValueError(f"axis='{Axis}' geçerli bir eksen degil! Sadece 'x', 'y' veya 'z' olmali.")
        else:
            raise ValueError("Parametreler yanlis girildi!")
    
    def rot_local(self, axis:str, rot_angle:Union[int, float, list]) -> np.ndarray:
        if len(axis) > 1 and type(rot_angle) is list:
            rot = np.identity(3)
            for _axis, _angle in zip(axis, rot_angle):
                rot = rot.dot( self.rot_local(_axis, _angle) )
            return rot
        if type(axis) is str and ( type(rot_angle) is float or type(rot_angle) is int ):
            return self.rot_global(Axis=axis, Rot_Angle=rot_angle).transpose()

    def rpy_to_rotmatrix(self, roll: Union[int, float], pitch:Union[int, float], yaw:Union[int, float]) -> np.ndarray:
        return self.rot_global('zyx', [yaw, pitch, roll])
    
    def rotmatrix_to_rpy(self, rot:np.ndarray) -> np.ndarray:
        """[roll, pitch, yaw]"""
        return np.array([
            np.arctan2(rot[2,1], rot[2,2]), 
            np.arctan2(-rot[2,0], np.sqrt( np.power(rot[2,1], 2) + np.power(rot[2,2], 2) ) ), 
            np.arctan2(rot[1,0], rot[0,0])
        ])

    def euler_to_rotmatrix(self, precission:Union[int, float], nutation:Union[int, float], spin:Union[int, float]) -> np.ndarray:
        return self.rot_local('zxz', [spin, nutation, precission])

    def rotmatrix_to_euler(self, rot:np.ndarray) -> np.ndarray:
        """[precision, nutation, spin]"""
        return np.array([
            np.arctan2(rot[2,0], -rot[2,1]),
            np.arctan2( np.sqrt( np.power(rot[2,0], 2) + np.power(rot[2,1], 2) ), rot[2,2] ),
            np.arctan2(rot[0,2], rot[1,2])
        ])