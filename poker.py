

"""#####################################################################################################################
# This is a simple game in which you will enter different combinations of card and it will tell you to winning situation
#####################################################################################################################"""


""""# This is the main input list which will took input from the user in the form of two character values
# First character is the suit
# 2nd Character is the face value
# Note: All the inputs will be in a single list """
# input list 
input_list = []

# We are splitting main input list into different small string according to their suits
hearts_list, spades_list, clubs_list, diamonds_list = [], [], [], []

# face_value variable is the list which will store only the inputs suits values
face_value = []

# cards_values is the list which will store all the face values
cards_values = []

# Here we are counting the occurrence of suits values and storing them in corresponding variables
# We are making the 4 different lists each contain only type of suits
hearts_count, spades_count, diamonds_count, clubs_count = 0, 0, 0, 0


def initial_fun():
    global hearts_count, spades_count, diamonds_count, clubs_count
    for x in input_list:
        face_value.append(x[1])
        cards_values.append(x[0])
    for idx in range(len(face_value)):

        # Counting Hearts and storing in separate list
        if face_value[idx] == 'H':
            hearts_count += 1
            hearts_list.append(input_list[idx])

        # Counting Spades and storing in separate list
        elif face_value[idx] == 'S':
            spades_count += 1
            spades_list.append(input_list[idx])

        # Counting Diamonds and storing in separate list
        elif face_value[idx] == 'D':
            diamonds_count += 1
            diamonds_list.append(input_list[idx])

        # Counting Clubs and storing in separate list
        elif face_value[idx] == 'C':
            clubs_count += 1
            clubs_list.append(input_list[idx])


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
cards_count_list = []


def face_values_count(card_ls):
    if 'A' in card_ls:
        cards_count_list.append(card_ls.count('A'))
    if 'K' in card_ls:
        cards_count_list.append(card_ls.count('K'))
    if 'Q' in card_ls:
        cards_count_list.append(card_ls.count('Q'))
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


def royal_flush(suit_ls):
    # check if suits values are equal or greater then 5
    if len(suit_ls) == 5 or len(suit_ls) > 5:
        card_val = []
        # Appending all the cards number of same suits in separate list
        for j in suit_ls:
            card_val.append(j[0])
        result = all(elem in card_val for elem in ['A', 'K', 'Q', 'J', 'T'])
        return True if result else False
    else:
        return False


"""*********************************************************************************************
# straight_flush function will take input argument a list of same suits and return true / false
**********************************************************************************************"""


def straight_flush(suit_ls):

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


"""*********************************************************************************************
# for_of_a_kind is the function which will take cards list as argument and return True / False
**********************************************************************************************"""


def four_of_a_kind(card_val):
    for j in range(len(card_val)):
        if card_val.count(card_val[j]) == 4:
            return True
    return False


"""*********************************************************************************************
# This function will take cards list as argument and will return true / false
**********************************************************************************************"""


def full_house():
    # Calling function to count number of same cards and storing it into new list
    if len(cards_count_list) == 0:
        face_values_count(cards_values)

    # Coping global list into local list for alterations
    card_cnt_ls = cards_count_list[:]

    # Finding Maximum occurrence of a card
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


"""*********************************************************************************************
# This function will take list of different suits as argument and return true / false
**********************************************************************************************"""


def flush(ls):
    # count the different suits list length and returning true / false
    return True if len(ls) == 5 or len(ls) > 5 else False


"""*********************************************************************************************
# This function will take cards values ad argument and return true / false
**********************************************************************************************"""


def straight(card_val):

    # Calling list_number_asg method to convert non integer values in to integer
    card_val = list_number_asg(card_val)

    # Casting strings values to integer
    for o in range(len(card_val)):
        y = card_val[o]
        y = int(y)
        card_val[o] = y

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


