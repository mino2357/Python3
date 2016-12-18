#if

score = int(input("score? "))

if score > 60 and score <= 100:
	print("まあまあ良いぞ〜")
elif score <= 60:
	print("まあ，気を落とすなよ")
elif score > 100:
	print("超越神！！！")

#print("great" if score > 80 else "so so ...")
