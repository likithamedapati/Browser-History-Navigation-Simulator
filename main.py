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
    elif choice == "4":
       print(f"Refreshing {current_page}… ")
    elif choice == "5":
      print(f"You are currently on: {current_page}")
    elif choice == "6":
      print("\n--- Browser History ---")

      if not history_list:
        print("No pages visited yet.")
      else:
        for i, page in enumerate(history_list, start=1):
            print(f"{i}. {page}")
    elif choice == "7":
     try:
        n = int(input("How many recent pages to show? "))

        if n <= 0:
            print("Enter a positive number.")
        else:
            print("\n--- Recent Pages ---")
            recent = history_list[-n:]

            if not recent:
                print("No history available.")
            else:
                for page in recent:
                    print(page)

     except:
        print("Invalid input.")
    elif choice == "8":
     page = input("Enter page name: ")

     if page in visit_count:
        print(f"{page} visited {visit_count[page]} times.")
     else:
        print("Page not found in history.")
    elif choice == "9":
     confirm = input("Are you sure you want to clear history? (yes/no): ").lower()

     if confirm == "yes":
        back_stack.clear()
        forward_stack.clear()
        history_list.clear()
        visit_count.clear()
        print("History cleared.")
     else:
        print("Cancelled.")
    elif choice == "10":
     back_stack.append(current_page)
     current_page = homepage
     forward_stack.clear()
     history_list.append(homepage)

     if homepage in visit_count:
        visit_count[homepage] += 1
     else:
        visit_count[homepage] = 1

     print(f"Returned to homepage: {homepage}")

    elif choice == "11":
        print("Closing browser")
        break
    else:
       print("Invalid choice! try again!...")
