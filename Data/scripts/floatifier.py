import sys
import random
import struct
import math

def any_float(floa, gen):
    if gen.random() >= 0.5:
        return str(floa).replace("e+", "e")
    else:
        return "{0:30f}".format(floa)


def pos_float(floa, gen):
    return "{0:30f}".format(floa)


def floatify(in_file, out_file, seed, bitlength=32, formatters=[("$$float$$", any_float), ("$$posfloat$$", pos_float)]):
    gen = random.Random()
    gen.seed(seed, version=2)
    with open(in_file, mode='r') as file_in, open(out_file, mode='w') as file_out:
        for s in file_in:
            floa = 0.0
            for formatter in formatters:
                done = False
                while not done:
                    while True:
                        floa = struct.unpack("=f", struct.pack("=L", gen.getrandbits(bitlength)))[0]
                        if not math.isnan(floa) and not math.isinf(floa):
                            break
                    new = s.replace(formatter[0], formatter[1](floa, gen), 1)
                    if new == s:
                        done = True
                    s = new
            file_out.write(s)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        floatify(sys.argv[0], sys.argv[1], random.getrandbits(64))
        with open(sys.argv[1]) as f:
            print(f.read)

