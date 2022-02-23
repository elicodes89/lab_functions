tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(tasks_list):
    tasks_to_return = []
    for currrent_task_in_loop in tasks_list:
        if currrent_task_in_loop['completed'] == False:
            tasks_to_return.append(currrent_task_in_loop)
    return tasks_to_return

filtered_tasks = uncompleted_tasks(tasks)

print(filtered_tasks)

def completed_tasks(tasks_list):
    tasks_to_return = []
    for current_task_in_loop in tasks_list:
        if current_task_in_loop['completed'] == True:
            tasks_to_return.append(current_task_in_loop)
    return tasks_to_return

filtered_tasks = completed_tasks(tasks)
print(filtered_tasks)

# def description(list_of_tasks):
#     descriptions_to_return = []
#     for task in list_of_tasks:
#         return list_of_tasks

# filtered_tasks = description(tasks)
# print(filtered_tasks)