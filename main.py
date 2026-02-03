print("Welcome to Smart Browser Simulator ")
print("-" * 40)

homepage = "home.com"
current_page = homepage

back_stack = []
forward_stack = []
history_list = []
visit_count = {}

print(f"You are on: {current_page}")
while True:
    print("\n------ MENU ------")
    print("1. Visit new page")
    print("2. Back")
    print("3. Forward")
    print("4. Refresh")
    print("5. Show current page")
    print("6. Show history")
    print("7. Recent pages")
    print("8. Visit counter")
    print("9. Clear history")
    print("10. Go to homepage")
    print("11. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
     new_page = input("Enter page URL: ")

     if current_page:
        back_stack.append(current_page)

     current_page = new_page
     forward_stack.clear()

     history_list.append(new_page)

     if new_page in visit_count:
        visit_count[new_page] += 1
     else:
        visit_count[new_page] = 1

     print(f"Visited: {current_page}")
    elif choice == "2":
     if not back_stack:
        print("No page to go back.")
     else:
        forward_stack.append(current_page)
        current_page = back_stack.pop()
        print(f"Moved back to: {current_page}")
    elif choice == "3":
     if not forward_stack:
        print("No page to go forward.")
     else:
        back_stack.append(current_page)
        current_page = forward_stack.pop()
        print(f"Moved forward to: {current_page}")

    elif choice == "11":
        print("Closing browser")
        break
