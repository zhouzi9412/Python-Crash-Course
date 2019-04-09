sandwich_orders = ['red','orange','blue']
finishied_sandwichs = []
while sandwich_orders:
    current_sandwichs = sandwich_orders.pop()
    print("I made your tuna sandwich. ")
    finishied_sandwichs.append(current_sandwichs)
print("\nThe following sandwich have been confirmed: ")
for finished_sandwich in finishied_sandwichs:
    print(finished_sandwich.title())