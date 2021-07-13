import numpy as np
from Botlab import Botlab

# botlab nesnesi olusturulur:
botlab = Botlab(angle_unit=Botlab.DEGREE)
# angle_unit := fonksiyonlara girdi olarak verilecek acilarin birimidir.
# buna karsilik, fonksiyonlara eger aci degeri donduruyorsa;
# HER ZAMAN RADYAN biriminde dondurur!

pos_vector_B = botlab.pos_vector(x=1, y=2, z=3) 
# pos_vector fonksiyonlara (3, 1) boyutunda konum vektoru uretilir

#### global eksenlerde donme
rotation_matrix = botlab.rot_global('x', 60) # (1) tek donusum ornegi
# rotation_matrix = botlab.rot_global('xy', [60, 30]) # (2) ardisik donusum ornegi

#### lokal eksenlerde donme
# rotation_matrix = botlab.rot_local('x', 60) # (1) tek donusum ornegi
# rotation_matrix = botlab.rot_local('xy', [60, 30]) # (2) ardisik donusum ornegi

# rot_global := global eksenlerde donusum matrisi uretir.
# rot_local := local eksenlerde donusum matrisi uretir.
# her iki fonk. da hem ardisik hem de tekli donusumler icin yukaridaki gibi kullanilabilir.
# ilk parametre donus ekseni(eksenleri),
# ikinci parametre donus acisi(acilaridir)

posA = botlab.rotmatrix_to_pos(
    rot_matrix=rotation_matrix,
    posB=pos_vector_B
)
# rotmatrix_to_pos := donusum matrisi (rot_matrix) ve pozisyon vektorunu alir,
# donusum matrisine gore diger lokal veya global pozisyonu (3, 1) boyutunda dondurur.

print('posA = rotX(60) * posB\nposA:')
print(posA)
