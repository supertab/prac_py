import ctypes
dll = ctypes.cdll.LoadLibrary
bitstream = dll('./bitstream.so')
a = '0111111011100011001'.encode('utf-8')
fn = "str.bits".encode('utf-8')
bitstream.write(a, fn)

