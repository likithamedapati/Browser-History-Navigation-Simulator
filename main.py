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

    if choice == "11":
        print("Closing browser")
        break
