#產生一個隨機整數 不要印出來
#讓使用者重複輸入數字去猜
#猜對的話 印出"恭喜你猜對了"
#猜錯的話 要告訴他比答案大/小

import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print("恭喜你答對了!")
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')


