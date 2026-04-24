USE ynov_ci;

CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO utilisateurs (nom, email) VALUES 
('Adrien', 'adrien@example.com'),
('Julie', 'julie@example.com'),
('Thomas', 'thomas@example.com'),
('Sarah', 'sarah@example.com');