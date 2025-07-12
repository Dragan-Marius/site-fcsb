from flask import Flask, render_template, session, redirect, url_for, request
import json
import os

app = Flask(__name__)
app.secret_key='supersecretkey'

products = [
    {'id' : 1, 'name': 'Caseta De Directie', 'price':499, 'image':'casetadedirctie499.jpg'},
    {'id' : 2, 'name': 'Disc De Ambreiaj', 'price':145, 'image':'discdeambreiaj.jpg'},
    {'id' : 3, 'name': 'Filtru de Aer', 'price':89, 'image':'filtrudeaer89.jpg'},
    {'id' : 4, 'name': 'Filtru de Particule', 'price':1499, 'image':'filtrudeparticule1499.jpg'},
    {'id' : 5, 'name': 'Filtru de Motorina', 'price':119, 'image':'filtrumotorina119.jpg'},
    {'id' : 6, 'name': 'Placa de Presiune', 'price':300, 'image':'placadepresiune300.jpg'},
    {'id' : 7, 'name': 'Radiator Apa', 'price':1199, 'image':'radiatorapa1199.jpg'},
    {'id' : 8, 'name': 'Condesator', 'price':89, 'image':'condesator.jpg'},
]

def get_cart_item_count():
      cart=session.get('cart',{})
      return sum(cart.values())

@app.route('/')
def index():
        return render_template('index.html',products=products, cart_item_count=get_cart_item_count())

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
        cart=session.get('cart',{})
        cart[str(product_id)] = cart.get(str(product_id),0) + 1
        session['cart'] = cart
        return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart=session.get('cart',{})
    items = []
    total = 0;
    for pid, qty in cart.items():
        for p in products:
            if p['id'] == int(pid):
                    item=p.copy()
                    item['qty'] = qty
                    item['subtotal']= qty *p['price']
                    items.append(item)
                    total = total + item['subtotal']
    return render_template('cart.html', items=items, total=total, cart_item_count=get_cart_item_count())

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart= session.get('cart',{})
    items=[]
    total=0
    for pid, qty in cart.items():
          for p in products:
                if p['id']==int(pid):
                      item=p.copy()
                      item['qty']=qty
                      item['subtotal']=qty*p['price']
                      items.append(item)
                      total=total+item['subtotal']

    if request.method == 'POST':
        order = {
                'full_name' : request.form['full_name'],
                'email' : request.form['email'],
                'phone' :request.form['phone'],
                'address' : request.form['address'],
                'payment_method':request.form['payment_method'],
                'items':items,
                'total':total
        }
        print("---COMANDA NOUA---")
        for k, v in order.items():
              print(f"{k}:{v}")

        if not os.path.exists('order.json'):
                with open('order.json','w') as f:
                      json.dump([], f)
        with open('order.json','r+') as f:
                      data=json.load(f)
                      data.append(order)
                      f.seek(0)
                      json.dump(data,f,indent=4)
        session.pop('cart', None)
        return redirect(url_for('success'))
    return render_template('checkout.html', items=items, total=total, cart_item_count=get_cart_item_count())

@app.route('/increase/<int:product_id>')
def increase_qty(product_id):
      cart = session.get('cart', {})
      pid = str(product_id)
      cart[pid] = cart.get(pid,0)+1
      session['cart'] =  cart
      return redirect(url_for('cart'))

@app.route('/decrease/<int:product_id>')
def decrease_qty(product_id):
    cart = session.get('cart',{})
    pid= str(product_id)
    if pid in cart:
        if cart[pid] > 1:
            cart[pid] -= 1
        else:
            del cart[pid]
    session['cart']=cart
    return redirect(url_for('cart'))




@app.route('/contact')
def contact():
      return render_template('contact.html', cart_item_count=get_cart_item_count())

@app.route('/success')
def success():
      return render_template('success.html', cart_item_count=get_cart_item_count())

if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')