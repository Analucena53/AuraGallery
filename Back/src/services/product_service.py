from src.database.db_phpMySql import get_connection
# from werkzeug.security import generate_password_hash
from src.models.product_model import  Product
# from werkzeug.security import generate_password_hash

class ProductService():
    @classmethod
    def get_product(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                # cursor.execute('SELECT * FROM product')
                cursor.callproc('sp_get_product')
                result = cursor.fetchall()
                # [Product.convert_desde_BD(fila) for fila in result]
                products_json = [{"id_product": row[0], "title_product": row[1], "image_product": row[2], "category_product": row[3], "description_product": row[4], "size_product": row[5], "price_product": row[6], "id_user_artistFK": row[7]} for row in result]
                print(result)
            connection.close()
            return products_json
        except Exception as ex:
            print(ex)
    @classmethod
    def post_product(cls, product_table:Product):
        try:
            connection  = get_connection()
            # id_product = product_table.id_product,
            # title_product = product_table.title_product,
            # image_product = product_table.image_product,
            # category_product = product_table.category_product,
            # description_product = product_table.description_product,
            # stock_product = product_table.stock_product,
            # price_product = product_table.price_product,
            # id_user_artistFK = product_table.user_artistFK
            with connection.cursor() as cursor:
                cursor.callproc('	sp_post_product', (
            #     sql = "INSERT INTO product(id_product, title_product, image_product, category_product, description_product, stock_product, price_product, id_user_artistFK) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            #     cursor.execute(sql, (
                    # product_table.id_product,
                    product_table.title_product,
                    product_table.image_product,
                    product_table.category_product,
                    product_table.description_product,
                    product_table.stock_product,
                    product_table.price_product,
                    product_table.user_artistFK
            ))  
            # connection.commit()
                    # cursor.execute("INSERT INTO product(id_product, title_product, image_product, category_product, description_product, stock_product, price_product, id_user_artistFK) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    #                (id_product,title_product,image_product,category_product,description_product,stock_product,price_product,user_artistFK))
                # cursor.callproc('	sp.post_product', (title_product,image_product,category_product,description_product,stock_product,price_product,id_user_artistFK))
            connection.commit()        
            print('Product added successfully')
        except Exception as ex:
                print(ex)
        finally:
            connection.close()
            return "Data base is close"
       
    # @classmethod
    # def patch_user(cls, user_table:User):
    #     try:
    #         connection  = get_connection()
    #         id_user = user_table.id_user
    #         name_user = user_table.name_user
    #         password_user = user_table.password_user
    #         user_typeFK = user_table.user_typeFK
            
    #         encriped_password = generate_password_hash(password_user, 'pbkdf2', 30)
            
    #         with connection.cursor() as cursor:
    #             # cursor.execute("UPDATE user SET  name_user = '{0}', password_user = '{1}', id_user_typeFK = {2}  WHERE user.id_user = {3}".format(name_user,password_user,user_typeFK,id_user))
    #             cursor.callproc('update_user', (id_user,name_user,encriped_password,user_typeFK))
    #             connection.commit()
    #             print('User updated successfully')
    #         connection.close()
    #         return "Data base is close"
    #     except Exception as ex:
    #         print(ex)
    # @classmethod
    # def delete_user(cls, id_user):
    #     try:
    #         connection  = get_connection()
    #         print(connection)
    #         with connection.cursor() as cursor:
    #             # cursor.execute('DELETE FROM user WHERE user.id_user = %s', (id_user)) 
    #             cursor.callproc('delete_user', (id_user,)) # Aqui uso otro metodo callproc para trabajar con procedimientos
    #             connection.commit()
    #         connection.close()
    #         return "Data base is close"
    #     except Exception as ex:
    #         print(ex)





