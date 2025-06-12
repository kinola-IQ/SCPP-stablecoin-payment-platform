
-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS stablecoin;

-- Switch to the 'stablecoin' database
USE stablecoin;

-- Remove the 'wallets' table if it exists (to avoid conflicts during creation)
DROP TABLE IF EXISTS wallets;

-- Remove the 'users_registration' table if it exists
DROP TABLE IF EXISTS users_registration;

-- Create the 'users_registration' table to store user details
CREATE TABLE users_registration (
    user_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-incrementing primary key
    Full_Name NVARCHAR(100),               -- User's full name
    email NVARCHAR(100),                   -- User's email address
    Password NVARCHAR(255),                -- User's password (should be hashed for security)
    country NVARCHAR(20)                   -- User's country
);

-- Create the 'wallets' table to store wallet balances and status
CREATE TABLE wallets (
    wallet_id UNIQUEIDENTIFIER DEFAULT NEWID() PRIMARY KEY, -- Unique wallet ID generated automatically
    user_id INT NOT NULL,                                   -- Foreign key linking to users_registration
    email NVARCHAR(100),                                    -- Email associated with the wallet
    cNGN REAL DEFAULT 0,                                    -- Balance in cNGN (default 0)
    GBP REAL DEFAULT 0,                                     -- Balance in GBP (default 0)
    USDx REAL DEFAULT 0,                                    -- Balance in USDx (default 0)
    EURx REAL DEFAULT 0,                                    -- Balance in EURx (default 0)
    wallet_status VARCHAR(10) NOT NULL CHECK (wallet_status IN ('active', 'suspended', 'closed')), -- Wallet status with allowed values
    creation_date DATETIME DEFAULT GETDATE(),               -- Timestamp of wallet creation
    FOREIGN KEY (user_id) REFERENCES users_registration(user_id) -- Enforce relationship with users_registration
);
