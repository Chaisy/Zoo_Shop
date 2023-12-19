--Select all goods wiht it's category title.@
SELECT 
    g.Id, 
    g.Title, 
    c.Title AS Category

    FROM Goods g 
    LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id;


--Select goods by a specific category.@
SELECT
    g.Id,
    g.Title,
    c.Title

    FROM Goods g 
    LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id
    
    WHERE LOWER(c.Title) = LOWER('Toys');



--Select coupons of specific user.@
SELECT 
    u.Name AS User,
    c.Id AS CouponId,
    c.Sale
    
    FROM Coupons c
    JOIN Users u ON u.CouponId = c.Id AND LOWER(u.Name) = LOWER('User name');
    


--Select user role.@
SELECT
    r.Id,
    u.Name,
    r.Name AS Role
    
    FROM Roles r
    JOIN Users u ON u.RoleId = r.Id AND LOWER(u.Name) = LOWER('User Name');

--Select goods by a specific animal.@
SELECT
    g.Id,
    g.Title,
    a.Type AS Animal
    
     FROM Goods g 
    LEFT JOIN Animals a ON g.AnimalId = a.Id
    
    WHERE LOWER(a.Type) = LOWER('Animal Type');
    

--Select users by role.@
SELECT 
    u.Id,
    u.Name,
    u.Login, 
    r.Name   
    
    FROM Users u
    JOIN Roles r ON u.RoleId = r.Id AND LOWER(r.Name) = LOWER('Role Name');
    

   

--Select users that have specific good in a cart.
SELECT 
    u.Id,
    u.Name,
    u.Login,
    g.Id AS GoodId,
    g.Title     
     
    FROM CartsGoods cg
    JOIN Goods g ON cg.GoodId = g.Id AND g.Id = 2
    JOIN Carts c ON cg.GoodId = c.Id
    JOIN Users u ON c.UserId = u.Id;
    

--Select all goods from specific user cart.@
SELECT 
    u.Name,
    g.Id As GoodId,
    g.Title AS Good,
    cog.Title AS Category
    
    FROM CartsGoods cg
    JOIN Carts c ON cg.CartId = c.Id
    JOIN Users u ON c.UserId = u.Id AND LOWER(u.Name) = LOWER('User Name')
    JOIN Goods g ON cg.GoodId = g.Id
    LEFT JOIN CategoriesOfGood cog ON g.CategoryOfGoodId = cog.Id;


--Select users that have specific good in orders.
SELECT 
    u.Id,
    u.Name,
    g.Title,
    g.Id AS GoodId   
     
    FROM OrderGoods og
    JOIN Goods g ON og.GoodId = g.Id AND g.Id = 3
    JOIN Orders o ON og.OrderId = o.Id
    JOIN Users u ON o.UserId = u.Id;
    
    
    

--Select goods that was ordered by specific user.
SELECT 
    g.Id,
    g.Title,
    u.Name AS User
    
    FROM OrderGoods og
    JOIN Orders o ON og.OrderId = o.Id
    JOIN Users u ON o.UserId = u.Id AND LOWER(u.Name) = LOWER('User Name')
    JOIN Goods g ON og.GoodId = g.Id; 
    


    
--Select firms by specific good.@
SELECT 
    f.Naming ,
    g.Id AS good_id,
    g.Title
    
    FROM Firms f
    JOIN Goods g ON g.FirmId = f.Id AND g.Id = '1' ;
    

--Select goods that provide by special firm.
SELECT 
    g.Id,
    g.Title,
    f.Naming
FROM Firms f
    JOIN Goods g ON g.FirmId = f.Id AND LOWER(f.Naming) = LOWER('Acana')  ; 
    

--Select count of orders of every good.
-- SELECT
--     g.Id, 
--     g.Title, 
--     f.Naming AS firm_name,
--     SUM(og.Count) AS orders_count

--     FROM Goods g 
--     LEFT JOIN Firms f ON g.FirmId = f.Id
--     LEFT JOIN OrderGoods og ON og.GoodId = g.Id
    
--     GROUP BY g.Id;
    

--Select goods that are in the cart of at least two users.
-- SELECT
--     g.Id, 
--     g.Title, 
--     f.Naming AS firm_name,
--     SUM(cg.Count) AS in_cart_count

--     FROM Goods g 
--     LEFT JOIN Firms f ON g.FirmId = f.Id
--     LEFT JOIN CartsGoods cg ON cg.GoodId = g.Id
    
--     GROUP BY g.Id 
--     HAVING SUM(cg.Count) >= 2;
             

 --Select all firms and names.
SELECT u.Name FROM Users u
UNION 
SELECT f.Naming FROM Firms f;






--Select goods and it's popularity level.
SELECT g.Id, 
       g.Title, 
       f.Naming AS firm,
       CASE 
           WHEN gto.total_ordered > 5 THEN 'Super popular'
           WHEN gto.total_ordered BETWEEN 2 AND 5 THEN 'Meadle popular'
           ELSE 'Not popular'
       END AS popularity                          
       

       FROM Goods g
            LEFT JOIN Firms f ON g.FirmId = f.Id
            JOIN (SELECT og.GoodId AS good_id, 
                         SUM(og.Count) AS total_ordered 
                    FROM OrderGoods og 
                GROUP BY og.GoodId) AS gto
              ON gto.good_id = g.Id;



-- --Select goods with max price of it's author book.
-- SELECT g.Id, 
--        g.Title, 
--        f.Naming AS firm,
--        MAX(g.Price)OVER (PARTITION BY g.FirmId) AS max_price_of_firm;


