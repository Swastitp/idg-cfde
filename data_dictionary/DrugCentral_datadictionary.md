# DrugCentral Data Dictionary
**last updated: 9/1/2021**


 | ﻿table_name |column_name |data_type |column_descr | |
 |--- | --- | --- | --- | --- |
 | act_table_full | `act_id` | integer(32) | Unique id for activity data |  |
 | act_table_full | `struct_id` | integer(32) | DrugCentral structure id for drugs |  |
 | act_table_full | `target_id` | integer(32) | DrugCentral target id for targets |  |
 | act_table_full | `target_name` | character varying(200) | Target name |  |
 | act_table_full | `target_class` | character varying(50) | Protein target class |  |
 | act_table_full | `accession` | character varying(1000) | Unique entry identifier from UniProtKB |  |
 | act_table_full | `gene` | character varying(1000) | Name of the gene encoding the protein from UniProtKB |  |
 | act_table_full | `swissprot` | character varying(1000) | Entry name identifier from UniProtKB |  |
 | act_table_full | `act_value` | double precision(53) | Bioactivity data extracted from different sources |  |
 | act_table_full | `act_unit` | character varying(100) | Bioactivity measurement unit type |  |
 | act_table_full | `act_type` | character varying(100) | Bioactivity measurement type |  |
 | act_table_full | `act_comment` | character varying(1000) | Short description of the bioactivity data, e.g. assay type, measurement, conditions, etc |  |
 | act_table_full | `act_source` | character varying(100) | Source of the bioactivity data |  |
 | act_table_full | `relation` | character varying(5) | Mathematical identifier |  |
 | act_table_full | `moa` | smallint(16) | Mechanism of action of the drug |  |
 | act_table_full | `moa_source` | character varying(100) | Mechanism of action source |  |
 | act_table_full | `act_source_url` | character varying(500) | The URL for the source of the bioactivity data |  |
 | act_table_full | `moa_source_url` | character varying(500) | The URL for the source of the mechanism of action for a drug |  |
 | act_table_full | `action_type` | character varying(50) | Pharmacological action type |  |
 | act_table_full | `first_in_class` | smallint(16) | First in class drug annotation |  |
 | act_table_full | `tdl` | character varying(500) | Target development level, as defined at http://juniper.health.unm.edu/tcrd/ |  |
 | act_table_full | `act_ref_id` | integer(32) | Unique identifier of the bioactivity data reference |  |
 | act_table_full | `moa_ref_id` | integer(32) | Unique identifier of the reference for the mechanism of action |  |
 | act_table_full | `organism` | character varying(150) | The species expressing the target |  |
 | action_type | `id` | integer(32) | Unique identifier of the pharmacological action type |  |
 | action_type | `action_type` | character varying(50) | Pharmacological action type |  |
 | action_type | `description` | character varying(200) | Short description of each pharmacological action type |  |
 | action_type | `parent_type` | character varying(50) | Pharmacological action type of the parent molecule |  |
 | active_ingredient | `id` | integer(32) | DrugCentral unique identifier for active ingredient entry extracted from DailyMed data |  |
 | active_ingredient | `active_moiety_unii` | character varying(20) | UNII moiety code of the active substance extracted from DailyMed data |  |
 | active_ingredient | `active_moiety_name` | character varying(4000) | UNII moiety nameof the active substance extracted from DailyMed data |  |
 | active_ingredient | `unit` | character varying(20) | Measurement unit type |  |
 | active_ingredient | `quantity` | double precision(53) | The amount of active ingredient |  |
 | active_ingredient | `substance_unii` | character varying(20) | UNII code of the active substance extracted from DailyMed data |  |
 | active_ingredient | `substance_name` | character varying(4000) | Active substance name extracted from DailyMed data |  |
 | active_ingredient | `ndc_product_code` | character varying(20) | FDA NDC code of the drug product extracted from DailyMed data |  |
 | active_ingredient | `struct_id` | integer(32) | DrugCentral structure id mapped to the active substance |  |
 | active_ingredient | `quantity_denom_unit` | character varying(20) | Unit type for the quantitiy of the active substance in the drug product (DailyMed) |  |
 | active_ingredient | `quantity_denom_value` | double precision(53) | Quantitiy value of the active substance in the drug product (DailyMed) |  |
 | approval | `id` | integer(32) | Unique identifier for the approval entry |  |
 | approval | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | approval | `approval` | date(3) | Approval date of the drug |  |
 | approval | `type` | character varying(200) | Approval agency |  |
 | approval | `applicant` | character varying(100) | The name of the applicant |  |
 | approval | `orphan` | boolean | Orphan status |  |
 | approval_type | `id` | integer(32) | Unique DrugCentral identifier for the indexed approval agencies |  |
 | approval_type | `descr` | character varying(200) | The name of the approval agengies indexed in DrugCentral |  |
 | atc | `id` | integer(32) | DrugCentral identifier for the ATC codes |  |
 | atc | `code` | character(7) | The ATC code of the specific drug |  |
 | atc | `chemical_substance` | character varying(250) | The drug name |  |
 | atc | `l1_code` | character(1) | The ATC level 1 of the drug |  |
 | atc | `l1_name` | character varying(200) | The corresponding name of the level 1 ATC code of the drug |  |
 | atc | `l2_code` | character(3) | The ATC level 2 of the drug |  |
 | atc | `l2_name` | character varying(200) | The corresponding name of the level 2 ATC code of the drug |  |
 | atc | `l3_code` | character(4) | The ATC level 3 of the drug |  |
 | atc | `l3_name` | character varying(200) | The corresponding name of the level 3 ATC code of the drug |  |
 | atc | `l4_code` | character(5) | The ATC level 4 of the drug |  |
 | atc | `l4_name` | character varying(200) | The corresponding name of the level 4 ATC code of the drug |  |
 | atc | `chemical_substance_count` | integer(32) | Number of active substances in the drug product |  |
 | atc_ddd | `id` | integer(32) | Unique identifier for the entry |  |
 | atc_ddd | `atc_code` | character(7) | The corresponding ATC code of the drug |  |
 | atc_ddd | `ddd` | real(24) | Defined daily dose |  |
 | atc_ddd | `unit_type` | character varying(10) | Measurement unit type |  |
 | atc_ddd | `route` | character varying(20) | Administration route of the drug |  |
 | atc_ddd | `comment` | character varying(100) | Remarks regarding the drug or administration route |  |
 | atc_ddd | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | attr_type | `id` | integer(32) | Unique identifier for the entry |  |
 | attr_type | `name` | character varying(100) | Attribute name |  |
 | attr_type | `type` | character varying(20) | Data type of the attribute (e.g., STRING) |  |
 | data_source | `src_id` | smallint(16) | Unique identifier for each entry |  |
 | data_source | `source_name` | character varying(100) | Name of the source for bioactivity data |  |
 | dbversion | `version` | bigint(64) | Version of the database |  |
 | dbversion | `dtime` | timestamp without time zone(6) | Time and date of the version release |  |
 | ddi | `id` | integer(32) | Unique identifier for each  entry of the table |  |
 | ddi | `drug_class1` | character varying(500) | Drug-drug interaction class 1 |  |
 | ddi | `drug_class2` | character varying(500) | Drug-drug interaction class 2 |  |
 | ddi | `ddi_ref_id` | integer(32) | Drug-drug interaction reference  |  |
 | ddi | `ddi_risk` | character varying(200) | Risk assement of the drug-drug interaction |  |
 | ddi | `description` | character varying(4000) | Description of the drug-drug interaction |  |
 | ddi | `source_id` | character varying(200) | Drug class interactions as DDI sources |  |
 | ddi_risk | `id` | integer(32) | Unique identifier for each risk class |  |
 | ddi_risk | `risk` | character varying(200) | Name of the risk classes |  |
 | ddi_risk | `ddi_ref_id` | integer(32) | Reference for the DDI risk |  |
 | doid | `id` | integer(32) | Unique identifier for each  entry of the table |  |
 | doid | `label` | character varying(1000) | Disease name |  |
 | doid | `doid` | character varying(50) | Disease ontology ID |  |
 | doid | `url` | character varying(100) | URL link of the disease to the Disease Ontology DB |  |
 | doid_xref | `id` | integer(32) | Table identifier for each entry |  |
 | doid_xref | `doid` | character varying(50) | Disease ontology ID |  |
 | doid_xref | `source` | character varying(50) | Source for the data |  |
 | doid_xref | `xref` | character varying(50) | External reference id of the medical term |  |
 | drug_class | `id` | integer(32) | Table identifier for each entry |  |
 | drug_class | `name` | character varying(500) | Drug class name |  |
 | drug_class | `is_group` | smallint(16) | 1/0 if group or not |  |
 | drug_class | `source` | character varying(100) | Source for the data |  |
 | faers | `id` | integer(32) | Table identifier for each entry |  |
 | faers | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | faers | `meddra_name` | character varying(200) | MEDDRA term for the disease |  |
 | faers | `meddra_code` | bigint(64) | MEDDRA code for the disease |  |
 | faers | `level` | character varying(5) | Class of the MEDDRA term |  |
 | faers | `llr` | double precision(53) | Likelihood Ratio based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers | `llr_threshold` | double precision(53) | Likelihood Ratio threshold based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers | `drug_ae` | integer(32) | Number of patients taking drug and having adverse event |  |
 | faers | `drug_no_ae` | integer(32) | Number of patients taking drug and not having adverse event |  |
 | faers | `no_drug_ae` | integer(32) | Number of patients not taking drug and having adverse event |  |
 | faers | `no_drug_no_ae` | integer(32) | Number of patients not taking drug and not having adverse event |  |
 | faers_female | `id` | integer(32) | Table identifier for each entry |  |
 | faers_female | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | faers_female | `meddra_name` | character varying(200) | MEDDRA term for the disease |  |
 | faers_female | `meddra_code` | bigint(64) | MEDDRA code for the disease |  |
 | faers_female | `level` | character varying(5) | Class of the MEDDRA term |  |
 | faers_female | `llr` | double precision(53) | Likelihood Ratio based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers_female | `llr_threshold` | double precision(53) | Likelihood Ratio threshold based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers_female | `drug_ae` | integer(32) | Number of female patients taking drug and having adverse event |  |
 | faers_female | `drug_no_ae` | integer(32) | Number of female patients taking drug and not having adverse event |  |
 | faers_female | `no_drug_ae` | integer(32) | Number of female patients not taking drug and having adverse event |  |
 | faers_female | `no_drug_no_ae` | integer(32) | Number of female patients not taking drug and not having adverse event |  |
 | faers_male | `id` | integer(32) | Table identifier for each entry |  |
 | faers_male | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | faers_male | `meddra_name` | character varying(200) | MEDDRA term for the disease |  |
 | faers_male | `meddra_code` | bigint(64) | MEDDRA code for the disease |  |
 | faers_male | `level` | character varying(5) | Class of the MEDDRA term |  |
 | faers_male | `llr` | double precision(53) | Likelihood Ratio based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers_male | `llr_threshold` | double precision(53) | Likelihood Ratio threshold based on method described in http://dx.doi.org/10.1198/jasa.2011.ap10243 |  |
 | faers_male | `drug_ae` | integer(32) | Number of male patients taking drug and having adverse event |  |
 | faers_male | `drug_no_ae` | integer(32) | Number of male patients taking drug and not having adverse event |  |
 | faers_male | `no_drug_ae` | integer(32) | Number of male patients not taking drug and having adverse event |  |
 | faers_male | `no_drug_no_ae` | integer(32) | Number of male patients not taking drug and not having adverse event |  |
 | faers_top | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | faers_top | `meddra_name` | character varying(200) | MEDDRA term for the disease |  |
 | id_type | `id` | integer(32) | Unique id for bioactivity databases linked to DrugCentreal |  |
 | id_type | `type` | character varying(50) | Name of the identifier linked to DrugCentral |  |
 | id_type | `description` | character varying(500) | Name of the source database |  |
 | id_type | `url` | character varying(500) | Link url to the webpage of the database |  |
 | identifier | `id` | integer(32) | Table identifier for each entry |  |
 | identifier | `identifier` | character varying(50) | Identifier extracted from the linked databases |  |
 | identifier | `id_type` | character varying(50) | Identifier type |  |
 | identifier | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | identifier | `parent_match` | boolean | signals parent molecules for the identifier |  |
 | inn_stem | `id` | integer(32) | Table identifier for each entry |  |
 | inn_stem | `stem` | character varying(50) | STEM |  |
 | inn_stem | `definition` | character varying(1000) | STEM definition |  |
 | inn_stem | `national_name` | character varying(20) | STEM source |  |
 | inn_stem | `length` | smallint(16) | STEM length in characters |  |
 | inn_stem | `discontinued` | boolean | STEM status, boolean value |  |
 | label | `id` | character varying(50) | Label ID |  |
 | label | `category` | character varying(100) | Label type |  |
 | label | `title` | character varying(1000) | Drug name |  |
 | label | `effective_date` | date(3) | Label issued date |  |
 | label | `assigned_entity` | character varying(500) | The entity issuing the label |  |
 | label | `pdf_url` | character varying(500) | Link url to the label pdf |  |
 | lincs_signature | `id` | integer(32) | Unique ID for lincs data |  |
 | lincs_signature | `struct_id1` | integer(32) | First drug structure id  |  |
 | lincs_signature | `struct_id2` | integer(32) | Second drug structure id  |  |
 | lincs_signature | `is_parent1` | boolean | Signals if the first drug is a parent structure of the DC structure id  |  |
 | lincs_signature | `is_parent2` | boolean | Signals if the second drug is a parent structure of the DC structure id  |  |
 | lincs_signature | `cell_id` | character varying(10) | Id of the cell type |  |
 | lincs_signature | `rmsd` | double precision(53) | Root-mean-square deviation value |  |
 | lincs_signature | `rmsd_norm` | double precision(53) | Normalized root-mean-square deviation value |  |
 | lincs_signature | `pearson` | double precision(53) | Value of the Pearson correlation coefficient |  |
 | lincs_signature | `euclid` | double precision(53) | Value of the Euclidean distance |  |
 | ob_exclusivity | `id` | integer(32) | Table identifier for each entry |  |
 | ob_exclusivity | `appl_type` | character(1) | Patent application type |  |
 | ob_exclusivity | `appl_no` | character(6) | Application number |  |
 | ob_exclusivity | `product_no` | character(3) | Product numbers assigend to application number by FDA |  |
 | ob_exclusivity | `exclusivity_code` | character varying(10) | Exclusivity code |  |
 | ob_exclusivity | `exclusivity_date` | date(3) | Expiring date for the exclusivity |  |
 | ob_exclusivity_code | `code` | character varying(10) | Exclusivity code |  |
 | ob_exclusivity_code | `description` | character varying(500) | Description of the exclusivity code |  |
 | ob_exclusivity_view | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | ob_exclusivity_view | `strength` | character varying(4000) | Concentration of active substance in product |  |
 | ob_exclusivity_view | `trade_name` | character varying(200) | Commercial name of the drug |  |
 | ob_exclusivity_view | `applicant` | character varying(50) | Name of the applying company |  |
 | ob_exclusivity_view | `appl_type` | character(1) | Type of FDA application |  |
 | ob_exclusivity_view | `appl_no` | character(6) | FDA applciation number |  |
 | ob_exclusivity_view | `approval_date` | date(3) | Approval date of the drug |  |
 | ob_exclusivity_view | `type` | character varying(5) | Type of exclusivity |  |
 | ob_exclusivity_view | `dose_form` | character varying(50) | Pharmaceutical formulation |  |
 | ob_exclusivity_view | `route` | character varying(100) | Administration route |  |
 | ob_exclusivity_view | `exclusivity_date` | date(3) | Exclusivity expiration date |  |
 | ob_exclusivity_view | `description` | character varying(500) | Exclusivity description |  |
 | ob_patent | `id` | integer(32) | Unique ID for OrangeBook (OB) patent entry in DrugCentral  |  |
 | ob_patent | `appl_type` | character(1) | FDA application type associtated with the patent id  |  |
 | ob_patent | `appl_no` | character(6) | FDA application number associtated with the patent id  |  |
 | ob_patent | `product_no` | character(3) | FDA product number |  |
 | ob_patent | `patent_no` | character varying(200) | Patent number |  |
 | ob_patent | `patent_expire_date` | date(3) | Patent expiration date |  |
 | ob_patent | `drug_substance_flag` | character(1) | Signals if the patent is covers the drug substance |  |
 | ob_patent | `drug_product_flag` | character(1) | Signals if the patent is covers the drug product |  |
 | ob_patent | `patent_use_code` | character varying(10) | Patent use code |  |
 | ob_patent | `delist_flag` | character(1) | Signals delisted patents |  |
 | ob_patent_use_code | `code` | character varying(10) | Patent use code |  |
 | ob_patent_use_code | `description` | character varying(500) | Patent use code description |  |
 | ob_patent_view | `struct_id` | integer(32) | DrugCental structure id mapped to an active substance in a drug product associateed to a patent  |  |
 | ob_patent_view | `strength` | character varying(4000) | Concentration of active substance in product |  |
 | ob_patent_view | `patent_no` | character varying(200) | Patent number |  |
 | ob_patent_view | `description` | character varying(500) | Patent description |  |
 | ob_patent_view | `trade_name` | character varying(200) | Commercial name of the drug |  |
 | ob_patent_view | `applicant` | character varying(50) | Name of the applying company |  |
 | ob_patent_view | `appl_type` | character(1) | FDA application type |  |
 | ob_patent_view | `appl_no` | character(6) | FDA application number |  |
 | ob_patent_view | `type` | character varying(5) | Patent type |  |
 | ob_patent_view | `dose_form` | character varying(50) | Pharmaceutical formulation of the drug product |  |
 | ob_patent_view | `route` | character varying(100) | Administration route |  |
 | ob_patent_view | `approval_date` | date(3) | Approval date of the drug |  |
 | ob_patent_view | `patent_expire_date` | date(3) | Patent expiration date |  |
 | ob_product | `id` | integer(32) | Unique ID in DrugCentral for a OB product |  |
 | ob_product | `ingredient` | character varying(500) | Active substance in OB product |  |
 | ob_product | `trade_name` | character varying(200) | Commercial name of the OB product |  |
 | ob_product | `applicant` | character varying(50) | Name of the applying company |  |
 | ob_product | `strength` | character varying(500) | Concentration of active substance in product |  |
 | ob_product | `appl_type` | character(1) | FDA application type |  |
 | ob_product | `appl_no` | character(6) | FDA application number |  |
 | ob_product | `te_code` | character varying(20) | Therapeutic Equivalence Code |  |
 | ob_product | `approval_date` | date(3) | Approval date of the drug |  |
 | ob_product | `rld` | smallint(16) | Reference Listed Drug |  |
 | ob_product | `type` | character varying(5) | Rx or OTC drug product |  |
 | ob_product | `applicant_full_name` | character varying(200) | Name of the applying company |  |
 | ob_product | `dose_form` | character varying(50) | Pharmaceutical formulation of the drug product |  |
 | ob_product | `route` | character varying(100) | Administration route |  |
 | ob_product | `product_no` | character(3) | FDA product number |  |
 | omop_relationship | `id` | integer(32) | DrugCentral unique table identifier |  |
 | omop_relationship | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | omop_relationship | `concept_id` | integer(32) | DrugCentral Identifier of each concept name |  |
 | omop_relationship | `relationship_name` | character varying(256) | Type of concept name: indication/contraindication |  |
 | omop_relationship | `concept_name` | character varying(256) | Disease name according to UMLS MetaThesaurus |  |
 | omop_relationship | `umls_cui` | character(8) | Concept Unique Identifier extracted from UMLS MetaThesaurus |  |
 | omop_relationship | `snomed_full_name` | character varying(500) | Concept full name from SNOMED CT |  |
 | omop_relationship | `cui_semantic_type` | character(4) | Concept semantic type from UMLS MetaThesaurus |  |
 | omop_relationship | `snomed_conceptid` | bigint(64) | Unique identifier of each concept from SNOMED CT |  |
 | omop_relationship_doid_view | `id` | integer(32) | DrugCentral unique table identifier |  |
 | omop_relationship_doid_view | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | omop_relationship_doid_view | `concept_id` | integer(32) | DrugCentral Identifier of each concept name |  |
 | omop_relationship_doid_view | `relationship_name` | character varying(256) | Type of concept name: indication/contraindication |  |
 | omop_relationship_doid_view | `concept_name` | character varying(256) | Disease name according to UMLS MetaThesaurus |  |
 | omop_relationship_doid_view | `umls_cui` | character(8) | Concept Unique Identifier extracted from UMLS MetaThesaurus |  |
 | omop_relationship_doid_view | `snomed_full_name` | character varying(500) | Concept full name from SNOMED CT |  |
 | omop_relationship_doid_view | `cui_semantic_type` | character(4) | Concept semantic type from UMLS MetaThesaurus |  |
 | omop_relationship_doid_view | `snomed_conceptid` | bigint(64) | Unique identifier of each concept from SNOMED CT |  |
 | omop_relationship_doid_view | `doid` | text | Disease Ontology ID linked to doid table |  |
 | parentmol | `cd_id` | integer(32) | DrugCentral unique table identifier |  |
 | parentmol | `name` | character varying(250) | Drug name |  |
 | parentmol | `cas_reg_no` | character varying(50) | Drug CAS number |  |
 | parentmol | `inchi` | character varying(32672) | Drug INCHI |  |
 | parentmol | `nostereo_inchi` | character varying(32672) | Drug INCHI without chirality |  |
 | parentmol | `molfile` | text | MDL file format of the molecular structure |  |
 | parentmol | `molimg` | bytea | Encoded image of the molecular structure |  |
 | parentmol | `smiles` | character varying(32672) | SMILES code |  |
 | parentmol | `inchikey` | character(27) | Drug INCHI key |  |
 | pdb | `id` | integer(32) | DrugCentral unique table identifier |  |
 | pdb | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | pdb | `pdb` | character(4) | PDB identifier of the drug-protein complex |  |
 | pdb | `chain_id` | character varying(3) | CHAIN ID extracted from PDB |  |
 | pdb | `accession` | character varying(20) | Entry ID of the target from UniProt |  |
 | pdb | `title` | character varying(1000) | PDB title |  |
 | pdb | `pubmed_id` | integer(32) | PUBMED identifier of the reference |  |
 | pdb | `exp_method` | character varying(50) | Experimental method used to solve the structure |  |
 | pdb | `deposition_date` | date(3) | PDB deposition date of the solved protein-drug complex |  |
 | pdb | `ligand_id` | character varying(20) | PDB drug identifier |  |
 | pharma_class | `id` | integer(32) | DrugCentral unique table identifier |  |
 | pharma_class | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | pharma_class | `type` | character varying(20) | Pharmacological class type according to the source |  |
 | pharma_class | `name` | character varying(1000) | Pharmacological class name |  |
 | pharma_class | `class_code` | character varying(20) | Pharmacological class code according to the source |  |
 | pharma_class | `source` | character varying(100) | Source of the pharmacological class |  |
 | pka | `id` | integer(32) | DrugCentral unique table identifier |  |
 | pka | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | pka | `pka_level` | character varying(5) | The pKa type for multiprotic molecules |  |
 | pka | `value` | double precision(53) | The predicted pKa value |  |
 | pka | `pka_type` | character(1) | Basic or acidic pKa type |  |
 | prd2label | `ndc_product_code` | character varying(20) | FDA NDC product code |  |
 | prd2label | `label_id` | character varying(50) | FDA label ID |  |
 | prd2label | `id` | integer(32) | DrugCentral unique table identifier to link products to labels |  |
 | product | `id` | integer(32) | DrugCentral unique product table identifier |  |
 | product | `ndc_product_code` | character varying(20) | FDA NDC product code |  |
 | product | `form` | character varying(250) | Drug product formulation |  |
 | product | `generic_name` | character varying(4000) | Drug generic name |  |
 | product | `product_name` | character varying(1000) | Drug product name |  |
 | product | `route` | character varying(50) | Administration route |  |
 | product | `marketing_status` | character varying(500) | Market status of a drug product in USA |  |
 | product | `active_ingredient_count` | integer(32) | Number of active ingredients in the drug product |  |
 | property | `id` | integer(32) | DrugCentral unique property table identifier |  |
 | property | `property_type_id` | integer(32) | (null) |  |
 | property | `property_type_symbol` | character varying(10) | (null) |  |
 | property | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | property | `value` | double precision(53) | Property value |  |
 | property | `reference_id` | integer(32) | The DrugCentral reference identifier |  |
 | property | `reference_type` | character varying(50) | Reference type |  |
 | property | `source` | character varying(80) | Reference source |  |
 | property_type | `id` | integer(32) | DrugCentral unique property_type table identifier |  |
 | property_type | `category` | character varying(20) | Property class |  |
 | property_type | `name` | character varying(80) | Property name |  |
 | property_type | `symbol` | character varying(10) | Property abbreviation |  |
 | property_type | `units` | character varying(10) | Property measeurment unit |  |
 | protein_type | `id` | integer(32) | DrugCentral unique protein_type table identifier |  |
 | protein_type | `type` | character varying(50) | Protein class |  |
 | ref_type | `id` | integer(32) | Reference type identifier assigned in DrugCentral |  |
 | ref_type | `type` | character varying(50) | Reference type indexed in DrugCentral |  |
 | reference | `id` | integer(32) | table identifier |  |
 | reference | `pmid` | integer(32) | PUBMED identifier of the reference |  |
 | reference | `doi` | character varying(50) | DOI number for the reference |  |
 | reference | `document_id` | character varying(200) | Drug label ID extracted from FDA, EMA, PMDA, etc |  |
 | reference | `type` | character varying(50) | Reference type according to ref_type table |  |
 | reference | `authors` | character varying(4000) | Reference authors |  |
 | reference | `title` | character varying(500) | Reference title |  |
 | reference | `isbn10` | character(10) | Reference ISBN for books, book chapter, etc |  |
 | reference | `url` | character varying(1000) | Link to the webpage of the reference |  |
 | reference | `journal` | character varying(100) | Journal name for the reference |  |
 | reference | `volume` | character varying(20) | Journal volume |  |
 | reference | `issue` | character varying(20) | Journal issue |  |
 | reference | `dp_year` | integer(32) | Journal article publication year |  |
 | reference | `pages` | character varying(50) | Journal article pages |  |
 | section | `id` | integer(32) | Unique ID in DrugCentral table |  |
 | section | `text` | text | Drug label content of the product |  |
 | section | `label_id` | character varying(50) | Drug label id |  |
 | section | `code` | character varying(20) | Drug label code |  |
 | section | `title` | character varying(4000) | Drug label title |  |
 | struct2atc | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | struct2atc | `atc_code` | character(7) | Drug ATC code |  |
 | struct2drgclass | `id` | integer(32) | DrugCentral table identifier |  |
 | struct2drgclass | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | struct2drgclass | `drug_class_id` | integer(32) | Drug class identifier from DrugCentral |  |
 | struct2obprod | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | struct2obprod | `prod_id` | integer(32) | DrugCentral drug product identifier |  |
 | struct2obprod | `strength` | character varying(4000) | Concentration of the active substance |  |
 | struct2parent | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | struct2parent | `parent_id` | integer(32) | DrugCentral parentmol table identifier |  |
 | struct_type_def | `id` | integer(32) | DrugCentral unique identifier for structure type |  |
 | struct_type_def | `type` | character varying(50) | Type of structures defined in DrugCentral |  |
 | struct_type_def | `description` | character varying(200) | Short description of the structure type |  |
 | structure_type | `id` | integer(32) | DrugCentral table identifier |  |
 | structure_type | `struct_id` | integer(32) | DrugCentral structure id for drug |  |
 | structure_type | `type` | character varying(50) | Type of structures defined in DrugCentral |  |
 | structures | `cd_id` | integer(32) | DrugCentral structure id for drug |  |
 | structures | `cd_formula` | character varying(100) | Drug chemical formula |  |
 | structures | `cd_molweight` | double precision(53) | Drug molecular weight |  |
 | structures | `id` | integer(32) | DrugCentral structure ID |  |
 | structures | `clogp` | double precision(53) | Calculated clogP of the drug |  |
 | structures | `alogs` | double precision(53) | Calculated clogS of the drug |  |
 | structures | `cas_reg_no` | character varying(50) | CAS number of the drug |  |
 | structures | `tpsa` | real(24) | Calculated TPSA property of the drug |  |
 | structures | `lipinski` | integer(32) | Calculated Lipinski rule for the drug |  |
 | structures | `name` | character varying(250) | Preffered drug name |  |
 | structures | `no_formulations` | integer(32) | Number of formulations |  |
 | structures | `stem` | character varying(50) | INN STEM of the drug |  |
 | structures | `molfile` | text | Depiction of the chemical structure of the drug |  |
 | structures | `mrdef` | character varying(32672) | Drug description |  |
 | structures | `enhanced_stereo` | boolean | Signals a structure with chiral centers |  |
 | structures | `arom_c` | integer(32) | Calculated number of aromatic C atoms of the drug |  |
 | structures | `sp3_c` | integer(32) | Calculated number of sp3 C atoms of the drug |  |
 | structures | `sp2_c` | integer(32) | Calculated number of sp2 C atoms of the drug |  |
 | structures | `sp_c` | integer(32) | Calculated number of sp C atoms of the drug |  |
 | structures | `halogen` | integer(32) | Calculated number of halogen atoms of the drug |  |
 | structures | `hetero_sp2_c` | integer(32) | Calculated number of hetero and sp2 C atoms of the drug |  |
 | structures | `rotb` | integer(32) | Number of rotatable bonds |  |
 | structures | `molimg` | bytea | Image file of the chemical structure of the drug |  |
 | structures | `o_n` | integer(32) | Number of H-bond acceptor |  |
 | structures | `oh_nh` | integer(32) | Number of H-bond donors |  |
 | structures | `inchi` | character varying(32672) | INCHI code |  |
 | structures | `smiles` | character varying(32672) | SMILES code |  |
 | structures | `rgb` | integer(32) | number of rigid bonds |  |
 | structures | `fda_labels` | integer(32) | Has labels in FDA |  |
 | structures | `inchikey` | character(27) | INCHI KEY |  |
 | structures | `status` | character varying(10) | Drug status regarding patent and/or marketing status od the product containing the drug substance |  |
 | synonyms | `syn_id` | integer(32) | DrugCentral synonim ID |  |
 | synonyms | `id` | integer(32) | DrugCentral structure id for drug |  |
 | synonyms | `name` | character varying(250) | Drug name |  |
 | synonyms | `preferred_name` | smallint(16) | Preffered name of the drug |  |
 | synonyms | `parent_id` | integer(32) | ID of a parent drug |  |
 | synonyms | `lname` | character varying(250) | Synonim names |  |
 | target_class | `l1` | character varying(50) | Target class name |  |
 | target_class | `id` | integer(32) | Unique identifier for target class |  |
 | target_component | `id` | integer(32) | DrugCentral table identifier |  |
 | target_component | `accession` | character varying(20) | Unique entry identifier from UniProtKB |  |
 | target_component | `swissprot` | character varying(20) | Entry name identifier from UniProtKB |  |
 | target_component | `organism` | character varying(150) | The species expressing the target from UniProtKB |  |
 | target_component | `name` | character varying(200) | Target full-name from UniProtKB |  |
 | target_component | `gene` | character varying(25) | Name of the gene encoding the protein from UniProtKB |  |
 | target_component | `geneid` | bigint(64) | Gene identifier from UniProtKB |  |
 | target_component | `tdl` | character varying(5) | Target development level, as defined at http://juniper.health.unm.edu/tcrd/ |  |
 | target_dictionary | `id` | integer(32) | DrugCentral table identifier |  |
 | target_dictionary | `name` | character varying(200) | Target full-name from UniProtKB |  |
 | target_dictionary | `target_class` | character varying(50) | DrugCentral target class definition |  |
 | target_dictionary | `protein_components` | smallint(16) | Number of components of a target |  |
 | target_dictionary | `protein_type` | character varying(50) | Target type as defined in DrugCentral |  |
 | target_dictionary | `tdl` | character varying(500) | Target development level, as defined at http://juniper.health.unm.edu/tcrd/ |  |
 | target_go | `id` | character(10) | Gene ontology ID |  |
 | target_go | `term` | character varying(200) | Term description |  |
 | target_go | `type` | character(1) | Type of GO term |  |
 | target_keyword | `id` | character(7) | DrugCentral table identifier |  |
 | target_keyword | `descr` | character varying(4000) | Target description |  |
 | target_keyword | `category` | character varying(50) | Term describing the functional category for a target |  |
 | target_keyword | `keyword` | character varying(200) | DrugCentral keyword |  |
 | td2tc | `target_id` | integer(32) | Target ID extracted from target_dictionary table |  |
 | td2tc | `component_id` | integer(32) | Target ID extracted from target_component table |  |
 | tdgo2tc | `id` | integer(32) | DrugCentral table identifier |  |
 | tdgo2tc | `go_id` | character(10) | Gene ontology ID |  |
 | tdgo2tc | `component_id` | integer(32) | Target ID corresponding to target_component table |  |
 | tdkey2tc | `id` | integer(32) | DrugCentral table identifier |  |
 | tdkey2tc | `tdkey_id` | character(7) | Identifier corresponding to target_keyword table |  |
 | tdkey2tc | `component_id` | integer(32) | Target ID corresponding to target_component table |  |
 |  |  |  |  |  |
