import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Wprowadz numer konta : "))
        self.name = input("Imie wlasciciela konta : ")
        self.type = input("Typ konta [B/O] : ")
        self.deposit = int(input("Wprowadz wartosc pocztkowa(>=500 dla Oszczednosci >=1000 dla Bierzacego"))
        print("\n\n\nKonto utworzono")
    
    def showAccount(self):
        print("Numer Konta : ",self.accNo)
        print("Imie wlasciciela : ", self.name)
        print("Typ konta",self.type)
        print("Stan konta : ",self.deposit)
    
    def modifyAccount(self):
        print("Numer Konta : ",self.accNo)
        self.name = input("Modyfikuj imie wlasciciela :")
        self.type = input("Modyfikuj typ konta :")
        self.deposit = int(input("Modyfikuj stan :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tSYSTEM BANKOWY")
    print("\t\t\t\t**********************")

    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("Nie znaleziono ionformacji")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Stan twojego konta to = ",item.deposit)
                found = True
    else :
        print("Brak danych")
    if not found :
        print("Konto nie istnieje")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Wprowadz kwote depozytu : "))
                    item.deposit += amount
                    print("Wprowadzono zmiany")
                elif num2 == 2 :
                    amount = int(input("Wrowadz kwote wyplaty : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("Nie mozesz wyplacic wiecej")
                
    else :
        print("Brak danych")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Wprowadz imie wlasciciela : ")
                item.type = input("Wprowadz typ kontae : ")
                item.deposit = int(input("Wprowadz kwote : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        

ch=''
num=0
intro()

while ch != 8:
    print("\tPULPIT")
    print("\t1. NOWE KONTO")
    print("\t2. KWOTA DEPOZYTU")
    print("\t3. KWOTA WYPLATY")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. WSZYSTKIE KONTA")
    print("\t6. ZAMKNIJ KONTO")
    print("\t7. ZMIEN KONTO")
    print("\t8. WYJSCIE")
    print("\tWybierz opcje (1-8) ")
    ch = input()
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tWprowadz numer konta : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tWprowadz numer konta  : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tWprowadz numer konta  : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tWprowadz numer konta  : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tWprowadz numer konta  : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tDziekuje za skorzystanie z naszych uslug")
        break
    else :
        print("Bledny wybor")
    
    ch = input("Wprowadz wybor : ")
    


    
    
    
    
    
    
    
    
    
    
