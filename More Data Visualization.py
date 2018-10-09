##Produces a nice line graph, will likely use for publication


reflect17_zones = reflect717[['Site-2', 'Site-14', 'Site-21']]
#reflect17_zones = reflect17_zones.rename(columns={'Site-4':'Zone-1', 'Site-14':'Zone-2', 'Site-20':'Zone-3'})


fig17 = plt.figure(figsize = (7,5))
line1, = plt.plot(reflect17_zones['Site-2'], color = 'black', linewidth = 2, linestyle = '--', markersize = 4)
line2, = plt.plot(reflect17_zones['Site-14'], color = 'black', linewidth = 3, linestyle = ':', markersize = 10)
line3, = plt.plot(reflect17_zones['Site-21'], color = 'black', linewidth = 2,)
plt.legend(handles = [line1, line2, line3], loc="upper right")
#plt.axvline(x=591, linewidth = 2, color = 'm')
#plt.axvline(x=596, linewidth = 2, color = 'k')
plt.xlim(400,900)
plt.ylim(0,15)
plt.xlabel('Wavelength', fontsize = 16)
plt.ylabel('Reflectance', fontsize = 16)
plt.title('Reflectance Spectrum, 17 July 2017', fontsize = 18)
plt.show()
plt.close()
fig17.savefig('reflect17graph.png')
