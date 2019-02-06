

"""#####################################################################################################################
# This is a simple game in which you will enter different combinations of card and it will tell you to winning situation
#####################################################################################################################"""


""""# This is the main input list which will took input from the user in the form of two character values
# First character is the suit
# 2nd Character is the face value
# Note: All the inputs will be store in a single list """
input_list = []

# statement is a String which will take string representation of hands and deck cards
statement = ""

# We are splitting main input list into different small string according to their suits
hearts_list, spades_list, clubs_list, diamonds_list = [], [], [], []

# face_value variable is the list which will store only the inputs suits values
face_value = []

# index variable store first and 2nd number of card in deck
index1 = 0
index2 = 0

# cards_values is the list which will store all the face values
cards_values = []

# Here we are counting the occurrence of suits values and storing them in corresponding variables
# We are making the 4 different lists each contain only type of suits
hearts_count, spades_count, diamonds_count, clubs_count = 0, 0, 0, 0


"""#####################################################################################################################
# suits_counter is the function which will count all same suits card and store the in a separate lists
#####################################################################################################################"""


def suits_counter(input_val):
    global hearts_count, spades_count, diamonds_count, clubs_count
    hearts_count, spades_count, diamonds_count, clubs_count = 0, 0, 0, 0
    del face_value[:]
    del cards_values[:]
    del hearts_list[:]
    del spades_list[:]
    del clubs_list[:]
    del diamonds_list[:]

    # Appending or separating suits and face values in separate lists
    for x in input_val:
        face_value.append(x[1])
        cards_values.append(x[0])
    for idx in range(len(face_value)):
        # Counting Hearts and storing in separate list
        if face_value[idx] == 'H':
            hearts_count += 1
            hearts_list.append(input_val[idx])

        # Counting Spades and storing in separate list
        elif face_value[idx] == 'S':
            spades_count += 1
            spades_list.append(input_val[idx])

        # Counting Diamonds and storing in separate list
        elif face_value[idx] == 'D':
            diamonds_count += 1
            diamonds_list.append(input_val[idx])

        # Counting Clubs and storing in separate list
        elif face_value[idx] == 'C':
            clubs_count += 1
            clubs_list.append(input_val[idx])


"""******************************************************************************************
# list_number_asg method will take list of face values and return its with assign number 
******************************************************************************************"""


def list_number_asg(card_val):
    for j in range(len(card_val)):

        # Changing values of non integer values in list with integer values
        if 'A' in card_val:
            index = card_val.index('A')
            card_val[index] = 14
        if 'K' in card_val:
            index = card_val.index('K')
            card_val[index] = 13
        if 'Q' in card_val:
            index = card_val.index('Q')
            card_val[index] = 12
        if 'J' in card_val:
            index = card_val.index('J')
            card_val[index] = 11
        if 'T' in card_val:
            index = card_val.index('T')
            card_val[index] = 10
    return card_val


"""*********************************************************************************************
# face_value_count function will count the number of occurrences of different card 
# and store them in a global list
**********************************************************************************************"""
# Cards_count_list will store number of occurrence of same cards in a list
cards_count_list = []


def face_values_count(card_ls):
    if 'A' in card_ls:
        cards_count_list.append(card_ls.count('A'))
    if 'K' in card_ls:
        cards_count_list.append(card_ls.count('K'))
    if 'Q' in card_ls:
        cards_count_list.append(card_ls.count('Q'))
    if 'J' in card_ls:
        cards_count_list.append(card_ls.count('J'))
    if 'T' in card_ls:
        cards_count_list.append(card_ls.count('T'))
    if '9' in card_ls:
        cards_count_list.append(card_ls.count('9'))
    if '8' in card_ls:
        cards_count_list.append(card_ls.count('8'))
    if '7' in card_ls:
        cards_count_list.append(card_ls.count('7'))
    if '6' in card_ls:
        cards_count_list.append(card_ls.count('6'))
    if '5' in card_ls:
        cards_count_list.append(card_ls.count('5'))
    if '4' in card_ls:
        cards_count_list.append(card_ls.count('4'))
    if '3' in card_ls:
        cards_count_list.append(card_ls.count('3'))
    if '2' in card_ls:
        cards_count_list.append(card_ls.count('2'))


"""*********************************************************************************************
# The royal_ flush function will take input argument a list of same suits and return true / false
**********************************************************************************************"""


def royal(suit_list):
    if len(suit_list) == 5 or len(suit_list) > 5:
        card_val = []

        # Appending all the cards number of same suits in separate list
        for j in hearts_list:
            card_val.append(j[0])
        result = all(elem in card_val for elem in ['A', 'K', 'Q', 'J', 'T'])
        return True if result else False


def royal_flush(input_val):

    # check all different suits values and them to suits_counter function
    suits_counter(input_val)
    if royal(hearts_list):
        return True
    elif royal(spades_list):
        return True
    elif royal(diamonds_list):
        return True
    elif royal(clubs_list):
        return True
    else:
        return False


