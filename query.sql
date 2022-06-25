USE url_shortner;

-- CREATE DATABASE url_shortner;

CREATE TABLE urlshort(
id INT PRIMARY KEY AUTO_INCREMENT,
long_url LONGTEXT NOT NULL,
short_url VARCHAR(5) NOT NULL);

