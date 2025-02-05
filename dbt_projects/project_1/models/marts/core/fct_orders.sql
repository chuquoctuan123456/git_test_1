with orders as (
    select *
    from {{ ref('staging__orders') }}
)

select * from orders