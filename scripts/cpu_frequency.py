import psutil

cpu_freq = psutil.cpu_freq()[0]
cpu_temp = psutil.sensors_temperatures()["coretemp"][0].current
print("{:04d}MHz {}°C".format(round(cpu_freq), round(cpu_temp)))
