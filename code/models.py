class User:
    def __init__(self, id_, name, password, login, role, coupon=None):
        self.id = id_
        self.name = name
        self.password = password
        self.coupon_id = coupon
        self.role_id = role
        self.login = login


class Role:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


class Coupon:
    def __init__(self, id_, sale):
        self.id = id_
        self.sale = sale


class Cart:
    def __init__(self, id_, user):
        self.id = id_
        self.user_id = user


class Firm:
    def __init__(self, id_, naming):
        self.id = id_
        self.naming = naming


class Animal:
    def __init__(self, id_, type_name):
        self.id = id_
        self.type = type_name


class CategoryOfGood:
    def __init__(self, id_, title):
        self.id = id_
        self.title = title


class Good:
    def __init__(self, id_, title, firm, category_of_good, animal):
        self.id = id_
        self.title = title
        self.firm_id = firm
        self.categoryOfGood_id = category_of_good
        self.animal_id = animal


class Order:
    def __init__(self, id_, user):
        self.id = id_
        self.user_id = user
