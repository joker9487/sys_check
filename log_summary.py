import json
import logging
class LogSummary:
    def __init__(self):
        self.counts={}
        self.skipped = 0
    def add_files(self,path) :
        for line in read_lines(path):
            self.add(line)  

    def add(self,line):
        if (line.startswith("[") and "]" in line ):
            level = line[1:line.index("]")] 
            self.counts[level]=(self.counts.get(level,0)+1)
        else :
            self.skipped+=1
            return 

    def total(self):
        return sum(self.counts.values())
    
    def save(self, path):
        with open(path,"w",encoding="utf-8")as conf:
            json.dump(self.counts,conf,ensure_ascii=False,indent=2)

def read_lines(path):
    list_return=[]
    try:
        with open(path, 'r',encoding="utf-8") as f:
            for line in f :
                s=line.strip()
                if s:
                    list_return.append(s)
        return list_return
    except FileNotFoundError:
        logging.error(f"找不到檔案:{path}")
        return list_return