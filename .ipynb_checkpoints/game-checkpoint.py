import random
from time import sleep
import keyboard
import sys

class game:

	def __init__(self):

		self.own_party_name = "A党"
		self.enemy_party_name = "B党"

		self.own_party_inside_support = 60
		self.own_party_outside_support = 20

		self.day = 0

		# 各行動が行われた回数
		self.action1_num = 0
		self.action2_num = 0
		self.action3_num = 0
		self.action4_num = 0

		self.game_end_flag = False

		print("選挙ゲーム！野党から政権を守り抜け！")
		sleep(1)
		print(f"あなたは某国で政権を握る{self.own_party_name}の党首だ。{self.own_party_name}は政権成立当初は国民の支持を集めていたが、公約の不履行や強権的な政治手法や汚職により、支持率が急落している。４年前の総選挙では、不正選挙によってかろうじて政権を維持した。")
		sleep(1)
		print("しかし不正選挙疑惑が浮上し、政府は批判を避けるために連邦議会を解散して総選挙を行うことになった。")
		sleep(1)
		print(f"野党の{self.enemy_party_name}は、国民の与党への不信を背景に支持を多く集めている。")
		sleep(1)
		print(f"しかし{self.own_party_name}は軍人層からは強い支持を受けており、退役軍人が多く所属する組織で軍部との深いつながりがある国家国民守護連盟は{self.own_party_name}による一党独裁体制をもくろんでいる")
		sleep(1)
		print("一週間後の選挙に勝利し、国家を守り抜け！")
		sleep(1)
		print("\n\n")
		print("【ゲームのルール】")
		print("・選挙は7日後に行われる。")
		print("・各日に行動を選択し、支持率を上げていく。")
		print("・支持率が0%になると与党が解体され、ゲームオーバー。")
		print("・軍部支持率が85%を超えると軍事クーデターを起こして政権を乗っ取ることができる。")
		print("・選挙時に半数を超える支持を得ていると政権を維持できる。")
		print("\n\n")
		sleep(1)

		
	
	def show_status(self):

		print( 
			  f"【現在の状況】\n"
			  f"【{self.own_party_name}】\n"
			  f"軍部支持率：{self.own_party_inside_support}%\n"
			  f"民衆支持率：{self.own_party_outside_support}%\n\n"
			  f"【{self.enemy_party_name}】\n"
			  f"軍部支持率：{100-self.own_party_inside_support}%\n"
			  f"民衆支持率：{100-self.own_party_outside_support}%\n")

	def next_day(self):

		self.day += 1
		print(f"{self.day}日目")
		self.show_status()
		result = self.waitUserAction()
		print("")
		if result == 1:
			self.action1()
		elif result == 2:
			self.action2()
		elif result == 3:
			self.action3()
		elif result == 4:
			self.action4()
			return
		elif result == 5:
			pass
		else:
			print("1から5の数字を入力してください")
			self.day -= 1
			self.next_day()
			print("1から5の数字を入力してください")
			self.day -= 1
			self.next_day()
		if self.own_party_outside_support <= 0:
			self.game_end(isPartyCrashed=True)
			return
		if self.day == 7:
			self.game_end()


	def action1(self):

		print("各地で街頭演説を行いました。")
		inc_num = random.randint(1, 8)
		if inc_num > 4:
			print(f"演説では野党の公約の問題点を的確に指示することができ、観衆からは拍手が巻き起こりました。民衆支持率が{inc_num}%上昇しました。")
		else:
			print(f"演説では野党批判をとにかく行い、問題なく終わりました。民衆支持率が{inc_num}%上昇しました。")
		self.own_party_outside_support += inc_num
		self.action1_num += 1

	def action2(self):

		print("わいろを贈って票を買いました。")
		num = random.randint(1, 10+self.action2_num)
		if num < 7:
			print("わいろを贈ることで、野党支持者からも票を買うことができました。民衆支持率が15%上昇しました。")
			self.own_party_outside_support += 15
		else:
			print("わいろを送ったことが発覚し、メディアからの総叩きにあってしまいました。民衆支持率が10%減少しました。")
			self.own_party_outside_support -= 10
		self.action2_num += 1

	def action3(self):

		print("軍人にわいろを贈って軍部の支持を得ました。")
		num = random.randint(1, 10+self.action3_num)
		if num < 6:
			print("軍部の支持を得ることができました。軍部支持率が15%上昇しました。")
			self.own_party_inside_support += 15
		else:
			print("わいろを送ったことが発覚し、メディアからの総叩きにあってしまいました。民衆支持率が10%減少しました。")
			self.own_party_outside_support -= 10
		self.action3_num += 1
	
	def action4(self):

		print("軍部と結託して軍事クーデターを起こしました。")
		self.game_end(isCoup=True)
		self.action4_num += 1


	def game_end(self, isCoup=False, isPartyCrashed=False):

		self.game_end_flag = True
		if isPartyCrashed:
			print("[ ラジオ放送が始まる ]")
			print("「こちらは第一放送、第一放送です。緊急ニュースをお伝えします。」")
			sleep(1)
			print(f"「{self.own_party_name}は支持率低下を受けて臨時党大会を開き、党の解散が決定されました。」")
			print("「総裁は『国民の皆様には大変申し訳ないことをした。私たちの政治は終わりを迎えた。』との声明を発表しました。」")
			sleep(1)
			print("「では、次のニュースに移ります...」")
			print("")
			print("これにてゲームは終了です。お疲れさまでした。")
			return
		if isCoup:
			sleep(1)
			print("[ ラジオ放送が始まる ]")
			print("「こちらは第一放送、第一放送です。緊急ニュースをお伝えします。」")
			sleep(1)
			print("「陸軍が連邦議会を襲撃しました。陸軍は連邦議会に侵入し、 ...」")
			sleep(2)
			if self.own_party_inside_support > 85:
				print(f"「連邦議会を占拠して連邦議会議長、副議長を拘束しました。陸軍総司令官は『我々は国家再建委員会を組織し、議会は無期限に停止される。また、{self.own_party_name}以外の政治団体は速やかに解散しなければならない。』との声明を発表しました。」")
				sleep(1)
				print(f"「今後は強大で安定した国家体制を作るべく、わが{self.own_party_name}と国家国民守護連盟によって新体制が建設されるでしょう！」")
				sleep(1)
			else:
				print("「襲撃に参加しなかった陸軍部隊によって直ちに排除されました。連邦議会議長は『この襲撃は民主主義に対する攻撃であり、断じて許されない。』との声明を発表しました。」")
				sleep(1)
				print(f"「また、議会関係者からは{self.own_party_name}が襲撃にかかわっているのではないかという声もあり、{self.own_party_name}は国内外から非難を浴びることになるでしょう。」")
			sleep(1)
			print("「では、次のニュースに移ります...」")
			sleep(1)
			print("")
			sleep(1)
			print("これにてゲームは終了です。お疲れさまでした。")
			return
		print("選挙は投開票日を迎えました。")
		sleep(1)
		print("早速開票結果を見てみましょう。")
		sleep(1)
		print("[ ラジオ放送が始まる ]")
		print("「こちらは第一放送、第一放送です。連邦議会選挙の開票結果をお伝えします。」")
		sleep(1)
		print(f"与党{self.own_party_name}は...")
		sleep(2)
		if self.own_party_outside_support > 50:
			print("「過半数の議席を獲得し、政権を維持する見通しです。」")
			sleep(1)
			print("「与党総裁は選挙結果を受けて、『国民の政権への信頼が依然として高いことを示す重要な選挙となった。国民の皆様に感謝を申し上げたい。』との声明を発表しました。」")
		else:
			print("「大幅に議席数を減らし、政権を野党に明け渡す見通しです。」")
			sleep(1)
			print("「野党総裁は選挙結果を受けて、『国民の政権への不信感がこのような結果につながった。我々も政権を担う身として国民を失望させないように職務に邁進していきたい。』との声明を発表しました。」")
		sleep(1)
		print("「では、次のニュースに移ります...」")
		sleep(1)
		print("")
		print("これにてゲームは終了です。お疲れさまでした。")



	def waitUserAction(self):

		location = 1

		print(
			"\r"
			"次の中から行動を選択してください。\n"
			"▶1. 各地で街頭演説を行う\n"
			"2. わいろを贈って票を買う\n"
			"3. 軍人にわいろを贈って軍部の支持を得る\n"
			"4. 軍部と結託して軍事クーデターを起こす\n"
			"5. 何もしない"
			)
		sys.stdout.flush()

		while True:

			if keyboard.is_pressed("up") and location != 1:
				location -= 1
			elif keyboard.is_pressed("down") and location != 5:
				location += 1
			elif keyboard.is_pressed("enter"):
				break
			else:
				continue

			if location == 1:
				print(
				"\r"
				"次の中から行動を選択してください。\n"
				"▶1. 各地で街頭演説を行う\n"
				"2. わいろを贈って票を買う\n"
				"3. 軍人にわいろを贈って軍部の支持を得る\n"
				"4. 軍部と結託して軍事クーデターを起こす\n"
				"5. 何もしない"
				)
				sys.stdout.flush()
			elif location == 2:
				print(
				"\r"
				"次の中から行動を選択してください。\n"
				"1. 各地で街頭演説を行う\n"
				"▶2. わいろを贈って票を買う\n"
				"3. 軍人にわいろを贈って軍部の支持を得る\n"
				"4. 軍部と結託して軍事クーデターを起こす\n"
				"5. 何もしない"
				)
				sys.stdout.flush()
			elif location == 3:
				print(
				"\r"
				"次の中から行動を選択してください。\n"
				"1. 各地で街頭演説を行う\n"
				"2. わいろを贈って票を買う\n"
				"▶3. 軍人にわいろを贈って軍部の支持を得る\n"
				"4. 軍部と結託して軍事クーデターを起こす\n"
				"5. 何もしない"
				)
				sys.stdout.flush()
			elif location == 4:
				print(
				"\r"
				"次の中から行動を選択してください。\n"
				"1. 各地で街頭演説を行う\n"
				"2. わいろを贈って票を買う\n"
				"3. 軍人にわいろを贈って軍部の支持を得る\n"
				"▶4. 軍部と結託して軍事クーデターを起こす\n"
				"5. 何もしない"
				)
				sys.stdout.flush()
			elif location == 5:
				print(
				"\r"
				"次の中から行動を選択してください。\n"
				"1. 各地で街頭演説を行う\n"
				"2. わいろを贈って票を買う\n"
				"3. 軍人にわいろを贈って軍部の支持を得る\n"
				"4. 軍部と結託して軍事クーデターを起こす\n"
				"▶5. 何もしない"
				)
				sys.stdout.flush()
			
		print()
		return location


		

def main():

	obj = game()
	while obj.game_end_flag == False:
		obj.next_day()
		sleep(1)

main()