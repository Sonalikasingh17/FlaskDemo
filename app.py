# This is a simple Flask application setup.
# Flask app routing


from flask import Flask,render_template,request,redirect,url_for,jsonify

## # Create a Flask application instance

app=Flask(__name__)

@app.route('/')  # Define the route for the root URL
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index') # Define the route for the index page
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')   # Define the route for success message
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>') # Define the route for fail message
def fail(score):
    return "the person has failed and the score is "+str(score)


@app.route('/calculate',methods=['POST','GET'])  # Define the route for calculating average marks
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks)) # Redirect to success or fail route based on the result


        return render_template('result.html',results=average_marks)
    
@app.route('/api',methods=["POST"])  # Define an API endpoint
def calculate_sum():
    data = request.get_json()

    a_val = float(dict(data)["a"])
    b_val = float(dict(data)["b"])
    result = a_val + b_val
    return jsonify({"result": result})

    # Uncomment the following lines if you want to handle JSON data
    # if not data:
    #     return jsonify({"error": "No data provided"}), 400
    # a = data.get('a')
    # b = data.get('b')
    # if a is None or b is None:
    #     return jsonify({"error": "Missing 'a' or 'b' in data"}), 400
    # result = a + b



if __name__ == "__main__":    # Run the Flask application
    app.run(debug=True)



