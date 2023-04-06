from base import db
from base.com.vo.product_vo import ProductVO


class ProductDAO:
    def insert_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        product_vo_list = ProductVO.query.all()
        return product_vo_list

    def delete_product(self, product_vo):
        product_vo_list = ProductVO.query.get(product_vo.product_id)
        db.session.delete(product_vo_list)
        db.session.commit()

    def edit_product(self, product_vo):
        product_vo_list = ProductVO.query.filter_by(product_id=product_vo.product_id).all()
        return product_vo_list

    def update_product(self, product_vo):
        db.session.merge(product_vo)
        db.session.commit()
