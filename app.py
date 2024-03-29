from model import Product, Category, Manage
from flask import *
import mlab
import cloudinary
from cloudinary import uploader
mlab.connect()
app = Flask(__name__)

cloudinary.config(
    cloud_name='nikefanboy',
    api_key="218223287849854",
    api_secret="etOBypj_IV0WiUXsKG2d89HvIkY"
)


@app.route('/')
def index():
    products = Product.objects.all()
    return render_template('index.html', products=products)


@app.route("/product/<id>")
def shoe_info(id):
    product = Product.objects.get(id=id)
    return render_template('product-detail.html', product=product)


@app.route("/category/<cate_name>")
def category(cate_name):
    products = Product.objects(cate_name=cate_name)
    return render_template('cate_info.html', products=products)


@app.route('/admin/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template("admin_upload.html")
    else:
        file = request.files.getlist('image')[0]
        # upload image cloudinary
        img_cloud = uploader.upload(file)
        img_link = img_cloud['url']

        name = request.form['name']
        code = request.form['code']
        price = request.form['price']
        detail = request.form['detail']
        cate_name = request.form['cate_name']

        product = Product(image=img_link, name=name, code=code,
                          cate_name=cate_name, price=price, detail=detail)
        product.save()

        return redirect(url_for('index'))


# @app.route('customer_manage', methods=['GET', 'POST'])
# def manage():
#     if request.method == "GET":
#         return render_template("customer_manage.html")
#     elif request.method == "POST":
#
#         form = request.form
#         customer_name = form['customer_name']
#         customer_phone = form['customer_phone']
#         customer_email = form['customer_email']
#         customer_address = form['customer_address']
#         customer_payments = form['customer_payments']
#
#         new_customer = manage(customer_name=customer_name,
#                               customer_phone=customer_phone,
#                               customer_email=customer_email,
#                               customer_address=customer_address,
#                               customer_payments=customer_payments)
#         new_customer.save()
#         return redirect(url_for('customer_manage'))


if __name__ == '__main__':
    app.run(debug=True)
