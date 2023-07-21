/*
Considere uma tabela chamada "Customers" que contém as seguintes colunas:

ID (inteiro, chave primária)
Name (texto)
Email (texto)
Age (inteiro)
City (texto)
Crie uma instrução SQL que:
   
Insira 3 novos clientes  na tabela Customers. Os clientes devem ter as seguintes informações:
  
Nome: João, E-mail: joao@email.com, Idade: 30, Cidade: São Paulo
Nome: Maria, E-mail: maria@email.com, Idade: 25, Cidade: Rio de Janeiro
Nome: Pedro, E-mail: pedro@email.com, Idade: 35, Cidade: Belo Horizonte
Atualize a idade de João para 31 anos.

Exclua o registro de Pedro da tabela.

Selecione o nome e a cidade de todos os clientes que moram em São Paulo.

Selecione o nome e o e-mail de todos os clientes com idade superior a 26 anos.
*/


create table Customers (
  id int not null,
  nome varchar(20) not null,
  email varchar(50) not null,
  age int not null,
  city varchar(30)
  );

insert into Customers(id,nome,email,age,city) values (42424,'luca','x@gmail.com',34,'New');
insert into Customers(id,nome,email,age,city) values (32333,'Gon','x@gmail.com',34,'New');
insert into Customers(id,nome,email,age,city) values (67677,'Luis','x@gmail.com',34,'New');

UPDATE Customers
SET 'age' = 43
WHERE nome = 'luca';

UPDATE Customers
SET 'age' = 56
WHERE nome = 'Gon';

UPDATE Customers
SET 'age' = 23
WHERE nome = 'Luis';

DELETE FROM Customers
WHERE id = 67677;

select * from Customers where age > 30;
