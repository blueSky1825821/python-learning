"""
pyecharts
"""

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts

# 创建折线图对象
line = Line()
# x轴
line.add_xaxis(["中国", "美国", "日本"])
# y轴
line.add_yaxis("GDP", [30.83, 17.55, 4.11])
#全局设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    #图例
    legend_opts=LegendOpts(is_show=True),
    #工具箱
    tooltip_opts=TooltipOpts(is_show=True),
    #视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
)

#  显示图表
line.render("02_pyecharts.html")