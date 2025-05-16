{% macro delete_insert() %}
  delete from {{ this }}
  where emp_id in (
    select emp_id from {{ ref('raw_data_source') }}
  )
{% endmacro %}
