from matplotlib import pyplot as plt

date=['2.21','2.25','2.29','3.4','3.8','3.12',\
      '3.16','3.20','3.24', '3.28','4.1',\
      '4.5','4.9','4.13','4.17','4.21']
# date = [2.21,2.25,2.29,3.4,3.8,3.12,3.16,3.20,3.24,3.28,4.1,4.5,4.9,4.13,4.17,4.21]
num=[399,411,579,143,45,11,39,116,99,128,93,75,56,\
     99,31,37]
line_blue_Y=[123,56,562,12,369,112,78,258,156,751,25,20,125,256,420,98]

#  设置图片大小要在前面
plt.figure(figsize=(15, 6))

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 绘制第一条折线，并设置折线属性
plt.plot(date, num, c='red',marker='*',label='总新增确诊')

# 设置x轴坐标显示
plt.xticks(rotation=50)

# 设置x,y轴名称
plt.xlabel ("日期")
plt.ylabel ("数量")

# 设置标题
plt.title("全国 总新增确诊 趋势", loc='left')

# 绘制第二条折线
plt.plot(date,line_blue_Y, c='blue',lw=2, marker='p',ms=12, label='Y2')

# 添加图例，注意绘制图例前需要在plt.plot中添加label属性
plt.legend()

# 显示图片
plt.show()