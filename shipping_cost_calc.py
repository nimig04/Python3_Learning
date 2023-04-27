# Calculates shipping based on weight and transportation methods

weight = 4.8

#Ground shipping
if weight <= 2:
  cost_ground = (weight * 1.5) + 20.00
elif weight <= 6:
  cost_ground = (weight * 3.0) + 20.00
elif weight <= 10:
  cost_ground = (weight * 4.0) + 20.00
else:
  cost_ground = (weight * 4.75) + 20.00
#print(cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125.00
print("Cost of ground premium is: $", cost_ground_premium)
#Drone Shipping
if weight <= 2:
  cost_drone = (weight * 4.5)
elif weight <= 6:
  cost_drone = (weight * 9.0)
elif weight <= 10:
  cost_drone = (weight * 12.0)
else:
  cost_drone = (weight * 14.25)
#print(cost_drone)

if cost_ground < cost_drone and cost_ground < cost_ground_premium:
  print(f"Ground shipping is cheaper. It will cost ${cost_ground}, which is ${cost_drone - cost_ground} cheaper than drone shipping.")
elif cost_ground > cost_drone and cost_drone < cost_ground_premium:
  print(f"Drone shipping is cheaper. It will cost ${cost_drone}, which is ${cost_ground - cost_drone} cheaper than ground shipping.")
elif cost_ground > cost_ground_premium and cost_drone > cost_ground_premium:
  print(f"The cost of Ground Premium Shipping is the cheapest option. At $125.00 it is ${cost_ground - cost_ground_premium} cheaper than ground shipping and ${cost_drone - cost_ground_premium} cheaper than drone shipping.")
else:
  print(f"There is no difference in price. It will cost ${cost_ground}")
