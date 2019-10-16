Общая выборка
```
select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id)
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;
```
результат
```
  id  | year |                 model                 |      size_body       |     body type      |  engine  | manufacturersize |    country     |           email           
-----+------+---------------------------------------+----------------------+--------------------+----------+------------------+----------------+---------------------------
   1 | 2019 | Acura ILX                             | Compact              | Sedan              | gasoline | Acura            | Japan          | www.acura.me
   2 | 2020 | Acura MDX Sport Hybrid                | Midsize              | SUV                | hybrid   | Acura            | Japan          | www.acura.me
   3 | 2019 | Acura NSX                             | Midsize              | Sports Car         | hybrid   | Acura            | Japan          | www.acura.me
   4 | 2018 | Alfa Romeo 4C Spider                  | Compact              | Sports Car         | gasoline | Alfa Romeo       | Italy          | www.alfaromeo.com
   5 | 2019 | Alfa Romeo Giulia                     | Midsize              | Sedan              | gasoline | Alfa Romeo       | Italy          | www.alfaromeo.com
   6 | 2019 | Alfa Romeo Stelvio                    | Compact              | SUV                | gasoline | Alfa Romeo       | Italy          | www.alfaromeo.com
   7 | 2017 | Aston Martin V12 Vantage S            | Compact              | Sports Car         | gasoline | Aston Martin     | United Kingdom | www.astonmartin.com
   8 | 2018 | Aston Martin DB11                     | Compact              | Coupe              | gasoline | Aston Martin     | United Kingdom | www.astonmartin.com
   9 | 2018 | Aston Martin Vanquish                 | Compact              | Coupe              | gasoline | Aston Martin     | United Kingdom | www.astonmartin.com
  10 | 2018 | Audi A8                               | Full-Size            | Luxury Car         | gasoline | Audi             | Germany        | www.audi.com
  11 | 2018 | Audi Q7                               | Full-Size            | SUV                | diesel   | Audi             | Germany        | www.audi.com
  12 | 2018 | Audi R8                               | Full-Size            | Coupe              | gasoline | Audi             | Germany        | www.audi.com
  13 | 2019 | Bentley Mulsanne                      | Full-Size            | Sedan              | gasoline | Bentley          | United Kingdom | www.bentleymotors.com
  14 | 2018 | Bentley Continental GT                | Midsize              | Convertible        | gasoline | Bentley          | United Kingdom | www.bentleymotors.com
  15 | 2017 | BMW 330                               | Compact              | Sedan              | gasoline | BMW              | Germany        | www.bmwgroup.com
  16 | 2018 | BMW 330 Gran Turismo                  | Midsize              | Wagon or Hatchback | diesel   | BMW              | Germany        | www.bmwgroup.com
  17 | 2018 | BMW 750                               | Full-Size            | Sedan              | gasoline | BMW              | Germany        | www.bmwgroup.com
  18 | 2019 | Buick Cascada                         | Compact              | Convertible        | gasoline | Buick            | USA            | www.buick.com
  19 | 2018 | Buick Regal TourX                     | Midsize              | Wagon or Hatchback | diesel   | Buick            | USA            | www.buick.com
  20 | 2017 | Buick Enclave                         | Full-Size            | SUV                | diesel   | Buick            | USA            | www.buick.com
  21 | 2018 | Cadillac ATS-V                        | Compact              | Sports Car         | gasoline | Cadillac         | USA            | www.cadillac.com
  22 | 2019 | Cadillac CTS                          | Midsize              | Luxury Car         | gasoline | Cadillac         | USA            | www.cadillac.com
  23 | 2019 | Cadillac Escalade ESV                 | Full-Size            | SUV                | hybrid   | Cadillac         | USA            | www.cadillac.com
  24 | 2019 | Chevrolet Silverado 2500              | Heavy-Duty - Pickups | Pickup Truck       | gasoline | Chevrolet        | USA            | www.chevrolet.com
  25 | 2019 | Chevrolet Bolt EV                     | Compact              | Wagon or Hatchback | electro  | Chevrolet        | USA            | www.chevrolet.com
  26 | 2017 | Chevrolet Express 2500                | Heavy-Duty - Pickups | Minivan or Van     | diesel   | Chevrolet        | USA            | www.chevrolet.com
  27 | 2017 | Chrysler Pacifica Hybrid              | Midsize              | Minivan or Van     | hydrogen | Chrysler         | USA            | www.fcagroup.com
  28 | 2017 | Chrysler 300C                         | Full-Size            | SUV                | gasoline | Chrysler         | USA            | www.fcagroup.com
  29 | 2017 | Chrysler 200                          | Midsize              | Sedan              | gasoline | Chrysler         | USA            | www.fcagroup.com
  30 | 2017 | Dodge Challenger                      | Midsize              | Coupe              | gasoline | Dodge            | USA            | www.dodge.com
  31 | 2017 | Dodge Charger                         | Full-Size            | Sedan              | gasoline | Dodge            | USA            | www.dodge.com
  32 | 2017 | Dodge Durango                         | Full-Size            | SUV                | gasoline | Dodge            | USA            | www.dodge.com
  33 | 2017 | Ferrari California                    | Compact              | Convertible        | gasoline | Ferrari          | Italy          | www.ferrari.com
  34 | 2018 | Ferrari 812 Superfast                 | Compact              | Sports Car         | gasoline | Ferrari          | Italy          | www.ferrari.com
  35 | 2018 | Ferrari 488 GTB                       | Compact              | Coupe              | gasoline | Ferrari          | Italy          | www.ferrari.com
  36 | 2017 | FIAT 500                              | Compact              | Wagon or Hatchback | gasoline | FIAT             | Italy          | www.fiat.com
  37 | 2017 | FIAT 124 Spider                       | Compact              | Sports Car         | gasoline | FIAT             | Italy          | www.fiat.com
  38 | 2017 | FIAT 500X                             | Compact              | SUV                | gasoline | FIAT             | Italy          | www.fiat.com
  39 | 2017 | Ford F-450                            | Heavy-Duty - Pickups | Pickup Truck       | diesel   | Ford             | USA            | www.ford.com
  40 | 2019 | Ford Mustang                          | Compact              | Sports Car         | gasoline | Ford             | USA            | www.ford.com
  41 | 2019 | Ford Focus Electric                   | Midsize              | Sedan              | electro  | Ford             | USA            | www.ford.com
  42 | 2017 | Genesis G90                           | Full-Size            | Sedan              | gasoline | Genesis          | South Korea    | www.genesis.com
  43 | 2018 | Genesis G80                           | Midsize              | Sedan              | gasoline | Genesis          | South Korea    | www.genesis.com
  44 | 2019 | Genesis G70                           | Compact              | Sedan              | gasoline | Genesis          | South Korea    | www.genesis.com
  45 | 2017 | GMC Savana 2500                       | Heavy-Duty - Pickups | Minivan or Van     | diesel   | GMC              | USA            | www.gmc.com
  46 | 2017 | GMC Yukon XL                          | Heavy-Duty - Pickups | SUV                | gasoline | GMC              | USA            | www.gmc.com
  47 | 2018 | GMC Sierra 3500                       | Heavy-Duty - Pickups | Pickup Truck       | diesel   | GMC              | USA            | www.gmc.com
  48 | 2018 | Honda Civic Type R                    | Compact              | Sports Car         | gasoline | Honda            | Japan          | global.honda
  49 | 2019 | Honda Clarity Plug-In Hybrid          | Midsize              | Sedan              | hybrid   | Honda            | Japan          | global.honda
  50 | 2017 | Honda Pilot                           | Full-Size            | SUV                | gasoline | Honda            | Japan          | global.honda
  51 | 2018 | Hyundai Santa Fe                      | Full-Size            | SUV                | gasoline | Hyundai          | South Korea    | www.hyundaimotorgroup.com
  52 | 2017 | Hyundai Sonata Hybrid                 | Midsize              | Sedan              | hybrid   | Hyundai          | South Korea    | www.hyundaimotorgroup.com
  53 | 2019 | Hyundai Veloster                      | Compact              | Wagon or Hatchback | gasoline | Hyundai          | South Korea    | www.hyundaimotorgroup.com
  54 | 2018 | INFINITI QX80                         | Full-Size            | Luxury Car         | gasoline | INFINITI         | Japan          | www.infiniti.com
  55 | 2018 | INFINITI Q70h                         | Midsize              | Sedan              | hybrid   | INFINITI         | Japan          | www.infiniti.com
  56 | 2018 | INFINITI Q60                          | Compact              | Coupe              | gasoline | INFINITI         | Japan          | www.infiniti.com
  57 | 2017 | Jaguar XJ                             | Full-Size            | Sedan              | gasoline | Jaguar           | United Kingdom | www.jaguar.com
  58 | 2018 | Jaguar XF                             | Midsize              | Sedan              | hybrid   | Jaguar           | United Kingdom | www.jaguar.com
  59 | 2020 | 2020 Jaguar F-TYPE                    | Compact              | Sports Car         | gasoline | Jaguar           | United Kingdom | www.jaguar.com
  60 | 2017 | Jeep Grand Cherokee                   | Midsize              | SUV                | gasoline | Jeep             | USA            | www.jeep.com
  61 | 2017 | Jeep New Compass                      | Compact              | SUV                | gasoline | Jeep             | USA            | www.jeep.com
  62 | 2020 | Jeep Gladiator                        | Compact              | Pickup Truck       | gasoline | Jeep             | USA            | www.jeep.com
  63 | 2017 | Kia K900                              | Full-Size            | Luxury Car         | gasoline | Kia              | South Korea    | www.kia.com
  64 | 2017 | Kia Stinger                           | Midsize              | Sedan              | gasoline | Kia              | South Korea    | www.kia.com
  65 | 2019 | Kia Soul EV                           | Compact              | Wagon or Hatchback | electro  | Kia              | South Korea    | www.kia.com
  66 | 2018 | Lamborghini Aventador S               | Midsize              | Coupe              | gasoline | Lamborghini      | Italy          | www.lamborghini.com
  67 | 2019 | Lamborghini Urus                      | Midsize              | SUV                | gasoline | Lamborghini      | Italy          | www.lamborghini.com
  68 | 2017 | Lamborghini Aventador                 | Midsize              | Sports Car         | gasoline | Lamborghini      | Italy          | www.lamborghini.com
  69 | 2019 | Land Rover Range Rover Velar          | Full-Size            | SUV                | diesel   | Land Rover       | United Kingdom | www.landrover.com
  70 | 2017 | Land Rover Range Rover Evoque         | Compact              | SUV                | gasoline | Land Rover       | United Kingdom | www.landrover.com
  71 | 2019 | Land Rover Range Rover Sport          | Midsize              | SUV                | diesel   | Land Rover       | United Kingdom | www.landrover.com
  72 | 2018 | Lexus LS 500h                         | Full-Size            | Sedan              | hybrid   | Lexus            | Japan          | discoverlexus.com
  73 | 2017 | Lexus RC F                            | Midsize              | Sports Car         | gasoline | Lexus            | Japan          | discoverlexus.com
  74 | 2017 | Lexus CT 200h                         | Compact              | Wagon or Hatchback | hybrid   | Lexus            | Japan          | discoverlexus.com
  75 | 2011 | Lincoln Navigator                     | Full-Size            | SUV                | gasoline | Lincoln          | USA            | www.lincoln.com
  76 | 2019 | Lincoln MKZ Hybrid                    | Midsize              | Sedan              | gasoline | Lincoln          | USA            | www.lincoln.com
  77 | 2017 | Lincoln MKC                           | Compact              | SUV                | gasoline | Lincoln          | USA            | www.lincoln.com
  78 | 2018 | Lotus Evora 400                       | Compact              | Sports Car         | gasoline | Lotus            | United Kingdom | www.lotuscars.com
  79 | 2011 | Lotus Exige                           | Compact              | Sports Car         | gasoline | Lotus            | United Kingdom | www.lotuscars.com
  80 | 2008 | Lotus Elise                           | Compact              | Sports Car         | gasoline | Lotus            | United Kingdom | www.lotuscars.com
  81 | 2010 | Maserati GranTurismo Convertible      | Midsize              | Sports Car         | gasoline | Maserati         | Italy          | www.maserati.com
  82 | 2014 | Maserati Quattroporte                 | Full-Size            | Sedan              | gasoline | Maserati         | Italy          | www.maserati.com
  83 | 2019 | Maserati Levante Trofeo               | Midsize              | SUV                | gasoline | Maserati         | Italy          | www.maserati.com
  84 | 2019 | Mazda СХ-9                            | Full-Size            | SUV                | gasoline | Mazda            | Japan          | www.mazda.com
  85 | 2018 | Mazda 6                               | Midsize              | Sedan              | gasoline | Mazda            | Japan          | www.mazda.com
  86 | 2017 | Mazda MX-5 Miata                      | Compact              | Sports Car         | gasoline | Mazda            | Japan          | www.mazda.com
  87 | 2017 | McLaren 570GT                         | Compact              | Sports Car         | gasoline | McLaren          | United Kingdom | www.mclaren.com
  88 | 2019 | McLaren 570GT                         | Compact              | Sports Car         | gasoline | McLaren          | United Kingdom | www.mclaren.com
  89 | 2018 | McLaren 570S Spider                   | Compact              | Sports Car         | gasoline | McLaren          | United Kingdom | www.mclaren.com
  90 | 2020 | Mercedes-AMG ONE                      | Compact              | Sports Car         | gasoline | Mercedes-Benz    | Germany        | www.mercedes-benz.com
  91 | 2018 | Mercedes-AMG GLS 63                   | Full-Size            | SUV                | gasoline | Mercedes-Benz    | Germany        | www.mercedes-benz.com
  92 | 2019 | Mercedes-Benz CLS-Class               | Midsize              | Sedan              | gasoline | Mercedes-Benz    | Germany        | www.mercedes-benz.com
  93 | 2016 | MINI John Cooper Works Hardtop        | Midsize              | Wagon or Hatchback | gasoline | MINI             | United Kingdom | www.mini.com
  94 | 2013 | MINI Cooper Convertible               | Compact              | Convertible        | gasoline | MINI             | United Kingdom | www.mini.com
  95 | 2018 | MINI Cooper Countryman Plug-in Hybrid | Midsize              | SUV                | hybrid   | MINI             | United Kingdom | www.mini.com
  96 | 2018 | Mitsubishi Mirage                     | Compact              | Wagon or Hatchback | gasoline | Mitsubishi       | Japan          | www.mitsubishi-motors.com
  97 | 2020 | Mitsubishi Outlander PHEV             | Midsize              | SUV                | hybrid   | Mitsubishi       | Japan          | www.mitsubishi-motors.com
  98 | 2015 | Mitsubishi Lancer Evolution           | Midsize              | Sedan              | gasoline | Mitsubishi       | Japan          | www.mitsubishi-motors.com
  99 | 2018 | Nissan 370Z Nismo                     | Compact              | Coupe              | gasoline | Nissan           | Japan          | www.nissan-global.com
 100 | 2010 | Nissan Titan                          | Heavy-Duty - Pickups | Pickup Truck       | gasoline | Nissan           | Japan          | www.nissan-global.com
 101 | 2019 | Nissan GT-R NISMO                     | Midsize              | Sports Car         | gasoline | Nissan           | Japan          | www.nissan-global.com
(101 rows)
```
выбор по стране изготоления
```select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id)
  inner join manufacturersize as m1 on (m1.id = models.idm and m1.country = 'USA') order by 1;
```
результат
``` id | year |          model           |      size_body       |     body type      |  engine  | manufacturersize | country |       email       
----+------+--------------------------+----------------------+--------------------+----------+------------------+---------+-------------------
 18 | 2019 | Buick Cascada            | Compact              | Convertible        | gasoline | Buick            | USA     | www.buick.com
 19 | 2018 | Buick Regal TourX        | Midsize              | Wagon or Hatchback | diesel   | Buick            | USA     | www.buick.com
 20 | 2017 | Buick Enclave            | Full-Size            | SUV                | diesel   | Buick            | USA     | www.buick.com
 21 | 2018 | Cadillac ATS-V           | Compact              | Sports Car         | gasoline | Cadillac         | USA     | www.cadillac.com
 22 | 2019 | Cadillac CTS             | Midsize              | Luxury Car         | gasoline | Cadillac         | USA     | www.cadillac.com
 23 | 2019 | Cadillac Escalade ESV    | Full-Size            | SUV                | hybrid   | Cadillac         | USA     | www.cadillac.com
 24 | 2019 | Chevrolet Silverado 2500 | Heavy-Duty - Pickups | Pickup Truck       | gasoline | Chevrolet        | USA     | www.chevrolet.com
 25 | 2019 | Chevrolet Bolt EV        | Compact              | Wagon or Hatchback | electro  | Chevrolet        | USA     | www.chevrolet.com
 26 | 2017 | Chevrolet Express 2500   | Heavy-Duty - Pickups | Minivan or Van     | diesel   | Chevrolet        | USA     | www.chevrolet.com
 27 | 2017 | Chrysler Pacifica Hybrid | Midsize              | Minivan or Van     | hydrogen | Chrysler         | USA     | www.fcagroup.com
 28 | 2017 | Chrysler 300C            | Full-Size            | SUV                | gasoline | Chrysler         | USA     | www.fcagroup.com
 29 | 2017 | Chrysler 200             | Midsize              | Sedan              | gasoline | Chrysler         | USA     | www.fcagroup.com
 30 | 2017 | Dodge Challenger         | Midsize              | Coupe              | gasoline | Dodge            | USA     | www.dodge.com
 31 | 2017 | Dodge Charger            | Full-Size            | Sedan              | gasoline | Dodge            | USA     | www.dodge.com
 32 | 2017 | Dodge Durango            | Full-Size            | SUV                | gasoline | Dodge            | USA     | www.dodge.com
 39 | 2017 | Ford F-450               | Heavy-Duty - Pickups | Pickup Truck       | diesel   | Ford             | USA     | www.ford.com
 40 | 2019 | Ford Mustang             | Compact              | Sports Car         | gasoline | Ford             | USA     | www.ford.com
 41 | 2019 | Ford Focus Electric      | Midsize              | Sedan              | electro  | Ford             | USA     | www.ford.com
 45 | 2017 | GMC Savana 2500          | Heavy-Duty - Pickups | Minivan or Van     | diesel   | GMC              | USA     | www.gmc.com
 46 | 2017 | GMC Yukon XL             | Heavy-Duty - Pickups | SUV                | gasoline | GMC              | USA     | www.gmc.com
 47 | 2018 | GMC Sierra 3500          | Heavy-Duty - Pickups | Pickup Truck       | diesel   | GMC              | USA     | www.gmc.com
 60 | 2017 | Jeep Grand Cherokee      | Midsize              | SUV                | gasoline | Jeep             | USA     | www.jeep.com
 61 | 2017 | Jeep New Compass         | Compact              | SUV                | gasoline | Jeep             | USA     | www.jeep.com
 62 | 2020 | Jeep Gladiator           | Compact              | Pickup Truck       | gasoline | Jeep             | USA     | www.jeep.com
 75 | 2011 | Lincoln Navigator        | Full-Size            | SUV                | gasoline | Lincoln          | USA     | www.lincoln.com
 76 | 2019 | Lincoln MKZ Hybrid       | Midsize              | Sedan              | gasoline | Lincoln          | USA     | www.lincoln.com
 77 | 2017 | Lincoln MKC              | Compact              | SUV                | gasoline | Lincoln          | USA     | www.lincoln.com
(27 rows)
```


