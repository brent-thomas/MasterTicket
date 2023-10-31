TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100

def print_divider():
    print()
    print(('*-' * 24) + '*')
    print()

def calculate_price(number_of_tickets):
    return ((number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE)

while tickets_remaining > 0: 
    print_divider()
    print("Act Now! There are only {} tickets remaining.".format(tickets_remaining))
    print_divider()
    name = input("What is your name? ")
    try:
        number_of_tickets = int(input("Hi {}! How many tickets would you like? ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining. Nice try.".format(tickets_remaining))
    except ValueError as err:
        print('-' * 12)
        print('-' * 12)
        print("Oh no! Something went wrong.\n{}\nPlease try again.".format(err))
        print('-' * 12)
        print('-' * 12)
    else:
        total_price = calculate_price(number_of_tickets)
        print("The total due is ${}".format(total_price))
        should_proceed = input("Do you want to proceed? [Y/N] ")
        if should_proceed.upper() =='Y':
            print('-----')
            print('\nSOLD!\n')
            print('-----\n')
            tickets_remaining -= number_of_tickets
            if(tickets_remaining > 0):
                print("Tell your friends to buy their tickets today!\nThere are now only {} tickets remaining".format(tickets_remaining))
        else:
            print("Thank you anyways, {}. Goodbye.".format(name))
            print_divider()
print("Sorry, the concert has sold out! Don't worry will be back in your city next year!")