import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
import json

class RcllMqttCmd:
    def __init__(self, hostname, teamname):
        self.teamname = teamname
        self.hostname = hostname
        self.color_red = "Red"
        self.color_silver = "Silver"
        self.color_black = "Black"
        self.cap_retrieve = "RetrieveCap"
        self.cap_mount = "MountCap"

    def set_teamname(self, name):
        self.teamname = name
        print(f"Team name set to: {self.teamname}")

    def set_machine_report(self, machine, x, y, yaw):
        payload = f'{{ "machine": "{machine}", "x": {abs(x)}, "y": {abs(y)}, "yaw": {yaw} }}'
        publish.single(f"{self.teamname}/report", payload, hostname=self.hostname)

    def set_robot_beacon1(self, x, y, yaw):
        self.set_robot_beacon("R1", x, y, yaw)

    def set_robot_beacon2(self, x, y, yaw):
        self.set_robot_beacon("R2", x, y, yaw)

    def set_robot_beacon3(self, x, y, yaw):
        self.set_robot_beacon("R3", x, y, yaw)

    def set_prepare_BS_input(self, color="Red"):
        """color can be Red, Silver, Black"""
        publish.single(f"{self.teamname}/prepare/BS/input", color, hostname=self.hostname)

    def set_prepare_BS_output(self, cap="Red"):
        """Cap can be Red, Silver, Black"""
        publish.single(f"{self.teamname}/prepare/BS/input", color, hostname=self.hostname)

    def set_prepare_cap1(self, cap="MountCap"):
        """color can be MountCap, RetrieveCap"""
        publish.single(f"{self.teamname}/prepare/CS1", cap, hostname=self.hostname)

    def set_prepare_cap2(self, cap="MountCap"):
        """color can be MountCap, RetrieveCap"""
        publish.single(f"{self.teamname}/prepare/CS2", cap, hostname=self.hostname)

    def set_prepare_ring1(self, color="Blue"):
        """color can be Blue, Green, Orange, Yellow"""
        publish.single(f"{self.teamname}/prepare/RS1", color, hostname=self.hostname)

    def set_prepare_ring2(self, color="Blue"):
        """color can be Blue, Green, Orange, Yellow"""
        publish.single(f"{self.teamname}/prepare/RS2", color, hostname=self.hostname)

    def set_prepare_delivery(self, ORDER_ID):
        publish.single(f"{self.teamname}/prepare/DS", ORDER_ID, hostname=self.hostname)

    def set_robot_beacon(self, robot_name, x, y, yaw):
        payload = f'{{ "name": {robot_name}, "x": {x}, "y": {y}, "yaw": {yaw} }}'
        publish.single(f"{self.teamname}/beacon/{robot_name}", payload, hostname=self.hostname)


