![Repo Size](https://img.shields.io/github/repo-size/mahima0099/dbt-airflow-capstone)
![Last Commit](https://img.shields.io/github/last-commit/mahima0099/dbt-airflow-capstone)
![Top Language](https://img.shields.io/github/languages/top/mahima0099/dbt-airflow-capstone)
![License](https://img.shields.io/github/license/mahima0099/dbt-airflow-capstone)

# **DBT + PostgreSQL + Apache Airflow Capstone Project**

This capstone project demonstrates a complete modern data pipeline using:

- **DBT** for data modeling and transformation  
- **PostgreSQL** as the warehouse  
- **Apache Airflow** for orchestration and automation  

---

## **Project Structure**

```
project_ms_airflow/
├── dags/
│   └── dbt_airflow_dag.py
├── dbt/
│   └── models/
│       └── example/
│           ├── my_first_dbt_model.sql
│           ├── my_second_dbt_model.sql
│           └── staging/
│               ├── stg_mahima.sql
│               └── schema.yml
│   └── macros/
│       └── delete_insert.sql
├── snapshots/
├── seeds/
├── dbt_project.yml
├── profiles.yml
├── docker-compose.yml
└── README.md
```

---

## **How to Run the Project**

1. **Clone the repository**  
```bash
git clone https://github.com/mahima0099/dbt-airflow-capstone.git
cd dbt-airflow-capstone
```

2. **Start the environment**  
```bash
source venv/bin/activate
airflow db init
airflow webserver
airflow scheduler
```

3. **Open Airflow in your browser**  
[http://localhost:8080](http://localhost:8080)

---

## **License**

This project is licensed under the MIT License.












