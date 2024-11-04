import random
import matplotlib.pyplot as plt

exec_cnt = int(input())
dice_result_list = []
cnt_result_list = []

for i in range(exec_cnt):
	dice_result_list.append(random.randint(1, 6))

for i in range(6):
	cnt_result_list.append(dice_result_list.count(i+1)/exec_cnt)

plt.bar(range(1, 7), cnt_result_list)
plt.hlines(1/6, 1, 7, color='g', linestyles='dotted')
plt.show()