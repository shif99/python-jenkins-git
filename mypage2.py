
from flask import Flask, render_template,jsonify,abort,request,redirect,url_for
#jsonify will convert object into a json
from model import db, save_data

app = Flask(__name__)  #

@app.route("/")
def welcome():
   product = db[0]# print first one only
   return render_template("product.html", product= product)
#app.run(port=4003)

@app.route("/api/products")
# see page http://127.0.0.1:4003/api/products
def products_api():
    return  jsonify(db)

@app.route("/api/products/<int:index>")
# page http://127.0.0.1:4003//api/products/1
#whichever index we give if we give one like above it will output second  product in product json
def products_api_by_index(index):
   try:
       product = db[index]
       return  jsonify(product)
   except IndexError:
       abort(404)

@app.route("/api/products/form",methods=["GET","POST"])
#reading input from html form ,so add modules like request,redirect,url_for
def add_new_product():
    if request.method == "POST":
       try:
           product ={"productId": request.form['productId'],
                     "productId": request.form['productNmae'],
                     "productId": request.form['Price'],
                     "productId": request.form['Rating'],
                     }
           # passing products with db.append(product)
           db.append(product)
           save_data()
       except IndexError:
           abort(404)
       return redirect(url_for("products_api_by_index", index=len(db) - 1))

    else:
        return render_template("add_product.html")

if __name__  == '   main  ':
    app.run(port=4003)



