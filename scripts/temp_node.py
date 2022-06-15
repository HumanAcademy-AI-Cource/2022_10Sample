#!/usr/bin/env python3

# 必要なライブラリをインポート
import subprocess
import rospy
from sensor_msgs.msg import Temperature

# ノードの名前を設定
rospy.init_node("temp")
# パブリッシャーの準備
pub = rospy.Publisher("/raspi_temp", Temperature, queue_size=1)

while not rospy.is_shutdown():
    # RaspberryPiの温度情報を取得
    read_temp = int(subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout)
    # 取得した温度情報は1000倍された数値なので、1000で割って元に戻す
    temp = int(read_temp) / 1000.0

    # RaspberryPiの温度と取得時刻を変数に入れる
    temp_info = Temperature()
    temp_info.temperature = temp
    temp_info.header.stamp = rospy.Time.now()
    
    # 温度情報と取得時刻をパプリッシュする
    pub.publish(temp_info)
    
    # 指定した秒数待つ
    rospy.sleep(1)


##################################################
##### Pythonのクラスを使ったROSノードの書き方 ######
##################################################

# class TempNode(object):
#     def __init__(self):
#         # パブリッシャーの準備
#         self.pub = rospy.Publisher("/raspi_temp", Temperature, queue_size=1)

#     def run(self):
#         while not rospy.is_shutdown():
#             # RaspberryPiの温度情報を取得
#             read_temp = int(subprocess.run("cat /sys/class/thermal/thermal_zone0/temp", shell=True, encoding='utf-8', stdout=subprocess.PIPE).stdout)
#             # 取得した温度情報は1000倍された数値なので、1000で割って元に戻す
#             temp = int(read_temp) / 1000.0

#             # RaspberryPiの温度と取得時刻を変数に入れる
#             temp_info = Temperature()
#             temp_info.temperature = temp
#             temp_info.header.stamp = rospy.Time.now()
            
#             # 温度情報と取得時刻をパプリッシュする
#             self.pub.publish(temp_info)
            
#             # 指定した秒数待つ
#             rospy.sleep(1)

# if __name__ == "__main__":
#     # ノードの名前を設定
#     rospy.init_node("temp_class")
#     TempNode().run()