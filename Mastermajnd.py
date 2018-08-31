from tkinter import *
import random


class Mastetermind:
    def __init__(self, window):
        self.window = window
        window.title("MASTERMAJND")

        self.secret_number = self.ranoomy() #lista z wylosowaną liczbą
        self.entry_number = 0
        self.guess = 0
        self.guess_counter = 0
        self.list = [] #lista z twoim zgadnieciem
        self.hint = []
        self.oszust=self.fraud()

        self.message = "Guess the number : "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(window, textvariable=self.label_text)

        self.message = "LEGENDA : x-nie trafiles,  i-odpowiednia liczba na zlej pozycji,  o-trafienie! "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.legend = Label(window, textvariable=self.label_text)

        self.guess_text = StringVar()

        self.guess_text1 = StringVar()
        self.message1=""

        self.guess_text1 = StringVar()
        self.guess_text2 = StringVar()
        self.guess_text3 = StringVar()
        self.guess_text4 = StringVar()
        self.guess_text5 = StringVar()
        self.guess_text6 = StringVar()
        self.guess_text7 = StringVar()
        self.guess_text8 = StringVar()
        self.guess_text9 = StringVar()
        self.guess_text10 = StringVar()
        self.guess_text11 = StringVar()
        self.guess_text12 = StringVar()

        self.label1 = Label(window, textvariable=self.guess_text1).grid(row=6,column=0)
        self.label2 = Label(window, textvariable=self.guess_text2).grid(row=7,column=0)
        self.label3 = Label(window, textvariable=self.guess_text3).grid(row=8,column=0)
        self.label4 = Label(window, textvariable=self.guess_text4).grid(row=9,column=0)
        self.label5 = Label(window, textvariable=self.guess_text5).grid(row=10,column=0)
        self.label6 = Label(window, textvariable=self.guess_text6).grid(row=11,column=0)
        self.label7 = Label(window, textvariable=self.guess_text7).grid(row=12,column=0)
        self.label8 = Label(window, textvariable=self.guess_text8).grid(row=13,column=0)
        self.label9 = Label(window, textvariable=self.guess_text9).grid(row=14,column=0)
        self.label10 = Label(window, textvariable=self.guess_text10).grid(row=15,column=0)
        self.label11 = Label(window, textvariable=self.guess_text11).grid(row=16,column=0)
        self.label12 = Label(window, textvariable=self.guess_text12).grid(row=17,column=0)

        self.listofmessages=[self.guess_text1,self.guess_text2,self.guess_text3,self.guess_text4,self.guess_text5,self.guess_text6,self.guess_text7,self.guess_text8,self.guess_text9,self.guess_text10,self.guess_text11,self.guess_text12]
        self.listoflabels = [self.label1, self.label2, self.label3,self.label4, self.label5, self.label6,self.label7, self.label8, self.label9,self.label10, self.label11, self.label12]

        self.hint_text1 = StringVar()
        self.hint_text2 = StringVar()
        self.hint_text3 = StringVar()
        self.hint_text4 = StringVar()
        self.hint_text5 = StringVar()
        self.hint_text6 = StringVar()
        self.hint_text7 = StringVar()
        self.hint_text8 = StringVar()
        self.hint_text9 = StringVar()
        self.hint_text10 = StringVar()
        self.hint_text11 = StringVar()
        self.hint_text12 = StringVar()

        self.hint1 = Label(window, textvariable=self.hint_text1).grid(row=6,column=1)
        self.hint2 = Label(window, textvariable=self.hint_text2).grid(row=7,column=1)
        self.hint3 = Label(window, textvariable=self.hint_text3).grid(row=8,column=1)
        self.hint4 = Label(window, textvariable=self.hint_text4).grid(row=9,column=1)
        self.hint5 = Label(window, textvariable=self.hint_text5).grid(row=10,column=1)
        self.hint6 = Label(window, textvariable=self.hint_text6).grid(row=11,column=1)
        self.hint7 = Label(window, textvariable=self.hint_text7).grid(row=12,column=1)
        self.hint8 = Label(window, textvariable=self.hint_text8).grid(row=13,column=1)
        self.hint9 = Label(window, textvariable=self.hint_text9).grid(row=14,column=1)
        self.hint10 = Label(window, textvariable=self.hint_text10).grid(row=15,column=1)
        self.hint11 = Label(window, textvariable=self.hint_text11).grid(row=16,column=1)
        self.hint12 = Label(window, textvariable=self.hint_text12).grid(row=17,column=1)

        self.hints_text = [self.hint_text1,self.hint_text2,self.hint_text3,self.hint_text4,self.hint_text5,
                           self.hint_text6,self.hint_text7,self.hint_text8,self.hint_text9,self.hint_text10,
                           self.hint_text11,self.hint_text12]

        self.hints = [self.hint1, self.hint2, self.hint3, self.hint4, self.hint5, self.hint6, self.hint7,
                             self.hint8, self.hint9, self.hint10, self.hint11, self.hint12]

        vcmd = window.register(self.validate)

        self.entry = Entry(window, validate="key", validatecommand=(vcmd, '%P'))

        self.button1 = Button(window, text="GUESS", command=self.guess_number, state=DISABLED)

        self.button2 = Button(window, text="Reset", command=self.reset)

        self.button3 = Button(window, text="OSZUST!", command=self.bla)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W + E)
        self.legend.grid(row=4, column=0, columnspan=3, sticky=W + E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W + E)
        self.button1.grid(row=0, column=2)
        self.button2.grid(row=0, column=3)
        self.button3.grid(row=0, column=5)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.guess = None
            return True
        try:
            guess = int(new_text)
            if self.checkif6(guess) == True:
                return True
            else:
                return False
        except ValueError:
            return False



        #####  LOSOWANIE LICZBY

    def k6(self):
        return random.randint(1, 6)

    def ranoomy(self):
        list=[self.k6() for i in range(4)]
        #print(list)
        return list

    #### OGRANICZENIE DO WPISYWANIA TYLKO 1 2 3 4 5 6
    def checkif6(self, number):
        b=number
        self.button1.configure(state=DISABLED)
        if(len(str(number))>4):
            self.button1.configure(state=NORMAL)
        if(len(str(number))==1):
            if (1<=b<=6):
                return True
            else:
                return False
        if(len(str(number))==2):
            a=b%10
            if (1<=a<=6):
                return True
            else:
                return False
        if(len(str(number))==3):
            a=b%100
            a=a%10
            if (1<=a<=6):
                return True
            else:
                return False

        if(len(str(number))==4):
            a=b%1000
            a=a%100
            a=a%10
            if (1<=a<=6):
                self.guess=number
                self.button1.configure(state=NORMAL)
                return True
            else:
                return False
            
        


    def toList4(self,number):
        kroki = [1000, 100, 10, 1]
        self.list=[]
        a = 1
        b = number
        for i in kroki:
            a = b % i
            b = b - a
            self.list.append(b / i)
            b = a

        #print(self.list)


    def guess_number(self):
        self.guess_text.set(self.guess)
        # self.listoflabels.pop[self.guess_counter].textvariable=self.guess_text
        print("TWOJ ZGAD to :", self.guess)
        #print("A STRING TO: ", len(str(self.guess)))
        #print("KALNETER :", self.guess_counter)
        #print("sekret lista :", self.secret_number)
        self.listofmessages[self.guess_counter].set(str(self.guess))
        #self.guess_text1.set(self.message1)
        #self.guess_text1.set(self.guess)
        self.toList4(self.guess)
        self.compare()
        if(self.guess_counter==12):
            self.loser()
            exit
        self.entry.delete(0, 'end')
        self.button1.configure(state=DISABLED)



        #print("TWOJA LISTA -> ",self.list)
        #print("SIKRET LISTA -> ",self.secret_number)

    #POROWNAJ DWIE LIST I ZROB LADNE GUI I TO W SUMIE TYLE
    def compare(self):
        self.hint=["x","x","x","x"]
        #test=self.secret_number[:]
        test=[x for x in self.secret_number]
        #print("TETTSTSTETETS ->",test)
        i=0
        j=0
        goodposition=0
        badposition=0
        everythingischanging=0
        index=[0,0,0,0]
        while(i<4):
            if(self.secret_number[i]==self.list[i]):
                goodposition=goodposition+1
                index[i]=1
                test[i]='p'
                self.list[i]='x'
            i = i + 1

        #print("INDEKSY i -> ",index)
        #print(self.list,"WYZER")
        #print(test,"WYZER test")
        i=0
        while(i<4):
            everythingischanging=badposition
            while(j<4):
                if(self.list[i]==test[j]):
                    badposition=badposition+1
                    index[j]=1
                j = j + 1
                if(everythingischanging != badposition):
                    break
            i=i+1
            j=0
        #print("BAD = ", badposition)
        #print("GUD = ",goodposition)
        i=0
        j=0
        #print("INDEKSY po j -> ",index)

        if(self.oszust==0):
            while(goodposition!=i):
                self.hint[i]="o"
                i=i+1
            while(badposition!=0):
                self.hint[i]="i"
                i=i+1
                badposition=badposition-1
        else:
            self.badhints()


        print("HINT -> ",self.hint)
        self.hints_text[self.guess_counter].set(self.hint)
        self.guess_counter += 1
        if(goodposition==4):
            self.winner()

    def reset(self):
        self.secret_number = self.ranoomy()  # lista z wylosowaną liczbą
        self.entry_number = 0
        self.guess = 0
        self.guess_counter = 0
        self.list = []  # lista z twoim zgadnieciem
        self.hint = []
        self.oszust=self.fraud()
        for i in self.listofmessages:
           i.set("")
        #self.listofmessages=[i.set("") for i in self]
        for i in self.hints_text:
            i.set("")
        self.entry.delete(0, 'end')
        self.button1.configure(state=DISABLED)


    def winner(self):
        self.window.withdraw()
        okno = Tk()
        okno.geometry("180x80")
        okno.title("WIENER")
        okno.grab_set()
        label1 = Label(okno, text="WIENER !",font=("Helvetica", 16)).grid(column=2, row=1, sticky=W)
        button1=Button(okno,text="NOWA GRA",command=lambda: self.endingbutton(okno)).grid(row=3,column=2)

    def feelsbad(self):
        self.window.withdraw()
        okno = Tk()
        okno.geometry("270x80")
        okno.title("PRZEPRASZAM :(")
        okno.grab_set()
        label1 = Label(okno, text="TAK TAK.. OSZUKIWALEM !",font=("Helvetica", 16)).grid(column=2, row=1, sticky=W)
        button1=Button(okno,text="NOWA GRA",command=lambda: self.endingbutton(okno)).grid(row=3,column=2)


    def endingbutton(self,bla):
        self.reset()
        bla.destroy()
        self.window.update()
        self.window.deiconify()

    def loser(self):
        okno = Tk()
        okno.geometry("180x80")
        okno.title("LUSER !!!!")
        label1 = Label(okno, text="LUSER !",font=("Helvetica", 16)).grid(column=2, row=1, sticky=W)
        button1 = Button(okno, text="NOWA GRA", command=lambda: self.endingbutton(okno)).grid(row=3, column=2,columnspan=3)

    def terefere(self):
        self.window.withdraw()
        okno = Tk()
        okno.geometry("180x80")
        okno.title("TEREFERE !!!!")
        label1 = Label(okno, text="TEREFEREFE !",font=("Helvetica", 16)).grid(column=2, row=1, sticky=W)
        button1 = Button(okno, text="NOWA GRA", command=lambda: self.endingbutton(okno)).grid(row=3, column=2,columnspan=3)
        
    def fraud(self):#SZANSA NA OSZUSTWO TO 1/10
        rand=random.randint(0,10)
        print("sekret lista :", self.secret_number)
        if(rand==4):
            print("OSZUKUJE CIE")
            return 1
        else:
            print("NIE OSZUKUJE CIE")
            return 0

    def badhints(self):
        answers=["x","o","i"]
        i=0
        self.hint=[answers[random.randint(0, 2)] for i in range(4)]

    def bla(self):
        if(self.oszust==1):
            self.feelsbad()
        else:
            self.terefere()


root = Tk()
gui = Mastetermind(root)
root.mainloop()
