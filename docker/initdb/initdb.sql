\c postgres;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  firebase_id VARCHAR(255),
  display_name VARCHAR(255),
  email VARCHAR(255)
);

DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id UUID,
  category_id INT,
  amount DECIMAL(10, 2),
  transaction_type VARCHAR(255),
  description VARCHAR(255),
  date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (firebase_id, display_name, email)
VALUES ('123', 'test', 'test@example.com'),
       ('456', 'test2', 'test2@example.com');

INSERT INTO transactions (user_id, category_id, amount, transaction_type, description, date)
VALUES ((SELECT id FROM users WHERE firebase_id = '123'), 1, 100.00, 'expense', 'test', '2021-01-01'),
       ((SELECT id FROM users WHERE firebase_id = '123'), 2, 200.00, 'income', 'test2', '2021-01-02'),
       ((SELECT id FROM users WHERE firebase_id = '456'), 1, 300.00, 'expense', 'test3', '2021-01-03');
