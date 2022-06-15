#!/usr/bin/env python3

# 必要なライブラリをインポート
import psutil

# RaspberryPiのメモリ使用率を調べる
memory = psutil.virtual_memory()
print("メモリ使用率: {}%".format(memory.percent))