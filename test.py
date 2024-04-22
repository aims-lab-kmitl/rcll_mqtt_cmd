import rcll_mqtt_cmd

rcll = rcll_mqtt_cmd.RcllMqttCmd("10.26.11.13", "GRIPS")
# rcll = rcll_mqtt_cmd.RcllMqttCmd("172.30.72.76", "GRIPS")


rcll.set_machine_report("M-BS", -1.5,3.5,180)
# rcll.set_robot_beacon1(0, 0, 0)
# rcll.set_robot_beacon2(0, 0, 0)
# rcll.set_robot_beacon3(0, 0, 0)

rcll.set_prepare_BS_input(rcll.color_red)

# data = rcll.fetch_data()
# print(data)

# print("JAMES", rcll.get_machine_status("M-BS"))


