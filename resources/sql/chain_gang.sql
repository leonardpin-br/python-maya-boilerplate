# Database code based on this great course taught by Kevin Skoglund:
# PHP: Object-Oriented Programming with Databases
# https://www.linkedin.com/learning/php-object-oriented-programming-with-databases
# I highly recommend it.
USE chain_gang;

DROP TABLE IF EXISTS admins;

DROP TABLE IF EXISTS bicycles;

CREATE TABLE bicycles (
  id            int(11) NOT NULL AUTO_INCREMENT,
  brand         varchar(255) NOT NULL,
  model         varchar(255) NOT NULL,
  `year`        int(4) NOT NULL,
  category      varchar(255) NOT NULL,
  gender        varchar(255) NOT NULL,
  color         varchar(255) NOT NULL,
  price         decimal(9,2) NOT NULL,
  weight_kg     decimal(9,5) NOT NULL,
  condition_id  tinyint(3) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

INSERT INTO bicycles VALUES (1,'Trek','Emonda',2017,'Hybrid','Unisex','black',1495.00,1.50000,5,''),
                            (2,'Cannondale','Synapse',2016,'Road','Unisex','matte black',1999.00,1.00000,5,'');

