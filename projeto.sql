CREATE DATABASE sistema_carros;
USE sistema_carros;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INT,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
    
);

SELECT * FROM clientes;
SELECT * FROM carros;

SELECT carros.id, marca, modelo, ano, clientes.nome
FROM carros
JOIN clientes ON carros.cliente_id = clientes.id;

SELECT 
    clientes.id AS cliente_id,
    clientes.nome AS cliente_nome,
    clientes.email,
    carros.id AS carro_id,
    carros.marca,
    carros.modelo,
    carros.ano
FROM clientes
LEFT JOIN carros ON clientes.id = carros.cliente_id;




