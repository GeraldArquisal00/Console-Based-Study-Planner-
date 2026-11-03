# ====================================================
#  CONSOLE-BASED STUDY PLANNER
# ====================================================
from datetime import datetime

subject_list = []
task_list = []

def add_subject():
    while True:
        subject = input("Enter subject name: ").strip()
        if subject in subject_list:
            print("[INFO] This subject is already added.\n")
            break
        is_valid = True
        for char in subject:
            if not (char.isalpha() or char == " "):
                is_valid = False
                break
        if is_valid and subject != "":
            subject_list.append(subject)
            print(f"[SUCCESS] Subject '{subject}' added.\n")
            break
        else:
            print("[INVALID] Enter letters only.\n")

def add_task():
    if len(subject_list) == 0:
        print("[INFO] You have no subjects yet. Add a subject first.\n")
        return
    print("Available Subjects:")
    for i, subj in enumerate(subject_list, 1):
        print(f"  {i}. {subj}")
    while True:
        choice = input("Enter subject number or name: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(subject_list):
                subject = subject_list[idx]
                break
            print("[INVALID] Number not in list.\n")
        elif choice in subject_list:
            subject = choice
            break
        else:
            print("[INVALID] Subject not found. Add it first.\n")
    task_name = input("Enter task name: ").strip()
    
    # Date validation
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("[INVALID] Use valid date in YYYY-MM-DD format only.\n")
    
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip()
        if priority in ["High", "Medium", "Low"]:
            break
        print("[INVALID] Enter High, Medium, or Low only.\n")
    new_task = [subject, task_name, due_date, priority, "Pending"]
    task_list.append(new_task)
    print(f"[SUCCESS] Task '{task_name}' added to '{subject}'.\n")

def view_tasks():
    if len(task_list) == 0:
        print("[INFO] No tasks found.\n")
        return
    print("=" * 52)
    print("YOUR STUDY TASKS")
    print("=" * 52)
    for index in range(len(task_list)):
        num = index + 1
        subj = task_list[index][0]
        name = task_list[index][1]
        due = task_list[index][2]
        prio = task_list[index][3]
        stat = task_list[index][4]
        print(f"{num}. {name}")
        print(f"   Subject: {subj}")
        print(f"   Due: {due} | Priority: {prio} | Status: {stat}")
        print("-" * 52)
    print()

def update_status():
    if len(task_list) == 0:
        print("[INFO] No tasks to update.\n")
        return
    while True:
        number_input = input("Enter task number: ").strip()
        if number_input.isdigit():
            task_num = int(number_input) - 1
            break
        print("[INVALID] Enter numbers only.\n")
    if 0 <= task_num < len(task_list):
        while True:
            new_status = input("Enter new status (Pending/In Progress/Completed): ").strip()
            if new_status in ["Pending", "In Progress", "Completed"]:
                task_list[task_num][4] = new_status
                print("[SUCCESS] Status updated.\n")
                break
            print("[INVALID] Enter Pending, In Progress, or Completed only.\n")
    else:
        print("[ERROR] Task number does not exist.\n")

def progress_summary():
    total = len(task_list)
    completed = 0
    for t in task_list:
        if t[4] == "Completed":
            completed += 1
    pending = total - completed
    print("=" * 32)
    print("PROGRESS SUMMARY")
    print("=" * 32)
    print(f"Total Subjects: {len(subject_list)}")
    print(f"Total Tasks  : {total}")
    print(f"Completed    : {completed}")
    print(f"Pending      : {pending}")
    if total > 0:
        percentage = (completed / total) * 100
        print(f"Progress     : {percentage:.1f}%")
    print("=" * 32)
    print()

def main():
    while True:
        print("===== STUDY PLANNER MENU =====")
        print("1. Add Subject")
        print("2. Add Task")
        print("3. View All Tasks")
        print("4. Update Task Status")
        print("5. Progress Summary")
        print("6. Exit")
        print("===============================")
        while True:
            choice = input("Enter your choice: ").strip()
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= 6:
                    break
            print("[INVALID] Please enter 1 to 6 only.\n")
        if choice_num == 1:
            add_subject()
        elif choice_num == 2:
            add_task()
        elif choice_num == 3:
            view_tasks()
        elif choice_num == 4:
            update_status()
        elif choice_num == 5:
            progress_summary()
        elif choice_num == 6:
            print("\nThank you for using Study Planner! Goodbye.")
            break

if __name__ == "__main__":
    main()