def three_of_kind(card_val):

    # Calling list_number_asg method to convert non integer values in to integer
    card_val = list_number_asg(card_val)

    # Casting strings values to integer
    for o in range(len(card_val)):
        y = card_val[o]
        y = int(y)
        card_val[o] = y

    # Sorting list in descending order
    card_val.sort(reverse=True)
    for j in range(len(card_val)):
        return True if card_val.count(card_val[j]) == 3 else False


"""*********************************************************************************************
# The Two pair function will take values list as argument and returns true / false
**********************************************************************************************"""


def two_pair(card_ls):

    # Calling function to count number of same cards and storing it into new list
    if len(cards_count_list) == 0:
        face_values_count(card_ls)

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


def pair(card_ls):

    # Calling function to count number of same cards and storing it into new list
    if len(cards_count_list) == 0:
        face_values_count(card_ls)

    # Coping global list into local list for alterations
    cards_cnt_ls = cards_count_list[:]

    # Finding Maximum occurrence of a card and returning true / false
    return True if max(cards_cnt_ls) == 2 else False


"""*********************************************************************************************
# The High card function will take cards Values as argument and return true / false
**********************************************************************************************"""


def high_card(card_val):

    # Calling list_number_asg method to convert non integer values in to integer
    card_val = list_number_asg(card_val)

    # Casting strings values to integer
    for o in range(len(card_val)):
        y = card_val[o]
        y = int(y)
        card_val[o] = y
    return input_list[card_val.index(max(card_val))]


def main():
    global input_list
    print("Kindly Enter input in this form (TH JH QC QD QS QH KH 9H 2S 6S)")
    item = ""
    try:
        item = raw_input("Enter your cards : ")
    except ValueError:
        print("Kindly Enter Correct Values !!!! ")
    li = item.split()
    input_list = li[:]
    initial_fun()
    if royal_flush(hearts_list):
        print (str(input_list) + " : Best Hand : " + "Royal Flush of Hearts")
    elif royal_flush(spades_list):
        print (str(input_list) + " : Best Hand : " + "Royal Flush of Spades")
    elif royal_flush(clubs_list):
        print (str(input_list) + " : Best Hand : " + "Royal Flush of Clubs")
    elif royal_flush(diamonds_list):
        print (str(input_list) + " : Best Hand : " + "Royal Flush of Diamonds")
    elif straight_flush(hearts_list):
        print (str(input_list) + " : Best Hand : " + "Straight Flush of Hearts Cards")
    elif straight_flush(spades_list):
        print (str(input_list) + " : Best Hand : " + "Straight Flush of Hearts Cards")
    elif straight_flush(clubs_list):
        print (str(input_list) + " : Best Hand : " + "Straight Flush of Hearts Cards")
    elif straight_flush(diamonds_list):
        print (str(input_list) + " : Best Hand : " + "Straight Flush of Hearts Cards")
    elif four_of_a_kind(cards_values):
        print (str(input_list) + " : Best Hand : " + "Four of a kind")
    elif full_house():
        print (str(input_list) + " : Best Hand : " + "Full House")
    elif flush(hearts_list):
        print (str(input_list) + " : Best Hand : " + "Flush of Hearts")
    elif flush(spades_list):
        print (str(input_list) + " : Best Hand : " + "Flush of Spades")
    elif flush(clubs_list):
        print (str(input_list) + " : Best Hand : " + "Flush of clubs")
    elif flush(diamonds_list):
        print (str(input_list) + " : Best Hand : " + "Flush of diamonds")
    elif straight_flush(input_list):
        print (str(input_list) + " : Best Hand : " + "Straight")
    elif three_of_kind(cards_values):
        print(str(input_list) + " : Best Hand : " + "Three of A Kind")
    elif two_pair(cards_values):
        print (str(input_list) + " : Best Hand : " + "Two Pairs")
    elif pair(cards_values):
        print(str(input_list) + " : Best Hand : " + "Pair")
    else:
        print (str(input_list) + " : Best Hand : " + "High Card : ")


main()
