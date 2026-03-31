
# Labs – Where the Magic Happens (or the Errors Happen 😂)

هون بنحط إيدينا بالطين. الكلام النظري خلص، الحين دور التطبيق العملي.

> **"I don't always test my code, but when I do, I do it in production."**  
> — Someone who never worked in data warehousing

---

## 📁 Lab Structure

```

labs/
├── postgres_connection.py          # Python script to connect to PostgreSQL (your best friend)
└── star_schema_lab/
├── lab_instructions.pdf        # The lab exercise (the problem)
└── lab_solution.sql            # The solution (the answer you'll cry over)

```

---

## 🐘 Lab 1: PostgreSQL Connection (Python)

### What is this?
A Python script that connects to PostgreSQL so you don't have to type SQL commands manually like a caveman.

### File: `postgres_connection.py`

### What it does:
- Connects to your local PostgreSQL database
- Executes SELECT queries (reading data)
- Executes INSERT/UPDATE/DELETE queries (writing data)
- Returns results as Python objects or pandas DataFrames

### How to use it (without breaking everything):

1. **Install the required packages:**
   ```bash
   pip install psycopg2-binary pandas
```

1. Edit the database credentials (don't leave them as "your_database_name" unless you enjoy error messages):
   ```python
   dbname = "your_database_name"    # change this!
   user = "your_username"            # change this!
   password = "your_password"        # change this!
   ```
2. Run the script:
   ```bash
   python postgres_connection.py
   ```

What the script does (step by step):

```python
# 1. Create connection object
db = PostgreSQLConnection(dbname, user, password)

# 2. Connect to database
db.connect()

# 3. Read data
result = db.execute_extract_query("SELECT * FROM your_table LIMIT 10")

# 4. Write data
db.execute_load_query("INSERT INTO your_table VALUES ('value1', 'value2')")

# 5. Disconnect (don't leave it hanging!)
db.disconnect()
```

Pro Tips:

· If you get "connection refused" error → PostgreSQL not running (go start it)
· If you get "database does not exist" → you didn't create the database yet (create it!)
· If you get "permission denied" → wrong username/password (check your credentials)
· If it works on the first try → you're a wizard, congratulations 🧙‍♀️

---

⭐ Lab 2: Star Schema Lab (The Real Deal)

Scenario

You're working as a database analyst for a small retail store. The store tracks:

· Products (what they sell)
· Customers (who buys)
· Sales (who bought what and how much)

Schema (The Star Schema)

```
┌─────────────────┐     ┌─────────────────┐
│   Dim_Product   │     │  Dim_Customer   │
├─────────────────┤     ├─────────────────┤
│ Product_ID (PK) │     │ Customer_ID (PK)│
│ Product_Name    │     │ Customer_Name   │
│ Category        │     │ Loyalty_Status  │
│ Price           │     └────────┬────────┘
└────────┬────────┘              │
         │                       │
         │    ┌─────────────────┐│
         └────┤   Fact_Sales    ├┘
              ├─────────────────┤
              │ Sales_ID (PK)   │
              │ Product_ID (FK) │
              │ Customer_ID (FK)│
              │ Sales_Amount    │
              └─────────────────┘
```

The Tables

Table Columns Description
Dim_Product Product_ID, Product_Name, Category, Price Product catalog
Dim_Customer Customer_ID, Customer_Name, Loyalty_Status Customer info
Fact_Sales Sales_ID, Product_ID, Customer_ID, Sales_Amount Sales transactions

Sample Data

Dim_Product:

Product_ID Product_Name Category Price
101 Laptop Electronics 1000
102 Desk Furniture 700

Dim_Customer:

Customer_ID Customer_Name Loyalty_Status
1 Alice Premium
2 Bob Regular

Fact_Sales:

Sales_ID Product_ID Customer_ID Sales_Amount
1 101 1 1000
2 102 2 700

---

📝 Lab Tasks (6 Questions)

Q1: CREATE Tables

Create the three tables with:

· Primary keys
· Foreign keys (for Fact_Sales referencing Dim_Product and Dim_Customer)

File: star_schema_lab/lab_solution.sql (lines 1-20)

---

Q2: INSERT Data

Insert the sample data into all three tables.

File: star_schema_lab/lab_solution.sql (lines 22-35)

---

Q3: SELECT Queries

Select all products in category 'Electronics' or 'Furniture' with price > 500.
Order by price descending and show only top 2.

Expected Output:

Product_Name Category Price
Laptop Electronics 1000
Desk Furniture 700

File: star_schema_lab/lab_solution.sql (lines 37-45)

---

Q4: UPDATE & DELETE

· Update the price of 'Laptop' to 1200
· Delete the product 'Desk'

File: star_schema_lab/lab_solution.sql (lines 47-55)

---

Q5: Aggregate Functions

Calculate:

· Total sales (SUM)
· Average sale per transaction (AVG)
· Number of sales transactions (COUNT)
· Maximum and minimum sale (MAX, MIN)

Expected Output:

Total_Sales Avg_Sale Total_Transactions Max_Sale Min_Sale
1700 850 2 1000 700

File: star_schema_lab/lab_solution.sql (lines 57-75)

---

Q6: GROUP BY & HAVING

· Show total sales per product
· Show products with total sales > 1000

Expected Output (Total Sales per Product):

Product_ID Total_Sales
101 1000
102 700

Products with Total Sales > 1000: (none in this dataset)

File: star_schema_lab/lab_solution.sql (lines 77-90)

---

🚀 How to Run the Lab

Option 1: Using pgAdmin (GUI)

1. Open pgAdmin
2. Connect to your PostgreSQL server
3. Open Query Tool
4. Copy and paste the SQL from lab_solution.sql
5. Run each section (or run all)

Option 2: Using Python (Your friend postgres_connection.py)

```python
# Load the SQL file
with open('star_schema_lab/lab_solution.sql', 'r') as f:
    sql_commands = f.read()

# Execute each command
for command in sql_commands.split(';'):
    if command.strip():
        db.execute_load_query(command)
```

Option 3: Using psql (Command Line)

```bash
psql -U your_username -d your_database -f star_schema_lab/lab_solution.sql
```

---

🐛 Common Errors (and How to Fix Them)

Error What It Means Fix
relation "dim_product" does not exist You forgot to create the table Run CREATE TABLE first
duplicate key value violates unique constraint You're inserting duplicate IDs Check your INSERT statements
null value in column "product_id" violates not-null constraint Missing required value Make sure all columns have values
ERROR: column "product_name" does not exist Typo in column name Check spelling (case matters!)
ERROR: syntax error at or near "FROM" Missing semicolon or wrong syntax Check your SQL syntax

---

✅ Lab Completion Checklist

· PostgreSQL installed and running
· Created database
· Created tables (Q1)
· Inserted sample data (Q2)
· Ran SELECT query successfully (Q3)
· Updated and deleted data (Q4)
· Calculated aggregates (Q5)
· Used GROUP BY and HAVING (Q6)
· Celebrated with coffee/tea ☕

---

💡 Pro Tips (From Someone Who Learned the Hard Way)

1. Save your queries – You'll need them for the exam (trust me)
2. Test each query separately – Don't run everything at once and pray
3. Use meaningful aliases – SUM(Sales_Amount) AS Total_Sales not SUM(Sales_Amount)
4. Commit after writes – If using Python, make sure to commit (the script does it for you)
5. Backup your data – Because DELETE FROM Dim_Product without WHERE is painful

---

📚 Resources

· PostgreSQL Official Documentation
· psycopg2 Documentation
· W3Schools SQL Tutorial (quick reference)
· Lecture 4: Dimensional Modeling (for theory)

---

🎯 Lab Outcomes

After completing these labs, you will be able to:

· Connect Python applications to PostgreSQL databases
· Design and implement Star Schema structures
· Write SQL queries for data warehousing analytics
· Use aggregate functions and grouping for business reporting
· Update and delete data with proper constraints
· Debug common SQL errors (without crying)

---

Remember: Every SQL error you fix makes you stronger.
And if all else fails, SELECT * FROM internet WHERE answer = 'your problem' 😉

---

For lecture materials, see the lectures/ folder.
For exam preparation, see the exams/ folder.

```

---
العملي هوا أملي 😂🥲
