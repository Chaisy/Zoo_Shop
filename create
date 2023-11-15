CREATE TABLE Roles (
    Id           SERIAL           PRIMARY KEY,      
    Name         VARCHAR (64)     NOT NULL UNIQUE
);

CREATE TABLE Coupons (
    Id           SERIAL           PRIMARY KEY,        
    Sale     	 INTEGER          NOT NULL UNIQUE
);

CREATE TABLE Users (
    Id           SERIAL           PRIMARY KEY,
    Login        VARCHAR (64)     NOT NULL UNIQUE,
    Password     VARCHAR (64)     NOT NULL,	
    Name         VARCHAR (64)     NOT NULL UNIQUE,
    RoleId       INTEGER          REFERENCES Roles (Id) ON DELETE SET NULL,
    CouponId     INTEGER          REFERENCES Coupons (Id) ON DELETE SET NULL
);

CREATE TABLE Carts (
    Id           SERIAL           PRIMARY KEY,       
    UserId       INTEGER          NOT NULL UNIQUE REFERENCES Users (Id) ON DELETE CASCADE
);

CREATE TABLE Firms (
    Id           SERIAL           PRIMARY KEY,      
    Naming       VARCHAR (64)     NOT NULL UNIQUE
);

CREATE TABLE Animals (
    Id           SERIAL           PRIMARY KEY,
    Type         VARCHAR (64)     NOT NULL UNIQUE
);

CREATE TABLE CategoriesOfGood (
    Id           SERIAL          PRIMARY KEY,
    Title   	 VARCHAR(64)     NOT NULL UNIQUE
);

CREATE TABLE Goods (
    Id           SERIAL           PRIMARY KEY, 
    Title        VARCHAR (64)     NOT NULL,
    FirmId       INTEGER          REFERENCES Firms (Id) ON DELETE CASCADE,
    CategoryOfGoodId     INTEGER          REFERENCES CategoriesOfGood (Id) ON DELETE CASCADE,
    AnimalId         INTEGER        REFERENCES Animals (Id) ON DELETE CASCADE
);

CREATE TABLE Orders (
    Id           SERIAL          PRIMARY KEY,      
    UserId       INTEGER          REFERENCES Users (Id) ON DELETE SET NULL
);

CREATE TABLE OrderGoods (
    IId          SERIAL           PRIMARY KEY,    
    OrderId      INTEGER          REFERENCES Orders (Id) ON DELETE CASCADE,
    GoodId       INTEGER          REFERENCES Goods (Id) ON DELETE CASCADE,
    Count        INTEGER          NOT NULL DEFAULT 1,   
    DateTime 	 TIMESTAMP 		  NOT NULL, 

    UNIQUE (OrderId, GoodId)
);


CREATE TABLE CartsGoods (
    Id           SERIAL           PRIMARY KEY,    
    CartId       INTEGER          REFERENCES Carts (Id) ON DELETE CASCADE,
    GoodId       INTEGER          REFERENCES Goods (Id) ON DELETE CASCADE,
    Count        INTEGER          NOT NULL DEFAULT 1,

    UNIQUE (CartId, GoodId)
);

