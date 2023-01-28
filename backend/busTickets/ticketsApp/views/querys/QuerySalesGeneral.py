
SQL_TOTAL_COMPANY_SALES = """
select sum(t.total_value::integer) as total, b.name, b.nit
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where bo.id = %s and t.generate_date
between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
group by b.name, b.nit
"""

SQL_SALES_BY_COMPANY_DATE = """
select v.internal_number,t.generate_date,t.departure_time, concat(u.name,' ',u.last_name) as full_name, r.destiny,t.total_value::integer as total,
sum(t.quantity::integer) as quantity,t.id,b.name,v.plate
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_road" r on t.road_id = r.id
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where b.nit = %s and t.generate_date
between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
group by t.generate_date,u.name,u.last_name,v.internal_number,r.destiny,t.departure_time,t.departure_time,t.id,b.name,v.plate,t.quantity
order by t.id desc
"""

SQL_SALES_BY_BOX_OFFICE = """
select v.internal_number,t.generate_date,t.departure_time, concat(u.name,' ',u.last_name) as full_name, r.destiny,t.total_value::integer as total,
sum(t.quantity::integer) as quantity,t.id,b.name,v.plate
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_road" r on t.road_id = r.id
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where bo.id = %s and b.nit = %s and t.generate_date
between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
and t.total_value <> '0'
group by t.generate_date,u.name,u.last_name,v.internal_number,r.destiny,t.departure_time,t.departure_time,t.id,b.name,v.plate,t.quantity
order by t.generate_date,v.internal_number,t.departure_time desc
"""

SQL_SALES_BY_VEHICLE = """
select v.internal_number,t.generate_date,t.departure_time, concat(u.name,' ',u.last_name) as full_name, r.destiny,t.total_value::integer as total,
sum(t.quantity::integer) as quantity,t.id,b.name,v.plate
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_road" r on t.road_id = r.id
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where v.internal_number = %s and t.total_value <> '0' and t.generate_date
between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
group by t.generate_date,u.name,u.last_name,v.internal_number,r.destiny,t.departure_time,t.departure_time,t.id,b.name,v.plate,t.quantity
order by t.id desc
"""

SQL_SALES_BY_DESTINY_AND_COMPANY = """
select v.internal_number,t.generate_date,t.departure_time, concat(u.name,' ',u.last_name) as full_name, r.destiny,t.total_value::integer as total,
sum(t.quantity::integer) as quantity,t.id,b.name,v.plate
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id join "ticketsApp_business" b on v.business_id = b.nit
where t.total_value <> '0' and t.generate_date
between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd') and r.id = %s and b.nit = %s
group by t.generate_date,u.name,u.last_name,v.internal_number,r.destiny,t.departure_time,t.departure_time,t.id,b.name,v.plate,t.quantity
order by t.id desc
"""

