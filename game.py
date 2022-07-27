import random
def vending_machine_sim():
    global number_of_days 
    global amount
    global number_of_days
    global total_days
    global total_vending_machine_profit   
    global lays_stock, jalapeno_chips_stock, pack_stock
    global famous_amos_stock, grandma_cookies_stock, snickers_stock, kit_kat_four_stock
    global coca_cola_pack_stock, pepsi_can_stock, caprisun_pack_stock
    global hot_cheetos_stock, pop_tarts_stock
    global all_stock
    global money_spent_market
    global chips_stock, cookie_and_candy_stock, soda_beverages_stock
    global vending_machine_profit_chips, vending_machine_profit_cookies, vending_machine_profit_beverages
    global information
    global vending_machine_owner_name
    global owner_name
    


    print("\n*****Welcome to Brandon's Virtual Vending Machine Simulator*****")
    try:
        owner_name = input("Enter name: ")
        if int(owner_name):
            while True:
                owner_name = input("Invalid name. Enter your name: ")
                if int(owner_name) == False:
                    False

    except ValueError:
        print('Name: {owner_name}'.format(owner_name=str(owner_name)))


    try:
        number_of_days = int(input("""In this simulator, your objective is to buy items from the market and resell them by stocking in the vending machine. 
If you earn profit for the amount of days, you win. If you lose money, you lose. This will help develop the learning of side hustling of a vending machine business. Enter the number of days that you want to play (example: 1): """))
    except ValueError:
        while True:
            try:
                number_of_days = int(input("Not a valid number. Enter days: "))
                if number_of_days:
                    break
            except ValueError:
                continue
            
    
    print("You will play for {days} days.".format(days=number_of_days))

    total_days = number_of_days
   
    
    vending_machine_price = 4000.00
    amount = 5000.0
    amount -= vending_machine_price

    total_vending_machine_profit = 0.00

    all_stock = 0

    lays_stock = 0
    jalapeno_chips_stock = 0
    pack_stock = 0

    famous_amos_stock = 0
    grandma_cookies_stock = 0
    snickers_stock = 0 
    kit_kat_four_stock = 0

    coca_cola_pack_stock = 0
    pepsi_can_stock = 0
    caprisun_pack_stock = 0

    hot_cheetos_stock = 0
    pop_tarts_stock = 0 

    chips_stock = 0
    cookie_and_candy_stock = 0
    soda_beverages_stock = 0
    money_spent_market = 0.00

    vending_machine_profit_chips = 0
    vending_machine_profit_cookies = 0
    vending_machine_profit_beverages = 0


    print("You decide to buy a used vending machine for $4000.00 and is located at a very popular mall in California. Your budget for buying snacks will be ${amount}.".format(amount=amount))
    print("**********************************************************************************************************************************************************")
    market()
    
def market():
    global aisle_number
    
    try: 
        aisle_number = int(input("""Welcome to the AP Supermarket! You can choose a variety of snacks, individually or in packs. Select an aisle

    Aisle 1: Potato Chips
    Aisle 2: Cookies and Deserts
    Aisle 3: Soda and Beverages
    Aisle 4: Miscellanious
    
Enter aisle number (example: 1 for Potato Chips aisle): """))
        if aisle_number > 4:
            while True:
                aisle_number = int(input("Invalid input. Select aisle: "))
                if aisle_number < 5:
                    break
    except ValueError:
        while True:
            try:
                aisle_number = int(input("Invalid input. Select aisle: "))
                if aisle_number and aisle_number < 5:
                    break
            except ValueError:
                continue
    market_items()
    
def market_items():
    global aisle_number
    global amount

    if aisle_number == 1:
        aisle_one_stock()
    if aisle_number == 2:
        aisle_two_stock()
    if aisle_number == 3:
        aisle_three_stock()
    if aisle_number == 4:
        aisle_four_stock()

