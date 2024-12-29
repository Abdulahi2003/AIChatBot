#description: this program simulates a chatbot

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#download the punkt package
nltk.download('punkt', quiet='true')

#get article
article = Article('https://stacker.com/space/15-basic-physics-concepts-help-you-understand-our-world')
article.download()
article.parse()
article.nlp()
corpus = article.text

#print the article text
#print(corpus)

#tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)
#print(sentence_list)

#function to return random greeting response to users greeting
def greeting_response(text):
    text = text.lower()
    
    bot_greeting = ['hello', 'hi', 'hey', 'hola', 'greetings', 'howdy', 'good morning', 'good evening', 'good afternoon']
    users_greeting = ['hello', 'hi', 'hey', 'hola', 'wassup', 'howdy', 'good morning', 'good evening', 'good afternoon']
    
    for word in text.split():
        if word in users_greeting:
            return random.choice(bot_greeting)
        
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index
        
#create bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response +' '+ sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
        
    if response_flag == 0:
        bot_response = bot_response+' '+"I apologize, I don't understand."
        
    sentence_list.remove(user_input)
    
    return bot_response

print('Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer your queries about Physics. If you want to exit, type bye.')

exit_list = ['exit', 'see you later', 'bye', 'quite', 'break']

while(True):
    user_input = input() 
    if user_input.lower() in exit_list:
        print('Doc Bot: Chat with you later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: '+greeting_response(user_input))
        else:
            print('Doc Bot: '+bot_response(user_input))
    
    
    
            
            
            
    