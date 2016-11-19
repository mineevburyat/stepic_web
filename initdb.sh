mysql -u root -e "CREATE DATABASE webstepic CHARACTER SET = utf8;"
mysql -u root -e "CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';"
mysql -u root -e "GRANT ALL ON webstepic.* TO 'user'@'localhost';"