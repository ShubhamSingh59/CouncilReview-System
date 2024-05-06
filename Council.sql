create database council;
use council;
CREATE TABLE pdc_council (
  Secretary_rating int,
  Council_rating int,
  Feedback varchar(500)
);
CREATE TABLE tech_council (
  Secretary_rating INT,
  Council_rating INT,
  Metis_rating INT,
  Mean_mechanics_rating INT,
  Digis_rating INT,
  Odyssey_rating INT,
  Anveshanam_rating INT,
  Grasp_rating INT,
  ML_group_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE cult_council (
  Cultural_Secretary_rating INT,
  Cultural_Council_rating INT,
  Sargam_rating INT,
  Step_up_rating INT,
  Literary_Society_rating INT,
  Palette_rating INT,
  Pixels_rating INT,
  Abhinaya_rating INT,
  Vinteo_rating INT, 
  Cinematheque_rating INT,
  Orenda_rating INT,
  Quizzing_Society_rating INT,
  Awaam_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE sports_council(
  Sports_Secretary_rating INT,
  Sports_Council_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE welfare_council(
  Welfare_Secretary_rating INT,
  Welfare_Council_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE acad_council(
  Acadmic_Secretary_rating INT,
  Acadmic_Council_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE irp_council(
  IRP_Secretary_rating INT,
  IRP_Council_rating INT,
  Feedback VARCHAR(500)
);
CREATE TABLE users(
  email varchar(50) unique,
  password varchar(100)
);

select * from users;