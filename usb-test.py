import usb
import sys
import array

dev = usb.core.find(idVendor=0x0c45, idProduct=0x7160)
dev.reset()

if dev is None:
    raise ValueError('Device not found')

if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

f = open(sys.argv[1])

ep = dev[0][(0, 0)][0]


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


for l in f.readlines():
    l = l.split("\t")[0]
    data = int_to_bytes(int(l, 16))
    print(data)

    dev.ctrl_transfer(0x21, 9, 0x0200, 0, data, 1000)

    buf = array.array('b', [0x02, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
    ret = dev.read(0x81, buf, 1000)
    print(ret, buf)


