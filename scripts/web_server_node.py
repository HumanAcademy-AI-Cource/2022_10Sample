#!/usr/bin/env python3

# 必要なライブラリをインポート
import signal
import sys
import os
import http.server
import socketserver
import rospy


# ノードの名前を設定
rospy.init_node("web_server")

# 終了時の処理を設定
def handler(signal, frame):
    sys.exit(0)
signal.signal(signal.SIGINT, handler)

# Webページの素材があるディレクトリに移動
os.chdir(os.path.dirname(__file__) + "/contents")

with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as httpd:
    print("WebServer Start")
    httpd.serve_forever()