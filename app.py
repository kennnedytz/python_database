from flask import Flask, render_template, url_for, redirect, request
from connection import session
from models import Product

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':  
        name = request.form['name']
        price = request.form['price']

        our_product = Product(name=name, price=price)
        session.add(our_product)
        session.commit()

        return redirect(url_for('product'))  # Redirect to the product listing after submission

    return render_template('index.html')

@app.route('/product') 
def product():
    products = session.query(Product).all()  
    return render_template('products.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
