import sys 
TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100

def print_header():
    print_divider()
    print("The Pycharmers -- 11/1/2023 -- Atlanta, GA")
    print("Act Now! There are only {} tickets remaining.".format(tickets_remaining))
    print_divider()

def print_divider():
    print()
    print(('*-' * 24) + '*')
    print()

def calculate_price(number_of_tickets):
    return ((number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE)

name = ""
while tickets_remaining > 0: 
    
    try:
        print_header()
        if not name:
            name = input("What is your name? ").capitalize()
       
        number_of_tickets = int(input("Hi {}! How many tickets would you like? ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print('\n-----')
        print("Oh no! Something went wrong.\n{}\nPlease try again.".format(err))
        print('-----\n')
    else:
        total_price = calculate_price(number_of_tickets)
        print("Price per ticket: ${}".format(TICKET_PRICE))
        print("Number of Tickets: {}".format(number_of_tickets))
        print("Service charge: ${}".format(SERVICE_CHARGE))
        print("The total due is ${}".format(total_price))
        should_proceed = input("Do you want to proceed? [Y/N] ")
        if should_proceed.upper() =='Y':
            print('\n-----')
            print('\nSOLD!\n')
            print('-----\n')
            tickets_remaining -= number_of_tickets
            if(tickets_remaining > 0):
                additional_tickets = input("Would you like to buy any additional tickets? [Y/N] ")
                if(additional_tickets.upper() == 'Y'):
                    continue
                else:
                    print_divider()
                    print("Tell your friends to buy their tickets today!\nThere are now only {} tickets remaining. Goodbye for now!".format(tickets_remaining))
                    print_divider()
                    sys.exit()
        else:
            print_divider()
            print("Thank you anyways, {}. Goodbye.".format(name))
            print_divider()
            sys.exit()
print("The concert is completely sold out. We are so grateful to our Pycharmer fans!")