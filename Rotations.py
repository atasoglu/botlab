from numpy import array, ndarray, cos, sin

def ROT_X (alpha:float) -> ndarray: return array([
    [1.0,   0.0,                0.0],
    [0.0,   cos(alpha), -sin(alpha)],
    [0.0,   sin(alpha),  cos(alpha)]
])

def ROT_Y (beta:float) -> ndarray: return array([
    [cos(beta),     0.0,    sin(beta)],
    [0.0,           1.0,          0.0],
    [-sin(beta),    0.0,    cos(beta)]
])

def ROT_Z (gamma:float) -> ndarray: return array([
    [cos(gamma),    -sin(gamma),    0.0],
    [sin(gamma),    cos(gamma),     0.0],
    [0.0,           0.0,            1.0]
]) 