from flask import (
    Flask,
    render_template,
    redirect, 
    url_for, request
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

#form action
@app.route('/sum_result', methods = ['POST'])
def sum_result():
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    result = str(n1 + n2)
    return 'Answer is : %s' % result

@app.route('/sum/', methods = ['POST', 'GET'])
def sum():
    return render_template('sum.html')
    # else:
    #     return render_template('login.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)