# Namespaces

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")  

# Local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

drink_potion()
# wont print get an error
# print(potion_strength)  
  
# Global Scope

player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()
print(player_health) #should print 10

def game():
  def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()
print(player_health) #should get an error. drink_potion is not in scope
