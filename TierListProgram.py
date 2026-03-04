def printtier(tiername,tieritems): #prints the tier name joined with the items of that tier
    print(tiername,'|', ', '.join(tieritems))

def addspace(l,name): #returns the extra number of spaces to make all tiers have equal distance to their items
    space = ''
    for i in range(l - len(name)):
        space += ' '
    return space

def maketierlist():
    tierlist=[] #list in which items tiers and items are added at the end of the function
    items=[] #list of all items the user wants to rank
    while True: #loops to collect all items the user wants to rank and adds them to items list; stops when input='stop'
        obj=input('Enter items (enter stop to stop): ').lower()
        if obj!='stop':
            items.append(obj)
        else:
            break
    print('All items: ', ', '.join(items)) #prints all items the user entered seperated by commas
    tier_s=[] #list for items in s tier
    tier_a=[] #list for items in a tier
    tier_b=[] #list for items in b tier
    tier_c=[] #list for items in c tier
    tier_d=[] #list for items in d tier
    tier_f=[] #list for items in f tier
    for item in items: #loops through the items list and adds them to each tier list based on the users input
        while True:
            itemtier = input('What tier is ' + item + '? (enter tier name): ').lower()
            if itemtier == 's':
                tier_s.append(item)
                break
            elif itemtier == 'a':
                tier_a.append(item)
                break
            elif itemtier == 'b':
                tier_b.append(item)
                break
            elif itemtier == 'c':
                tier_c.append(item)
                break
            elif itemtier == 'd':
                tier_d.append(item)
                break
            elif itemtier == 'f':
                tier_f.append(item)
                break
            else:
                print('Invalid Choice') #prints invalid choice if user does not enter 's', 'a', 'b', 'c', 'd', or 'f'

    while True: #gives the user the option to rename the tiers
        rename=input('Would you like to rename tiers? (enter yes or no): ').lower()
        if rename=='yes': #asks the user for a new name for each tier
            name1 = input('Enter rename for S tier: ')
            name2 = input('Enter rename for A tier: ')
            name3 = input('Enter rename for B tier: ')
            name4 = input('Enter rename for C tier: ')
            name5 = input('Enter rename for D tier: ')
            name6 = input('Enter rename for F tier: ')
            names=[name1,name2,name3,name4,name5,name6] #adds all user inputted names into a list
            x=0
            for name in names: #finds the tier name with the most characters | used to make each tier equidistant
                if len(name)>x:
                    x=len(name)
            #uses the printtier and addspace functions to print the tiers for the user to see
            printtier(name1+addspace(x,name1), tier_s)
            printtier(name2+addspace(x,name2), tier_a)
            printtier(name3+addspace(x,name3), tier_b)
            printtier(name4+addspace(x,name4), tier_c)
            printtier(name5+addspace(x,name5), tier_d)
            printtier(name6+addspace(x,name6), tier_f)
            break
        elif rename=='no': #uses just the printtier function to print the tiers for the user to see
            printtier('S', tier_s)
            printtier('A', tier_a)
            printtier('B', tier_b)
            printtier('C', tier_c)
            printtier('D', tier_d)
            printtier('F', tier_f)
            break
        else:
            print('Invalid Choice') #prints invalid choice if user does not enter 'yes' or 'no'
    #adds all the lists of items to the tierlist list
    tierlist.append(tier_s)
    tierlist.append(tier_a)
    tierlist.append(tier_b)
    tierlist.append(tier_c)
    tierlist.append(tier_d)
    tierlist.append(tier_f)
    return tierlist #returns the tierlist list

def reset(listoflists): #takes a list of lists and resets it
    for list in listoflists:
        list.clear()

def exit(): #prints a goodbye message
    print('Exiting, Goodbye!')

if __name__ == '__main__':
    emptylist1=[] #creates an empty list used for comparison
    emptylist2=[[],[],[],[],[],[]] #creates an empty list of lists used for comparison
    lastlist=[] #creates an empty list
    while True: #prints menu options and takes a users input on which action to preform
        print('\nMake a Tier List')
        print('a. make new tier list')
        print('b. reset tier list')
        print('c. exit menu')
        choice=input('Enter Choice: ').lower()
        if choice=='a':
            if lastlist==emptylist1 or lastlist==emptylist2: #only allows the user to make a new tier list if the last one is empty
                lastlist=maketierlist() #sets last list equal to tierlist list, the return of the maketierlist function
            else:
                print('Please Reset List First')
        elif choice=='b':
            reset(lastlist) #uses the reset function on the lastlist list
            print('Tier List Reset')
        elif choice=='c':
            exit() #runs the exit function
            break
        else:
            print('Invalid Choice') #prints invalid choice if the user does not enter 'a', 'b', or 'c'
#small change