from flask import Flask 
  
app = Flask(__name__) 


@app.route('/<opt>/<a>/<b>') 
def calculator(opt, a, b):
    if opt == 'add':
        ans = float(a) + float(b)
        operation = '+'
    elif opt == 'sub':
        ans = float(a) - float(b)
        operation = '-'
    elif opt == 'mul':
        ans = float(a) * float(b)
        operation = '*'
    elif opt == 'div':
        if float(b) != 0:
            ans = float(a) / float(b)
            operation = '/'
        else:
            return 'Error: Division by zero!'
    else:
        return 'Error: Invalid operation!'
    
    return f'<h3>{a} {operation} {b} = {ans}</h3>'

@app.route('/')
def index():
    return 'Lab 9_4'
    
  
if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')