выбор только электрокаров
```
select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id and e1.engine = 'electro')
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;
```
результат
```
 id | year |        model        | size_body |     body type      | engine  | manufacturersize |   country   |       email       
----+------+---------------------+-----------+--------------------+---------+------------------+-------------+-------------------
 25 | 2019 | Chevrolet Bolt EV   | Compact   | Wagon or Hatchback | electro | Chevrolet        | USA         | www.chevrolet.com
 41 | 2019 | Ford Focus Electric | Midsize   | Sedan              | electro | Ford             | USA         | www.ford.com
 65 | 2019 | Kia Soul EV         | Compact   | Wagon or Hatchback | electro | Kia              | South Korea | www.kia.com
(3 rows)
```

только спорткары
```
select
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id )
  inner join body_type as b1 on (models.body_type = b1.id and b1."body type"= 'Sports Car')
  inner join engine as e1 on (models.engenie = e1.id )
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;
```
результат
```
 id | year |        model        | size_body |     body type      | engine  | manufacturersize |   country   |       email       
----+------+---------------------+-----------+--------------------+---------+------------------+-------------+-------------------
 25 | 2019 | Chevrolet Bolt EV   | Compact   | Wagon or Hatchback | electro | Chevrolet        | USA         | www.chevrolet.com
 41 | 2019 | Ford Focus Electric | Midsize   | Sedan              | electro | Ford             | USA         | www.ford.com
 65 | 2019 | Kia Soul EV         | Compact   | Wagon or Hatchback | electro | Kia              | South Korea | www.kia.com
(3 rows)
```
