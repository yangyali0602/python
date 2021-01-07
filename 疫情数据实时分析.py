from matplotlib import pyplot as plt
date=['12.08','12.10','12.12','12.14','12.16','12.18','12.20','12.22',\
      '12.24','12.26','12.28','12.30','01.01','01.03','01.06']
china=[117,131,101,103,96,89,100,82,85,84,96,81,67,78,90]
haiwai=[561210,671949,1441282,550652,677629,51523,603863,568707,647405,506574,482312,\
        698693,643338,574230,757151]
plt.figure(figsize=(15,6))
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(date,china,c='blue',label='中国')
plt.plot(date,haiwai,c='orange',label='海外')
y_s = [200000, 400000, 600000, 800000, 1000000]
y_x = ['20万', '40万', '60万', '80万', '100万']
plt.yticks(y_s, y_x)
plt.xticks(rotation=50)
plt.title("统计截止至1月6日", loc='left')
plt.legend()
plt.show()