"""*********************************************************************************************
# straight_flush function will take input argument a list of same suits and return true / false
**********************************************************************************************"""


def st_flush(suit_ls):

    # check if suits values are equal or greater then 5
    if len(suit_ls) == 5 or len(suit_ls) > 5:
        card_val = []

        # Appending all the cards number of same suits in separate list
        for j in suit_ls:
            card_val.append(j[0])

        # Now changing values of non integer values in list with integer values
        card_val = list_number_asg(card_val)

        # Converting all the String values into Integer
        for o in range(len(card_val)):
            y = int(card_val[o])
            card_val[o] = y

        # Sorting list into Descending Order
        card_val.sort(reverse=True)
        hit = 0

        # Checking consecutive number in list and increasing values of hit Variable
        for o in range(len(card_val)-1):
            if card_val[o]-1 == card_val[o+1]:
                hit += 1
            else:
                hit = 0

        # if we have 4 or greater than 4 consecutive hit return True else False
        return True if hit == 4 or hit > 4 else False
    else:
        return False


def straight_flush(input_val):

    # check all different suits values and passing them to suits_counter function
    suits_counter(input_val)
    if st_flush(hearts_list):
        return True
    elif st_flush(spades_list):
        return True
    elif st_flush(diamonds_list):
        return True
    elif st_flush(clubs_list):
        return True
    else:
        return False


"""*********************************************************************************************
# for_of_a_kind is the function which will take cards list as argument and return True / False
**********************************************************************************************"""


def four_of_a_kind(input_val):

    # removing all values from cards_value list
    del cards_values[:]

    # appending new values to the list
    for x in input_val:
        cards_values.append(x[0])

    # removing number of cards from number list
    del cards_count_list[:]

    # face_values_counter will assign new values to the global count list card_count_list
    face_values_count(cards_values)
    for j in range(len(cards_count_list)):
        if cards_count_list[j] == 4:
            return True
    return False


"""*********************************************************************************************
# This function will take cards list as argument and will return true / false
**********************************************************************************************"""


def full_house(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])
    del cards_count_list[:]
    face_values_count(cards_values)

    # Calling function to count number of same cards and storing it into new list
    if len(cards_count_list) == 0:
        face_values_count(cards_values)

    # Coping global list into local list for alterations
    card_cnt_ls = cards_count_list[:]

    # Finding Maximum occurrence of a card
    try:
        if max(card_cnt_ls) == 3:

            # Removing maximum value card from count list
            card_cnt_ls.remove(max(card_cnt_ls))
            loop_count = len(card_cnt_ls)

            # Checking next card occurrence in count list
            for j in range(len(card_cnt_ls)):
                if card_cnt_ls[j] == 2 or card_cnt_ls[j] == 3:
                    break
                else:
                    loop_count -= 1

            # Returning true if a 3 and 2 duplicate cards found otherwise false
            return False if loop_count == 0 else True
        else:
            return False

    except ValueError:
        print("Kindly Enter Correct Values !!!! ")
        exit()


"""*********************************************************************************************
# This function will take list of different suits as argument and return true / false
**********************************************************************************************"""


def flush_check(ls):
    # count the different suits list length and returning true / false
    return True if len(ls) == 5 or len(ls) > 5 else False


def flush(input_val):

    # checking all different suits values and passing them to suits_counter function
    suits_counter(input_val)
    if flush_check(hearts_list):
        return True
    elif flush_check(spades_list):
        return True
    elif flush_check(diamonds_list):
        return True
    elif flush_check(clubs_list):
        return True
    else:
        return False


"""*********************************************************************************************
# This function will take cards values ad argument and return true / false
**********************************************************************************************"""


def straight(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])
    del cards_count_list[:]
    # Calling list_number_asg method to convert non integer values in to integer
    card_val = list_number_asg(cards_values)

    # Casting strings values to integer
    try:
        for o in range(len(card_val)):
            y = card_val[o]
            y = int(y)
            card_val[o] = y
    except ValueError:
        print("Kindly Enter Correct Values")
        exit()

    # sorting list
    card_val.sort()
    hit_count = 0

    # Checking series of connective five cards
    for o in range(len(card_val)-1):
        if card_val[o]+1 == card_val[o+1]:
            hit_count += 1
            if hit_count == 4:
                return True
        else:
            hit_count = 0
    return False


"""*********************************************************************************************
# Three of Kind function will take list of card values as argument and return True / False
**********************************************************************************************"""


def three_of_a_kind(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])
    del cards_count_list[:]
    face_values_count(cards_values)
    for j in range(len(cards_count_list)):
        if cards_count_list[j] == 3:
            return True
    return False


"""*********************************************************************************************
# The Two pair function will take values list as argument and returns true / false
**********************************************************************************************"""


