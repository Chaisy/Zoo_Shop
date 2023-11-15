--Select goods with it's firms.
CREATE VIEW goods_firms_view AS
    SELECT g.Id, 
           g.Title, 
           f.Naming AS firmName
    
      FROM Goods g 
           LEFT JOIN Firms f 
                  ON g.FirmId = f.Id;
        




--Select goods, ordered less than two times
CREATE VIEW unpopular_goods_view AS
    SELECT *
      FROM goods_firms_view gf
           JOIN (SELECT og.GoodId AS good_id, 
                        SUM(og.Count) AS total_ordered 
                   FROM OrderGoods og 
               GROUP BY og.GoodId) AS gto
             ON gf.Id = gto.good_id AND gto.total_ordered < 2;    
             

--Select users and count of goods in a cart
CREATE VIEW users_and_count_goods_in_cart AS
    SELECT u.Id,
           u.Name,
           u.Login,
           cgc.summary_in_cart
           
           FROM User u
                JOIN (SELECT c.UserId AS user_id,
                             SUM(cg.Count) AS summary_in_cart
                        FROM Cart c
                             JOIN CartsGood cg
                               ON c.Id = cg.CartId
                    GROUP BY user_id) AS cgc                    
             ON cgc.user_id = u.Id;          
             

--Select users with it's role.
SELECT u.Id,
           u.Name,
           u.Login,
           u.RoleId,
           EXISTS
           (SELECT * 
              FROM Roles r 
             WHERE r.Id = u.RoleId) 
                AS is_moderator
                              
      FROM User u                     
                                    