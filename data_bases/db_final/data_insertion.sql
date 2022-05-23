INSERT INTO city(title) VALUES
    ('New York'),
    ('Los Angeles'),
    ('Chicago'),
    ('Houston'),
    ('Phoenix'),
    ('Philadelphia'),
    ('San Antonio'),
    ('San Diego'),
    ('Dallas'),
    ('San Jose'),
    ('Austin'),
    ('Jacksonville'),
    ('Fort Worth'),
    ('Columbus'),
    ('Charlotte'),
    ('San Francisco'),
    ('Indianapolis'),
    ('Seattle'),
    ('Denver'),
    ('Washington'),
    ('Boston'),
    ('El Paso'),
    ('Nashville'),
    ('Detroit'),
    ('Oklahoma City'),
    ('Portland'),
    ('Las Vegas'),
    ('Memphis'),
    ('Louisville'),
    ('Baltimore'),
    ('Milwaukee'),
    ('Albuquerque'),
    ('Tucson'),
    ('Fresno'),
    ('Mesa'),
    ('Sacramento'),
    ('Atlanta'),
    ('Kansas City'),
    ('Colorado Springs'),
    ('Omaha'),
    ('Raleigh'),
    ('Miami'),
    ('Long Beach'),
    ('Virginia Beach'),
    ('Oakland'),
    ('Minneapolis'),
    ('Tulsa'),
    ('Tampa'),
    ('Arlington'),
    ('New Orleans');


INSERT INTO street(title) VALUES
    ('Newcombe'),
    ('Fremont'),
    ('Early Morn'),
    ('Choctav'),
    ('Preston Road'),
    ('Parkwood Road'),
    ('Coit Road'),
    ('Alma Road'),
    ('Custer Road'),
    ('Park Boulevard'),
    ('Cliffside Park'),
    ('Myrtle Ave'),
    ('Birch Grove'),
    ('Cherry Hill'),
    ('Cherry Creek'),
    ('Leoforos Stratou'),
    ('Tritis Septemvriou'),
    ('Nikis'),
    ('Ethnikis aminis'),
    ('Ethnikis anoistasseos'),
    ('Royal Tern Ln'),
    ('Ravenwood Dr'),
    ('Rymfire Dr'),
    ('Waters Ct'),
    ('Williams Dr'),
    ('Wellington Dr'),
    ('Pacific Dr'),
    ('Prairie Ln'),
    ('Parkview Dr'),
    ('Colechester Ln'),
    ('Colorado Dr'),
    ('Curry Ct'),
    ('Fircrest Ln'),
    ('Forest Grove Dr'),
    ('Fellowship Dr'),
    ('Bickwick Ln'),
    ('Belle Terre Pkwy'),
    ('Linnet Way'),
    ('Lancaster Lane'),
    ('Lancelot Drive'),
    ('Lakeview Blvd'),
    ('George’s'),
    ('Mark’s Place'),
    ('Mark’s Avenue'),
    ('Cadman Plaza West'),
    ('Fulton'),
    ('Fulton Landing'),
    ('Old Fulton'),
    ('Bedford-Stuyvesant'),
    ('Clinton Hill'),
    ('El Barrio'),
    ('Queens Expressway'),
    ('Fort Greene'),
    ('Dyer Avenue'),
    ('Beach Boulevard');


do $$
begin
    for i in 1..50
    loop
        for j in 1..57
        loop
            for k in 1..10
            loop
                INSERT INTO address(city_id, street_id, house_number) VALUES
                    (i, j, k);
            end loop;
        end loop;
    end loop;
end;
$$;


INSERT INTO branch(address_id, phone_number)
SELECT floor(random()*28500+1),
       round(random()*(9999999999 - 1000000000)) + 1000000000
FROM generate_series(1, 100) AS i;


INSERT INTO customer(first_name, last_name, address_id, phone_number)
SELECT 'name_' || round(random()*100),
       'last_name_' || round(random()*100),
       floor(random()*28500+1),
       round(random()*(9999999999 - 1000000000)) + 1000000000
