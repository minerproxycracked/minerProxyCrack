#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import hashlib


def print_md5(file):
    try:
        with open(file, 'rb') as f:
            content = bytearray(f.read())

        ob = hashlib.md5()
        ob.update(content)
        print(ob.hexdigest())
    except Exception as e:
        print(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help=u'要获取md5的文件名', required=True)
    args = parser.parse_args()

    print_md5(args.file)


if __name__ == '__main__':
    main()
