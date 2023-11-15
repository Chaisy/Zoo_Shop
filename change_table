INSERT INTO Users (Name, Login, Password, RoleId)
SELECT  f.Name, f.Name, 'pass', 1
FROM Roles f
WHERE EXISTS(SELECT * FROM Goods g WHERE f.Id = g.FirmId);