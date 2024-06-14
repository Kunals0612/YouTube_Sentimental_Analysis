USE youtube;
CREATE TABLE comments(
   Serial_id INT AUTO_INCREMENT PRIMARY KEY,
   Author VARCHAR(100),
   Likes INT,
   Texts VARCHAR(10000)
);