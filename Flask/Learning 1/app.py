from distutils.log import debug
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')

def welcome():
    return 'Ajay Satya'

@app.route('/members')

def members():
    return 'Ajay\nHarsha'

@app.route('/success/<int:score>')
def success(score):
    return 'He passed and scored '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'He failed and scored '+str(score)




@app.route('/results/<int:marks>')
def mark(marks):
    results=''
    if marks<35:
        results='fail'
    else:
        results='success'

    return redirect(url_for(results,score=marks))

    
    
    
    





if __name__=='__main__':
    app.run(debug=True)
