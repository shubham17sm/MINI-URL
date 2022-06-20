USE url_shortner;

-- CREATE DATABASE url_shortner;

CREATE TABLE urlshort(
id INT PRIMARY KEY AUTO_INCREMENT,
long_url LONGTEXT NOT NULL,
short_url VARCHAR(5) NOT NULL);


INSERT INTO urlshort VALUES (1, 'https://www.youtube.com/watch?v=YI16KWyA3M0', 'CDDSA'),
(2, 'https://www.reddit.com/r/learnpython/comments/4fnjma/unsupported_method_post_by_simple_python_server/', 'ASASA'),
(3, 'https://stackoverflow.com/questions/36909047/do-post-not-working-on-http-server-with-python', 'SAZAS');


SELECT long_url, short_url FROM urlshort WHERE short_url = "ASASA" LIMIT 1; 

SELECT * FROM urlshort;