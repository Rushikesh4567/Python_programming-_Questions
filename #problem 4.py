#problem 4
total_passengers = 0

for stop in range(1, 6): 
    passengers = int(input(f"Enter the number of passengers at stop {stop}: "))
    total_passengers += passengers 

print("Total number of passengers at the end: ",total_passengers)
