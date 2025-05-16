{{ config(
    materialized='incremental',
    unique_key='emp_id',
    pre_hook="{{ delete_insert() }}"
) }}

with raw_data_source as (

    select 
        1 as emp_id,
        'Mahima Shah' as full_name,
        '2000-06-08' as birth_date,
        '2023-01-15' as doj,
        current_date as record_date

)

select 
    emp_id,
    full_name,
    birth_date,
    doj,
    record_date
from raw_data_source
