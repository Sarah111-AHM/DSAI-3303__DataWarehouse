
---

### 5. Challenges of NoSQL for Data Warehousing

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| **Querying** | Limited SQL-like querying in some NoSQL systems | Use SQL-on-NoSQL tools (Presto, Drill) |
| **Data Consistency** | Eventual consistency may not suit all use cases | Choose databases with strong consistency options |
| **Expertise** | Learning curve for designing and optimizing NoSQL | Invest in training, use managed services |
| **Tooling** | Fewer BI tools support NoSQL natively | Use connectors, ODBC/JDBC drivers |

---

### 6. Data Warehouse Governance

#### Role-Based Access Control (RBAC)
- Grant users access based on their role (e.g., analyst, admin, viewer)
- Minimize over-permissions following principle of least privilege

#### Data Classification
- Define access levels for sensitive vs non-sensitive data
- Categories: Public, Internal, Confidential, Restricted

#### Auditing and Monitoring
- Track user activities to ensure compliance
- Detect anomalies and unauthorized access attempts

#### Compliance
- Align with regulations like GDPR, HIPAA, CCPA
- Maintain audit trails and data lineage

---

### 7. Data Warehouse Backup Strategies

#### Hardware Backup
- Deploy redundant servers and storage devices across data centers
- Use RAID configurations for disk redundancy
- Implement high availability (HA) clusters

#### Software Backup

| Backup Type | Description |
|-------------|-------------|
| **Full Backup** | Complete copy of all data (periodic, e.g., weekly) |
| **Incremental Backup** | Only changes since last backup (daily) |
| **Differential Backup** | Changes since last full backup |

#### Disaster Recovery Plan
- Test backup restoration regularly
- Maintain detailed:
  - **RTO (Recovery Time Objective):** Maximum acceptable downtime
  - **RPO (Recovery Point Objective):** Maximum acceptable data loss

**Best Practices:**
- Store backups in multiple locations (on-premises and cloud)
- Follow 3-2-1 backup rule: 3 copies, 2 media types, 1 off-site
- Automate backup verification

---

### 8. Data Cleaning

#### Why Data Cleaning?
- Remove inconsistencies, duplicates, and errors
- Improve data quality for reliable analytics
- Ensure accurate business decisions

#### Key Cleaning Processes

| Process | Description | Example |
|---------|-------------|---------|
| **Deduplication** | Eliminating redundant records | Remove duplicate customer entries |
| **Handling Missing Data** | Imputation or removal of incomplete records | Fill NULL values with default or median |
| **Standardization** | Consistent formatting | Dates: DD/MM/YYYY → YYYY-MM-DD |
| **Validation** | Ensuring data adheres to defined rules | Email format validation |
| **Outlier Detection** | Identifying and handling anomalies | Remove or cap extreme values |

---

### 9. Data Transformation

#### Purpose
Convert raw data into a structured format optimized for analysis and align with the data warehouse schema (star or snowflake models).

#### Common Transformation Techniques

| Technique | Description | Example |
|-----------|-------------|---------|
| **Aggregation** | Summarizing data | Total sales per region per month |
| **Data Enrichment** | Adding external data | Append demographic data to customer records |
| **Data Splitting/Merging** | Adjusting granularity | Split full name into first/last name |
| **Encoding** | Converting categorical to numerical | Gender: M/F → 1/0 |
| **Normalization** | Scaling numerical values | 0-1 range for ML models |
| **Type Conversion** | Changing data types | String dates to DATE type |

---

## 🖼️ Figures and Diagrams

> *Note: Images will be added to the `images/lecture_03/` folder*

### Figure 1: NoSQL Database Types
*Diagram showing four types: Document, Key-Value, Column, Graph with example databases*

### Figure 2: NoSQL Integration Architecture
*How NoSQL fits with data warehouse, BI tools, and analytics platforms*

