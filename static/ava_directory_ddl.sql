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



INSERT INTO users VALUES(1, 'Elizabeth', 'Gunz', "elizabeth@venezuelaenaustin.org", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(2, 'Samaris', 'Barrios', "samarisbarrios@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(3, 'Luz', 'Cardona', "luzcardona.o@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(4, 'Jeanette', 'Aviles', "jeanette_aviles@us.aflac.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(5, 'Ismael', 'Aviles', "ismael7486@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(6, 'Orland', 'Moreno', "ifstex01@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(7, 'Juan', 'Ramírez', "janakairaustin@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(8, 'Maria', 'Ordonez', "sales@arepaxpress.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(9, 'Jhonny', 'Marcano', "jhonnymark@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(10, 'Juan Antonio', 'Lozada', "juan@tximmigrationlaw.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(11, 'Daniela', 'De Jongh', "cuentologybooks@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(12, 'Dante', 'Torres', "enviopronto@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');
INSERT INTO users VALUES(13, 'Remesis' 'Torres', "remesistorees@gmail.com", 'sha256$qRfO99PO$08d173fb730211707fb3f0a86656c9ce495b5720292838445d555028b9c1c520');


INSERT INTO business VALUES (1, "Ava", 1, "elizabeth@venezuelaenaustin.org", "5125174482", "AVA", "200362 Austin tx 78720", "Junta directiva de AVA");
INSERT INTO business VALUES (2, "Sassychic", 2, "samarisbarrios@gmail.com", "3462459827", "Manicura", "4201 Monterey Oaks Blvd", "Depilacion facial y corporal");
INSERT INTO business VALUES (3, "Cirugía capilar", 3, "luzcardona.o@gmail.com", "9548674588", "Peluqueria", "335 cypress Creek rd 78613", "Cirugía Capilar hidratación profunda");
INSERT INTO business VALUES (4, "Aflac", 4, "jeanette_aviles@us.aflac.com", "3059047477", "Seguro", "19705 Per Lange Pass Manor TX 78653", "Seguro Madico Suplementario");
INSERT INTO business VALUES (5, "Aviles Carpenter", 5, "ismael7486@gmail.com", "9542975564", "Reparaciones Generales", "19705 Per Lange Pass Manor TX 78653", "Diseño y construcción de muebles de baños, cocinas y closets.");
INSERT INTO business VALUES (6, "Installer Furniture Services LLC", 6, "ifstex01@gmail.com", "2105771903/5127609275", "Otro", "210 E Sonterra Blvd suite 628", "Instalación, mudanzas de mobiliario de oficinas");
INSERT INTO business VALUES (7, "JanakAir Austin ", 7, "janakairaustin@gmail.com", "5125768215", "Servicios Venezolanos", "7801 North Lamar blvd, suite a126, Austin,  Tx. 78752", "Envíos aéreos y marítimos a toda venezuela, Casilleros virtuales gratis, Trámites de aduana, Entrega puerta a puerta, Reempacamos tu Compra (Consolidado de mercancía)")
INSERT INTO business VALUES (8, "Arepa Xpress Cafe", 8, "sales@arepaxpress.com", "7133598930", "Restaurantes", "4334 FM 2920 Rd Spring, Tx. 77388", "Restaurante Venezolano");
INSERT INTO business VALUES (9, "Premier Financial", 9, "jhonnymark@gmail.com", "15124300291", "Seguro", "2102 AGARITA TRL", "Venta de seguros de vida contra muerte, enfermedades criticas, desmembramiento, pérdida de la capacidad para trabajar, etc.
Además de seguro que puedes usar sin tener que morir primero conocido como Beneficios en Vida. ");
INSERT INTO business VALUES (10, "The Law Office of Juan Antonio Lozada, PLLC", 10, "juan@tximmigrationlaw.com", "5122965033", "Abogado", "3305 W Slaughter Ln, Austin Texas 78748", "Servicios legales");
INSERT INTO business VALUES (11, "Cuentology Books", 11, "cuentologybooks@gmail.com", "5127878170", "Escuelas y Colegios", "Austin, TX 78749", "Libreria en linea de literatura infantil y juvenil en español. También puedes encontrarnos en eventos comunitarios en toda Texas y en ferias de libros en español en las escuelas.
Contactanos si tienes sugerencias de libros o temas que quieras leer o si quieres organizar una feria de libros en tu colegio. ");
INSERT INTO business VALUES (12, "Enviopronto", 12, "enviopronto@gmail.com", "5122901111", "Servicios Venezolanos", "15411 Ranch Rd. 620 N Austin TX 78717", "Servicio de paqueteria  a Venezuela aereo y maritimo");
INSERT INTO business VALUES (13, "Panes", 13, "remesistorees@gmail.com", "5127855676", "Comida", "Austin Texas ", "Venta de ponche cremas venezolano y panes de jamón tradicional, de masa de hojaldre ");