from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fname_form = request.form['first_name']
    lname_form = request.form['last_name']
    id_form = request.form['student_id']
    strawberry_form = request.form['strawberry']
    raspberry_form = request.form['raspberry']
    apple_form = request.form['apple']
    total_fruits = int(strawberry_form) + int(raspberry_form) + int(apple_form)
    print(f"Charging {fname_form} {lname_form} for {total_fruits} fruits")
    return render_template("checkout.html", strawberry_form = strawberry_form, fname_form=fname_form,lname_form=lname_form,id_form=id_form,raspberry_form=raspberry_form,apple_form=apple_form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    