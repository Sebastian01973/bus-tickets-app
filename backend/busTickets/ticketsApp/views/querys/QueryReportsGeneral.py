
SQL_QUERY_REPORT_GENERAL = """
select v.internal_number, t.generate_date, t.departure_time, concat(u.name, ' ', u.last_name) as full_name, r.destiny, t.total_value,
v.plate,b.name, sum(t.quantity::integer) as quantity
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_client" c on t.client_id = c.id join "ticketsApp_user" u on c.user_id = u.id
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_business" b on v.business_id = b.nit
where b.nit = %s and t.departure_time between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
group by t.departure_time, v.internal_number, t.generate_date, u.last_name, u.name, r.destiny, t.total_value, v.plate, b.name
"""

SQL_REPORT_GENERAL_TOTAL = """
select v.plate,v.internal_number,concat(u.name,' ',u.last_name) as name,sum(t.total_value::integer) as total,b.name
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_user" u on v.user_id = u.id
join "ticketsApp_business" b on v.business_id = b.nit
where t.generate_date between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
    and t.total_value NOT IN ('0') and b.nit = %s
group by v.plate,v.internal_number,b.name,u.name,u.last_name
order by v.internal_number ASC
"""

SQL_PURCHASE_BY_CLIENT = """
select v.internal_number,t.generate_date,t.departure_time, concat(u.name, ' ', u.last_name) as full_name, r.destiny, sum(t.total_value::integer) as total,
sum(t.quantity::integer) as quantity, t.id, v.plate,b.nit
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_client" c on t.client_id = c.id join "ticketsApp_user" u on c.user_id = u.id
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_business" b on v.business_id = b.nit
where c.id = %s and t.generate_date BETWEEN to_date(%s,'yyyy-MM-dd') AND to_date(%s,'yyyy-MM-dd')
AND t.total_value <> '0' and b.nit = %s
group by v.internal_number, t.generate_date, t.departure_time, u.name, u.last_name, r.destiny, t.id, v.plate, b.nit
"""

SQL_USER_REPORT = """
select concat( u.name,' ', u.last_name) as full_name,u.identification,r.destiny,sum(t.total_value::integer) as total,sum(t.quantity::integer) as quantity
from "ticketsApp_ticket" t
    join "ticketsApp_road" r on t.road_id = r.id
    join "ticketsApp_boxoffice" b on t.box_office_id = b.id
    join "ticketsApp_user" u on b.user_id = u.id
    where u.identification = %s and t.generate_date between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
    AND t.total_value <> '0'
group by u.name, u.last_name, u.identification, r.destiny
"""

SQL_GENERAL_USER_REPORT = """
select v.internal_number, t.generate_date,t.departure_time, concat(u.name,' ',u.last_name) as full_name, r.destiny,t.total_value, SUM(t.quantity) as quantity
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_boxoffice" bo on t.box_office_id = bo.id join "ticketsApp_user" u on bo.user_id = u.id
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_business" b on v.business_id = b.nit
where t.total_value not in ('0') and t.generate_date between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
and b.nit = %s and bo.id = %s
group by t.id,v.internal_number, t.generate_date, t.departure_time, u.name, u.last_name, r.destiny, t.total_value
order by t.id desc
"""

SQL_PAYROLL_REPORT = """
select concat(u.name, ' ', u.last_name) as nUser, p.date, p.date_start,p.date_end,v.internal_number,v.plate
from "ticketsApp_payroll" p join "ticketsApp_boxoffice" b on p."boxOffice_id" = b.id
join "ticketsApp_user" u on b.user_id = u.id join "ticketsApp_vehicle" v on p.vehicle_id = v.plate
where p.date between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
and b.id = %s
"""

"""
Reporte por hora TABLA Assitance
Reporte despachos por usuario (Descuentos por usuario ingeniero Andres) TABLA Planilla 
"""




