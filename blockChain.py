import hashlib

import json

reward = 500.0



genesisBlock = {

   'previousHash': '',

   'index': 0,

   'transaction': [],

   'nonce': 23

}

blockchain = [genesisBlock]

openTransactions = []

owner = 'Guru'



def hashBlock(block):
   
   ## Hashing using the hashlib algo
   ## jason.dump convets block dictionary into jason string
   ## encode() converts the string into redable UTF-8 string for hashlib
   return hashlib.sha256(json.dumps(block).encode()).hexdigest()

##---------------------------------------------------------------

def validProof(transactions, lastHash, nonce):

   guess = (str(transactions) + str(lastHash) + str(nonce)).encode()

   guesshash = hashlib.sha256(guess).hexdigest()

   print(guesshash)
   
   ## Hash is only accepted if the first two letters are zeros (make mining difficult)
   return guesshash[0:2] == '00'


## Proof of work. 
def pow():

   lastBlock = blockchain[-1]
   
   ## Hashing the last block
   lastHash = hashBlock(lastBlock)

   nonce = 0
   
   ## This runs till validProff returns TRUE.
   while not validProof(openTransactions, lastHash, nonce):

       nonce += 1

   return nonce

##---------------------------------------------------------------


##def getLastValue():

##    return(blockchain[-1])


## Metadata of the transaction is appended to openTransactions
def addValue(recipient, sender=owner, amount=1.0):

   transaction = {'sender': sender,

   'recipient': recipient,

   'amount': amount}

   openTransactions.append(transaction)


##--------------------------------------------

## This is where we mine blocks.
## 
def mineBlock():

   lastBlock = blockchain[-1]

   hashedBlock = hashBlock(lastBlock)
   
   ## Extracting nonce
   nonce = pow()

   rewardTransaction = {

           'sender': 'Guru',

           'recipient': owner,

           'amount': reward

       }

   openTransactions.append(rewardTransaction)
   
   ## New metadata
   block = {

       'previousHash': hashedBlock,

       'index': len(blockchain),

       'transaction': openTransactions,

       'nonce': nonce

   }

   blockchain.append(block)


##----------------------------------------------------------

def getTransactionValue():

   tRecipient = input('Enter the recipient of the transaction: ')

   tAmount = float(input('Enter your transaction amount '))
   
   ## Returns a 'tuple'
   return tRecipient, tAmount



def getUserChoice():

   userInput = input("Enter your choice here: ")

   return userInput
##----------------------------------------------------------
def printBlock():

   for block in blockchain:

       print("Here is your block")

       print(block)
##-----------------------------------------------------------
while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for mining a new block')

   print('Choose 3 for printing the blockchain')

   print('Choose anything else to quit')

   userChoice = int(getUserChoice())

   

   if userChoice == 1:

       txData = getTransactionValue()

       recipient, amount = txData

       addValue(recipient, amount=amount)

       print(openTransactions)



   elif userChoice == 2:

       mineBlock()


   elif userChoice == 3:

       printBlock()
   

   else:

       break

