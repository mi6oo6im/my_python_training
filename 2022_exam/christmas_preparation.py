paper_price = 5.8
cloth_price = 7.2
glue_price = 1.2

num_paper = int(input())
num_cloth = int(input())
liters_glue = float(input())
discount = int(input())

paper_cost = paper_price * num_paper
cloth_cost = cloth_price * num_cloth
glue_cost = glue_price * liters_glue

total_cost = paper_cost + cloth_cost + glue_cost

total_cost *= 1 - discount / 100

print(f"{total_cost:.3f}")
