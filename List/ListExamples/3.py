# to do list

todo_list = ["Clean room", "Code Python", "Read book"]
print(todo_list)

taskAdd = todo_list.append("Go to market")
print("After adding new task : ", todo_list)

done_task = todo_list.pop(0)
print(f"Completed: {done_task}")
print("Remaining tasks:", todo_list)