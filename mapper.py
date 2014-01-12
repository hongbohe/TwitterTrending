#!/usr/bin/python
import os,sys
import logging

import string


class wiki_pop:
     def __init__(self):
          
          self.logger_file = "wiki_log_mapper1.txt"
          self.forbid = set(('hi','hey','im','urs','ur','hav','didnt','tat','wen','1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'much', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us','u', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your'))
                 

     def initialize_logger(self):
          
         logging.basicConfig(filename=self.logger_file, level=logging.INFO)
         logging.info("Initialized logger")
         
     def mapper(self):
          #self.initialize_logger()
         
          #Mapper function for preprocessing
          #f=open('tweets_file','r')
          #output = open('output','a')
          for line in sys.stdin:
          #for line in f:
               try:
                    if not line:
                         #print "line was empty"
                         continue
                    word_list = line.split()
                    for word in word_list:
                         if word[0]=='@' or word[0:4]=="http" or word=="RT":
                              continue
                         out = word.translate(string.maketrans("",""), string.punctuation)
                         outword = out.strip()
                         if outword:
                              if outword.lower() not in self.forbid:
                                   print "%s\t1" % (outword.lower())
                                   #output.write(outword.lower()+"\t"+"1"+"\n")

               except:
                    continue
          #f.close()
          #output.close()
                                    
               
                    

                    
           
if __name__ == "__main__":
    wp_obj = wiki_pop()
    wp_obj.mapper() 
                

        
        
