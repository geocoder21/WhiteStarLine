# Firestarter

# PARAMETERS

number_of_iterations = 10
width = 10
height = 10
fire_start_x = 4
fire_start_y = 4
fuel_amount = 5


environment = []
results = []
for h in range(height):
    row = []
    results_row = []
    for w in range(width):
        row.append(fuel_amount)
        results_row.append(fuel_amount)
    environment.append(row)
    results.append(results_row)

def print_environment():
    for h in range(height):
        for w in range(width):
            print(environment[h][w], end=" ")
        print("")
    print("")

print_environment()

environment[fire_start_y][fire_start_x] -= 1
print_environment()


for step in range(number_of_iterations):
    for h in range(1, height - 1):
        for w in range(1, width - 1):
            fire = False
            if (environment[h-1][w-1] < fuel_amount): fire = True
            if (environment[h-1][w] < fuel_amount): fire = True
            if (environment[h-1][w+1] < fuel_amount): fire = True
            if (environment[h][w-1] < fuel_amount): fire = True
            if (environment[h][w] < fuel_amount): fire = True
            if (environment[h][w+1] < fuel_amount): fire = True
            if (environment[h+1][w-1] < fuel_amount): fire = True
            if (environment[h+1][w] < fuel_amount): fire = True
            if (environment[h+1][w+1] < fuel_amount): fire = True
            if (fire == True) & (environment[h][w] > 0):
                results[h][w] -= 1
    environment = results
    print_environment()