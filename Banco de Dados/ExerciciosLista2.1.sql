create database warehouse2;

create table productlines(
	id bigint not null auto_increment,
    textDescription varchar(200) not null,
    htmlDescription varchar(200) not null,
    image varchar(1000) not null,
    primary key(id)
);

insert into productlines (textDescription, htmlDescription, image) values
("Produtos de Limpeza", "<h1>Produtos de Limpeza</h1>", "http://google.com"), ("Açougue", "<h1>Açougue</h1>", "http://microsoft.com");

create table products(
	id bigint not null auto_increment,
    name varchar(100) not null,
    productLineFK bigint not null,
    scale float,
    vendor varchar(100) not null,
    description varchar(100),
    quantity float not null,
    price float not null,
    msrp float,
    primary key(id),
    foreign key(productLineFK) references productLines(id)
);

insert into products (name, productLineFK, vendor, quantity, price) values
("Sabonete", 1, "Lux", 300, 2.6), ("Shampoo", 1, "Palmolive", 100, 19), ("Contra Filé", 2, "Friboi", 400, 59);

create table offices(
	id bigint not null auto_increment,
    city varchar(100) not null,
    phone varchar(13) not null,
    address1 varchar(150) not null,
    address2 varchar(150),
    state varchar(100) not null,
    postalCode varchar(10),
    primary key(id)
);

create table employees(
	id bigint not null auto_increment,
    lastName varchar(100) not null,
    firstName varchar(100) not null,
    email varchar(100) not null,
    officeFK bigint not null,
    job varchar(100),
    primary key(id),
    foreign key(officeFK) references offices(id)
);

create table customers(
	id bigint not null auto_increment,
    name varchar(100) not null,
    phone varchar(13) not null,
    address varchar(100) not null,
    address2 varchar(100),
    city varchar(100) not null,
    state varchar(100) not null,
    country varchar(100) not null,
    postalCode varchar(10),
    creditLmit float not null,
    employeeFK bigint not null,
    primary key(id),
    foreign key(employeeFK) references employees(id)
);

create table payments(
	id bigint not null auto_increment,
    customerFK bigint not null,
    paymentDate datetime not null default now(),
    amount float not null,
    primary key(id),
    foreign key (customerFK) references customers(id)
);

create table orders(
	id bigint not null auto_increment,
    orderDate datetime not null default now(),
    requiredDate datetime not null default now(),
    shippedDate datetime not null default now(),
    status varchar(1) not null,
    comments varchar(100),
    customerFK bigint not null,
    primary key(id),
    foreign key (customerFK) references customers(id)
);

create table orderDetails(
	id bigint not null auto_increment,
    productFK bigint not null,
    orderFK bigint not null,
    quantity float not null,
    price float not null,
    primary key(id),
    foreign key (productFK) references products(id),
    foreign key (orderFK) references orders(id)
);
