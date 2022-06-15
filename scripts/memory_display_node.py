#!/usr/bin/env python3

# 必要なライブラリをインポート
import rospy
import datetime
from std_msgs.msg import Float64

# ノードの名前を設定
rospy.init_node("memory_display")

# メモリ使用率の情報が送られてきたら呼び出される関数
def memory_callback(msg):
    date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), "JST"))
    ymd = date.strftime("%Y/%m/%d")
    hms = date.strftime("%H:%M:%S")
    print("({} {}) メモリ使用率: {:.1f}%".format(ymd, hms, msg.data))

# サブスクライバーの準備
rospy.Subscriber("/raspi_memory", Float64, memory_callback)
rospy.spin()