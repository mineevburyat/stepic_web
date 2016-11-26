mysql -u root -p -e  "CREATE DATABASE webstepic CHARACTER SET = utf8;"
mysql -u root -p -e "CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';"
mysql -u root -p -e "GRANT ALL ON webstepic.* TO 'user'@'localhost';"
