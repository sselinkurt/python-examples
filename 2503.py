#tekrarlanan kelimelerin frekansini veren program yazilacak,  constructor olacak
#space e gore bakilacak


class myClass():
    def __init__(self, myfile=""):
        #http://www.gutenberg.org/files/1342/1342-0.txt
        f = open("test_1.txt", "r") #islem yapmak istedigimiz dosyayi aciyor
        myContent = f.read() #file i okuyor
        mySentences = myContent.split(".")  #split ayristirma komutu. Noktaya gore ayristiriyor.mySentences bir liste
        self.myWords = []
        for sentence in mySentences:
            Words_In_The_sentence = sentence.split(" ") #space e gore ayristir 
            for word_1 in Words_In_The_sentence:
                self.myWords.append(word_1)
        #print(self.myWords)  test teki butun kelimeleri gosteriyor

        self.my_frequency_1()
        self.write_frequency_1()
        self.my_frequency_2()
        self.write_frequency_2()
    
    def my_frequency_1(self):
        self.frequency_list_1 = {}
        for word in self.myWords:
            if(word in self.frequency_list_1):
                self.frequency_list_1[word] += 1
            else:
                self.frequency_list_1[word] = 1

    def write_frequency_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1+" "+str(self.frequency_list_1[word_1]))
    
    def my_frequency_2(self): #ard arda tekrar eden iki kelime icin
        self.frequency_list_2 = {}
        for i in range(len(self.myWords)-1):
            w_1, w_2 = self.myWords[i], self.myWords[i+1]
            if((w_1, w_2) in self.frequency_list_2):
                self.frequency_list_2[(w_1, w_2)] += 1
            else:
                self.frequency_list_2[(w_1, w_2)] = 1
    
    def write_frequency_2(self):
        for w_1 in self.frequency_list_2:
            print(str(w_1)+""+str(self.frequency_list_2[w_1]))

a=myClass()


