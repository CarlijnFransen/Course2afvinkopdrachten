#
# geschreven ubuntu
# Auteur: Carlijn Fransen
import re

class DNA:
           

        
    def __init__(self, fasta):
        self.geefBestand(fasta)
       
    def geefBestand(self,fasta):
        self.fasta =  fasta

    def setDNA(self):
        bestand = open(self.fasta)
        self.headers = []
        self.seqs = []
        seq=''

        for line in bestand:
            if '>'  in line:
                line = line.replace('\n','')
                self.headers.append(line)
                if len(seq) != 0:
                    seq += ' '
            
            else:
                line = line.replace('\n','')
                seq += line

        self.seqs = seq.split(' ') 

        print(self.headers)
        print(self.seqs)
                    
    def checkDNA(self):
        #dna = ''
        dna = self.seqs[self.indgroot]
        result =  True
        for line in dna:
            if '>' not in line:
                line = line.replace('\n','')
        
                x = re.search("[^ATCGN]", dna)
                if x:
                    result = True
        if result is True:
            print('Uw sequentie is DNA')
        else:
            print('Uw sequentie is geen DNA')
                                  
            
        

    def getDNA(self):
        return self.sequentie

    def getTranscript(self):
        
        transcript = ''

        for x in self.seqs[self.indgroot]:
            if x == 'A':
                transcript += 'U'        
            if x == 'T':
                transcript += 'A'
            if x == 'G':
                transcript += 'C'          
            if x == 'C':
                transcript += 'G'
        return transcript
    
    def getLength(self):
        return len(self.seqs)

    def gcPercentage(self):
        self.gcl = []
        for i in self.seqs:
            g = i.count('G')
            c = i.count('C')
            t =len(i)
            #print(t)
            gc = c + g
            #print(gc)
            print(t)
            a = gc/t
            b = a * 100
            #print('gc percenage is: ')
            self.gcl.append(b)
        return self.gcl
    
    def maxPrinten(self):
        self.indgroot = self.gcl.index(max(self.gcl))
        #print(self.indgroot)
        print(self.checkDNA())
        print('index = ',self.indgroot)
        print('lengte : ', self.getLength())
        print('transcript :','\n' , self.getTranscript())
        
        #print('gc% = ' self.groot)
        

appel = DNA('test2.fa')
appel.setDNA()
#appel.getTranscript()
appel.gcPercentage()
appel.maxPrinten()
