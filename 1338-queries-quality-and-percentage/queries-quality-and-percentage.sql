select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(count(case when rating < 3 then 1 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;