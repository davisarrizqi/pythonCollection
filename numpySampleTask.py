import numpy

# first declaration
A = [1, 2, 3]; B = [4, 5, 6]

# second declaration
mA = [[1, 2, 3], [4, 2, -2]]
mB = [[-5, 1, 3], [4, -3, -1]]

# numpy practice
mA1 = numpy.array(mA)
mB1 = numpy.array(mB)
mC = mA1 - mB1

# example and namespace
print(mC); print("\n")


# Operasi Matriks
"""
1. Tunjukkan hasil pengurangan A dengan B
2. Tunjukkan hasil perkalian mA dengan mB
3. Balik matriks mB menjadi ordo 3x2 (transpose matriks)
4. Tunjukkan ordo matrik mB
5. Kerjakan soal nomor 2
6. Buatlah vektor baris "vc" yang merupakan gabungan
   dari mA dan mB
7. Hitunglah nilai terendah, tertinggi, rata-rata, dan
   standar deviasi dari vc
8. Ubah bentuk vektor vc menjadi matriks dengan ukuran 4x3
"""

# Header_Divider
print("Penyelesaian Tugas\n")

# 1. Menunjukkan hasil pengurangan A dengan B
print('1. Penyelesaian\n', numpy.array(A) - numpy.array(B)); print('')

# 2. Menunjukkan hasil perkalian mA dengan mB
print('2. Penyelesaian\n', numpy.array(mA) * numpy.array(mB)); print('')

# 3. Transpose matriks mB menjadi ordo 3x2
print('3. Penyelesaian')
mB = numpy.transpose(mB); print(mB, '\n')

# 4. Menunjukkan ordo matriks mB
print('4. Penyelesaian\n')
