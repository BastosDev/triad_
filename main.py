

print('Triad Online')

# user name
usr_name = input('Enter your username : ')
print(f'Hi {usr_name}, Triad is ready to help you.')

# ToDo list
toDo = []

print("Type your tasks below. Type 'exit' to stop.")
while True:
    task = input('Enter the task')
    
    if task.lower() == 'exit':
        break

    toDo.append(task)

    print(f'>> [{task}] have been added!')

print("\n--- Your ToDo List ---")

for i, item in enumerate(toDo, 1):
    print(f"{i}. {item}")




