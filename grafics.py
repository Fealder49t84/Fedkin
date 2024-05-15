import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

with open ("data.txt", "r") as data:

    with open("settings.txt", "r") as settings:

        smth        = float(settings.readline())
        frequency   = float(settings.readline())

        ax_voltage  = [int(line) for line in data]
        ax_time     = [frequency * i for i in range(len(ax_voltage))]

        ax.plot(ax_time, ax_voltage)

        ax.grid(True)

        ax.set_xlabel("Time, sec")
        ax.set_ylabel("Voltage, v")

        ax.set_title("Addiction V(t)")

        max_voltage = np.max(ax_voltage)
        ind_of_max_voltage = ax_voltage.index(max_voltage)

        ax.plot([ax_time[ind_of_max_voltage]] * 2, [0, max_voltage], color='r', linestyle='dashed')
        ax.plot([0, ax_time[ind_of_max_voltage]], [max_voltage] * 2, color='r', linestyle='dashed')

        ax.scatter(ax_time[ind_of_max_voltage], max_voltage, color='g')
        plt.text(ax_time[ind_of_max_voltage]*1.01, max_voltage*1.01, "Max voltage", size=12, color='g')

        plt.xlim(0, ax_time[-1] * 1.1)
        plt.ylim(0, max_voltage * 1.1)

        fig.set_size_inches(16, 8)
        plt.show()
