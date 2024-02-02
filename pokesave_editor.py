#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## mod_name
## File description:
## modify the name of the player
##

import sys

if __name__ == "__main__":
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read())
        sav[0x2598] = 0x84
        sav[0x2599] = 0x8D
        sav[0x259A] = 0x88
        sav[0x259B] = 0x91
        sav[0x259C] = 0x84
        sav[0x259D] = 0x82
        sav[0x259E] = 0x86
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)
