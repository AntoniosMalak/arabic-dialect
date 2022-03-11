import os
import re
import pickle
import warnings
import numpy as np
from tashaphyne import normalize
warnings.filterwarnings('ignore')
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, request, json, render_template

# Create flask app
app = Flask(__name__)

# Load pkl model
os.chdir(".")
path = os.path.abspath(os.curdir) + '\\Model\\log_model.pkl'
model = pickle.load(open(path, 'rb'))

#dict = {
#    'EG':0, 'PL':1, 'KW':2, 'LY':3, 'QA':4, 'JO':5, 'LB':6, 'SA':7, 'AE':8, 'BH':9,
#    'OM':10, 'SY':11, 'DZ':12, 'IQ':13, 'SD':14, 'MA':15, 'YE':16, 'TN':17
#}

dict = {
    0:'EG', 1:'PL', 2:'KW', 3:'LY', 4:'QA', 5:'JO', 6:'LB', 7:'SA', 8:'AE', 9:'BH',
    10:'OM', 11:'SY', 12:'DZ', 13:'IQ', 14:'SD', 15:'MA', 16:'YE', 17:'TN'
}

labels = ['EG', 'PL', 'KW', 'LY', 'QA', 'JO', 'LB', 'SA', 'AE', 'BH', 'OM', 'SY', 
          'DZ', 'IQ', 'SD', 'MA', 'YE', 'TN']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    
    text = list(request.form.values())[0]
    
    #preprocessing text
    pre_text = preprocessing_text(text)
    

    # making prediction for DL model
    padded  = get_padded(pre_text)
    pred = model.predict(padded )
    dl_output =  labels[np.argmax(pred)]
    #return render_template('index.html', prediction_text = f'Your country is {output}')

    # making prediction for log model
    prediction = model.predict(get_tfidf(pre_text))
    log_output = dict[prediction[0]]

    log_output = f'Your country with log_model is {log_output}'
    dl_output = f'Your country with dl_model is {dl_output}'
    return render_template('index.html', prediction_text1 = log_output, prediction_text2 = dl_output)


def cleaning(text): 
    newtext = re.sub('([@A-Za-z0-9_])|[^\w\s]|#|http\S+|', '', text).replace('\n',' ').lstrip().rstrip()
    return re.sub(r'(.)\1+', r'\1', newtext)

def preprocessing_text(text):
    text = normalize.normalize_searchtext(text)
    return cleaning(text)

def get_tfidf(text):
    path = os.path.abspath(os.curdir) + '\\Model\\tfidf.pkl'
    tfidf = pickle.load(open(path, 'rb'))
    text_tfidf = tfidf.transform([text])
    return text_tfidf

def get_padded(text):
    com = [text]
    MAX_SEQUENCE_LENGTH = 361792
    path = os.path.abspath(os.curdir) + '\\Model\\tokenizer.pkl'
    tokenizer = pickle.load(open(path, 'rb'))
    seq = tokenizer.texts_to_sequences(com)
    text_padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
    return text_padded

if __name__ == "__main__":
    app.run(debug=True)