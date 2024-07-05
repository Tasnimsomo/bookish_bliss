from flask import Blueprint, render_template, request, session
from your_app.models import Product, CartItem

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart')
def view_cart():
    cart_items = session.get('cart', [])
    cart_total = sum(item.product.price for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, cart_total=cart_total)

@cart_blueprint.route('/cart/add', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    product = Product.query.get(product_id)
    if product:
        cart = session.get('cart', [])
        cart_item = CartItem(product=product)
        if cart_item not in cart:
            cart.append(cart_item)
            session['cart'] = cart
    return 'Added to cart!'

@cart_blueprint.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    product_id = request.form['product_id']
    cart = session.get('cart', [])
    new_cart = [item for item in cart if item.product.id != product_id]
    session['cart'] = new_cart
    return 'Removed from cart!'