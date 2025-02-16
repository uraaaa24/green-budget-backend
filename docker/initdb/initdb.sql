\c postgres;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  display_name VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE,
  image VARCHAR(255), 
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
  category_id INT,
  amount INT NOT NULL CHECK (amount >= 0),
  transaction_type VARCHAR(255) CHECK (transaction_type IN ('expense', 'income')),
  note VARCHAR(255),
  date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

INSERT INTO users (display_name, email)
VALUES
  ('test', 'test@example.com'),
  ('test2', 'test2@example.com');

INSERT INTO categories (name, description, transaction_type)
VALUES 
  ('食費', '外食やスーパー、コンビニでの食事関連の支出。', 'expense'),
  ('日用品', '洗剤やトイレットペーパーなどの生活必需品。', 'expense'),
  ('交通費', '電車、バス、ガソリン代などの移動費。', 'expense'),
  ('住居費', '家賃、ローン、光熱費などの住居関連の支出。', 'expense'),
  ('通信費', 'スマホ料金やインターネット料金。', 'expense'),
  ('娯楽・趣味', 'サブスク、映画、ゲームなどの娯楽費。', 'expense'),
  ('交際費', '飲み会やプレゼントなどの交際関連の費用。', 'expense'),
  ('医療・美容', '病院、薬、美容院などの健康・美容関連。', 'expense'),
  ('貯金・投資', '貯金や証券投資、積立など。', 'expense'),
  ('その他', '分類しづらい支出。', 'expense'),
  ('給料', '仕事の収入。', 'income'),
  ('副収入', 'フリーランスや副業の収入。', 'income'),
  ('ボーナス', '年末や業績によるボーナス。', 'income'),
  ('その他の収入', '予期しない収入や追加の収入。', 'income');

INSERT INTO transactions (user_id, category_id, amount, transaction_type, note, date)
VALUES ((SELECT id FROM users WHERE email = 'test@example.com'), 1, 100, 'expense', 'test', '2021-01-01'),
  ((SELECT id FROM users WHERE email = 'test@example.com'), 2, 200, 'income', 'test2', '2021-01-02'),
  ((SELECT id FROM users WHERE email = 'test2@example.com'), 3, 300, 'expense', 'test3', '2021-01-03');
