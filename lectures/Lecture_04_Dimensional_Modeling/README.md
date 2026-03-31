# Lecture 4: Dimensional Modeling

**File:** [`Lecture_04_Dimensional_Modeling.pdf`](./Lecture_04_Dimensional_Modeling.pdf)

**Instructor:** Dr. Jehan Y. Abu-Elreesh

**Academic Year:** 2025 - 2026

---

## 🎯 Learning Objectives

By the end of this lecture, students will be able to:
- Understand the concepts of facts, dimensions, and attributes
- Differentiate between fact tables and dimension tables
- Explain the concept of grain (level of granularity)
- Design and implement Star Schema structures
- Design and implement Snowflake Schema structures
- Compare Star Schema vs Snowflake Schema
- Understand multi-fact star models and conformed dimensions
- Differentiate between ER modeling and dimensional modeling
- Understand OLAP server architectures (ROLAP vs MOLAP)

---

## 📚 Topics Covered

### 1. Introduction to Dimensional Modeling

Dimensional modeling is a technique used in data warehousing for structuring data to optimize query performance and ease of understanding for business users.

**Key Concepts:**
- **Facts:** Measurements of business performance (what happened)
- **Dimensions:** Descriptive attributes that provide context (who, what, where, when, why)
- **Grain:** Level of detail in the measurement

---

### 2. Facts and Fact Tables

#### What is a Fact?
- A measurement of business performance
- Also referred to as **organizational performance measure**
- Contains redundancy
- 90% of data in a dimensional model is typically located in fact tables

#### Fact Table Structure
Fact tables are composed of two types of columns:

| Column Type | Description |
|-------------|-------------|
| **Keys** | Foreign keys (FK) pointing to dimension tables |
| **Measures** | Actual business metrics (numeric values) |

#### Relationships
- Fact tables have **one-to-many** relationships with dimension tables

#### Grain (Level of Granularity)
Every measurement has a grain, which is the level of detail:
- Unit of measure (e.g., dollars, units)
- Currency used
- Time period (e.g., daily balance, monthly total)

#### Example Measures
- SalesQuantity
- SalesAmount
- ReturnAmount
- ReturnQuantity
- DiscountAmount
- DiscountQuantity
- TotalCost

---

### 3. Dimensions and Dimension Tables

#### What are Dimensions?
Dimensions provide context for facts. They answer:
- **Who:** Customer
- **What:** Product
- **Where:** Store, Location
- **When:** Date, Time
- **Why:** Promotion, Reason

#### Dimension Table Structure
- Contain descriptive attributes
- Have hierarchies (e.g., Category → Subcategory → Product)
- Used to "slice and dice" fact data

---

### 4. Star Schema

#### Definition
The star schema (sometimes referenced as star join schema) is the most commonly used and simplest style of dimensional modeling.

#### Structure
- A central **fact table** surrounded by and connected to several **dimension tables**
- Fact table contains foreign keys and measures
- Dimension tables contain descriptive attributes

#### Star Schema Main Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Simplicity** | Simplest type of DW schema |
| **Query Effectiveness** | Fewer joins needed; optimized for large datasets |
| **Data Redundancy** | Denormalized structure causes redundancy |
| **Large Table Size** | Fact tables can be huge |
| **Widely Supported** | Most BI tools work well with star schema |

#### Additional Characteristics
- Dimensions represented by single dimension tables
- Dimension tables are not joined to each other
- Fact tables contain keys and measures
- Data integrity not enforced due to denormalized structure

#### Advantages
- Fast query response time
- Simplicity and ease of understanding
- Easy maintenance for read-only database structure

---

### 5. Snowflake Schema

#### Definition
Closely related to star schema, the snowflake schema takes the star schema one step further by **normalizing the hierarchies** within a particular dimension.

#### Structure
- Centralized fact tables connected to multiple dimensions
- Each level in the dimensional hierarchy becomes its own dimension table
- Parent keys link the hierarchical structure together
- Fact table stores foreign key to the lowest level of the dimensional hierarchy

