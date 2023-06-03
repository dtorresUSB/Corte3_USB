DROP TABLE IF EXISTS users ;


CREATE TABLE users (
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) PRIMARY KEY NOT NULL,
  password VARCHAR(100) NOT NULL,
  last_login timestamp,
  created_at timestamp NOT NULL,
  updated_at timestamp NOT NULL
);
