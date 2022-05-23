quantity = int(input())
days_to_christmas = int(input())
budget = 0
total_spirit = 0
ornament_set_cost_spirit = [2, 5]
tree_skirt_cost_spirit = [5, 3]
tree_garland_cost_spirit = [3, 10]
tree_lights_cost_spirit = [15, 17]

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_set_cost_spirit[0] * quantity
        total_spirit += ornament_set_cost_spirit[1]
    if day % 3 == 0:
        budget += (tree_skirt_cost_spirit[0] + tree_garland_cost_spirit[0]) * quantity
        total_spirit += tree_skirt_cost_spirit[1] + tree_garland_cost_spirit[1]
    if day % 5 == 0:
        budget += tree_lights_cost_spirit[0] * quantity
        total_spirit += tree_lights_cost_spirit[1]
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt_cost_spirit[0] + tree_garland_cost_spirit[0] + tree_lights_cost_spirit[0]
if days_to_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
