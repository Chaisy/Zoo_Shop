CREATE OR REPLACE FUNCTION select_goods_by_category(category_name TEXT) 
RETURNS TABLE(Id INTEGER, Title varchar(64), firm_name varchar(64)) AS $$
BEGIN
  RETURN QUERY SELECT
    g.Id,
    g.Title,
    f.Naming AS firm_name

    FROM Goods g
    JOIN CategoriesOfGood cg ON g.CategoryOfGoodId = cg.Id AND LOWER(cg.Title) = LOWER(category_name)    
    LEFT JOIN Firms f ON g.FirmId = f.Id;
END;
$$ LANGUAGE plpgsql;
