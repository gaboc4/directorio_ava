CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `business` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `owner_id` varchar(255) NOT NULL,
  `business_email` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `sector` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    owner = db.Column(db.Integer)
    business_email = db.Column(db.String(1000))
    phone_number = db.Column(db.String(1000))
    sector = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    description = db.Column(db.String(1000000))