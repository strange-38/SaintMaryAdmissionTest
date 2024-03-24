-- -- Decomposing the source table into separate tables for products and categories to eliminate functional dependency.

-- create product table
CREATE TABLE Product 
(
    ProductName	VARCHAR(512),
    CategoryId	CHAR(3),
    Year INT,
    QuantityPurchased INT
);
-- insert
INSERT INTO Product (ProductName, CategoryId, Year, QuantityPurchased) VALUES
    ('Shampoo', '006', 2020, 10070),
    ('Bowl', '005', 2021, 210),
    ('Potato', '002', 2021, 30130),
    ('Protein Powder', '001', 2022, 400),
    ('Energy Drink', '001', 2020, 834),
    ('Light Bulbs', '005', 2022, 900),
    ('Baking Powder', '004', 2020, 5000),
    ('Skimmed Milk', '003', 2021, 300000),
    ('Yogurt', '003', 2020, 98700),
    ('Cake Mix', '004', 2020, 720),
    ('Lotion', '006', 2020, 100),
    ('Grapes', '002', 2020, 59000),
    ('Hand Soap', '006', 2021, 89211),
    ('Flour', '004', 2021, 39091),
    ('Brownie Mix', '004', 2021, 2131),
    ('Tomato', '002', 2021, 653);

-- create category table
CREATE TABLE Category 
(
    CategoryId CHAR(3),
    Category VARCHAR(512)
);
-- insert
INSERT INTO Category (CategoryId, Category) VALUES
	('001', 'Sports and travel'),
	('002', 'Produce'),
	('003', 'Dairy'),
	('004', 'Baking'),
	('005', 'Home and lifestyle'),
	('006', 'Health and beauty');

-- the total quantity purchased per year for each category, sorted by category and year.
SELECT c.CategoryId, c.Category, p.Year, SUM(p.QuantityPurchased) AS TotalQuantityPurchased
FROM Product AS p
JOIN Category AS c ON p.CategoryId = c.CategoryId
GROUP BY c.CategoryId, c.Category, p.Year
ORDER BY c.Category, p.Year;