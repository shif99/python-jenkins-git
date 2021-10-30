
from flask import Flask, render_template,jsonify,abort,request,redirect,url_for
from model import db, save_data

app = Flask(__name__)  

@app.route("/")
def welcome():
   product = db[0]# print first one only
   return render_template("product.html", product= product)

@app.route("/api/products")
def products_api():
    return  jsonify(db)

@app.route("/api/products/<int:index>")
def products_api_by_index(index):
   try:
       product = db[index]
       return  jsonify(product)
   except IndexError:
       abort(404)

@app.route("/api/products/form",methods=["GET","POST"])
def add_new_product():
    if request.method == "POST":
       try:
           product ={"productId": request.form['productId'],
                     "productId": request.form['productNmae'],
                     "productId": request.form['Price'],
                     "productId": request.form['Rating'],
                     }
        
           db.append(product)
           save_data()
       except IndexError:
           abort(404)
       return redirect(url_for("products_api_by_index", index=len(db) - 1))

    else:
        return render_template("add_product.html")




