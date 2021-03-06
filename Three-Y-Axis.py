import matplotlib.pyplot as plt
from matplotlib import dates
import pandas as pd

data = pd.read_csv("E:/Thesis/Thesis-Excel-files/climate-data.csv", sep = ",")

Temp = data['AvgTemp']
Pre = data['Precip(in)']
Dis = data['Discharge, cubic feet per second (Mean)']
Date = data['X']

#Date = str(Date)

#Date = dates.datestr2num(Date)

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

fig = plt.figure(figsize = (10,7))
        
fig, host = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)

p1, = host.plot(Date, Dis, "b-", linewidth = 1, label="Discharge")
p2, = par1.plot(Date, Temp, "r-", linewidth = 1, label="Temperature")
p3, = par2.plot(Date, Pre, "g-", linewidth = 1, label="Precipitation")

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)
#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

host.set_xlabel("Date")
host.set_ylabel("Discharge cubic feet per second")
par1.set_ylabel("Mean Temperature")
par2.set_ylabel("Precipitation")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

lines = [p1, p2, p3]

host.legend(lines, [l.get_label() for l in lines])

plt.axvline(x=17, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)
plt.axvline(x=25, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)
plt.axvline(x=32, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)
plt.axvline(x=39, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)
plt.axvline(x=49, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)
plt.axvline(x=54, linewidth = 2, color = 'k', linestyle = '--', markersize = 4)

labels = ['Jul 1', 'Jul-10', 'Jul-20', 'Jul-30', 'Aug-8', 'Aug-18']
plt.xticks(Date, labels, rotation='vertical')
plt.xticks(np.arange(min(Date), max(Date)+1, 10.0), size = 12)

#labels = [item.get_text() for item in ax.get_xticklabels()]
#labels[0] = 'July 1st'
#labels[10] = 'July 10th'
#labels[20] = 'July 20th'
#labels[30] = 'July 30th'
#labels[40] = 'August 8th'
#labels[50] = 'August 18th'

#ax.set_xticklabels(labels)

plt.show()

fig.savefig('weather.png')
