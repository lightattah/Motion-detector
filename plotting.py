from motion_detector import df
from bokeh.plotting import figure, show, output_file

height = []
base = []
p = figure(x_axis_type='datetime', height = 100, width = 500, title="Motion Graph")

for i in range(len(df["Entry Time"])):
    height.append(1)

for item in height:
    base.append(0)

q = p.quad(top = height, bottom = base, left = df["Entry Time"], right = df["Exit Time"], color = "Orange")

output_file("TIme plot.html")
show(p)

