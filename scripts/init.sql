INSERT INTO Roles (Id, Name) VALUES
(1, 'Customer'),
(2, 'Moderator'),
(3, 'Admin');

INSERT INTO Coupons (Id, Sale) VALUES 
(1, 30), 
(2, 50), 
(3, 90);

INSERT INTO Users (Id, Login, Password, Name, RoleId, CouponId) VALUES
(1, 'L1', 'P1', 'Daria', 2, NULL),
(2, 'L2', 'P2', 'Lina', 2, 2),
(3, 'L3', 'P2', 'Liza', 2, 1),
(4, 'L4', 'P4', 'Pavel', 1, 2),
(5, 'L5', 'P5', 'SuperAdmin', 3, NULL);

INSERT INTO CategoriesOfGood (Id, Title) VALUES
(1, 'Homes'),
(2, 'Food'),
(3, 'Fillers'),
(4, 'Grooming'),
(5, 'Toys'),
(6, 'Medicine');

INSERT INTO Firms (Id, Naming) VALUES
(1, 'Happy Tail'),
(2, 'Trixie'),
(3, 'Acana'),
(4, 'Fluffy Paws');

INSERT INTO Animals (Id, Type) VALUES 
(1, 'Dogs'),
(2, 'Cats'),
(3, 'Birds'),
(4, 'Rodent'),
(5, 'Fish');

INSERT INTO Goods (Id, Title, FirmId, CategoryOfGoodId, AnimalId) VALUES
(1, 'Sweet Home', 1, 1, 1),
(2, 'Acana for Cats', 3, 2,  2),
(3, 'Castle', 2, 5, 5),
(4, 'Ball for walk', 2, 5, 4),
(5, 'Shampoo', 4, 4, 2),
(6, 'Toilet Filler', 4, 3, 2),
(7, 'Cream for beak', 2, 6, 3),
(8, 'Pillow', 1, 1, 1);

INSERT INTO Orders (Id, UserId) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO Carts (Id, UserId) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 5);

INSERT INTO CartsGoods (Id, CartId, GoodId) VALUES
(1, 1, 1), (2, 1, 5), (3, 1, 7),
(4, 2, 2), (5, 2, 5),
(6, 3, 4), 
(7, 4, 3);


INSERT INTO OrderGoods (Id, OrderId, GoodId) VALUES
(1, 1, 4), (2, 1, 3),
(3, 2, 1), (4, 2, 2),
(5, 3, 7), (6, 3, 6), (7, 3, 5);


