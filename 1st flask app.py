from flask import Flask

app= Flask(__name__)
@app.route('/')
def first_page():
    return "Navigate Through My Profile"

@app.route('/My Profile')
def my_info():
    return "I am Akshay Bhasme."

@app.route('/Experience')
def exp():
    return "I am 27 yo and have 4 years of experience."

if __name__=='__main__':
    app.run(debug=True, port=5000)