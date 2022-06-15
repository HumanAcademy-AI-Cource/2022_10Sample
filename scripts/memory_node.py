#!/usr/bin/env python3

# 必要なライブラリをインポート
import psutil
import rospy
from std_msgs.msg import Float64

# ノードの名前を設定
rospy.init_node("memory")
# パブリッシャーの準備
pub = rospy.Publisher("/raspi_memory", Float64, queue_size=1)

while not rospy.is_shutdown():
    # RaspberryPiのメモリ使用率を調べる
    

    # RaspberryPiのメモリ使用率を変数に入れる
    memory_info = Float64()
    memory_info.data = memory.percent
    
    # メモリ使用率をパプリッシュする
    pub.publish(memory_info)
    
    # 指定した秒数待つ
    rospy.sleep(1)