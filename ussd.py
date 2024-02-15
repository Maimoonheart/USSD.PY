user = input('USSD Code:')
if user != '*312#':
    print("invalid USSD code")
else:
    print('''
          1.Data balance
          2.Data plans
          3.Borrow Credit or Recharge
          4.Gift data
          5.Social bundles
         ''')
    
    user = input('Choice:')
    if user == '1':
        print('You do not have any active data bundle.')
    elif user == '2':
        print('''
                1.100mb for 100naira
                2.200mb for 200naira 
                3.1gb f0r 350naira
             ''')
    elif user == '3':
        print('Pay your outstanding debt')
    elif user == '4':
        print('''
                1.Data plans
                2.Social bundles
                ''')
    elif user == '5':
        print('''
                1.Whatsapp
                2.Facebooka
                3.Twitter
                4.All social bundles
                ''')
    else:
        print('Seems you have given the wrong input')
    