### Figure 3: E-Commerce Personalization Architecture
*Complete flow from user activity to real-time recommendations*

### Figure 4: IoT Smart City Architecture
*Sensor data ingestion, storage, ML processing, and optimization flow*

### Figure 5: Data Governance Framework
*RBAC, data classification, auditing, compliance components*

### Figure 6: Backup Strategies (3-2-1 Rule)
*Visual representation of 3 copies, 2 media types, 1 off-site*

### Figure 7: Data Cleaning Process Workflow
*Step-by-step cleaning and transformation pipeline*

### Figure 8: ETL vs ELT with NoSQL
*Comparison of traditional ETL and modern ELT approaches*

---

## 💡 Key Takeaways

1. **NoSQL complements traditional data warehouses** – Not a replacement, but a solution for real-time, unstructured, and scalable use cases
2. **Schema flexibility enables agility** – Adapt to changing data requirements without migration
3. **Horizontal scaling is cost-effective** – Cloud-native NoSQL scales with demand
4. **Governance is critical** – Access control, auditing, and compliance ensure data security
5. **Data quality matters** – Cleaning and transformation are essential for reliable analytics
6. **Backup strategies protect business continuity** – RTO/RPO define acceptable loss and downtime
7. **NoSQL excels in real-time scenarios** – E-commerce personalization and IoT analytics are prime examples

---

## 📝 Quick Review Questions

### Basic Questions
1. What are the four types of NoSQL databases? Give an example of each.
2. What are the main strengths of NoSQL compared to relational databases?
3. Why would an e-commerce company use NoSQL for personalization?

### Advanced Questions
4. How does NoSQL handle scalability differently from relational databases?
5. What are the three main challenges of using NoSQL for data warehousing?
6. What is RBAC and why is it important for data warehouse governance?
7. What is the 3-2-1 backup rule?

### Application Questions
8. Design a NoSQL data warehouse architecture for a social media analytics platform.
9. Compare and contrast data cleaning vs data transformation.
10. What is the difference between RTO and RPO? Why are they important?

---

## 📊 Summary Table: NoSQL vs Traditional DW

| Feature | Traditional DW | NoSQL as DW |
|---------|----------------|-------------|
| **Schema** | Fixed, predefined | Flexible, schema-on-read |
| **Scaling** | Vertical | Horizontal |
| **Query Language** | SQL | API, limited SQL |
| **Data Types** | Structured | All types |
| **Latency** | Batch (minutes-hours) | Real-time (milliseconds) |
| **Consistency** | Strong | Often eventual |
| **Best For** | BI, reporting | Real-time, IoT, personalization |
| **Cost Model** | High upfront | Pay-as-you-go |

---

## 🔗 Related Resources

- [Lecture 2: Introduction to DW](./Lecture_02_Introduction_to_DW.pdf) – Foundation concepts
- [Lecture 4: Dimensional Modeling](./Lecture_04_Dimensional_Modeling.pdf) – Traditional DW modeling
- [PostgreSQL Functions Reference](../exams/postgresql_functions_reference.pdf) – SQL functions for transformation
- [PostgreSQL Connection Lab](../labs/postgres_connection.py) – Hands-on database practice

---

## 📖 References

- Sharda, R., Delen, D., & Turban, E. (2018). *Business Intelligence, Analytics, and Data Science: A Managerial Perspective*. Pearson.
- MongoDB Documentation. (2023). *NoSQL Explained*.
- Amazon Web Services. (2023). *What is NoSQL?*
- Apache Cassandra Documentation. (2023). *NoSQL for Big Data*.

---

## 📌 Next Lecture

**[Lecture 4: Dimensional Modeling](./Lecture_04_Dimensional_Modeling.pdf)** – Deep dive into Star Schema, Snowflake Schema, Facts, and Dimensions

---

*For lab exercises, see the [`labs/`](../labs/) folder.*
*For exam preparation, see the [`exams/`](../exams/) folder.*
