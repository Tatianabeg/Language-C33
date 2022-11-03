print()
print("tel_book_v1")

filename = "tel_book.csv" 
myfile = open(filename, "a+") 
myfile.close
  
def main_menu(): 
    print( "\n main menu\n") 
    print( "1. all contacts") 
    print( "2.  new contact") 
    print( "3. search for an existing contact") 
    print( "4. exit") 
    choice = input("selecting a menu item: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "contact not found") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("enter") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("enter") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("enter") 
        main_menu() 
    elif choice == "4": 
        print("") 
    else: 
        print( "repeat input\n") 
        enter = input("enter")
        main_menu()
        
def searchcontact(): 
    searchname = input("name from contacts: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print("contact found: ", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print(f"contact {searchname} not found") 
 
def input_firstname(): 
    first = input("entering a name: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
  
def input_lastname(): 
    last = input("surname: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
    return firstchar.upper() + remlname

def key_gen():
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(4))
    return key
key = key_gen()

# conservation 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("number phone: ") 
    emailID = input(" E-mail: ") 
    contactDetails =(f"{ttt}" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID +  "\n") 
    contactDetails =(f"{key};" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID +  "\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print("new entry in the telephone directory: \n " + contactDetails + " created!")  
 
main_menu()
time.sleep(5)