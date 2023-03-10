select * from customers c
inner join employees e on c.salesRepEmployeeNumber = e.employeeNumber
inner join offices o on e.officeCode = o.officeCode
inner join payments p on c.customerNumber = p.customerNumber
inner join orders od on c.customerNumber = od.customerNumber
inner join orderdetails d on od.orderNumber = d.orderNumber
inner join products pr on d.productCode = pr.productCode
inner join productlines pl on pr.productLine = pl.productLine; 

-- Como selecionar itens específicos e renomear colunas
select customerName as Nome, phone as Telefone, e.firstName as Funcionário 
from customers c
inner join employees e on c.salesRepEmployeeNumber = e.employeeNumber;

-- Como selecionar utilizando Filtros
select * from customers where country = 'USA' and city in ('San Francisco', 'Las vegas');

-- Ordenando os dados
select * from customers where country = 'France' and creditLimit > 10000
order by customerName;

-- Como selecionar algo que comece, termine ou contenha determinada palavra
select * from customers where customerName like '%mini%';

-- Como contar os registros e agrupar
select count(*) as totalClientes from customers
where creditLimit > 25000;

select country, count(*) from customers
group by country
order by 1; 