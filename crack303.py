#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import logging

_MinerProxy = {
    # linux

    8182977:  0x0032780d,  # minerProxy/minerProxy_cmd:      大小8182977字节， 钱包地址位于0x0032780d
    8484988:  0x0034d1cb,  # minerProxy_config:              大小8484988字节， 钱包地址位于0x0034d1cb
    17611821: 0x00495638,  # minerProxy_web:                 大小17611821字节，钱包地址位于0x00495638

    # win32

    8391168:  0x0032a8ac,  # minerProxy/minerProxy_cmd.exe:  大小8391168字节， 钱包地址位于0x0032a8ac
    8757248:  0x00357b1c,  # minerProxy_config.exe:          大小8757248字节， 钱包地址位于0x00357b1c
    17880576: 0x004a07d5,  # minerProxy_web.exe:             大小17880576字节，钱包地址位于0x004a07d5
}


def crack(target, size, wallet, output):
    try:
        with open(target, 'rb') as file:
            minerProxy = bytearray(file.read())

        addr = _MinerProxy[size]
        old_wallet = minerProxy[addr: addr + 40].decode()
        minerProxy[addr: addr + 40] = wallet.encode()

        with open(output, 'wb') as file:
            file.write(minerProxy)

        assert os.path.getsize(output) == size
    except Exception as e:
        logging.error(u'发生未知错误: {}'.format(e))
    else:
        logging.info(u'替换成功。旧钱包地址为0x{}, 已替换为0x{}'.format(old_wallet, wallet))
        logging.info(u'文件已写入{}'.format(output))


def parse_wallet(args_wallet):
    return (len(args_wallet) == 42, args_wallet[2:]) \
        if args_wallet.startswith('0x') else (len(args_wallet) == 40, args_wallet)


def main():
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, help=u'要破解的minerProxy文件', required=True)
    parser.add_argument('-w', '--wallet', type=str, help=u'要替换的钱包地址', required=True)
    parser.add_argument('-o', '--output', type=str, help=u'要生成的文件名', required=True)
    args = parser.parse_args()

    target, output = args.target, args.output

    try:
        size = os.path.getsize(target)
    except FileNotFoundError:
        return logging.error(u'文件{}不存在'.format(target))
    except Exception as e:
        return logging.error(u'发生未知错误: {}'.format(e))

    valid, wallet = parse_wallet(args.wallet)

    if not valid:
        logging.error(u'钱包地址长度不正确, 请检查')
    if not _MinerProxy.get(size):
        logging.error(u'{}文件大小为{}字节, 不匹配任意一个303版本, 请检查'.format(target, size))
    else:
        logging.info(u'开始破解{}, 大小{}字节, 要替换的钱包地址为0x{}'.format(target, os.path.getsize(target), wallet))
        crack(target, size, wallet, output)


if __name__ == '__main__':
    main()
