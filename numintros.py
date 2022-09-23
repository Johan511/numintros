import re
class NumIntros:
    regex_new_num = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{2}, [0-9]{2}:[0-9]{2} - \+91 ")
    regex_joined = re.compile("joined using this group's invite link")
    regex_intro = re.compile("NAMELESS \s*\t*\n*AND \s*\t*\n*SHAMELESS")
    def __init__(self, inPath , outPath):
        self.inFile = open(inPath, "r")
        self.outFile = open(outPath, "w")
        self.num_intros = {}
        self.state = 'searching for start'


    def read(self):
        self.lines = self.inFile.readlines()
        for self.line_index in range(len(self.lines) - 2):
            if(re.match(NumIntros.regex_new_num, self.lines[self.line_index]) ):
                self.state = 'found start'
                self.found_start(self.get_key())
        print(self.num_intros)

        
    def found_start(self, key):
        self.state = 'searching for tag'
        i = 1
        while(self.state != 'found start'):
            if(re.search(NumIntros.regex_intro,  
            self.lines[self.line_index  + i].upper()) != None and self.state == 'searching for tag'):
                if(key not in self.num_intros):
                    self.num_intros[key] = 1
                else:
                    self.num_intros[key] +=1
                self.state = 'searching for start'
            if(re.match(NumIntros.regex_new_num,  
            self.lines[self.line_index + i].upper()) != None):
                self.state = 'found start'
            i= i+1
        self.line_index = self.line_index + i


    def get_key(self):
        s = ""
        i = 21
        while(len(s) < 10):
            if(self.lines[self.line_index][i] <= '9' and self.lines[self.line_index][i] >= '0'):
                s = s+ self.lines[self.line_index][i]
            i = i+1      
        return s

    def write(self):
        for i in self.num_intros:
            self.outFile.write(f'@{i} : {self.num_intros[i]}\n')


if __name__ == '__main__':
    n = NumIntros(inPath = './WhatsApp Chat with IITM CS22.txt', outPath = './out.txt')
    n.read()
    n.write()