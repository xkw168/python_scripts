import plotly.plotly as py
import plotly.figure_factory as ff
import plotly

df = [dict(Task="跑通基础模型", Start='2019-01-01', Finish='2019-01-15'),
      dict(Task="调参优化模型", Start='2019-01-10', Finish='2019-02-15'),
      dict(Task="增加空间分析", Start='2019-02-10', Finish='2019-04-01'),
      dict(Task="系统优化收尾", Start='2019-04-01', Finish='2019-04-15'),
      dict(Task="论文,PPT", Start='2019-04-10', Finish='2019-05-10'),
      dict(Task="分类,整理资料", Start='2019-01-01', Finish='2019-05-10')]
df.reverse()

plotly.tools.set_credentials_file(username='xiakewei96', api_key='tPdihqvLea9gdeeL4DgK')
fig = ff.create_gantt(df, showgrid_x=True, showgrid_y=True)
py.iplot(fig, filename='time1')
