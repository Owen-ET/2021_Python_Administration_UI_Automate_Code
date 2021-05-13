#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/05/12 15:07
# @Author  : zc
# @File    : test2.py


def main():
    fish = 1
    while True:
        total, enough = fish, True
        print("打印total："+str(total))
        for _ in range(5):
            if (total - 1) % 5 == 0:
                print("新:",total)
                total = (total - 1)  //  5 * 4
                print("旧",total)
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1
        #print(fish)


if __name__ == '__main__':
    main()
