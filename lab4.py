import numpy as np

# a = np.array([0, 1])
# print(a)

# a = np.arange(2)
# print(a)
# print(type(a))

# a = np.arange(2, dtype='int32')
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)

# print(a.ndim)

# m = np.array((np.arange(2), np.arange(2)))
# print(m.shape)

# m1 = np.array([[5, 4, 5],[4, 8, 3]])
# print(m1)
# print(m1.shape)
# print(m1.ndim)

# zera = np.zeros((5, 5))
# jedynki = np.ones((4,4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)

# pusta = np.empty((2,2))
# print(pusta)
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)

# liczby = np.arange(1, 2, 0.1)
# print(liczby)

# liczby_lin = np.linspace(1, 2, 5)
# print(liczby_lin)

# z = np.indices((5, 3))
# print(z)
# print(z[0, 3, 2])
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)

# mat_diag_k = np.diag([a for a in range(5)])
# print(mat_diag_k)

# z = np.fromiter(range(5), dtype='int32')
# print(z)

# znaki = b'abcdef'
# zn1 = np.frombuffer(znaki, dtype='S1')
# print(zn1)
# zn2 = np.frombuffer(znaki, dtype='S1')
# print(zn2)
# znaki = 'abcdef'
# zn3 - np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))
# zn6 = np.fromiter(znaki, dtype='S1')
# zn7 = np.fromiter(znaki, dtype=='U1')

# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)

