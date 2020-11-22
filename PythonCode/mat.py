import matplotlib.pyplot a Figure
import numpy

f = Figure(figsize=(5, 4), dpi=100)

ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27)

ind = numpy.arange(5)  # the x locations for the groups
width = .5

rects1 = ax.bar(ind, data, width)

f.show()