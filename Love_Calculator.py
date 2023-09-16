def love_calculator():
    your_name = input("Enter your Name: ")
    crush_name = input("Enter your Crush Name: ")
    true = ['T', 'R', 'U', 'E']
    love = ['L', 'O', 'V', 'E']
    true_count = 0
    love_count = 0
    for i in range(4):
        # true count
        true_count += your_name.upper().count(true[i]) + crush_name.upper().count(true[i])
        # love count
        love_count += your_name.upper().count(love[i]) + crush_name.upper().count(love[i])
    
    # compute the result   
    result = str(true_count) + str(love_count)
       
    print(f"Your Love Score {result}")
  
# call function              
love_calculator()   