-- Create fmr_bird_data database

CREATE DATABASE fmr_bird_data;

-- Create Flint Hills table

/*
Noise: 0= no background noise, 1=barely reduces hearing, 2=noticeable hearing reduction, 3=prohibitive hearing reduction
*/

DROP TABLE IF EXISTS 'flint_hills';

CREATE TABLE flint_hills(
       	species_code VARCHAR(20),
	noise int,
	time_heard DATETIME,
	survey_area_number int,
	);



