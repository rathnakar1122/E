 ++++++++++++++++++:
7:45 AM 11.11.2024
++++++++++++++++++:

*******************:
 GCP Data Engineer
*******************:

Session Title - Introduction to Databases and Database Management Systems (DBMS):
Session Duration - 1 Hour:

Learning Objectives:
    •	Understand the fundamental purpose of databases in managing and querying data.
    •	Recognize different types of databases and the role of Database Management Systems (DBMS) in data engineering.
    •	Become familiar with popular cloud-based databases and data warehousing solutions like MySQL, BigQuery, Redshift, RDS and Athena.
    
•	Objective: Understand the purpose and types of databases in data engineering.


Recap: - Data Eng: Cloud Comuting: Different Service Models[IaaS, PaaS, SaaS, FaaS], Diff Cloud and OnPrem: Imp of SQL and Python

Pre-requisites: Cloud Accounts[AWS, GCP] - CC 
                - to have hands-on exp: Querying in MySQL, BigQuery, Redshift, RDS and Athena
                
Key-Words: Database, DBMS 

1. What is DATA?:

Data is a collection of facts, measurements, observations, or words that can be used to generate information: 

Sample1:
    Collection of info/data: 23,45,us, aus,34, uk, 66 -null - facts[numerals]
            Extra Point:
                Countries --> us, uk, aus, japan
                Population in Millions --> 23, 45, 34, 66
                
                System Collection Process:
                    --> File System: Google Sheets, Excel Sheets (65*)   
                                   Country Population
                                   us       23
                                   uk       34
                    --> Web Application/Mobile Application
                        DBMS System: Scalability
                    
    Meaningful DATA/information: 
        - Context Adding: Those are the ages of the people in village
                          The marks of the students
                          The balance of tokens in a bucket
                          the number of people in a country(in millions)
                          the avg intake of milk by humans in a specific states - ltrs
                          
        - Examples:
        Data can include the number of people in a country, the value of sales of a product, or the number of times a country has won a cricket match.
        
        Types:
        Data can be classified as qualitative or quantitative. Qualitative data captures subjective qualities, while quantitative data is numerical and can be measured.
        
        Sources:
        Data can come from many sources, including user input, sensors, or algorithms. 
            -- SignUp with the different CRM Servers, Application Servers, E-Commerce site
            -- Weather Report
            -- Mobility Sensors
            -- Speed Sensors
            -- Gamming Applications
        -- Importance:
            Data is the starting point for processes that deliver informed insights in scientific research or business analytics.
Ref: 
https://bloomfire.com/blog/data-vs-information/

2. What is Database?

A database is a structured collection of data that is stored electronically and organized for easy access, retrieval, and modification:

Key-Words: Database -  
           a place/storage system wherein the data actually resides in a designed pattern...
           
           DBMS - It mainly depends on the software system you are utilisiting for storing your data
The goal of the databse: Storing and retriving and Manipulation


3. What is DBMS?

DBMS stands for Database Management System, which is a software tool that helps users create, store, manage, and retrieve data in a database.:

MySQL 

Create database e-commerce;
use e-commerce;

sql - create tables - 

Travelling - Seat 

Sleeper Coaches - 

Semi-Sleeper 

No-Sleeper 

DATA - Structure(Designment), Semi-Structured(desingn), and Un-Structured -- 


Windows OS, Mac OS --- 

DBMS --> SQL, NoSQL and Warehouse --->


Types of databases:
    - 3 Types:
        - RDBMS: MySQL, PostgreSQL, Oracle, DB2, Netizza, Terradata
            - OLTP - Transactional Servers
            - It actually stores the data in tabular format - Tables - 
            - Table will be having predifined/fixed schemas
            - Schema is nothing but - columns and rows
            - SQL is the language we use to communicate with these type of databases
            - Real-World - Retailer Shops - Customer, Order, Products
                                          - And establish relation among different tables 
            
        - [DATA] - [DATABASE]- Structured data -- [DBMS] - Handling with a Software -- [RDBMS] - Relational Model (Concept)
        
        - Order - 1 lakh orders [Today]
        
        - NoSQL Databases: MongoDB(Document Store), Cassandra(column-family), Bigtable(column-family)
            - Non - Relational Dabases
            - these are schema-flexible
            - semi-structured, unstructured data support
            - Types - documets, key-value stores, column-family stores 
            
        - Data Warehouses: BigQuery, Redshift, Snowflake
            - OLAP - Analytical Platforms
            - analytical queries 
            - decision-making 
            
        - Order - 1 lakh orders [ yesterday] - old(historical)
        - Order - 1 lakh orders [Today]
            - decision-making - No of orders placed from different countries and the top 5 countries from which country 
            - analytical queries - 
                with cte as(select count(*) as no_of_orders from orders group by country)
                select * from cte order by  no_of_orders desc limit 5;
            - Complex Queries

Listing products:

MySQL
Cloud SQL(GCP)
BigQuery(GCP)
Redshift(AWS)
RDS(AWS)
and Athena(AWS)
Bigtable(GCP)
Spanner(GCP)