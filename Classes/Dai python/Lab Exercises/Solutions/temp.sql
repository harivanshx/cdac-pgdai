CREATE TABLE PRODUCT_MASTER (
    PRODUCTNO VARCHAR(6) PRIMARY KEY 
        CHECK (PRODUCTNO LIKE 'P%'),
    
    DESCRIPTION VARCHAR(15) NOT NULL,
    
    PROFITPERCENT DECIMAL(4,2) NOT NULL,
    
    UNITMEASURE VARCHAR(10) NOT NULL,
    
    QTYONHAND INT NOT NULL,
    
    REORDERLVL INT NOT NULL,
    
    SELLPRICE DECIMAL(8,2) NOT NULL CHECK (SELLPRICE > 0),
    
    COSTPRICE DECIMAL(8,2) NOT NULL CHECK (COSTPRICE > 0)
);












CREATE TABLE SALESMAN_MASTER (
    SALESMANNO VARCHAR(6) PRIMARY KEY
        CHECK (SALESMANNO LIKE 'S%'),
    
    SALESMANNAME VARCHAR(20) NOT NULL,
    
    ADDRESS1 VARCHAR(30) NOT NULL,
    
    ADDRESS2 VARCHAR(30),
    
    CITY VARCHAR(20),
    
    PINCODE INT,   -- 8-digit integer
    
    STATE VARCHAR(20),
    
    SALAMT DECIMAL(8,2) NOT NULL CHECK (SALAMT > 0),
    
    TGTTOGET DECIMAL(6,2) NOT NULL CHECK (TGTTOGET > 0),
    
    YTDSALES DECIMAL(6,2) NOT NULL,
    
    REMARKS VARCHAR(60)
);


























Table_Name: SALES_ORDER
Column Name Data Type Size Attributes
ORDERNO Varchar 6 Primary Key / First letter must start with

‘O’

CLIENTNO Varchar 6 Foreign Key references ClientNo of

Client_Master table

ORDERDATE Date Not Null
DELYADDR Varchar 25
SALESMANNO Varchar 6 Foreign Key references SalesmanNo of

Salesman_Master table

DELYTYPE

Char 1
BILLYN Char 1
DELYDATE Date
ORDERSTATUS Varchar 10

Table_Name: SALES_ORDER_DETAILS
Column Name Data Type Size Attributes
ORDERNO Varchar 6 Foreign Key references OrderNo of

Sales_Order table

PRODUCTNO Varchar 6 Foreign Key references ProductNo of

Product_Master table

QTYORDERED Number 8
QTYDISP Number 8
PRODUCTRATE Number 10,2