# Lecture 2: Introduction to Data Warehousing (Deep Dive)

**File:** [`Lecture_02_Introduction_to_DW.pdf`](./Lecture_02_Introduction_to_DW.pdf)

**Instructor:** Dr. Jehan Y. Abu-Elreesh

---

## 🎯 Learning Objectives

By the end of this lecture, students will be able to:
- Understand the central role of Data Warehouse in Business Intelligence
- Differentiate between Data Warehouse Offline and Online states
- Compare Inmon and Kimball methodologies
- Identify the four characteristics of a Data Warehouse (Subject-Oriented, Integrated, Time-Variant, Nonvolatile)
- Distinguish between EDW, ODS, and Data Mart
- Explain Metadata Repository and its components
- Describe how Data Warehouse works (ETL/ELT process)
- Compare OLAP vs OLTP systems in detail

---

## 📚 Topics Covered

### 1. Data Warehouse Definition & Role
- Central repository for BI activities
- Collects, integrates, and analyzes data from various sources
- Provides historical and current data for decision making

### 2. States of Data Warehouse

| State | Description |
|-------|-------------|
| **Data Warehouse Offline** | Data copied from operational system to another server; reporting doesn't affect operational performance |
| **Data Warehouse Online** | Regularly updated from operational database; real-time updates with every transaction |

### 3. Historical Perspective: Inmon vs Kimball

#### Bill Inmon – "The Father of Data Warehousing"
- **1980s:** Introduced "Corporate Information Factory" (CIF)
- **Approach:** Centralized, normalized data model
- **Output:** Enterprise Data Warehouse (EDW)
- **Focus:** Data integration through ETL processes

#### Ralph Kimball – Dimensional Modeling Pioneer
- **1990s:** Introduced "Data Warehouse Bus Architecture"
- **Approach:** Data marts (subject-specific warehouses)
- **Output:** Dimensional modeling (fact and dimension tables)
- **Focus:** Simplified data retrieval for business users

### 4. Four Characteristics of Data Warehouse

| Characteristic | Description |
|----------------|-------------|
| **Subject-Oriented** | Organized around major subjects (customer, product, sales) |
| **Integrated** | Combines data from multiple heterogeneous sources |
| **Time-Variant** | Stores historical data (5-10 years) |
| **Nonvolatile** | Data is read-only; no updates or deletions |

### 5. Types of Data Warehouses

| Type | Description |
|------|-------------|
| **Enterprise Data Warehouse (EDW)** | Central database serving entire enterprise |
| **Operational Data Store (ODS)** | Real-time refreshing for routine activities |
| **Data Mart** | Subset for specific department, region, or business unit |

### 6. Metadata Repository

**Definition:** Data defining warehouse objects

**Stores:**
- **Structural metadata:** Schema, views, dimensions, hierarchies
- **Operational metadata:** Data lineage, currency, monitoring information
- **Summarization algorithms**
- **Mapping from operational environment to DW**
- **Business data:** Business terms, ownership, policies

### 7. How Data Warehouse Works

1. **Extract:** Data from source systems (databases, files, APIs)
2. **Transform:** Clean, filter, manipulate data
3. **Load:** Load into data warehouse
4. **Access:** Users access via SQL queries, BI tools (Power BI, CRM)

### 8. OLAP vs OLTP – Detailed Comparison

| Feature | OLTP | OLAP |
|---------|------|------|
| **Purpose** | Transaction processing | Analytical processing |
| **Response Time** | Fast (milliseconds) | Varies (seconds to minutes) |
| **Data Structure** | Normalized (3NF) | Denormalized (Star/Snowflake) |
| **Data Updates** | Frequent (INSERT, UPDATE, DELETE) | Batch loads (no updates) |
| **History** | Current data only | Historical data (5-10 years) |
| **Users** | Operational staff | Analysts, managers |
| **Queries** | Simple, repetitive | Complex, ad-hoc |
| **Technology** | MySQL, Oracle, ACID | SQL Server Analysis Services, OLAP cubes |

### 9. Database vs Data Warehouse

| Aspect | Database (OLTP) | Data Warehouse (OLAP) |
|--------|----------------|----------------------|
| **Purpose** | Transaction processing | Analytics and reporting |
| **Data** | Real-time, current | Historical, aggregated |
| **Queries** | Simple CRUD operations | Complex analytical queries |
| **Design** | Normalized | Denormalized |

---

## 🖼️ Figures and Diagrams

> *Note: Images will be added to the `images/lecture_02/` folder*

### Figure 1: Data Warehouse States
*Diagram showing Offline vs Online states with data flow*

### Figure 2: Inmon vs Kimball Comparison
*Side-by-side comparison of both methodologies*

### Figure 3: Four Characteristics of Data Warehouse
*Visual representation of Subject-Oriented, Integrated, Time-Variant, Nonvolatile*

### Figure 4: Types of Data Warehouses (EDW, ODS, Data Mart)
*Hierarchy diagram showing relationships*

### Figure 5: Metadata Repository Structure
*Components and their relationships*

### Figure 6: How Data Warehouse Works
*ETL/ELT process flow diagram*

### Figure 7: OLAP vs OLTP Comparison Table
*Detailed comparison with icons and descriptions*

---

## 💡 Key Takeaways

1. **Data Warehouse is separate from operational databases** – Optimized for analytics, not transactions
2. **Inmon and Kimball offer complementary approaches** – Centralized EDW vs dimensional data marts
3. **Four characteristics define a DW** – Subject-Oriented, Integrated, Time-Variant, Nonvolatile
4. **Metadata is critical** – "Data about data" enables effective warehouse management
5. **OLAP vs OLTP serve different purposes** – One for transactions, one for analytics

---

## 📝 Quick Review Questions

1. What is the difference between Data Warehouse Offline and Data Warehouse Online?
2. How does Inmon's approach differ from Kimball's approach?
3. What are the four characteristics of a data warehouse? Explain each.
4. What is the difference between EDW, ODS, and Data Mart?
5. What information is stored in the Metadata Repository?
6. List 5 differences between OLAP and OLTP systems.

---

## 🔗 Related Resources

- [Lecture 1: Introduction to Data Warehousing](./Lecture_01_Introduction.pptx) – Foundation concepts
- [Lecture 4: Dimensional Modeling](./Lecture_04_Dimensional_Modeling.pdf) – Deep dive into schemas
- [PostgreSQL Connection Lab](../labs/postgres_connection.py) – Hands-on database connection

---

## 📖 References

- Sharda, R., Delen, D., & Turban, E. (2018). *Business Intelligence, Analytics, and Data Science: A Managerial Perspective*. Pearson.
- Inmon, W. H. (2005). *Building the Data Warehouse*. Wiley.
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit*. Wiley.

---

**Next Lecture:** [Lecture 3: NoSQL and Selected Topics](./Lecture_03_NoSQL_and_Selected_Topics.pptx)
