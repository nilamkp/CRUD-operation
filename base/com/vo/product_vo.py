from  base import db

class ProductVO(db.Model):
    __tablename__ = 'product_table'
    product_id = db.Column('product_id',db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column('product_name',db.String(255),nullable=False)
    product_discription = db.Column('product_description', db.String(255),nullable=False)
    product_image_name = db.Column('product_image_name', db.String(255), nullable=False)
    product_image_path = db.Column('product_image_path', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'product_id':self.product_id,
            'product_name':self.product_name,
            'product_discription':self.product_discription,
            'product_image_name':self.product_image_name,
            'product_image_path':self.product_image_path
        }

db.create_all()