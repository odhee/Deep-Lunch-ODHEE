# 숫자를 추측하는 게임
import random
secretNumber = random.randint(1,20)
print('1부터 20까지의 숫자가 있습니다.')

# 플레이어에게 6번의 추측을 요청한다.
for guessTaken in range(1,7):
  print('예상하는 숫자를 입력하세요.')
  guess = int(input())

  if guess < secretNumber:
    print('예상한 숫자가 너무 작습니다.')
  elif guess > secretNumber:
    print('예상한 숫자가 너무 큽니다.')
  else:
    break
if guess == secretNumber:
  print('예상한 숫자' + str(guess) + '는 정답입니다.')
else:
  print('아니오. 내가 생각하고 있던 번호는 ' + str(secretNumber) + '입니다')
  