FROM generate_series(1, 10000) AS i;


INSERT INTO brand(title) VALUES
    ('Tesla'),
    ('BMW'),
    ('Ford'),
    ('Honda'),
    ('Toyota'),
    ('Audi'),
    ('Mazda'),
    ('Nissan'),
    ('Suzuki'),
    ('Lamborghini'),
    ('Porsche'),
    ('Ferrari'),
    ('Subaru'),
    ('Cadillac'),
    ('Hyundai'),
    ('Chevrolet'),
    ('KIA'),
    ('Mercedes-Benz'),
    ('Mitsubishi'),
    ('Citroen');


INSERT INTO model(brand_id, title) VALUES
    (1, 'Model X'),
    (1, 'Model Y'),
    (1, 'Model S'),
    (1, 'Model 3'),

    (2, 'i5'),
    (2, 'i8'),
    (2, 'X3'),
    (2, 'X5'),

    (3, 'Escort'),
    (3, 'Mustang'),
    (3, 'F-Series'),
    (3, 'Fiesta'),

    (4, 'Civic'),
    (4, 'Accord'),
    (4, 'CR-V'),
    (4, 'Pilot'),

    (5, 'Avalon'),
    (5, 'Camry'),
    (5, 'Highlander'),
    (5, 'Prius'),

    (6, 'RSQ8'),
    (6, 'TT'),
    (6, 'RS6 Avant'),
    (6, 'A8'),

    (7, 'RX-8'),
    (7, '2'),
    (7, '5'),
    (7, 'CX5'),

    (8, 'Altima'),
    (8, 'Versa'),
    (8, 'Sentra'),
    (8, 'Rogue'),

    (9, 'Celerio'),
    (9, 'Alto Variants'),
    (9, 'Swift Variants'),
    (9, 'Jimny'),

    (10, 'Countach'),
    (10, 'Espada'),
    (10, 'Aventador'),
    (10, 'Sesto Elemento'),

    (11, 'Phaeton'),
    (11, 'Cayman'),
    (11, 'Spyder'),
    (11, 'Carrera'),

    (12, 'Portofino'),
    (12, 'Stradale'),
    (12, 'Roma'),
    (12, 'Superfast'),

    (13, 'Exiga'),
    (13, 'Tribeca'),
    (13, 'Legacy'),
    (13, 'WRX STI'),

    (14, 'DeVille'),
    (14, 'ATS-V'),
    (14, 'CTS-V Wagon'),
    (14, 'CT5-V Blackwing'),

    (15, 'Elantra'),
    (15, 'Sonata'),
    (15, 'Accent'),
    (15, 'Tucson'),

    (16, 'Corvette'),
    (16, 'Tahoe'),
    (16, 'Caprice PPV'),
    (16, 'Spark'),

    (17, 'Stinger'),
    (17, 'Forte'),
    (17, 'Sorento'),
    (17, 'K5'),

    (18, 'GLE 350'),
    (18, 'C 300'),
    (18, 'E 350'),
    (18, 'CLA 250'),

    (19, 'Pajero'),
    (19, 'Lancer Evolution'),
    (19, 'Evo X'),
    (19, 'Montero'),

    (20, 'Aircross'),
    (20, 'C3'),
    (20, 'Hatchback'),
    (20, 'SUV');


INSERT INTO car(branch_id, model_id, plate_number, rental_price)
SELECT floor(random()*100+1),
       floor(random()*80+1),
       '#' || upper(left(md5(random()::text), 10)),
       round((random()*300+300)::numeric, 2)
FROM generate_series(1, 2000);


INSERT INTO rent(customer_id, car_id, rental_date, period)
SELECT floor(random()*10000+1),
       floor(random()*2000+1),
       random() * (now() - timestamp '2021-01-01') + timestamp '2021-01-01',
       ((random()*10+1)::char || 'day')::interval
FROM generate_series(1, 30000);
