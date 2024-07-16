#sleaping calculator

#un function
def ask_for_un():
    while True:
        user_name = input ("Please enter your user name (user name must have just letters): ")
        if user_name.isalpha() and len(user_name) == 8:
            print ("Your user_name is", user_name )
            break
        else:
            print ("Please enter a valid user name")

#ask_for_st
def ask_for_st ():
    while True:
        st = input("How many hours do you sleape")
        if st.isdigit():
            st = int(st)
            print ("You are sleaping, ",st," Hours")
            return st
        else:
            print ("please enter a valid number")


#comp
def comp(st):
    if st > 7:
        print("You are too lazy")
    elif st < 7:
        print("You most sleape more than 7 Hours")
    else:
        print("Your okey")

#main_program
def main_programe():
    print ("Hllo, Welcome in the programe of sleaping time")
    ask_for_un()
    st = ask_for_st()
    comp(st)

while True:
    main_programe()
    choice = input ("do you want to restart the program? (yes/no):").strip().lower()
    if choice != "yes":
        print ("Thank you")
        break
