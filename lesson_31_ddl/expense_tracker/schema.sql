```sql 
DROP TABLE IF EXISTS expenses; 
DROP TABLE IF EXISTS categories; 
DROP TABLE IF EXISTS users; 

CREATE TABLE users ( 
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
); 

CREATE TABLE categories ( 
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    user_id INTEGER NOT NULL, 
    name TEXT NOT NULL, 
    
    CONSTRAINT unique_category_per_user 
    UNIQUE(user_id, name), 
    
    FOREIGN KEY (user_id) 
        REFERENCES users(id) 

); 

CREATE TABLE expenses ( 
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    
    user_id INTEGER NOT NULL, 
    
    category_id INTEGER NOT NULL, 
    
    amount NUMERIC(10,2) NOT NULL 
        CHECK(amount > 0), 
        
    expense_date DATE NOT NULL, 
    
    description TEXT, 
    
    created_at TIMESTAMP NOT NULL 
        DEFAULT CURRENT_TIMESTAMP, 
    
    FOREIGN KEY (user_id) 
        REFERENCES users(id), 
    
    FOREIGN KEY (category_id) 
        REFERENCES categories(id) 

);