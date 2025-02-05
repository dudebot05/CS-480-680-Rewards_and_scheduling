-- Create the database first
CREATE DATABASE IF NOT EXISTS loyals_database;
USE loyals_database;

CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    total_spent DECIMAL(10, 2) NOT NULL DEFAULT 0,
    rewards_balance DECIMAL(10, 2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);clients