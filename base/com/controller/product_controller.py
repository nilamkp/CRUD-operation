import os

from flask import *
from werkzeug.utils import secure_filename

from base import app
from base.com.dao.product_dao import ProductDAO
from base.com.vo.product_vo import ProductVO

product_Folder = "base/static/product/"
app.config['PRODUCT_FOLDER'] = product_Folder


@app.route("/admin/load_product")
def load_product():
    return render_template('/admin/product.html')


@app.route('/admin/insert_product', methods=["POST"])
def insert_product():
    product_name = request.form.get('productname')
    product_discription = request.form.get('productdiscription')
    product_image = request.files.get('productimage')
    product_image_name = secure_filename(product_image.filename)
    product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
    product_image.save(os.path.join(product_image_path, product_image_name))

    product_vo = ProductVO()
    product_dao = ProductDAO()

    product_vo.product_name = product_name
    product_vo.product_discription = product_discription
    product_vo.product_image_name = product_image_name
    product_vo.product_image_path = product_image_path.replace("base", "..")

    product_dao.insert_product(product_vo)
    return redirect('admin/view_product')


@app.route('/admin/view_product')
def view_product():
    product_dao = ProductDAO()
    product_vo_list = product_dao.view_product()
    return render_template('admin/viewproduct.html', data=product_vo_list)


@app.route('/admin/delete_product')
def delete_product():
    product_vo = ProductVO()
    product_dao = ProductDAO()
    product_id = request.args.get('product_id')
    product_vo.product_id = product_id
    product_dao.delete_product(product_vo)
    return redirect('admin/view_product')


@app.route('/admin/edit_product')
def edit_product():
    product_vo = ProductVO()
    product_dao = ProductDAO()
    product_id = request.args.get('product_id')
    product_vo.product_id = product_id
    product_vo_list = product_dao.edit_product(product_vo)
    # print(">>>>>>>> image name = ",product_vo_list.product_image_name,">>>>>> image path",product_vo_list.product_image_path,">>>>>>> product name",product_vo_list.product_name)
    # print(">>>>>>>>",product_vo_list[0])
    return render_template('/admin/editproduct.html', data=product_vo_list)


@app.route('/admin/update_product', methods=["POST"])
def update_product():
    product_id = request.form.get('product_id')
    product_name = request.form.get('productname')
    product_discription = request.form.get('productdiscription')
    product_image = request.files.get('productimage')
    # product_image_name = secure_filename(product_image.filename)
    # product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
    # product_image.save(os.path.join(product_image_path, product_image_name))

    product_vo = ProductVO()
    product_dao = ProductDAO()

    product_vo.product_id = product_id
    product_vo.product_name = product_name
    product_vo.product_discription = product_discription
    product_vo.product_image = product_image
    # product_vo.product_image_path = product_image_path.replace("base","..")

    product_dao.update_product(product_vo)
    return redirect('admin/view_product')
