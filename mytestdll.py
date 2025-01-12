from ctypes import CDLL, c_size_t
from array import array
a1 = array("q", range(100))
a2 = array("q", range(100))
testlib = CDLL(r"C:\Users\hansc\source\repos\dlltest\mytest.dll")
add_vecs_int = testlib.add_vecs_int
add_vecs_int.argtypes = [
    c_size_t,
    c_size_t,
    c_size_t,
    c_size_t,
]
add_vecs_int.restype = None
add_vecs_int(*a1.buffer_info(), *a2.buffer_info())
