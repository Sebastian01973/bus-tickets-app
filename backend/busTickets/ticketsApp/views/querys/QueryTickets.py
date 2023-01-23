SQL_GENERAL_TICKET = """
select t.generate_date,t.departure_time, concat(u.name, ' ', u.last_name) as full_name, v.internal_number,r.destiny,t.total_value::integer, t.quantity::integer,
t.id,v.plate,b.nit,b.name as company_name
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_road" r on t.road_id = r.id
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where v.internal_number = %s and r.id = %s
and t.generate_date between to_date(%s,'YYYY-MM-DD') and to_date(%s,'YYYY-MM-DD')
order by t.generate_date desc 
"""

SQL_TICKET = """
select t.id ,t.generate_date, t.departure_time, concat(u.name, ' ', u.last_name) as nUser,r.destiny,t.quantity,t.total_value,
v.internal_number,v.plate, b.name as empresa, u2.name as name_client, u2.identification as client_identid
from "ticketsApp_ticket" t join "ticketsApp_boxoffice" bo on bo.id = t.box_office_id
join "ticketsApp_client" c on c.id = t.client_id join "ticketsApp_user" u on u.id = bo.user_id
join "ticketsApp_user" u2 on u2.id = c.user_id
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_vehicle" v on v.plate = t.vehicle_id
join "ticketsApp_business" b on b.nit = v.business_id
where bo.id = %s and t.id = %s
order by t.id desc
"""