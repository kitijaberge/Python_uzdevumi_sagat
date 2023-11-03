"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) kādus ciparus mēs zinām? parasti arābu cipari, kuri ir 10(decimāla skaitīšanas sistēma)
2) kādus romiešu ciparus ziniet? I, V, C, M, D, L, X             21 = XXI
3) kas ir klase? programmēšanas struktūra, kas var definēt datu uzvedību un metodes
4) klase sastāv no konstruktora/destruktora un metodēm(iekšējām funkcijām)
5) kādas datu struktūras zinām? 
 - list-saraksts    a="" (tukš saraksts)
 - arry - masīvs
 - dict- vārdnīca   a={}  a=dict()    tukša vārdnīca

***Vārdnīca ir tabula ar divām kolonnām, kollonai nav nosaukuma,
 viena kolonna ir atslēga otra kolonna ir tās vērtība
"""

class BBB:
    # jādefinē konstruktors
    def __init__(self):    #iekavās parametri- iekšējās klases mainīgie: self-klasē iekšā, ārā ir konstruktprs
        self.roma_sk={    #iekšējais mainīgais, vērtība
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
 }     # Definējām klases konstruktoru __init__

 #Definē nepieciešamās metodes
def to_roman(self, num):   #kad izsauc no klases, janodod skaitlis tpe ir num
        result = ""     # tukšs saraksts
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True):   #IR CIKLS sorted- sakartots saraksts roma sk. items nozime ka pārskatīs katru elementu un pirma vertiba ar indeksu 0
            while num >= value:   # pievienoju skaitli tukšam sarakstam
                result += numeral 
                num -= value  #num=num-value
        return result 
       
   #piemērs
        skaitlis=21
   #define objekru
        kk=BBB()
   #jaunajam objektam jaizsauc klases metode
     romiesu=kk.to_roman(skaitlis)

   #noformet izdruku
   print(f"{skaitlis} ar romiesu cipariem ir {romiesu}.")