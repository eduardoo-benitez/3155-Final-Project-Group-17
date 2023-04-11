DROP DATABASE IF EXISTS DatabaseDesignAssignment;

CREATE DATABASE IF NOT EXISTS DatabaseDesignAssignment;

CREATE TABLE users (
    email  VARCHAR(40) NOT NULL,
    username    CHAR(40) NOT NULL,
    password VARCHAR(40) NOT NULL,
    account_id   SERIAL,
    PRIMARY KEY (account_id)
);

CREATE TABLE posts (
    title  VARCHAR(40) NOT NULL,
    username    CHAR(40) NOT NULL,
    rating ENUM('1','2','3','4','5'),
    author_id INT NOT NULL,
    PRIMARY KEY (author_id),
	FOREIGN KEY (author_id) REFERENCES users(account_id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE userProfile (
    username    CHAR(40) NOT NULL,
    account_id INT NOT NULL,
    numPosts INT UNSIGNED AUTO_INCREMENT NOT NULL,
    PRIMARY KEY (account_id),
	FOREIGN KEY (account_id) REFERENCES users(account_id) ON UPDATE CASCADE ON DELETE SET NULL
);