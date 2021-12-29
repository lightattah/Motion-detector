from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Entry_string"] = df["Entry"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Exit_string"] = df["Exit"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height = 100, width = 500, title="Motion Graph")
p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips=[("Entry: ", "@Entry_string"),("Exit", "@Exit_string")])
p.add_tools(hover)

q = p.quad(top = 1, bottom = 0, left = "Entry", right = "Exit", color = "Orange", source=cds)

output_file("TIme plot.html")
show(p)