#### Snowflake Schema Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Extension** | Extension of Star Schema |
| **Normalized** | Dimension tables are normalized; each dimension may expand into additional tables |
| **Disk Space Efficiency** | Uses less disk space due to normalization |
| **Complicated** | Queries need more joins, which may reduce performance |

#### Advantages
- Reduced data redundancy
- Efficient disk space usage
- Easier to maintain dimension hierarchies

#### Disadvantages
- More complex queries (more joins)
- Slower query performance
- Harder for business users to understand

---

### 6. Star Schema vs Snowflake Schema

| Aspect | Star Schema | Snowflake Schema |
|--------|-------------|------------------|
| **Structure** | Denormalized | Normalized |
| **Number of Tables** | Fewer (fact + dimensions) | More (dimensions split into multiple tables) |
| **Query Performance** | Faster (fewer joins) | Slower (more joins) |
| **Storage Space** | More redundancy | Less redundancy |
| **Ease of Understanding** | Easier for business users | More complex |
| **Data Integrity** | Not enforced | Better enforced |
| **Best For** | Simple queries, BI reporting | Complex hierarchies, storage optimization |

---

### 7. Multi-Fact Star Models

#### Overview
Real-world data warehouses often require **multiple fact tables** representing different business events:
- Store Sales
- Store Inventory
- Expenses
- Customer Transactions

#### Conformed Dimensions
Dimensions shared across multiple fact tables are called **conformed dimensions**.

**Example:**
- Both Store Sales and Store Inventory share: Item, Date, and Buyer dimensions
- Customer dimension only relates to Store Sales
- Store dimension only relates to Store Inventory

#### Benefits
- Consistent definitions across the enterprise
- Ability to analyze data across multiple business processes
- Reusable dimensions

---

### 8. ER Modeling vs Dimensional Modeling

| Aspect | ER Modeling (OLTP) | Dimensional Modeling (OLAP/BI) |
|--------|-------------------|-------------------------------|
| **Purpose** | Transaction processing | Analytics and reporting |
| **Data Updates** | Highly volatile, frequently updated | Generally not updated, non-volatile |
| **Priority** | Transaction throughput | Query performance |
| **Data Structure** | Normalized (3NF) | Denormalized (Star/Snowflake) |
| **Redundancy** | Minimal | Increased |
| **Index Usage** | Limited | Extensive |
| **Storage Space** | Efficient | Increased |
| **Data Consistency** | Eliminate inconsistency | Consolidate inconsistent data |
| **Maintenance** | Few concerns | Increased maintenance issues |

#### Why Dimensional Modeling for BI?
- Optimized for complex analytical queries
- Easier for business users to understand
- Faster query response times
- Supports ad-hoc analysis

---

### 9. Three-Tier Data Warehouse Architecture

#### Middle Tier: OLAP Server

The OLAP server can be implemented in two ways:

| Type | Description |
|------|-------------|
| **ROLAP (Relational OLAP)** | Extended relational DBMS that maps multidimensional operations to standard relational operations |
| **MOLAP (Multidimensional OLAP)** | Directly implements multidimensional data and operations using specialized storage structures |

#### Comparison

| Aspect | ROLAP | MOLAP |
|--------|-------|-------|
| **Storage** | Relational tables | Multidimensional cubes |
| **Scalability** | More scalable | Less scalable |
| **Query Speed** | Slower for complex queries | Faster for complex queries |
| **Storage Space** | Less space | More space (pre-aggregated) |

---

## 🖼️ Figures and Diagrams

> *Note: Images will be added to the `images/lecture_04/` folder*

### Figure 1: Star Schema Structure
*Central fact table surrounded by dimension tables*

### Figure 2: Snowflake Schema Structure
*Normalized dimensions with hierarchical tables*

### Figure 3: Star vs Snowflake Comparison
*Side-by-side visual comparison of both schemas*

**Location:** Page 24 of the PDF

![Star vs Snowflake](../images/lecture_04/star_vs_snowflake.png)

---