def two_pair(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])
    del cards_count_list[:]
    face_values_count(cards_values)

    # Coping global list into local list for alterations
    cards_cnt_ls = cards_count_list[:]

    # Finding Maximum occurrence of a card
    if max(cards_cnt_ls) == 2:

        # Removing maximum value card from count list
        cards_cnt_ls.remove(max(cards_cnt_ls))
        loop_count = len(cards_cnt_ls)

        # Checking next card occurrence in count list
        for j in range(len(cards_cnt_ls)):
            if cards_cnt_ls[j] == 2 or cards_cnt_ls[j] > 2:
                break
            else:
                loop_count -= 1
        return False if loop_count == 0 else True
    else:
        return False


"""*********************************************************************************************
# pair function will take cards list as argument and return true / false
**********************************************************************************************"""


def pair(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])
    del cards_count_list[:]

    # Calling function to count number of same cards and storing it into new list
    face_values_count(cards_values)

    # Coping global list into local list for alterations
    cards_cnt_ls = cards_count_list[:]

    # Finding Maximum occurrence of a card and returning true / false
    return True if max(cards_cnt_ls) == 2 else False


"""*********************************************************************************************
# The High card function will take cards Values as argument and return true / false
**********************************************************************************************"""


def high_card(input_val):
    del cards_values[:]
    for x in input_val:
        cards_values.append(x[0])

    # Calling list_number_asg method to convert non integer values in to integer
    card_val = list_number_asg(cards_values)

    # Casting strings values to integer
    for o in range(len(card_val)):
        y = card_val[o]
        y = int(y)
        card_val[o] = y
    return card_val.index(max(card_val))


def main():
    global input_list, statement
    print("Kindly Enter input in this form (5D 2S 4H TD 3D 7S 8H AH JD KH)")
    item = raw_input("Enter your cards : ")
    item = item or "5D 2S 4H TD 3D 7S 8H AH JD KH"
    try:
        int(item)
        print("Kindly enter Correct input !!!")
        exit()
    except ValueError:
        pass
    input_list = item.split()

    # splitting user input into two different lists Hand and Deck
    hand_list = input_list[:5]
    deck_list = input_list[5:]

    # assigning output format string to the global variable
    statement = "Hand : "+str(hand_list)+" Deck : "+str(deck_list)+" : Best Hand : "
    checker = False

    # Checking royal flush
    if royal_flush(input_list):

        # checking every combination with deck cards
        for j in range(len(deck_list)):
            for k in range(j, len(deck_list)-1):

                # making now list with five member from hand and 2 member from deck
                li = hand_list[:]
                li.append(deck_list[j])
                li.append(deck_list[k+1])
                if royal_flush(li):
                    print (statement+"Royal Flush")
                    print("card at position : "+str(j+1)+" & "+str(k+2)+"In deck make Royla flush ")
                    checker = True
                    break

    # Checking Straight flush
    if checker is False:
        if straight_flush(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if straight_flush(li):
                        print (statement + " Straight Flush")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make Straight flush ")
                        checker = True
                        break
                    else:
                        pass

    # Checking Four of a kind
    if checker is False:
        if four_of_a_kind(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list) - 1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k + 1])
                    if four_of_a_kind(li):
                        print (statement + " Four Of A Kind")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make four Of A Kind ")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking Full House
    if checker is False:
        if full_house(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if full_house(li):
                        print (statement+" Full House")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make Full House")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking Straight Flush
    if checker is False:
        if flush(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if flush(li):
                        print (statement+" Flush")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make Flush")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking Straight Hand
    if checker is False:
        if straight(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if straight(li):
                        print (statement+" Straight")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make Straight")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking Three of a kind
    if checker is False:
        if three_of_a_kind(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if three_of_a_kind(li):
                        print (statement + " Three of a Kind")
                        print("card at position : "+str(j+1)+" & "+str(k+2)+" In deck make Three of a Kind")
                        checker = True
                        break
                if checker is True:
                    break

    # checking Two pairs
    if checker is False:
        if two_pair(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list)-1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k+1])
                    if two_pair(li):
                        print (statement + " Two Pair")
                        print("Cards at position : "+str(j+1)+" & "+str(k+2)+" In deck make Two pair")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking Pair
    if checker is False:
        if pair(input_list):
            for j in range(len(deck_list)):
                for k in range(j, len(deck_list) - 1):
                    li = hand_list[:]
                    li.append(deck_list[j])
                    li.append(deck_list[k + 1])
                    if pair(li):
                        print (statement + " Pair")
                        print("Cards at position : "+str(j+1)+" & "+str(k+2)+" In deck make Pair")
                        checker = True
                        break
                if checker is True:
                    break

    # Checking High Card
    if checker is False:
        print (statement + " High Card")
        card_index = high_card(input_list)
        card_index = int(card_index)
        print(card_index)
        if card_index > 5:
            print ("High card : "+str(deck_list[card_index-5])+" is At position in deck : "+str(card_index-4))
        else:
            print("High card : "+str(hand_list[card_index]) + " is At position in deck : " + str(card_index-4))


main()
