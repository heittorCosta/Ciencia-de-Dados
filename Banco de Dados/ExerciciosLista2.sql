select c.customerName as Cliente, p.productName as Produto 
from orders o 
inner join orderdetails od on o.orderNumber = od.orderNumber
inner join products p on od.productCode = p.productCode
inner join customers c on o.customerNumber = c.customerNumber
where p.productName = '2001 Ferrari Enzo';


select c.customerName, count(*) as Total 
from orders o
inner join customers c on o.customerNumber = c.customerNumber
group by c.customerNumber
having total > 2
order by 2 desc;


select * from orders;