def aisle_one_stock():
    global money_spent_market
    global amount
    global lays_stock, jalapeno_chips_stock, pack_stock
    
    invalidation = False
    game_status = False
    market_status = False
    shop_status = False

    while True:
        aisle_one_items = input("""*****Aisle 1: Potato Chips*****
        
1A: Lays (Small) for $0.50
1B: Jalapeno Baked Chips (Medium) for $1.00
1C: Pack of Frito-Lay Chips for $20 (Includes 10 Lays Chips, 10 Jalapeno Chips, and 10 Dorito Chips)
Choose section (Example: 1A): """)
        if aisle_one_items == '1A':
            lays = 0.50
            try:
                product_amount = int(input("Enter amount of lays: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue
                    
            lays_stock = product_amount
            charge_amount = lays * (product_amount)
            money_spent_market += charge_amount
            amount -= charge_amount

            confirmation = input("Would you like to buy {amount} of lays for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} bags of lays and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break
                    
                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
                        
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break
    
        elif aisle_one_items == '1B':
            jalapeno_chips = 1.00
            try:
                product_amount = int(input("Enter amount of Jalapeno Baked Chips: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            jalapeno_chips_stock = product_amount
            charge_amount = jalapeno_chips * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} of Jalapeno Baked Chips for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} bags of Jalapeno Baked Chips and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        elif aisle_one_items == '1C':
            pack_of_frito_lay = 20.00
            try:
                product_amount = int(input("Enter amount of packs: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            pack_stock = product_amount
            charge_amount = pack_of_frito_lay * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} pack(s) of Frito-Lay Chips for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} pack(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:

                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        else:
            print("invalid")
            invalidation = True
            break

    

    if (market_status == True) or (invalidation == True):
        aisle_one_stock()
    if game_status:
        vending_machine_game(total_days)
    if shop_status == True:
        market()

def aisle_two_stock():
    global money_spent_market
    global amount
    global famous_amos_stock, grandma_cookies_stock, snickers_stock, kit_kat_four_stock
    
    invalidation = False
    game_status = False
    market_status = False
    shop_status = False

    while True:
        aisle_two_items = input("""*****Aisle 2: Cookies and Candy*****
        
2A: Famous Amos Small Cookies for $0.75
2B: Grandma's Mini Cookies for $0.50
2C: Snickers Bar (Small) for $0.50
2D: Kit-Kat Bar 4 finger (4-sticks) for $ 1.00
Choose section (Example: 2B): """)

        if aisle_two_items == '2A':
            famous_amos = 0.75
            try:
                product_amount = int(input("Enter amount of famous amos cookie bags: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            famous_amos_stock = product_amount
            charge_amount = famous_amos * (product_amount)
            money_spent_market += charge_amount
            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} of famous amos cookie bag(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} bag(s) of famous amos cookies and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break
                    
                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
                        
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break
    

        elif aisle_two_items == '2B':
            grandma_cookies = 0.50
            try:
                product_amount = int(input("Enter amount of Grandma's Mini Cookie Bags: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            grandma_cookies_stock = product_amount
            charge_amount = grandma_cookies * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            
            confirmation = input("Would you like to buy {amount} bags of Grandma's Mini cookies for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} bags of Grandma's Mini cookies and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        elif aisle_two_items == '2C':
            snickers_bar = 0.50
            try:
                product_amount = int(input("Enter amount of Snickers Bar(s): "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            snickers_stock = product_amount
            charge_amount = snickers_bar * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} Snicker Bar(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} Snicker Bar(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:

                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        elif aisle_two_items == '2D':
            kit_kat_four_sticks = 1.00
            try:
                product_amount = int(input("Enter amount of Kit-Kat Four Finger bags: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            kit_kat_four_stock = product_amount
            charge_amount = kit_kat_four_sticks * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} Kit-Kat Four Finger bag(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} Kit-Kat Four Finger bag(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:

                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        else:
            print("invalid")
            invalidation = True
            break

    if (market_status == True) or (invalidation == True):
        aisle_two_stock()

    if game_status:
        vending_machine_game(total_days)

    if shop_status == True:
        market()


def aisle_three_stock():
    global money_spent_market
    global amount
    global coca_cola_pack_stock, pepsi_can_stock, caprisun_pack_stock
    
    invalidation = False
    game_status = False
    market_status = False
    shop_status = False
    while True:
        aisle_three_items = input("""*****Aisle 3: Soda and Beverages *****
        
3A: Coca-Cola 12 fl oz can pack (12 cans) for $6.00
3B: Pepsi soda can for $0.75
3C: Caprisun Strawberry Kiwi pack (10 caprisuns) for $2.50

Choose section (Example: 3B): """)

        if aisle_three_items == '3A':
            coca_cola_pack = 6.00
            try:
                product_amount = int(input("Enter amount of coca-cola packs: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            coca_cola_pack_stock = product_amount
            charge_amount = coca_cola_pack * (product_amount)
            money_spent_market += charge_amount
            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} coca-cola pack(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} coca-cola pack(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break
                    
                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
                        
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break
    
        elif aisle_three_items == '3B':
            pepsi_can = 0.75
            try:
                product_amount = int(input("Enter amount of pepsi cans: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            pepsi_can_stock = product_amount
            charge_amount = pepsi_can * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} pepsi can(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} pepsi can(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        elif aisle_three_items == '3C':
            caprisun_pack = 2.50
            try:
                product_amount = int(input("Enter amount of caprisun packs: "))
            except ValueError:
                while True:
                    try:
                        product_amount = int(input("Invalid input. Enter amount: "))
                        if product_amount:
                            break
                    except ValueError:
                        continue

            caprisun_pack_stock = product_amount
            charge_amount = caprisun_pack * (product_amount)

            money_spent_market += charge_amount

            amount -= charge_amount
            confirmation = input("Would you like to buy {amount} caprisun pack(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
            if confirmation.lower() == "yes":
                aisle_status = input("You got {amount} caprisun pack(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                if aisle_status.lower() == "yes":
                    market_status = True
                    break

                else:
                    shopping_status = input("Do you want to continue shopping? ")
                    if shopping_status.lower() == "yes":
                        shop_status = True
                        break
                    else:
                        game_status = True 
                        break
            else:
                amount += charge_amount
                money_spent_market -= charge_amount
                market_status = True
                break

        else:
            print("invalid")
            invalidation = True
            break

    if (market_status == True) or (invalidation == True):
        aisle_three_stock()
    if game_status:
        vending_machine_game(total_days)
    if shop_status == True:
        market()

def aisle_four_stock():
    global money_spent_market
    global amount
    global hot_cheetos_stock, pop_tarts_stock

    invalidation = False
    game_status = False
    market_status = False
    shop_status = False
    stock_chances = random.randint(1,5)
    while True:
        print("*****Aisle 4: Special Limited Offer Stock *****")
        if stock_chances == 1:
            print("     4A: Hot Cheetos Large for $1.00")
            hot_cheetos = input("Choose section: ")

            if hot_cheetos == "4A":
                hot_cheetos_price = 1.00
                try:
                    product_amount = int(input("Enter amount of hot cheetos bags: "))
                except ValueError:
                    while True:
                        try:
                            product_amount = int(input("Invalid input. Enter amount: "))
                            if product_amount:
                                break
                        except ValueError:
                            continue

                hot_cheetos_stock = product_amount
                charge_amount = hot_cheetos_price * (product_amount)

                money_spent_market += charge_amount

                amount -= charge_amount
                confirmation = input("Would you like to buy {amount} hot cheetos bag(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
                if confirmation.lower() == "yes":
                    aisle_status = input("You got {amount} hot cheetos bag(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                    if aisle_status.lower() == "yes":
                        market_status = True
                        break

                    else:
                        shopping_status = input("Do you want to continue shopping? ")
                        if shopping_status.lower() == "yes":
                            shop_status = True
                            break
                        else:
                            game_status = True 
                            break
                else:
                    amount += charge_amount
                    money_spent_market -= charge_amount
                    market_status = True
                    break
            else:
                print("invalid")
                invalidation = True
                break

        elif stock_chances == 2:
            print ("    4A: Pop Tarts Strawberry 2 pieces for $0.50")
            pop_tarts = input("Choose section: ")
            if pop_tarts == "4A":
                pop_tarts_price = 1.00
                try:    
                    product_amount = int(input("Enter amount of pop tarts snacks: "))
                except ValueError:
                    while True:
                        try:
                            product_amount = int(input("Invalid input. Enter amount: "))
                            if product_amount:
                                break
                        except ValueError:
                            continue

                pop_tarts_stock = product_amount
                charge_amount = pop_tarts_price * (product_amount)

                money_spent_market += charge_amount

                amount -= charge_amount
                confirmation = input("Would you like to buy {amount} pop tarts snack(s) for {price}?: ".format(amount=str(product_amount), price=str(charge_amount)))
                if confirmation.lower() == "yes":
                    aisle_status = input("You got {amount} pop tarts snack(s) and have {bank} remaining. Would you like to continue shopping in this aisle?: ".format(amount=str(product_amount),bank=str(amount)))
                    if aisle_status.lower() == "yes":
                        market_status = True
                        break

                    else:
                        shopping_status = input("Do you want to continue shopping? ")
                        if shopping_status.lower() == "yes":
                            shop_status = True
                            break
                        else:
                            game_status = True 
                            break
                else:
                    amount += charge_amount
                    money_spent_market -= charge_amount
                    market_status = True
                    break
            else:
                print("invalid")
                invalidation = True
                break
        else:
            print("There are no special stock available")
            shopping_status = input("Do you want to continue shopping? ")
            if shopping_status.lower() == "yes":
                shop_status = True
                break
            else:
                game_status = True 
                break

    if (market_status == True) or (invalidation == True):
        aisle_four_stock()
    if game_status:
        vending_machine_game(total_days)
    if shop_status == True:
        market()
        
def vending_machine_game(days_occured):
    global amount
    global chips_stock, cookie_and_candy_stock, soda_beverages_stock
    global lays_stock,jalapeno_chips_stock,pack_stock
    global famous_amos_stock, grandma_cookies_stock, snickers_stock, kit_kat_four_stock
    global coca_cola_pack_stock, pepsi_can_stock, caprisun_pack_stock
    global hot_cheetos_stock, pop_tarts_stock
    global all_stock
    global money_spent_market
    global number_of_days
    global total_days
    global total_vending_machine_profit
    global vending_machine_profit_chips, vending_machine_profit_cookies, vending_machine_profit_beverages
    global information
    global vending_machine_owner_name
    global final_days
    global owner_name

    print("**************************************")
    try:
        if lays_stock > 0 or jalapeno_chips_stock > 0 or pack_stock > 0 or hot_cheetos_stock > 0 or chips_stock > 0:
            price_for_chips = float(input("How much are you willing to sell each of your chips?: "))
            new_prices_chips = price_for_chips

        if famous_amos_stock > 0 or grandma_cookies_stock > 0 or snickers_stock > 0 or kit_kat_four_stock > 0 or pop_tarts_stock > 0 or cookie_and_candy_stock > 0:
            price_for_cookies = float(input("How much are you willing to sell each of your cookies/candies?: "))
            new_prices_cookies = price_for_cookies

        if coca_cola_pack_stock > 0 or pepsi_can_stock > 0 or caprisun_pack_stock > 0 or soda_beverages_stock > 0:
            price_for_soda = float(input("How much are you willing to sell each of your soda cans/juice pouches?: "))
            new_prices_soda = price_for_soda

    except ValueError:
        while True:
            try:
                if lays_stock > 0 or jalapeno_chips_stock > 0 or pack_stock > 0 or hot_cheetos_stock > 0 or chips_stock > 0 :
                    price_for_chips = float(input("Invalid price. Set a price for chips: "))
                    new_prices_chips = price_for_chips
                    break

                if famous_amos_stock > 0 or grandma_cookies_stock > 0 or snickers_stock > 0 or kit_kat_four_stock > 0 or pop_tarts_stock > 0 or cookie_and_candy_stock:
                    price_for_cookies = float(input("Invalid price. Set a price for cookies/candies: "))
                    new_prices_cookies = price_for_cookies
                    break

                if coca_cola_pack_stock > 0 or pepsi_can_stock > 0 or caprisun_pack_stock > 0 or soda_beverages_stock > 0:
                    price_for_soda = float(input("Invalid price. Set a price for soda cans/juice pouches: "))
                    new_prices_soda = price_for_soda
                    break
                
            except ValueError:
                continue

    
    chips_stock += (lays_stock + jalapeno_chips_stock + pack_stock + hot_cheetos_stock)
    cookie_and_candy_stock += (famous_amos_stock + grandma_cookies_stock + snickers_stock + kit_kat_four_stock + pop_tarts_stock)
    soda_beverages_stock += (coca_cola_pack_stock + pepsi_can_stock + caprisun_pack_stock)

    
    print('*****************************************************')
    if chips_stock > 0:
        guest_amount_bought_chips = random.randint(1, chips_stock)
        vending_machine_profit_chips += (float(guest_amount_bought_chips) * new_prices_chips)
        print("People decided to buy {amount} of your chips.".format(amount=guest_amount_bought_chips))

        chips_stock -= guest_amount_bought_chips

    if cookie_and_candy_stock > 0:
        guest_amount_bought_cookies = random.randint(1, cookie_and_candy_stock)
        vending_machine_profit_cookies += (float(guest_amount_bought_cookies) * new_prices_cookies)
        print("People decided to buy {amount} of your cookies/candies.".format(amount=guest_amount_bought_cookies))
        cookie_and_candy_stock -= guest_amount_bought_cookies

    if soda_beverages_stock > 0:
        guest_amount_bought_beverages = random.randint(1, soda_beverages_stock)
        vending_machine_profit_beverages += (float(guest_amount_bought_beverages) * new_prices_soda)
        print("People decided to buy {amount} of your beverages.".format(amount=guest_amount_bought_beverages))
        soda_beverages_stock -= guest_amount_bought_beverages

    total_vending_machine_profit += vending_machine_profit_beverages + vending_machine_profit_chips + vending_machine_profit_cookies

    days_occured = total_days
    final_days = days_occured

    lays_stock = 0
    jalapeno_chips_stock = 0
    pack_stock = 0

    famous_amos_stock = 0
    grandma_cookies_stock = 0
    snickers_stock = 0 
    kit_kat_four_stock = 0

    coca_cola_pack_stock = 0
    pepsi_can_stock = 0
    caprisun_pack_stock = 0

    hot_cheetos_stock = 0
    pop_tarts_stock = 0 

    if number_of_days == 1:
        if total_vending_machine_profit > money_spent_market:
            vending_machine_owner_name = owner_name

            information = [vending_machine_owner_name, final_days, amount, money_spent_market, vending_machine_profit_chips, vending_machine_profit_cookies, vending_machine_profit_beverages]

            print('You made ${amount} after {days} day(s). You successfully completed your objective and you learned how to make profit with a small vending machine business/hustle!'.format(amount=total_vending_machine_profit-money_spent_market, days=final_days))
            print('******************')
            for i in information:
                index = information.index(i)
                if index == 0:
                    print('Name of Vending Machine Owner: ' + i)
                if index == 1:
                    print('Days played in Vending Machine Simulator: ' + str(i))
                if index == 2:
                    print('Budget Remaining: ' + str(i))
                if index == 3:
                    print('Money Spent: ${num}'.format(num=i))
                if index == 4:
                    print('Money profited from chips: ${num}'.format(num=i))
                if index == 5:
                    print('Money profited from cookies/candies: ${num}'.format(num=i))
                if index == 6:
                    print('Money profited from beverages: ${num}'.format(num=i))
                
            print('******************')
            exit()
        else:
            vending_machine_owner_name = owner_name
            information = [vending_machine_owner_name, final_days, amount, money_spent_market, vending_machine_profit_chips, vending_machine_profit_cookies, vending_machine_profit_beverages]
            

            print('You lost ${amount} after {days} day(s). You failed to complete your objective. However, you learned the concept of reselling snacks through a vending machine.'.format(amount=abs(total_vending_machine_profit-money_spent_market), days=final_days))
            print('******************')
            for i in information:
                index = information.index(i)
                if index == 0:
                    print('Name of Vending Machine Owner:  ' + i)
                if index == 1:
                    print('Days played in Vending Machine Simulator: ' + str(i))
                if index == 2:
                    print('Budget Remaining: ' + str(i))
                if index == 3:
                    print('Money Spent: ${num}'.format(num=i))
                if index == 4:
                    print('Money lost from chips: ${num}'.format(num=i))
                if index == 5:
                    print('Money lost from cookies/candies: ${num}'.format(num=i))
                if index == 6:
                    print('Money lost from beverages: ${num}'.format(num=i))

            print('******************')
            exit()

    else:
        number_of_days -= 1
        print('Days remaining: {days}'.format(days=number_of_days))
        print('****************************')
        market()

vending_machine_sim()
