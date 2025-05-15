
CREATE DATABASE sistema_carros;


USE sistema_carros;


CREATE TABLE carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano INT NOT NULL,
    cor VARCHAR(50),
    valor DECIMAL(10,2)
);

SELECT * FROM carros;