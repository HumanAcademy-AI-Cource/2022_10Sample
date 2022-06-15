#!/usr/bin/env python3

# 必要なライブラリをインポート
import rospy
import datetime
from sensor_msgs.msg import Temperature

# ノードの名前を設定
rospy.init_node("temp_display")

# 温度情報が送られてきたら呼び出される関数
def temp_callback(msg):
    date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9), "JST"))
    ymd = date.strftime("%Y/%m/%d")
    hms = date.strftime("%H:%M:%S")
    print("({} {}) {:.1f}℃".format(ymd, hms, msg.temperature))

# サブスクライバーの準備
rospy.Subscriber("/raspi_temp", Temperature, temp_callback)
rospy.spin()