--Select goods by a specific category.
SELECT
    g.Id,
    g.Title,
    c.Title
	FROM Goods g 
    LEFT JOIN CategoriesOfGood c ON g.CategoryOfGoodId = c.Id
    
    WHERE LOWER(c.Title) = LOWER('Toys');



--Select coupons of specific user.
SELECT 
    u.Name AS User,
    c.Id AS CouponId,
    c.Sale
    
    FROM Coupons c
    JOIN Users u ON u.CouponId = c.Id AND LOWER(u.Name) = LOWER('User name');
    


--Select user role.
SELECT
    r.Id,
    u.Name,
    r.Name AS Role
    
    FROM Roles r
    JOIN Users u ON u.RoleId = r.Id AND LOWER(u.Name) = LOWER('User Name');

--Select goods by a specific animal.
SELECT
    g.Id,
    g.Title,
    a.Type AS Animal
    
     FROM Goods g 
    LEFT JOIN Animals a ON g.AnimalId = a.Id
    
    WHERE LOWER(a.Type) = LOWER('Animal Type');
    

--Select users by role.
SELECT 
    u.Id,
    u.Name,
    u.Login, 
    r.Name   
    
    FROM Users u
    JOIN Roles r ON u.RoleId = r.Id AND LOWER(r.Name) = LOWER('Role Name');
    

   

--Select users that have specific good in a cart.
SELECT 
    u.Id,
    u.Name,
    u.Login,
    g.Id AS GoodId,
    g.Title     
     
    FROM CartsGoods cg
    JOIN Goods g ON cg.GoodId = g.Id AND g.Id = 4
    JOIN Carts c ON cg.GoodId = c.Id
    JOIN Users u ON c.UserId = u.Id;
    

--Select all goods from specific user cart.
SELECT 
    u.Name,
    g.Id As GoodId,
    g.Title AS Good,
    cog.Title AS Category
    
    FROM CartsGoods cg
    JOIN Carts c ON cg.CartId = c.Id
    JOIN Users u ON c.UserId = u.Id AND LOWER(u.Name) = LOWER('User Name')
    JOIN Goods g ON cg.GoodId = g.Id
    LEFT JOIN CategoriesOfGood cog ON g.CategoryOfGoodId = cog.Id;


--Select users that have specific good in orders.
SELECT 
    u.Id,
    u.Name,
    g.Title,
    g.Id AS GoodId   
     
    FROM OrderGoods og
    JOIN Goods g ON og.GoodId = g.Id AND g.Id = 2
    JOIN Orders o ON og.OrderId = o.Id
    JOIN Users u ON o.UserId = u.Id;
    
    
    

--Select goods that was ordered by specific user.
SELECT 
    g.Id,
    g.Title,
    u.Name AS User
    
    FROM OrderGoods og
    JOIN Orders o ON og.OrderId = o.Id
    JOIN Users u ON o.UserId = u.Id AND LOWER(u.Name) = LOWER('User Name')
    JOIN Goods g ON og.GoodId = g.Id; 
    


    
--Select firms by specific good.
SELECT 
    f.Naming ,
    g.Id AS good_id,
    g.Title
    
    FROM Firms f
    JOIN Goods g ON g.FirmId = f.Id AND g.Id = '1' ;
    

--Select goods that provide by special firm.
SELECT 
    g.Id,
    g.Title,
    f.Naming
FROM Firms f
    JOIN Goods g ON g.FirmId = f.Id AND LOWER(f.Naming) = LOWER('Acana')  ; 
    

--Select count of orders of every good.
-- SELECT
--     g.Id, 
--     g.Title, 
--     f.Naming AS firm_name,
--     SUM(og.Count) AS orders_count

--     FROM Goods g 
--     LEFT JOIN Firms f ON g.FirmId = f.Id
--     LEFT JOIN OrderGoods og ON og.GoodId = g.Id
    
--     GROUP BY g.Id;
    

--Select goods that are in the cart of at least two users.
-- SELECT
--     g.Id, 
--     g.Title, 
--     f.Naming AS firm_name,
--     SUM(cg.Count) AS in_cart_count

--     FROM Goods g 
--     LEFT JOIN Firms f ON g.FirmId = f.Id
--     LEFT JOIN CartsGoods cg ON cg.GoodId = g.Id
    
--     GROUP BY g.Id 
--     HAVING SUM(cg.Count) >= 2;
             

 --Select all firms and names.
SELECT u.Name FROM Users u
UNION 
SELECT f.Naming FROM Firms f;






--Select goods and it's popularity level.
SELECT g.Id, 
       g.Title, 
       f.Naming AS firm,
       CASE 
           WHEN gto.total_ordered > 5 THEN 'Super popular'
           WHEN gto.total_ordered BETWEEN 2 AND 5 THEN 'Meadle popular'
           ELSE 'Not popular'
       END AS popularity                          
       

       FROM Goods g
            LEFT JOIN Firms f ON g.FirmId = f.Id
            JOIN (SELECT og.GoodId AS good_id, 
                         SUM(og.Count) AS total_ordered 
                    FROM OrderGoods og 
                GROUP BY og.GoodId) AS gto
              ON gto.good_id = g.Id;

ALTER TABLE Goods ADD COLUMN Price INTEGER NOT NULL DEFAULT 100;

--Select goods with max price of it's author book.
SELECT g.Id, 
       g.Title, 
       f.Naming AS firm,
       MAX(g.Price)OVER (PARTITION BY g.FirmId) AS max_price_of_firm
       
	FROM Goods g
       JOIN Firms f ON g.FirmId = f.Id;

    
