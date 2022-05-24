package_weight = float(input())
service_type = input()
distance_km = int(input())
price_per_km_stotinki = 0

if package_weight < 1:
    price_per_km_stotinki = 3
elif 1 <= package_weight < 10:
    price_per_km_stotinki = 5
elif 10 <= package_weight < 40:
    price_per_km_stotinki = 10
elif 40 <= package_weight < 90:
    price_per_km_stotinki = 15
elif 90 <= package_weight < 150:
    price_per_km_stotinki = 20

if service_type == "express":
    if package_weight < 1:
        price_per_km_stotinki *= (1 + package_weight * 80 /100)
    if 1 <= package_weight < 10:
        price_per_km_stotinki *= (1 + package_weight * 40 /100)
    elif 10 <= package_weight < 40:
        price_per_km_stotinki *= (1 + package_weight * 5 /100)
    elif 40 <= package_weight < 90:
        price_per_km_stotinki *= (1 + package_weight * 2 /100)
    elif 90 <= package_weight < 150:
        price_per_km_stotinki *= (1 + package_weight * 1 /100)

total_cost_stotinki = price_per_km_stotinki * distance_km
total_cost_lv = total_cost_stotinki / 100

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total_cost_lv:.2f} lv.")
