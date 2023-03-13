# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
score_1 = 'Ruud Gullit'
score_2 = 'Marco van Basten'

print (score_1)
print (score_2)

goal_0 = 32
goal_1 = 54

scorers = 'Ruud Gullit ' + str(goal_0) + ', Marco van Basten ' + str(goal_1)
print (scorers)

report = f"{score_1} scored in the {goal_0}nd minute {score_2} scored in the {goal_1}th minute"
print (report)

player = 'Frank Rijkaard'

first_name = player.find ('Frank')
print (first_name)

last_name_len =  len (player[player.find ('Rijkaard')])
print (last_name_len)    

name_short = 'G. von Examplestein'
print (name_short)

chant = 'Gut! Gut! Gut!'
print (chant)

good_chant = chant[-1]!=''
print (good_chant)

print(2 != 2)

print(2 != 3)