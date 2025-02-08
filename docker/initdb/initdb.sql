\c postgres;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  display_name VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255),
  transaction_type VARCHAR(255) CHECK (transaction_type IN ('expense', 'income')),
  user_id UUID,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id UUID NOT NULL,
  category_id INT NOT NULL,
  amount INT NOT NULL CHECK (amount >= 0),
  transaction_type VARCHAR(255) CHECK (transaction_type IN ('expense', 'income')),
  note VARCHAR(255),
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

INSERT INTO users (display_name, email)
VALUES
  ('test', 'test@example.com'),
  ('test2', 'test2@example.com');

INSERT INTO categories (name, description, transaction_type)
VALUES 
  ('Food', 'Expenses for daily meals and dining out.', 'expense'),
  ('Housing', 'Rent, utilities, and internet bills.', 'expense'),
  ('Transportation', 'Public transport, fuel, taxi fares.', 'expense'),
  ('Entertainment', 'Movies, games, hobbies, and travel.', 'expense'),
  ('Household Items', 'Daily necessities like cleaning supplies.', 'expense'),
  ('Other Expenses', 'Miscellaneous expenses not listed above.', 'expense'),
  ('Salary', 'Monthly income from work.', 'income'),
  ('Side Income', 'Earnings from freelancing or side jobs.', 'income'),
  ('Bonus', 'Year-end or performance bonuses.', 'income'),
  ('Other Income', 'Unexpected or additional income.', 'income');

INSERT INTO transactions (user_id, category_id, amount, transaction_type, note, date)
VALUES ((SELECT id FROM users WHERE email = 'test@example.com'), 1, 100, 'expense', 'test', '2021-01-01'),
  ((SELECT id FROM users WHERE email = 'test@example.com'), 2, 200, 'income', 'test2', '2021-01-02'),
  ((SELECT id FROM users WHERE email = 'test2@example.com'), 3, 300, 'expense', 'test3', '2021-01-03');
