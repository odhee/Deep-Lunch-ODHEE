print("베스킨라빈스 31 게임 프로그램입니다!")
order = input('''순서를 입력하세요. (선공 1, 후공 0 입력) : ''')
order = int(order)
call = 0
count = 1
if count % 2 == order:
  # 사용자의 차례
  print('사용자의 차례')
else:
  # 컴퓨터의 차례