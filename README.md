
# Poker
Normally the player cannot see the cards in the deck and so must use probability to decide which cards to discard. In this problem, we imagine that the poker player is psychic and knows which cards from the deck will make best hand.He or she can only draw two cards from the deck but the real challenge is to identify desired cards We are writing a program which advises the player  to which cards to discard and which card to select so as to maximize the value of the resulting hand.
Input and Output

Input will consist of a series of lines, each containing the initial five cards in the hand then the first five cards on top of the deck. Each card is represented as a two-character code. The first character is the face-value (A=Ace, 2-9, T=10, J=Jack, Q=Queen, K=King) and the second character is the suit (C=Clubs, D=Diamonds, H=Hearts, S=Spades). Cards will be separated by single spaces. Each input line will be from a single valid deck, that is there will be no duplicate cards in each hand and deck.


# Sample Input

AH 2C 9S AD 3C QH KS JS JD KD

# Sample Output

Hand : ['AH', '2C', '9S', 'AD', '3C'] Deck : ['QH', 'KS', 'JS', 'JD', 'KD'] : Best Hand :  Two Pair
Cards at position : 2 & 5 In deck make Two pair
