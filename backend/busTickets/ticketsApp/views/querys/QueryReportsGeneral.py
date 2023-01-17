
SQL_QUERY_REPORT_GENERAL = """
    select 1 as id, v.internal_number, t.generate_date, t.departure_time, concat(u.name, ' ', u.last_name), r.destiny, t.total_value::integer as total,
v.plate,b.name, sum(t.quantity::integer) as quantity
from "ticketsApp_ticket" t join "ticketsApp_vehicle" v on t.vehicle_id = v.plate
join "ticketsApp_client" c on t.client_id = c.id join "ticketsApp_user" u on c.user_id = u.id
join "ticketsApp_road" r on t.road_id = r.id join "ticketsApp_business" b on v.business_id = b.nit
where b.name = %s and t.departure_time between to_date(%s,'yyyy-MM-dd') and to_date(%s,'yyyy-MM-dd')
group by t.departure_time, v.internal_number, t.generate_date, u.last_name, u.name, r.destiny, t.total_value, v.plate, b.name
"""