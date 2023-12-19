import psycopg2 as pg
from models import User, Good


class Database:
    connection = None

    @staticmethod
    def connect():
        try:
            Database.connection = pg.connect(
                host='localhost',
                database='pet_shop',
                port=5432,
                user='postgres',
                password='1111'
            )
        except Exception as e:
            print("Something went wrong.")
            print(e)

    @staticmethod
    def disconnect():
        Database.connection.close()

    @staticmethod
    def get_user(login: str, password: str):
        query = ("SELECT  Users.Id,"
                 " Users.Name,"
                 " Users.Password,"
                 " Users.Login, "
                 " Roles.Id "
                 "FROM Users "
                 "JOIN Roles ON Users.RoleId = Roles.Id "
                 f" WHERE Users.Login = '{login}' AND Users.Password = '{password}';")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None

        user = User(*result)

        return user

    @staticmethod
    def get_good(title: str):
        query = ("SELECT  g.Id, "
                 "g.Title, "
                 "f.Naming "
                 "FROM Firms f "
                 f"JOIN Goods g ON g.FirmId = f.Id AND g.Title = '{title}'")

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return Good(result[0], result[1], result[2], None, None)

    @staticmethod
    def get_user_profile(login: str):
        query = f"SELECT * FROM Users WHERE Login = '{login}';"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    @staticmethod
    def get_user_coupons(login: str):
        user = Database.get_user_by_login(login)

        if user is None:
            return None

        query = (f"SELECT u.Name AS User,"
                 f" c.Id AS CouponId, "
                 f"c.Sale "
                 f"FROM Coupons c JOIN Users u ON u.CouponId = c.Id AND u.Name = {user.name};")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_user_goods(login: str):
        user = Database.get_user_by_login(login)

        if user is None:
            return None

        query = (f"SELECT u.Name,"
                 f" g.Id As GoodId,"
                 f" g.Title AS Good,"
                 f" cog.Title AS Category"
                 f" FROM CartsGoods cg "
                 f"JOIN Carts c ON cg.CartId = c.Id "
                 f"JOIN Users u ON c.UserId = u.Id AND u.Name = {user.name} "
                 f"JOIN Goods g ON cg.GoodId = g.Id LEFT JOIN CategoriesOfGood cog ON g.CategoryOfGoodId = cog.Id;")

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return result

    @staticmethod
    def get_goods_with_category():
        query = "SELECT  g.Id,"\
                 "  g.Title,"\
                 "  c.Title AS Category"\
                 " FROM Goods g  "\
                 "LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_firms():

        query = f"SELECT f.Id , f.Naming FROM Firms f;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_good_specific_category(category: str):

        query = (f"SELECT g.Id, g.Title, c.Title FROM Goods g  "
                 f"LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id WHERE c.Title = '{category}';")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_good_specific_name(name_good: str):

        query = (f"SELECT g.Id, g.Title, c.Title FROM Goods g  "
                 f"LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id WHERE g.Title = '{name_good}';")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    @staticmethod
    def get_clients_with_banned():
        query = "SELECT u.Id, u.Name, u.Login FROM Users u;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def ban_unban_client(login: str):
        login = Database.get_user_by_login(login)

        if login is None:
            return None

        query = f"UPDATE Users SET Banned = {str(not login.banned)} WHERE Id = {login.id}"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        Database.connection.commit()
        cursor.close()

        return not login.banned

    @staticmethod
    def get_actions():
        query = "SELECT " \
                "Actions.Name, Actions.DateTime, Users.Name " \
                "FROM Actions " \
                "JOIN Users ON Actions.UserId = Users.Id " \
                "ORDER BY Actions.DateTime DESC;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def edit_client_role(login: str):
        user = Database.get_user_by_login(login)

        if user is None:
            return False

        query = f"UPDATE Users SET RoleId = 2 WHERE Login = '{login}';"

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)
            return False

        return True

    @staticmethod
    def get_client_actions(login: str):
        if Database.get_user_by_login(login) is None:
            return None

        query = "SELECT " \
                "Actions.Name, Actions.DateTime FROM Actions " \
                "JOIN Users ON Actions.UserId = Users.Id " \
                f"WHERE Users.Login = '{login}' " \
                "ORDER BY Actions.DateTime DESC;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_user_role(login: str):
        user = Database.get_user_by_login(login)
        if user is None:
            return None

        query = "SELECT r.Id, u.Name, r.Name AS Role FROM Roles r " \
                f"JOIN Users u ON u.RoleId = r.Id AND u.Name = {user.name};"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    @staticmethod
    def get_user_by_login(login: str):
        query = "SELECT * FROM Users " \
                f"WHERE Users.Login = '{login}'" \
                f"AND (Users.RoleId = 1 OR Users.RoleId = 2);"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    @staticmethod
    def get_good_by_animal(animal_get: str):
        if animal_get is None:
            return None

        query = (f"SELECT g.Id, "
                 f"g.Title, "
                 f"a.Type AS Animal"
                 f" FROM Goods g "
                 f"LEFT JOIN Animals a ON g.AnimalId = a.Id WHERE a.Type= '{animal_get}';")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        Database.connection.commit()
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_user_by_role(role: str):
        query = ("SELECT  u.Id, u.Name, u.Login, r.Name FROM Users u"
                 f" JOIN Roles r ON u.RoleId = r.Id AND r.Name = '{role}';")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_all_goods_specific_user(login: str):
        user = Database.get_user_by_login(login)
        if user is None:
            return None
        query = "SELECT u.Name," \
                " g.Id As GoodId," \
                " g.Title AS Good, " \
                "cog.Title AS Category" \
                " FROM CartsGoods cg " \
                "JOIN Carts c ON cg.CartId = c.Id " \
                f"JOIN Users u ON c.UserId = u.Id AND u.Name = {user.name}" \
                " JOIN Goods g ON cg.GoodId = g.Id " \
                "LEFT JOIN CategoriesOfGood cog ON g.CategoryOfGoodId = cog.Id;"

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result

    @staticmethod
    def get_firm_by_specific_good_(good_title: str):
        query = (f"SELECT  f.Naming ,"
                 f" g.Id AS good_id, "
                 f"g.Title FROM Firms f "
                 f"JOIN Goods g ON g.FirmId = f.Id AND g.Title = {good_title};")

        cursor = Database.connection.cursor()
        cursor.execute(query)
        result = cursor.fetcone()
        cursor.close()

        return result

    @staticmethod
    def get_id(table: str):
        query = f"SELECT MAX(Id) FROM {table};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            id_ = cursor.fetchone()[0]
            cursor.close()
            return id_ + 1
        except Exception as e:
            print(e)
            return -1

    @staticmethod
    def add_good(title: str, firm: str, category: str, animal: str):
        query = f"SELECT f.Id FROM Firms f WHERE f.Naming = {firm};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            firm_id = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        query = f"SELECT c.Id, FROM CategoriesOfGood c WHERE c.Title = {category};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            category_id = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        query = f"SELECT c.Id FROM Animals c WHERE c.Type = {animal};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            animal_id = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        good_id = Database.get_id('Goods')
        if good_id == -1:
            return None
        query = "INSERT INTO Clients (Id, Title, FirmId, CategoryOfGoodId, AnimalId) " \
                f"VALUES ({good_id}, '{title}', '{firm_id}', '{category_id}', '{animal_id}');"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)
            return None

        Database.connection.commit()

        good = Good(good_id, title, firm, category, animal)

        return good

    @staticmethod
    def edit_client(user: User, login: str, password: str, name: str):
        if not login.isspace() and login != '':
            query = f"UPDATE Users SET Login = '{login}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.login = login

        if not password.isspace() and password != '':
            query = f"UPDATE Users SET Password = '{password}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.password = password

        if not name.isspace() and name != '':
            query = f"UPDATE Users SET Name = '{name}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.name = name

        Database.connection.commit()

        return user

    @staticmethod
    def add_client(login: str, password: str, name: str):
        if login.isspace() or login == '' or password.isspace() or password == '' \
                or name.isspace() or name == '':
            return None

        client_id = Database.get_id('Users')
        query = (f"INSERT INTO Users (Id, Login, Name, Password, RoleId) VALUES ({client_id}, '{login}', '{password}', "
                 f"'{name}', 1);")
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)
            return None

        user = User(id_=client_id, login=login, password=password, name=name, role=1, coupon=None)
        try:
            Database.add_cart(user)
        except Exception as e:
            print(e)
            return None

        Database.connection.commit()

        return user

    @staticmethod
    def get_firm(naming: str):
        query = f"SELECT Id FROM Firms WHERE Name = '{naming}';"

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            id_ = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return id_

    @staticmethod
    def get_category(title: str):
        query = f"SELECT Id FROM CategoriesOfGood WHERE Title = '{title}';"

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            id_ = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return id_

    @staticmethod
    def get_animal(type_name: str):
        query = f"SELECT Id FROM Animals WHERE Type = '{type_name}';"

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            id_ = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return id_

    @staticmethod
    def edit_good(title: str, new_title: str, firm: str, category: str, animal: str):
        good = Database.get_good(title)
        if good is None:
            return None

        if not new_title.isspace() and new_title != '':
            query = f"UPDATE Goods SET Title = '{new_title}' WHERE Id = {good.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

        if not firm.isspace() and firm != '':
            id_ = Database.get_firm(firm)

            query = f"UPDATE Goods SET FirmId = '{id_}' WHERE Id = {good.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

        if not category.isspace() and category != '':
            id_ = Database.get_category(category)

            query = f"UPDATE Goods SET CategoryOfGoodId = '{id_}' WHERE Id = {good.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

        if not animal.isspace() and animal != '':
            id_ = Database.get_animal(animal)

            query = f"UPDATE Goods SET AnimalId = '{id_}' WHERE Id = {good.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

        Database.connection.commit()

    @staticmethod
    def get_cart(user: User):
        query = f"SELECT Id FROM Carts WHERE UserId = {user.id};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cart_id = cursor.fetchone()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        return cart_id[0]

    @staticmethod
    def add_to_cart(user: User, good: Good):
        cart_id = Database.get_cart(user)
        if cart_id is None:
            return False

        carts_goods_id = Database.get_id('CartsGoods')
        query = f"INSERT INTO CartsGoods (Id, CartId, GoodId) VALUES ({carts_goods_id}, {cart_id}, {good.id});"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)
            return False

        return True

    @staticmethod
    def add_order(user: User):
        cart_id = Database.get_cart(user)
        if cart_id is None:
            return None

        query = f"SELECT Goods.Id FROM CartsGoods JOIN Goods ON Goods.Id = CartsGoods.GoodId WHERE CartId = {cart_id};"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            goods = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(e)
            return None

        order_id = Database.get_id('Orders')
        query = f"INSERT INTO Orders (Id, UserId) VALUES ({order_id}, {user.id});"
        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)
            return None

        for good in goods:
            order_goods_id = Database.get_id('OrderGoods')
            query = f"INSERT INTO OrderGoods (Id, OrderId, GoodId) VALUES ({order_goods_id}, {order_id}, {good});"
            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

    @staticmethod
    def is_banned(login: str):
        user = Database.get_user_by_login(login)

        if user is None or not user[6]:
            return False
        else:
            return True

    @staticmethod
    def add_cart(user: User):
        cart_id = Database.get_id('Carts')
        query = f"INSERT INTO Carts (Id, UserId) VALUES ({cart_id}, {user.id});"

        try:
            cursor = Database.connection.cursor()
            cursor.execute(query)
            cursor.close()
        except Exception as e:
            print(e)


    @staticmethod
    def edit_client_admin(user: User, login: str, password: str, name: str):
        if not login.isspace() and login != '':
            query = f"UPDATE Users SET Login = '{login}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.login = login

        if not password.isspace() and password != '':
            query = f"UPDATE Users SET Password = '{password}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.password = password

        if not name.isspace() and name != '':
            query = f"UPDATE Users SET Name = '{name}' WHERE Id = {user.id};"

            try:
                cursor = Database.connection.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(e)
                return None

            user.name = name

        Database.connection.commit()

        return user

