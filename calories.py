while True:
    caloriesGoal = float(input('Enter the calorie goal for number of calories for today: '))
    if 1500 <= caloriesGoal <= 3000:
        break
    else:
        print("Goal must be between 1500 and 3000 calories!")

totalConsumed = 0
items = 0

while True:
      caloriesConsumed = float(input('Item {}: How many calories was it? (-1 to stop)'.format(items+1)))

      if caloriesConsumed < 0:
          print("Input stopped")
          break

      totalConsumed += caloriesConsumed 
      items += 1

      if totalConsumed > caloriesGoal:
          print("Goal reached/exceeded!")
          break

print('You consumed {} calories in {} items.'.format(totalConsumed, items))

if caloriesGoal > totalConsumed:
      print('The user is within their goal by ', (caloriesGoal - totalConsumed))
else:
      print('The user exceeded their goal by', (totalConsumed - caloriesGoal))