### Figure 4: Multi-Fact Star Model
*Multiple fact tables sharing conformed dimensions*

**Location:** Pages 28-30 of the PDF

![Multi-Fact Star Model](../images/lecture_04/multi_fact_star.png)

**Components:**
- Fact Tables: Store Sales, Store Inventory
- Shared Dimensions: Item, Date, Buyer
- Unique Dimensions: Customer (with Sales), Store (with Inventory)

---

### Figure 5: ER vs Dimensional Modeling Comparison
*Detailed comparison table of OLTP vs OLAP characteristics*

**Location:** Page 33 of the PDF

![Operational vs BI Systems](../images/lecture_04/operational_vs_bi_comparison.png)

---

### Figure 6: Three-Tier Architecture with OLAP Server
*ROLAP vs MOLAP in the middle tier*

**Location:** Page 34 of the PDF

![OLAP Architecture](../images/lecture_04/olap_architecture.png)

---

## 💡 Key Takeaways

1. **Facts are measurements** – Numeric values representing business performance
2. **Dimensions provide context** – Descriptive attributes that answer who, what, where, when, why
3. **Grain determines level of detail** – Defines what each fact row represents
4. **Star Schema is simple and fast** – Denormalized structure for query performance
5. **Snowflake Schema saves space** – Normalized structure reduces redundancy
6. **Choose schema based on use case** – BI tools often prefer star schema
7. **Conformed dimensions enable integration** – Shared dimensions across multiple fact tables
8. **Dimensional modeling is for BI** – Different from ER modeling used in OLTP

---

## 📝 Quick Review Questions

### Basic Questions
1. What is a fact? What is a dimension?
2. What are the two types of columns in a fact table?
3. What is grain in dimensional modeling?
4. Draw the structure of a Star Schema.
5. Draw the structure of a Snowflake Schema.

### Advanced Questions
6. What are the main characteristics of Star Schema?
7. What are the main characteristics of Snowflake Schema?
8. When would you choose Star Schema over Snowflake Schema?
9. What are conformed dimensions? Give an example.
10. Compare ER modeling and dimensional modeling.

### Application Questions
11. A retail company wants to analyze sales by product, customer, and time. Which schema would you recommend? Why?
12. A company has complex product hierarchies (Category → Subcategory → Product). Which schema handles this better?

---

## 📊 Summary Table: Facts vs Dimensions

| Aspect | Facts | Dimensions |
|--------|-------|------------|
| **Purpose** | Measure business performance | Provide context |
| **Content** | Numeric measures | Descriptive attributes |
| **Examples** | SalesAmount, Quantity | ProductName, CustomerName, Date |
| **Table Type** | Fact Table | Dimension Table |
| **Cardinality** | Many rows (high) | Fewer rows (low) |
| **Updates** | Append-only | Slowly changing |

---

## 🔗 Related Resources

- [Lecture 1: Introduction to Data Warehousing](./Lecture_01_Introduction.pptx) – Foundation concepts
- [Lecture 2: Introduction to DW](./Lecture_02_Introduction_to_DW.pdf) – DW characteristics
- [Lecture 3: NoSQL and Selected Topics](./Lecture_03_NoSQL_and_Selected_Topics.pptx) – Alternative approaches
- [Star Schema Lab](../labs/star_schema_lab/lab_instructions.pdf) – Hands-on practice
- [PostgreSQL Functions Reference](../exams/postgresql_functions_reference.pdf) – SQL for queries

---

## 📖 References

- Sharda, R., Delen, D., & Turban, E. (2018). *Business Intelligence, Analytics, and Data Science: A Managerial Perspective*. Pearson.
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*. Wiley.
- https://gability.com/en/courses/big-data-in-depth/02-dwh/03-architecture/10-data-modeling/04-schema-types/

---

## 📌 Next Lecture

**Lecture 5:** NoSQL Database as Data Warehouse – Advanced topics in NoSQL integration

---

*For lab exercises, see the [`labs/`](../labs/) folder.*
*For exam preparation, see the [`exams/`](../exams/) folder.*
