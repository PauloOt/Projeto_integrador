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


INSERT INTO clientes (nome, email, telefone) VALUES
('Lucas Almeida', 'lucas.almeida@email.com', '11999998888'),
('Mariana Santos', 'mariana.santos@email.com', '11988887777'),
('Rafael Oliveira', 'rafael.oliveira@email.com', '11977776666'),
('Patrícia Gomes', 'patricia.gomes@email.com', '11966665555'),
('Thiago Costa', 'thiago.costa@email.com', '11955554444'),
('Fernanda Rocha', 'fernanda.rocha@email.com', '11944443333'),
('André Martins', 'andre.martins@email.com', '11933332222'),
('Juliana Ferreira', 'juliana.ferreira@email.com', '11922221111'),
('Gabriel Lima', 'gabriel.lima@email.com', '11911110000'),
('Camila Souza', 'camila.souza@email.com', '11900009999');


INSERT INTO carros (marca, modelo, ano, cliente_id) VALUES
('Honda', 'Fit', 2017, 3),
('Ford', 'Ka', 2018, 4),
('Chevrolet', 'Cruze', 2019, 5),
('Volkswagen', 'Polo', 2020, 6),
('Toyota', 'Yaris', 2021, 7),
('Hyundai', 'Creta', 2022, 8),
('Jeep', 'Compass', 2016, 9),
('Renault', 'Duster', 2015, 10),
('Nissan', 'Sentra', 2014, 11),
('Kia', 'Soul', 2013, 12);


SELECT * FROM clientes;
SELECT * FROM carros;

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