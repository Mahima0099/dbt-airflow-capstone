# **DBT + PostgreSQL + Apache Airflow Capstone Project**

This capstone project demonstrates a complete modern data pipeline using:

- **DBT** for data modeling and transformation  
- **PostgreSQL** as the warehouse  
- **Apache Airflow** for orchestration and automation

## 📁 Project Structure
project_ms_airflow/
├── dags/
│   └── dbt_airflow_dag.py
├── dbt/
│   ├── models/
│   │   ├── example/
│   │   │   ├── my_first_dbt_model.sql
│   │   │   ├── my_second_dbt_model.sql
│   │   │   └── staging/
│   │   │       ├── stg_mahima.sql
│   │   │       └── schema.yml
│   ├── macros/
│   │   └── delete_insert.sql
│   ├── snapshots/
│   ├── seeds/
│   ├── dbt_project.yml
│   └── profiles.yml
├── docker-compose.yml
└── README.md





