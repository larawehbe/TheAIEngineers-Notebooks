# 🔧 Setting Up PostgreSQL for Module 3

## ✅ 1. Install PostgreSQL
### 🖥️ macOS

brew install postgresql
brew services start postgresql
### 🖥️ Ubuntu / Debian

sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
### 🖥️ Windows

Download the installer from: https://www.postgresql.org/download/windows/
During setup, choose a username (e.g., postgres) and password.
After installation, open "SQL Shell (psql)" or use terminal.

## ✅ 2. Access PostgreSQL from Terminal
```psql postgres ```

If needed on ubuntu or Mac, use:

```sudo -u postgres psql``` 

## ✅ 3. Create Role and Database for Your App
Once inside the PostgreSQL prompt (psql), run the following:

```sql
-- Create a new user
CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';

-- Allow the user to create databases (optional)
ALTER ROLE myuser CREATEDB;

-- Create the app database
CREATE DATABASE myappdb OWNER myuser;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE myappdb TO myuser;

-- Exit
\q
```
Replace myuser, mypassword, and myappdb with values relevant to your app.
