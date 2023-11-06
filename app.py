from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/calculate',methods=['POST'])
def calculator():
    if request.method == 'POST':
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        operation=request.form.get('submit')
        result = None
        
        if 'add' in request.form:
            result = num1 + num2
            
        elif 'subtract' in request.form:
            result = num1 - num2
        return render_template('home.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)