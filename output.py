# Naman Gupta
# output.py
# namangupta9@gmail.com | namang@umich.edu


def print_initial_blockchain(blockchain_in):

    print "\nInitial Blockchain"
    print "-----------------------------------------"
    print blockchain_in[-1]
    print "\n"


def print_blockchain(blockchain_in):

    print "Blockchain Height: " + str(blockchain_in[-1].block_height)
    print "-----------------------------------------"

    if len(blockchain_in) > 0:
        print blockchain_in[-1]

        if len(blockchain_in) > 1:
            print blockchain_in[-2]

            if len(blockchain_in) > 2:
                print blockchain_in[-3]


def print_transaction_pool(transactions_in):

    print "Transaction Pool: "
    print "-----------------"

    index = 0
    for t in transactions_in:
        print "Priority " + str(index) + ": " + str(t[-1])
        index += 1

    print "\n"