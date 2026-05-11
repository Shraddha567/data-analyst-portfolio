* Altering and Dropping Tables
In SQL, we use ALTER to change a table structure and DROP to remove a table completely.

Altering a Table
ALTER TABLE modifies the table structure without deleting existing data.

Adding a New Column
ALTER TABLE orders
ADD COLUMN delivery_partner VARCHAR(50);

Adds a new column to the orders table. All existing rows remain unchanged.

Modifying a Column
ALTER TABLE orders
MODIFY price_per_unit DECIMAL(12,2);

Changes the data type or size of a column. Data stays as long as it fits the new definition.

* Renaming a Column
ALTER TABLE orders
RENAME COLUMN city TO customer_city;

Renames a column while keeping all data.

Dropping a Column
ALTER TABLE orders
DROP COLUMN rating;

Deletes only the column, not the table.

Deleting Table Data vs Table Structure
Delete All Rows but Keep Structure
DELETE FROM orders;

Removes all data
Table structure stays
Can be rolled back in transactions
Dropping a Table
Delete Everything Including Structure
DROP TABLE orders;

Deletes table data
Deletes table structure
Table no longer exists
Cannot be rolled back
Drop Table Only If It Exists
DROP TABLE IF EXISTS orders;

Prevents errors if the table does not exist.

# Quick Summary
ALTER TABLE Changes structure, data stays

DELETE FROM table Deletes data, structure stays

DROP TABLE Deletes data and structure completely

