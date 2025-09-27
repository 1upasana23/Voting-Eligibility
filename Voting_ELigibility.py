# Voting Eligibility

print("...WELCOME TO VOTING ELIGIBILITY SYSTEM...")
print("Type 2 to exit anytime you want to stop.")

# Counter to track the total number of people who checked
count = 0

# Loop starts here
while True:
  # Display the options
  print("Select the option you want to perform.")
  print(1,". Check voting eligibilty")
  print(2,". exit")
  
  # Take the input from the user
  choice = input("Enter your choice:").strip()

  # End of the loop
  if choice == "2":
    print("GoodBye! Thank you for using the system.")
    print("Total number of people who checked eligibility is:", count)
    break

  # Take the user input
  elif choice == "1":
    user_input = input("Enter your age:").strip()
  
  # Checking the age if age>=18 or age<18
    if user_input.isdigit(): #check if the user_input is digit or not
      age = int(user_input)
      if 0 <= age <= 120:
        count += 1 # increase the counter only for valid ages
        if age >= 18:
          print("You are eligible to vote.")
        else:
          print("You are not eligible to vote.")
      else:
        print("Invalid input!! Please enter a realistic age (0-120).")
  else:
      print("Invalid! Please enter a valid number or type exit.")