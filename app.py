from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/calculate',methods=['POST'])
def calculator():
    if request.method=='POST':
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if ops=='add':
            result=num1+num2
        if ops=='subtract':
            result=num1-num2
        if ops=='multiply':
            result=num1*num2
        if ops=='division':
            result=num1/num2 
    return render_template('home.html',result=result)
    #return render_template('home.html',result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)