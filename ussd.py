# user = input('USSD Code:')
# if user != '*312#':
#     print("invalid USSD code")
# else:
#     print('''
#           1.Data balance
#           2.Data plans
#           3.Borrow Credit or Recharge
#           4.Gift data
#           5.Social bundles
#          ''')
    
    # user = input('Choice:')
    # if user == '1':
    #     print('You do not have any active data bundle.')
    # elif user == '2':
    #     print('''
    #             1.100mb for 100naira
    #             2.200mb for 200naira 
    #             3.1gb f0r 350naira
    #          ''')
    # elif user == '3':
    #     print('Pay your outstanding debt')
    # elif user == '4':
    #    
    # elif user == '5':
    #     print('''
    #             1.Whatsapp
    #             2.Facebooka
    #             3.Twitter
    #             4.All social bundles
    #             ''')
    # else: print('''
    #             1.Data plans
    #             2.Social bundles
    #             ''')
    #     print('Seems you have given the wrong input')


        #   USSD USING FUNCTION 

def landing_page():
    user = input('USSD Code:')
    if user.strip() != '*312#':
        print("invalid USSD code")
    else:
     user_choice = (input('''
          1.Data balance
          2.Data plans
          3.Borrow Credit or Recharge
          4.Gift data
          5.Social bundles
       Option: '''))
    def Data_balance():
     print('Dear customer,You do not have any active data bundle.')
    def Data_plans():
     print('''
      1.100mb for 100naira
      2.200mb for 200naira 
      3.1gb f0r 350naira
      ''')
    def Borrow_credit():
        print('Pay your outstanding debt')
    def Gift_data():
      print('''
      1.Data plans
      2.Social bundles
      ''')   
    def Social_bundles():
       print('''
      1.Data plans
      2.Social bundles
      ''')
    
    if  user_choice.strip() == '1':
      Data_balance()
    elif user_choice.strip() == '2':
     Data_plans()
    elif user_choice.strip() == '3':
     Borrow_credit()
    elif user_choice.strip() == '4':
     Gift_data()
    elif user_choice.strip() == '5':
     Social_bundles()
    else:
     choice = (input('Invalid input,press 1 to go back to home and # exit.'))
     if choice == '1':
      landing_page()
     else:
       exit()
landing_page()



   





