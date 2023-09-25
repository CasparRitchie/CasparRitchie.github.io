-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: 127.0.0.1    Database: audit_responses_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attachments`
--

DROP TABLE IF EXISTS `attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attachments` (
  `attachment_id` int NOT NULL AUTO_INCREMENT,
  `constat_id` int DEFAULT NULL,
  `file` blob,
  PRIMARY KEY (`attachment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachments`
--

LOCK TABLES `attachments` WRITE;
/*!40000 ALTER TABLE `attachments` DISABLE KEYS */;
/*!40000 ALTER TABLE `attachments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auditeurs`
--

DROP TABLE IF EXISTS `auditeurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auditeurs` (
  `auditeur_id` int NOT NULL AUTO_INCREMENT,
  `auditeur_salutation_id` int DEFAULT NULL,
  `auditeur_prenom` varchar(100) DEFAULT NULL,
  `auditeur_nom` varchar(100) DEFAULT NULL,
  `auditeur_tel` varchar(15) DEFAULT NULL,
  `auditeur_email` varchar(255) DEFAULT NULL,
  `auditeur_login_id` text,
  `auditeur_permissions` text,
  PRIMARY KEY (`auditeur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditeurs`
--

LOCK TABLES `auditeurs` WRITE;
/*!40000 ALTER TABLE `auditeurs` DISABLE KEYS */;
INSERT INTO `auditeurs` VALUES (1,1,'Tom','Taylor','+1123456789','tom.taylor@idr.com',NULL,NULL),(2,2,'Sarah','Sanders','+2234567890','sarah.sanders@idr.com',NULL,NULL),(3,3,'Ulysses','Upton','+3345678901','ulysses.upton@idr.com',NULL,NULL),(4,4,'Vera','Vance','+4456789012','vera.vance@idr.com',NULL,NULL),(5,5,'Walter','White','+5567890123','walter.white@idr.com',NULL,NULL);
/*!40000 ALTER TABLE `auditeurs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audits`
--

DROP TABLE IF EXISTS `audits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audits` (
  `audit_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int DEFAULT NULL,
  `gestionnaire_id` int DEFAULT NULL,
  `auditeur_id` int DEFAULT NULL,
  `chapitre` int DEFAULT NULL,
  `restaurant_id` int DEFAULT NULL,
  `date_audit` datetime DEFAULT NULL,
  `client_contact_id` int DEFAULT NULL,
  `nombre_de_couverts` int DEFAULT NULL,
  `horaires_du_self_debut` time DEFAULT NULL,
  `horaires_du_self_fin` time DEFAULT NULL,
  PRIMARY KEY (`audit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audits`
--

LOCK TABLES `audits` WRITE;
/*!40000 ALTER TABLE `audits` DISABLE KEYS */;
INSERT INTO `audits` VALUES (1,1,1,1,1,4,'2023-09-05 10:00:00',1,100,'08:00:00','10:00:00'),(3,3,1,3,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','10:30:00'),(4,4,2,4,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:00:00'),(5,3,5,5,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:30:00'),(6,3,5,2,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','10:00:00'),(7,3,5,4,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:00:00'),(8,3,3,1,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','11:00:00'),(9,3,3,5,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:00:00'),(10,3,3,5,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:00:00'),(11,5,5,5,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:30:00'),(12,1,1,1,1,1,'2023-09-05 10:00:00',1,100,'08:00:00','12:30:00'),(13,1,NULL,NULL,NULL,NULL,'2022-01-01 00:00:00',1,NULL,NULL,NULL),(14,2,2,2,NULL,3,'2023-01-01 00:00:00',3,150,'11:34:00','14:02:00'),(15,2,5,2,1,4,'2023-02-09 00:00:00',4,400,'11:30:00','14:00:00'),(16,2,5,2,NULL,4,'2020-02-03 00:00:00',5,400,'11:30:00','14:00:00'),(17,6,3,3,NULL,4,'2000-01-01 00:00:00',3,300,'11:30:00','14:00:00'),(18,1,1,1,NULL,3,'2020-01-01 00:00:00',1,400,'11:30:00','14:00:00'),(19,1,5,2,NULL,1,'2000-01-01 00:00:00',2,400,'11:30:00','14:00:00'),(20,1,1,1,NULL,1,'2000-01-01 00:00:00',1,250,'11:30:00','14:00:00'),(21,1,1,2,NULL,3,'2000-01-01 00:00:00',1,400,'11:30:00','14:00:00'),(22,1,1,2,NULL,3,'2000-01-01 00:00:00',1,400,'11:30:00','14:00:00'),(23,1,1,2,NULL,3,'2000-01-01 00:00:00',1,400,'11:30:00','14:00:00'),(24,2,2,3,NULL,4,'2000-01-01 00:00:00',1,400,'11:30:00','14:00:00'),(25,4,5,4,NULL,6,'2023-09-07 00:00:00',5,250,'11:30:00','14:00:00');
/*!40000 ALTER TABLE `audits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_contacts`
--

DROP TABLE IF EXISTS `client_contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_contacts` (
  `client_contact_id` int NOT NULL AUTO_INCREMENT,
  `client_contact_salutation_id` int DEFAULT NULL,
  `client_contact_prenom` text,
  `client_contact_nom` text,
  `client_contact_adresse1` varchar(255) DEFAULT NULL,
  `client_contact_adresse2` varchar(255) DEFAULT NULL,
  `client_contact_adresse3` varchar(255) DEFAULT NULL,
  `client_contact_cp` int DEFAULT NULL,
  `client_contact_ville` varchar(100) DEFAULT NULL,
  `client_contact_coords` text,
  `client_contact_email` text,
  `client_contact_tel` text,
  `client_contact_role` text,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`client_contact_id`),
  CONSTRAINT `client_contacts_chk_1` CHECK ((length(`client_contact_cp`) = 5))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_contacts`
--

LOCK TABLES `client_contacts` WRITE;
/*!40000 ALTER TABLE `client_contacts` DISABLE KEYS */;
INSERT INTO `client_contacts` VALUES (1,1,'Frank','Sauze','123 Example St.',NULL,NULL,12345,'Example City',NULL,'sauze@client1.com',NULL,NULL,1),(2,2,'Philippe','Vilmot','456 Another Rd.',NULL,NULL,23456,'Another Town',NULL,'leroidefrance@client2.com',NULL,NULL,2),(3,3,'Herve','Renard','789 Third Ave.',NULL,NULL,34567,'Third City',NULL,'managerdefoot@client3.com',NULL,NULL,3),(4,4,'Harry','Kane','012 Fourth Blvd.',NULL,NULL,45678,'Fourth Village',NULL,'no_good_any_more@client4.com',NULL,NULL,4),(5,5,'Def','Leotard','345 Fifth Ln.',NULL,NULL,56789,'Fifth Hamlet',NULL,'musicienloupe@client4.com',NULL,NULL,4),(6,5,'Jef','Leopard','3 Rue de La Croix Brulante',NULL,NULL,56789,'Petit Hameau',NULL,'jef.leopard@client5.com',NULL,NULL,5),(7,1,'Caspar','Letest','Test House','Test St','Testerton',33333,'TESTTOWN','134012480148','caspar@jetest.com','03333333333','Chef de projet',1);
/*!40000 ALTER TABLE `client_contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `client_nom` text,
  `client_logo` blob,
  `client_adresse1` varchar(255) DEFAULT NULL,
  `client_adresse2` varchar(255) DEFAULT NULL,
  `client_adresse3` varchar(255) DEFAULT NULL,
  `client_cp` int DEFAULT NULL,
  `client_ville` varchar(100) DEFAULT NULL,
  `client_coords` text,
  `client_siret` varchar(255) DEFAULT NULL,
  `client_contact_principal` int DEFAULT NULL,
  PRIMARY KEY (`client_id`),
  KEY `client_contact_principal` (`client_contact_principal`),
  CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`client_contact_principal`) REFERENCES `client_contacts` (`client_contact_id`),
  CONSTRAINT `clients_chk_1` CHECK ((length(`client_cp`) = 5))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'Sodexo',NULL,'','','',33300,'','','',NULL),(2,'Example Corp. 2',NULL,'456 Another Rd.',NULL,NULL,23456,'Another Town',NULL,'23456789012345',NULL),(3,'Example Corp. 3',NULL,'789 Third Ave.',NULL,NULL,34567,'Third City',NULL,'34567890123456',NULL),(4,'Example Corp. 4',NULL,'012 Fourth Blvd.',NULL,NULL,45678,'Fourth Village',NULL,'45678901234567',NULL),(5,'Example Corp. 5',NULL,'345 Fifth Ln.',NULL,NULL,56789,'Fifth Hamlet',NULL,'56789012345678',NULL),(7,'Test customer 2',NULL,'111 rue de test','Test quartier','test sous prefecture machin',33000,'BORDEAUX','104810854814081','14081040148048408',NULL),(8,'7',NULL,'111 test st','Test quartzer','blah blah',33333,'BORDELAIS','19471940474','19055092575',NULL);
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constats`
--

DROP TABLE IF EXISTS `constats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `constats` (
  `constat_id` int NOT NULL AUTO_INCREMENT,
  `constat` int DEFAULT NULL,
  `elements_audites_details_prestation_id` int DEFAULT NULL,
  `element_id` int DEFAULT NULL,
  `heure_du_constat` datetime DEFAULT NULL,
  `score` int DEFAULT NULL,
  `observations` text,
  `piece_jointe` blob,
  `audit_id` int DEFAULT NULL,
  `auditeur_id` int DEFAULT NULL,
  PRIMARY KEY (`constat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constats`
--

LOCK TABLES `constats` WRITE;
/*!40000 ALTER TABLE `constats` DISABLE KEYS */;
INSERT INTO `constats` VALUES (1,1,NULL,NULL,NULL,NULL,NULL,NULL,13,NULL),(2,1,NULL,NULL,NULL,NULL,NULL,NULL,13,NULL),(4,1,NULL,NULL,NULL,NULL,NULL,NULL,14,NULL),(5,3,NULL,NULL,NULL,NULL,NULL,NULL,14,NULL),(6,5,NULL,NULL,NULL,NULL,NULL,NULL,14,NULL),(7,3,NULL,NULL,NULL,NULL,NULL,NULL,16,NULL),(9,5,NULL,NULL,NULL,NULL,NULL,NULL,16,NULL),(10,1,1,1,'2023-09-07 14:16:09',7,'ca va ca va',NULL,1,2),(11,2,NULL,NULL,NULL,NULL,NULL,NULL,17,NULL),(12,3,NULL,NULL,NULL,NULL,NULL,NULL,17,NULL),(13,3,NULL,NULL,NULL,NULL,NULL,NULL,17,NULL),(14,1,2,7,'2023-09-07 15:38:37',9,'trop cuit',NULL,1,2),(15,1,2,3,'2023-09-07 15:49:39',4,'test',NULL,1,2),(16,1,NULL,NULL,NULL,NULL,NULL,NULL,18,NULL),(17,2,NULL,NULL,NULL,NULL,NULL,NULL,18,NULL),(18,3,NULL,NULL,NULL,NULL,NULL,NULL,18,NULL),(19,NULL,NULL,843,NULL,21,'ok',NULL,23,NULL),(20,NULL,NULL,844,NULL,21,'ok',NULL,23,NULL),(21,NULL,NULL,845,NULL,21,'ok',NULL,23,NULL),(22,NULL,NULL,846,NULL,21,'ok',NULL,23,NULL),(23,NULL,NULL,847,NULL,21,'ok',NULL,23,NULL),(24,NULL,NULL,848,NULL,22,'pas la bonne temperature',NULL,23,NULL),(25,NULL,NULL,849,NULL,21,'ok',NULL,23,NULL),(26,NULL,NULL,850,NULL,21,'ok',NULL,23,NULL),(27,NULL,NULL,851,NULL,21,'ok',NULL,23,NULL),(28,NULL,NULL,852,NULL,21,'ok',NULL,23,NULL),(29,NULL,NULL,843,NULL,21,'ok',NULL,24,NULL),(30,NULL,NULL,844,NULL,21,'ok',NULL,24,NULL),(31,NULL,NULL,845,NULL,21,'ok',NULL,24,NULL),(32,NULL,NULL,846,NULL,21,'ok',NULL,24,NULL),(33,NULL,NULL,847,NULL,21,'ok',NULL,24,NULL),(34,NULL,NULL,848,NULL,21,'ok',NULL,24,NULL),(35,NULL,NULL,849,NULL,21,'ok',NULL,24,NULL),(36,NULL,NULL,850,NULL,21,'ok',NULL,24,NULL),(37,NULL,NULL,851,NULL,21,'ok',NULL,24,NULL),(38,NULL,NULL,852,NULL,21,'ok',NULL,24,NULL),(39,1,5,2,'2023-09-07 17:17:13',21,'RAS',NULL,3,2),(40,1,1,1,'2023-09-07 17:22:09',1,'1',NULL,1,1),(41,1,1,1,'2023-09-07 17:24:13',1,'1',NULL,1,1),(42,1,1,1,'2023-09-07 17:31:37',1,'1',NULL,1,1),(43,NULL,NULL,843,NULL,18,'',NULL,25,NULL),(44,NULL,NULL,844,NULL,18,'',NULL,25,NULL),(45,NULL,NULL,845,NULL,18,'',NULL,25,NULL),(46,NULL,NULL,846,NULL,18,'',NULL,25,NULL),(47,NULL,NULL,847,NULL,18,'',NULL,25,NULL),(48,NULL,NULL,848,NULL,18,'',NULL,25,NULL),(49,NULL,NULL,849,NULL,18,'',NULL,25,NULL),(50,NULL,NULL,850,NULL,18,'',NULL,25,NULL),(51,NULL,NULL,851,NULL,18,'',NULL,25,NULL),(52,NULL,NULL,852,NULL,18,'',NULL,25,NULL);
/*!40000 ALTER TABLE `constats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elements`
--

DROP TABLE IF EXISTS `elements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elements` (
  `element_id` int NOT NULL AUTO_INCREMENT,
  `chapitre` text,
  `titre` text,
  `sous_titre` varchar(255) DEFAULT NULL,
  `element_nom` varchar(255) DEFAULT NULL,
  `notes_structure_id` int DEFAULT NULL,
  PRIMARY KEY (`element_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3922 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elements`
--

LOCK TABLES `elements` WRITE;
/*!40000 ALTER TABLE `elements` DISABLE KEYS */;
INSERT INTO `elements` VALUES (3867,'EXPERIENCE CONVIVES','ENTRÉE DU SELF ','TEST','Affichage des horaires d\'ouverture du restaurant ',NULL),(3868,'EXPERIENCE CONVIVES','ENTRÉE DU SELF ',NULL,'Affichage des plats / menus ',NULL),(3869,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Disponibilité et état des plateaux ',NULL),(3870,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Disponibilité et état des couverts ',NULL),(3871,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Disponibilité et état des verres ',NULL),(3872,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'État des assiettes ',NULL),(3873,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Disponibilité des informations sur les allergènes ',NULL),(3874,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Affichage des stands ',NULL),(3875,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Uniformité de la vaisselle aux denrées ',NULL),(3876,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Maîtrise des flux ',NULL),(3877,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Propreté et état des locaux ',NULL),(3878,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Propreté et état du matériel de distribution ',NULL),(3879,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Temps d\'attente aux stands ',NULL),(3880,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Environnement / décoration ',NULL),(3881,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Respect des horaires de service ',NULL),(3882,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Le personnel ',NULL),(3883,'EXPERIENCE CONVIVES','DISTRIBUTION ','Le personnel','La tenue de travail ',NULL),(3884,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'L\'accueil, l\'amabilité, le sourire ',NULL),(3885,'EXPERIENCE CONVIVES','DISTRIBUTION ',NULL,'Les informations et le conseil ',NULL),(3886,'EXPERIENCE CONVIVES','LES DENRÉES ',NULL,'Alignement et présentation ',NULL),(3887,'EXPERIENCE CONVIVES','LES DENRÉES ',NULL,'Adaptation choix / espace ',NULL),(3888,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO dressés ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3889,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO dressés ','Température de service ',NULL),(3890,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO dressés ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3891,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Accessibilité / réapprovisionnement ',NULL),(3892,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Température de service ',NULL),(3893,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Affichage et information sur l\'origine des viandes bovines ',NULL),(3894,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Dressage et présentation / gestes de service ',NULL),(3895,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3896,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Adaptation choix / espace ',NULL),(3897,'EXPERIENCE CONVIVES','LES DENRÉES ','Les HO en libre-service ','Chaleur des assiettes ',NULL),(3898,'EXPERIENCE CONVIVES','LES DENRÉES ','Les fromages ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3899,'EXPERIENCE CONVIVES','LES DENRÉES ','Les fromages ','Accessibilité / réapprovisionnement ',NULL),(3900,'EXPERIENCE CONVIVES','LES DENRÉES ','Les fruits ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3901,'EXPERIENCE CONVIVES','LES DENRÉES ','Les fruits ','Accessibilité / réapprovisionnement ',NULL),(3902,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts dressés ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3903,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts dressés ','Accessibilité / réapprovisionnement ',NULL),(3904,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts dressés ','Température de service ',NULL),(3905,'EXPERIENCE CONVIVES','LES DENRÉES ','Les yaourts ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3906,'EXPERIENCE CONVIVES','LES DENRÉES ','Les yaourts ','Accessibilité / réapprovisionnement ',NULL),(3907,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts en libre-service ','Affichage, lisibilité (nom, tarifs...) ',NULL),(3908,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts en libre-service ','Accessibilité / réapprovisionnement ',NULL),(3909,'EXPERIENCE CONVIVES','LES DENRÉES ','Les desserts en libre-service ','Température de service ',NULL),(3910,'EXPERIENCE CONVIVES','LES DENRÉES ','Pain / Condiments ','Affichage / réapprovisionnement pain ',NULL),(3911,'EXPERIENCE CONVIVES','LES DENRÉES ','Pain / Condiments ','Affichage / réapprovisionnement condiments ',NULL),(3912,'EXPERIENCE CONVIVES','LES DENRÉES ','Pain / Condiments ','Qualité du pain / condiments ',NULL),(3913,'EXPERIENCE CONVIVES','EN SALLE ',NULL,'Propreté des chaises et des tables ',NULL),(3914,'EXPERIENCE CONVIVES','EN SALLE ',NULL,'Propreté des micro-ondes',NULL),(3915,'EXPERIENCE CONVIVES','EN SALLE ',NULL,'Propreté des fontaines à eau',NULL),(3916,'EXPERIENCE CONVIVES','EN SALLE ',NULL,'Disponibilité des places assises',NULL),(3917,'EXPERIENCE CONVIVES','EN SALLE ',NULL,'Ambiance (acoustique, luminosité) ',NULL),(3918,'EXPERIENCE CONVIVES','SORTIE DU SELF ',NULL,'Accessibilité convoyeurs / échelles ',NULL),(3919,'EXPERIENCE CONVIVES','SORTIE DU SELF ',NULL,'Propreté des murs et des sols ',NULL),(3920,'EXPERIENCE CONVIVES','SORTIE DU SELF ',NULL,'Propreté du convoyeur / échelles ',NULL);
/*!40000 ALTER TABLE `elements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elements_audites_details_prestations`
--

DROP TABLE IF EXISTS `elements_audites_details_prestations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elements_audites_details_prestations` (
  `elements_audites_details_prestation_id` int NOT NULL AUTO_INCREMENT,
  `elements_audites_details_prestation_nom` text,
  `elements_audites_details_prestation_grammage` text,
  `elements_audites_details_prestation_temperature` text,
  `elements_audites_details_prestation_sous_titre` int DEFAULT NULL,
  PRIMARY KEY (`elements_audites_details_prestation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elements_audites_details_prestations`
--

LOCK TABLES `elements_audites_details_prestations` WRITE;
/*!40000 ALTER TABLE `elements_audites_details_prestations` DISABLE KEYS */;
INSERT INTO `elements_audites_details_prestations` VALUES (1,'Detail A','50g','Hot',1),(2,'Detail B','100g','Cold',2),(3,'Detail C','150g','Warm',3),(4,'Detail D','200g','Hot',4),(5,'Detail E','250g','Cold',5),(7,'Test','100','63',1),(8,'TEst1','100','100',1),(9,'Test 123','123','123',1),(10,'1','1','1',1);
/*!40000 ALTER TABLE `elements_audites_details_prestations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionnaires`
--

DROP TABLE IF EXISTS `gestionnaires`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionnaires` (
  `gestionnaire_id` int NOT NULL AUTO_INCREMENT,
  `gestionnaire_nom` varchar(100) DEFAULT NULL,
  `gestionnaire_coords` text,
  PRIMARY KEY (`gestionnaire_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionnaires`
--

LOCK TABLES `gestionnaires` WRITE;
/*!40000 ALTER TABLE `gestionnaires` DISABLE KEYS */;
INSERT INTO `gestionnaires` VALUES (1,'Sodexo','Coord A'),(2,'Gestionnaire B','Coord B'),(3,'Gestionnaire C','Coord C'),(6,'Eurest','Rue de l\'Eurest'),(8,'Elior','Elior rue');
/*!40000 ALTER TABLE `gestionnaires` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `legendes`
--

DROP TABLE IF EXISTS `legendes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `legendes` (
  `legende_id` int NOT NULL AUTO_INCREMENT,
  `legende_name` text,
  `chapitre` int DEFAULT NULL,
  `legende_elements` text,
  PRIMARY KEY (`legende_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legendes`
--

LOCK TABLES `legendes` WRITE;
/*!40000 ALTER TABLE `legendes` DISABLE KEYS */;
INSERT INTO `legendes` VALUES (1,NULL,NULL,'Je sias maintennt'),(2,'Legend 2',2,'1|2'),(3,'Legend 3',3,'Element E|Element F'),(4,'Legend 4',4,'Element G|Element H'),(5,'Legend 5',5,'Element I|Element J'),(6,'TEst',1,'1');
/*!40000 ALTER TABLE `legendes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notes_structures`
--

DROP TABLE IF EXISTS `notes_structures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notes_structures` (
  `notes_structure_id` int NOT NULL AUTO_INCREMENT,
  `notes_structure_nom` text,
  `element_audite` int DEFAULT NULL,
  `est_actif` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`notes_structure_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes_structures`
--

LOCK TABLES `notes_structures` WRITE;
/*!40000 ALTER TABLE `notes_structures` DISABLE KEYS */;
INSERT INTO `notes_structures` VALUES (1,'Zero à cinq',NULL,1),(2,'NPS',NULL,1),(3,'Tripartite',NULL,1),(4,'Binaire',NULL,1),(5,'Oui ou non',NULL,1);
/*!40000 ALTER TABLE `notes_structures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reponses_possibles`
--

DROP TABLE IF EXISTS `reponses_possibles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reponses_possibles` (
  `response_id` int NOT NULL AUTO_INCREMENT,
  `response_value` text,
  `notes_structure_id` int DEFAULT NULL,
  PRIMARY KEY (`response_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reponses_possibles`
--

LOCK TABLES `reponses_possibles` WRITE;
/*!40000 ALTER TABLE `reponses_possibles` DISABLE KEYS */;
INSERT INTO `reponses_possibles` VALUES (1,'5',1),(2,'4',1),(3,'3',1),(4,'2',1),(5,'1',1),(6,'1',2),(7,'0',2),(8,'1',2),(9,'2',2),(10,'3',2),(11,'4',2),(12,'5',2),(13,'6',2),(14,'7',2),(15,'8',2),(16,'9',2),(17,'10',2),(18,'Conforme',3),(19,'Partiellement conforme',3),(20,'Non conforme',3),(21,'CONFORME',4),(22,'NON CONFORME',4),(23,'Oui',5),(24,'Non',5),(26,'Your Response Value Here',1),(27,'test reponse',1),(30,'philippe',3);
/*!40000 ALTER TABLE `reponses_possibles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurants` (
  `restaurant_id` int NOT NULL AUTO_INCREMENT,
  `restaurant_nom` varchar(100) DEFAULT NULL,
  `restaurant_adresse1` varchar(255) DEFAULT NULL,
  `restaurant_adresse2` varchar(255) DEFAULT NULL,
  `restaurant_adresse3` varchar(255) DEFAULT NULL,
  `restaurant_cp` int DEFAULT NULL,
  `restaurant_ville` varchar(100) DEFAULT NULL,
  `restaurant_coords` text,
  `client_id` int DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`),
  CONSTRAINT `restaurants_chk_1` CHECK ((length(`restaurant_cp`) = 5))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'Café One','123 Main St.',NULL,NULL,12345,'Example City',NULL,1),(2,'Bistro Two','456 Center Rd.',NULL,NULL,23456,'Another Town',NULL,2),(3,'Diner Three','789 Side Ave.',NULL,NULL,34567,'Third City',NULL,3),(4,'Eatery Four','012 Back Blvd.',NULL,NULL,45678,'Fourth Village',NULL,3),(5,'Restaurant Five','345 Cross Ln.',NULL,NULL,56789,'Fifth Hamlet',NULL,4),(6,'Restau TechHouse','345 Rue Sainte Croix',NULL,NULL,66666,'Sixth Chameau',NULL,5),(7,'Restaurant Tout Jeune Tout neuf','345 Cross Lucas.',NULL,NULL,11111,'Seventh Chalumeau',NULL,4),(10,'Test','TEst','test','test',33333,'bordeaux','19479404971409',1),(11,'test','test','test','test',33333,'test','1497149741097',3),(12,'Test resto','Test','ertezr','azofja',33000,'Bordeaux','29U29R209R902',1),(15,'Restau Phiphi','45Nrue du restau','rue Sintrac',NULL,16654,'Jesaispas','',3);
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salutations`
--

DROP TABLE IF EXISTS `salutations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salutations` (
  `salutation_id` int NOT NULL AUTO_INCREMENT,
  `salutation` text,
  PRIMARY KEY (`salutation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salutations`
--

LOCK TABLES `salutations` WRITE;
/*!40000 ALTER TABLE `salutations` DISABLE KEYS */;
INSERT INTO `salutations` VALUES (1,'M.'),(2,'Mme.'),(3,'Ms.'),(4,'Dr.'),(6,'Prof.'),(7,'Maître'),(8,'Lord'),(24,NULL),(25,'testt'),(29,'test'),(30,'testttttrtytfr'),(31,'iuguigiug'),(32,'teqgoiheoij'),(33,'test saluttot'),(34,'testtiqfho'),(36,'test autooo'),(38,'Hello'),(39,'tetzepoetugfopa');
/*!40000 ALTER TABLE `salutations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-21  9:29:09
