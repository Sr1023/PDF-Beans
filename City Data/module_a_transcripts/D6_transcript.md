# D6 — MODULE A transcript (PDF-DATAPACK v1.1)

## Metadata

- doc_id: D6
- source_file: GHSL_UCDB_R2024.pdf
- source_physical_pages: 1-633 (anchors `[D6-pN]` use the physical page number N of the source file)
- page_count: 633
- pdf_metadata_title: [not set in file]
- pdf_metadata_author: Marcello Schiavina
- pdf_metadata_creationDate: D:20250729114054+02'00'
- ocr_pages: [] (no page is a scanned image of text; see skipped-page lines for image-only pages)
- title / author_publisher / publication_date: quoted verbatim in `## Document identification` below, each with the page anchor it is copied from.

## Document identification

- title: "Stats in the City – the GHSL Urban Centre Database 2025" [D6-p1]
- author_publisher: "European Commission, Joint Research Centre" [D6-p2]
- publication_date: "Luxembourg: Publications Office of the European Union, 2024" [D6-p2]

## Running headers/footers (noted once, removed from page bodies)

- `#` (on 629 of 633 pages; `#` = page-number digits)

## Pages

### [D6-p1]

```text
Stats in the City –  the GHSL Urban Centre 
Database 2025 

Public release  GHS-UCDB R2024 

Melchiorri, M., Mari Rivero, I., Florio, P., Schiavina, 
M., Krasnodebska, K., Politis, P., Uhl, J., Pesaresi, M., 
Maffenini, L., Sulis, P., Crippa, M., Guizzardi, D., 
Pisoni, E., Belis, C., Oom, D., Branco, A., Mwaniki, D., 
Githira, D., Kochulem, E., Tommasi, P., Carioli, A., 
Ehrlich, D., Kemper, T., Dijkstra, L. 

2024 
```

### [D6-p2]

```text
This document is a publication by the Joint Research Centre (JRC), the European Commission’s science and knowledge 
service. It aims to provide evidence-based scientific support to the European policymaking process. The contents of this 
publication do not necessarily reflect the position or opinion of the European Commission. Neither the European 
Commission nor any person acting on behalf of the Commission is responsible for the use that might be made of this 
publication. For information on the methodology and quality underlying the data used in this publication for which the 

source is neither Eurostat nor other Commission services, users should contact the referenced source. The designations 
employed and the presentation of material on the maps do not imply the expression of any opinion whatsoever on the 
part of the European Union concerning the legal status of any country, territory, city or area or of its authorities, or 
concerning the delimitation of its frontiers or boundaries. 

Contact information 
Name: Thomas Kemper 
Address: Via E. Fermi, 2749 
Email: thomas.kemper@ec.europa.eu 
Tel.: +39 0332 78-5576 

EU Science Hub 
https://joint-research-centre.ec.europa.eu 

JRC139768 
Print  
ISBN 978-92-68-21609-5  doi:10.2760/5259274  
KJ-01-24-118-EN-C 
PDF  
ISBN 978-92-68-21603-3  doi:10.2760/3046391  
KJ-01-24-118-EN-N 
Luxembourg: Publications Office of the European Union, 2024  
© European Union, 2024  
The reuse policy of the European Commission documents is implemented by the Commission Decision 2011/833/EU of 12 
December 2011 on the reuse of Commission documents (OJ L 330, 14.12.2011, p. 39). Unless otherwise noted, the reuse of 
this document is authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence 
(https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed provided appropriate credit is given and 
any changes are indicated.  
For any use or reproduction of photos or other material that is not owned by the European Union permission must be 
sought directly from the copyright holders. 
How to cite this report: European Commission, Joint Research Centre, Melchiorri, M., Mari Rivero, I., Florio, P., Schiavina, 
M., Krasnodebska, K., Politis, P., Uhl, J., Pesaresi, M., Maffenini, L., Sulis, P., Crippa, M., Guizzardi, D., Pisoni, E., Belis, C., 
Oom, D., Branco, A., Mwaniki, D., Githira, D., Kochulem, E., Tommasi, P., Carioli, A., Ehrlich, D., Kemper, T. and Dijkstra, L., 
Stats in the City –  the GHSL Urban Centre Database 2025, Publications Office of the European Union, Luxembourg, 2024, 
https://data.europa.eu/doi/10.2760/3046391, JRC139768. 
```

### [D6-p3]

[LIST/CONTENTS PAGE — transcribed verbatim; used as completeness checklist]

```text
Contents 

Abstract .................................................................................................................................................. 1 

Authors .............................................................................................................................................. 2 

Contributors ....................................................................................................................................... 2 

1 Introduction ....................................................................................................................................... 3 

1.1 Overview .................................................................................................................................... 3 

1.2 Rationale .................................................................................................................................... 4 

1.3 History and Versioning .............................................................................................................. 4 

1.4 Main Characteristics .................................................................................................................. 4 

2 GHS_UCDB_GLOBE_R2024 - GHS Urban Centre Database multi-temporal and multi-dimensional 
attributes (1975-2030) ......................................................................................................................... 7 

2.1 Definitions ................................................................................................................................. 8 

2.1.1 
Thematic Domain ............................................................................................................ 8 

2.1.2 
Indicator groups .............................................................................................................. 8 

2.1.3 
Indicator .......................................................................................................................... 8 

2.1.4 
Attribute .......................................................................................................................... 8 

2.1.5 
value ................................................................................................................................ 8 

2.1.6 
Fixed Boundary ................................................................................................................ 9 

2.1.7 
Multi-temporal Boundary ................................................................................................ 9 

2.2 Improvements compared to the previous release .................................................................... 9 

2.3 Delineation of the Urban Centres – fix boundaries ................................................................ 10 

2.4 Delineation of the Urban Centres – multi-temporal boundaries ........................................... 11 

2.5 Geospatial data integration .................................................................................................... 13 

2.6 Quality control of the urban centres ....................................................................................... 14 

2.7 User guide ................................................................................................................................ 15 

2.7.1 
ArcGIS Pro ...................................................................................................................... 15 

2.7.2 
QGIS ............................................................................................................................... 18 

2.8 Fact sheets Specimen ............................................................................................................. 20 

2.9 GHS-UCDB indicator fact sheets – fixed boundary ................................................................ 22 

2.9.1 
General Characteristics ................................................................................................. 22 

2.9.2 
GHSL .............................................................................................................................. 36 

2.9.3 
Socioeconomic ............................................................................................................. 112 

2.9.4 
Land Use Land Cover .................................................................................................. 143 

2.9.5 
Exposure ...................................................................................................................... 164 
```

### [D6-p4]

[LIST/CONTENTS PAGE — transcribed verbatim; used as completeness checklist]

```text
2.9.6 
Hazards ....................................................................................................................... 322 

2.9.7 
SDGs ............................................................................................................................ 351 

2.9.8 
Climate ........................................................................................................................ 356 

2.9.9 
Emissions .................................................................................................................... 405 

2.9.10 Natural Systems .......................................................................................................... 494 

2.9.11 Health .......................................................................................................................... 510 

2.9.12 Water ........................................................................................................................... 520 

2.9.13 Infrastructure .............................................................................................................. 539 

2.9.14 Geography ................................................................................................................... 549 

2.9.15 Greenness .................................................................................................................... 579 

2.10 GHS-UCDB indicator fact sheets – multi-temporal boundaries ........................................... 590 

2.10.1 General Characteristics ............................................................................................... 590 

2.10.2 Multi-temporal GHSL................................................................................................... 599 

2.11 Input Data .............................................................................................................................. 613 

2.12 Technical Details ................................................................................................................... 613 

2.12.1 GHS_UCDB_GLOBE_R2024 ......................................................................................... 613 

2.12.2 GHS_UCDB_REGION_GLOBE_R2024A ........................................................................ 614 

2.12.3 GHS_UCDB_THEME_GLOBE_R2024A ......................................................................... 615 

2.12.4 GHS_UCDB_CONTRIBUTIONS_R2024A ....................................................................... 616 

2.12.5 GHS_UCDB_MTUC_GLOBE_R2024A ........................................................................... 616 

GHS_UCDB_MTUC_GLOBE_R2024A ........................................................................................ 617 

2.13 How to cite ............................................................................................................................. 617 

3 Conclusions ................................................................................................................................... 618 

References .......................................................................................................................................... 619 

List of Figures ..................................................................................................................................... 620 

List of Tables ...................................................................................................................................... 621 
```

### [D6-p5]

```text
Abstract 

The Global Human Settlement Layer (GHSL) project produces new global spatial information, 
evidence-based analytics and knowledge describing the human presence on Earth. It operates in a 
fully open and free data and methods access policy. The knowledge generated with the GHSL is 
supporting the definition, the public discussion and the implementation of European policies and the 
monitoring of international frameworks such as the 2030 Development Agenda. GHSL data continue 
to support the GEO Human Planet Initiative that is committed to developing a new generation of 
measurements and information products providing new scientific evidence and a comprehensive 
understanding of the human presence on the planet and that can support global policy processes with 
agreed, actionable and goal-driven metrics.  

This document describes the public release of the GHSL Urban Centre Database 2025 (GHS P2024). 
This release is based on the GHSL Data Package 2023, the Degree of Urbanisation to delineate spatial 
entities, and geospatial data integration from a variety of open source datasets to characterise them. 
The result is the most complete information system on cities to date with data for 11,422 quality 
controlled urban centres across 15 thematic domains, 63 indicator groups, 473 indicators, and 2602 
attributes. The UCDB has two data streams, one based on the fixed delineation of the 2025 
boundaries, the other based on a multi-temporal delineation of entities and their tracking over time. 

The UCDB integrates data from Copernicus Services (including Emergency, Land Monitoring, Marine 
and Climate), peer-reviewed datasets (i.e. from the scientific literature), and institutional information 
systems (i.e. from the United Nations). 

This document serves as a documentation to the dataset and includes indicator fact sheets to 
navigate the database. 

Prior to cite this report, please access the updated version available at: 
http://ghsl.jrc.ec.europa.eu/documents/GHS-UCDB_2024.pdf 
```

### [D6-p6]

```text
Authors 

Thomas, Kemper, JRC.E1 (team and project 
leader) 

Alessandra Carioli, JRC.E1 

Daniele Ehrlich, JRC. E1 

Pietro Florio, JRC.E1 

Katarzyna Krasnodebska, EUROPEAN 
DYNAMICS  

Luca Maffenini, Unisystems Luxembourg Sarl 

Ines Mari Rivero, Fincons SpA 

Michele Melchiorri, JRC.E1 

Contributors 

Panagiotis Politis, EUROPEAN DYNAMICS  

Martino Pesaresi, JRC.E1 

Marcello Schiavina, NTT Data 

Johannes Uhl, JRC.E1 

Pierpaolo Tommasi, Fincons SpA 

Lewis Dijkstra, JRC B.3 

Patrizia Sulis, JRC B.3 

Monica Crippa, Diego Guizzardi, Enrico Pisoni, 
Claudio Belis JRC C.5 

Duarte Oom, Alfredo Branco JRC E1 

Dennis Mwaniki, Edwin Kochulem, Daniel 
Githira, UN-Habitat Data and Analytics Section 

We wish to acknowledge the input of several other contributors who have helped the preparation of 
the UCDB with advices on data manipulation and sourcing, or for contributing datasets, in particular: 

Muriel Lux, Mercator Ocean for providing guidance on the use of Copernicus Marine data 

Guy Schvitz, JRC E.1 for provding instructions on the use of ACLED data 

Sepehr Marzi, Fincons SpA for provding support on hazard and exposure data 

Joao Porto de Albuquerque, University of Glasgow for providing the OSM completeness indicators 

Benjamin Herfort, Heidelberg University for providing the OSM completeness indicators 

Jeroen Smits, Radboud University for provding support for the Socio-economic data 
```

### [D6-p7]

```text
1 Introduction 

1.1 Overview 

The Global Human Settlement Layer (GHSL) project produces global spatial information, evidence-
based analytics, and knowledge describing the human presence on the planet. The GHSL relies on the 
design and implementation of spatial data processing technologies that allow automatic data 
analytics and information extraction from large amounts of heterogeneous geospatial data including 
global, fine-scale satellite image data streams, census data, and crowd sourced or volunteered 
geographic information sources.  

This document accompanies the public release of the GHSL Urban Centre Database 2025 (GHS-UCDB 
R2024A) and describes its contents. 

Each product is named according to the following convention: 

GHS-<name>_<spatial extent>_<release> 

For example, a product name GHS-UCDB_GLOBE_R2024A indicates the Urban Centre Database (GHS-
UCDB) produced globally in the release R2024A. 

Derived and sub-set products of the GHS-UCDB are named with a unique identifier according to the 
following convention:  

GHS_UCDB_<characteristic>_<spatialExtent>_<release> 

For example, a layer name GHS_UCDB_THEME_GLOBE_R2024A indicates the GHS-UCDB subset by 
thematic domain global, included in the release R2024A. 

The GHS-UCDB contains the following product and its distributions: 

• 
GHS_UCDB_GLOBE_R2024 – GHS Urban Centre Database global dataset as geopackage, and 
xlsx table with global coverage based on fixed boundary delineation of the urban centres in 
2025; 

• 
GHS_UCDB_REGION_GLOBE_R2024A – GHS Urban Centre Database by UN Region of the 
World as geopackage, and xlsx tables (all thematic domains, urban centres regional subset); 

• 
GHS_UCDB_THEME_GLOBE_R2024A– GHS Urban Centre Database by thematic area as 
geopackage, csv and xlsx tables (all urban centres, individual thematic are subset); 

• 
GHS_UCDB_CONTRIBUTIONS_R2024A – GHS Urban Centre Database contributors dataset as 
a csv and xlsx (all urban centres, a specific indicator); 

• 
GHS_UCDB_MTUC_GLOBE_R2024A – GHS Urban Centre Database global dataset as 
geopackage, csv and xlsx tables with global coverage based on multi-temporal delineation of 
entities and their tracking over time. 
```

### [D6-p8]

```text
1.2 Rationale 

Open data and free access are core principles of the GHSL (Melchiorri et al. 2019). They are aligned 
with the Directive on the re-use of public sector information (Directive 2003/98/EC1). The free and 
open access policy facilitates the information sharing and collective knowledge building, thus 
contributing to a democratisation of the information production. 

The GHSL Urban Centre Database contains the new GHSL data produced at the European Commission 
Directorate General Joint Research Centre in the Directorate for Societal Resilience and Security, in 
the Risk Management Unit (E.1) in the period 2023-2024 and its integration with other geospatial 
data. 

1.3 History and Versioning 

The GHSL Urban Centre Database 1.0 (GHS_STAT_UCDB2015MT_GLOBE_R2018A) was released first 
released in 2018 relaying on previous versions of the GHSL Data Package (R2018). The GHS Urban 
Centre Database (GHS-UCDB) described spatial entities called “urban centres” according to a set of 
multi-temporal thematic attributes gathered from the GHSL sources integrated with other sources 
available in the open scientific domain. 

A version v1.1 was released in 2019 (GHS_STAT_UCDB2015MT_GLOBE_R2019A) fixing values 
format, previously encoded as strings, and introduced the gpkg format (GeoPackage) OpenSource to 
encode UTF-8 characters (needed for new names) (v1.1), update of the Travel Time to Country Capital 
data by fixing issues in the algorithm and update of Greenness data by fixing issues in some values. 
In 2020, a v1.2 was released to update of CO2 and PM2 emissions data with the newly released 
EDGARv5.0 results aligned with the GHSL epochs (1975, 1990, 2000, 2015). This dataset is now 
based on population-based spatial proxies developed using the GHSL Data Package 2019 (Florczyk 
et al. 2019), update of the main Urban Centre name by using more reliable algorithm and input data 
(GISCO and OSM datasets). 

In 2023 and 2024 scientific contributions consolidated the GHS-UCDB foundations with a Nature 
Scientific Data descriptor, and a paper focusing on the innovations on urban data reporting introduced 
with the GHS-UCDB (Melchiorri 2022; Melchiorri et al. 2024). 

1.4 Main Characteristics 

The GHSL Urban Centre Database 2025 harmonises data reporting for cities addressing semantic 
clarity and consistency, and thematic and geographic consistency data gaps. 

The GHSL Urban Centre Database 2025 is a significantly improved, expanded and tailored product 
compared to its predecessor. Among the main characteristics: 

• 
Extended time series: 1975 – 2030 with 5 years interval up to annual coverage; 

• 
Wider thematic scope: 15 thematic domains (GHSL information, Socioeconomic, Land Use 
Land Cover, Exposure, Hazard and Risk, Greenness, SDGs, Climate, Natural Systems, Health, 
Water, Infrastructure, Geography, General Characteristics, Emissions), resulting in 473 
indicators, and 2602 attributes; 63 indicator groups for a fixed delineation of urban centres, 

1 http://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32003L0098 
```

### [D6-p9]

```text
and 2 thematic domains, 10 indicator groups, 21 indicators for multi-temporal urban centres 
delineation. 

• 
Copernicus Services data integration protocol: workflow for the aggregation or 
sampling, of geospatial data produced in the framework of Copernicus Services and 
reporting/integration for urban centres over time (from the Emergency, Land, Climate and 
Marine); 

• 
Off the shelf science for policy data: information format tailored to user types 
(geospatial, spreadsheet, thematic subsets, regional subsets) with direct link to SDG 11 
indicators, New Urban Agenda, Paris Agreement and Sendai Framework as well as EU policies. 
The dataset has been co-developed by policy stakeholders such as DG REGIO and UN-Habitat. 

• 
Collaborative dataset architecture: the specific distribution dedicated to collaborators 
allow to ingest indicators that are produced by the users-crowd and scientific community by 
keeping the Unique Identifier of the urban centres.  

The GHS-UCDB aggregates the most updated datasets from a variety of sources, including scientific 
datasets, literature, volunteered/crowd datasets, and data from institutional sources. The GHS-UCDB 
addresses the gaps in semantic clarity about urban/city datasets, the consistency of the delineation 
of such areas, and offers a complete and multi-thematic information for such harmonised areas –
the urban centres (Table 1). 
```

#### [D6-T1] TABLE — page 9
title_verbatim:
```text
Table 1 Relationship between observed data gaps, data features, design principles and solutions adopted for the 
```
table_flags: header: 2 printed header lines joined vertically per column (strings verbatim) [AMBIGUOUS: header words are placed in the column under which they are printed; labels printed across several columns (e.g. a year over a group of columns) sit in one of them]; 12 wrapped printed lines joined into their row's cells (line pitch tighter than the table's row pitch; text verbatim, joined with a space); cells marked `[merged in source]` hold one printed string spanning several columns

| Data gaps | Features | Principles [merged in source] | production of GHS-UCDB Principles [merged in source] | GHS-UCDB solutions |
|---|---|---|---|---|
|  | Definition | 1. | Standardized | Urban centres obtained by the application of |
|  |  |  | definition of the AOI | the Degree of Urbanisation Method – GHS- SMOD dataset. |
|  |  |  |  | Responsive to need for: |
| Semantic clarity and consistency |  |  |  | 2. analysis of the evolution of the territory that is today an urban centre (fixed boundary dataset GHS_UCDB_GLOBE_R2024) |
|  |  |  |  | 3. tracking over time of specific entities that change over time their territorial shape (multi-temporal boundaries dataset GHS_UCDB_MTUC_GLOBE_R2024A) |
|  | Coverage | 4. | Consistent global | Global geographical coverage, 11,422 quality-controlled entries with population ≥ |
|  |  |  | mapping | 50,000 inhabitants in 2025 |
| Thematic and geographic completeness | Spatial representation | 5. | Spatially explicit delineation of cities | Geospatial representation with extents at 1 km grid cell resolution (polygons), and centroid XY location (point) |
|  | Spatial, temporal and | 6. | multi- thematic, | Variables across 15 thematic domains, 63 indicator groups, 470+ indicators, and 2600+ |


### [D6-p10]

```text
thematic 
resolution 

multi-
dimensional, 
and multi-
temporal 
attributes 

Usability 
7. comparability 
of 
information 
in space and 
time 

Terms of Use 

attributes. Temporal domain spanning 1975 – 
2030 with 5 years interval up to annual 
coverage 

Thematic, geographical and semantic 
consistency 

The data in this data package are provided free-of-charge © European Union4. Reuse is authorised, 
provided the source is acknowledged. The reuse policy of the European Commission is implemented 
by a Decision of 12 December 2011 (2011/833/EU). For any inquiry related to the use of these data 
please contact the GHSL data producer team at the email address: JRC-GHSL-DATA@ec.europa.eu 

Disclaimer: The JRC data are provided "as is" and "as available" in conformity with the JRC Data 
Policy2 and the Commission Decision on reuse of Commission documents (2011/833/EU). Although 
the JRC guarantees its best effort in assuring quality when publishing these data, it provides them 
without any warranty of any kind, either express or implied, including, but not limited to, any implied 
warranty against infringement of third parties' property rights, or merchantability, integration, 
satisfactory quality and fitness for a particular purpose. The JRC has no obligation to provide technical 
support or remedies for the data. The JRC does not represent or warrant that the data will be error 
free or uninterrupted, or that all non-conformities can or will be corrected, or that any data are 
accurate or complete, or that they are of a satisfactory technical or scientific quality. The JRC or as 
the case may be the European Commission shall not be held liable for any direct or indirect, incidental, 
consequential or other damages, including but not limited to the loss of data, loss of profits, or any 
other financial loss arising from the use of the JRC data, or inability to use them, even if the JRC is 
notified of the possibility of such damages. 

The designations employed and the presentation of materials and maps do not imply the expression 
of any opinion whatsoever on the part of the European Union concerning the legal status of any 
country, territory or area or of its authorities, or concerning the delimitation of its frontiers or 
boundaries that if shown on the maps are only indicative. The boundaries and names shown on maps 
do not imply official endorsement or acceptance by the European Union. 

Prior to cite this report, please access the updated version available at: 
https://ghsl.jrc.ec.europa.eu/documents/GHS-
UCDB_R2024A.pdfhttp://ghsl.jrc.ec.europa.eu/documents/GHSL_Data_Package_2023.pdf 

2 JRC Data Policy https://doi.org/10.2788/607378 
```

### [D6-p11]

```text
2 GHS_UCDB_GLOBE_R2024 - GHS Urban Centre Database multi-temporal 
and multi-dimensional attributes (1975-2030) 

The GHS-UCDB is a dataset distributed in geospatial vector format, and in table format providing 
attributes to characterise 11,422 urban centres between 1975 and 2030 using the urban centres as 
reporting units (spatial entities). 

The GHS-UCDB is produced by geospatial data integration between Areas of Interest or “zones”, the 
urban centres defined according to the Degree of Urbanisation method, and a variety of open 
geospatial data. Figure 1 displays the GHSL data anatomy and the series of GHSL data that are 
upstream of the GHS-UCDB. The database is an Analytical Dataset of the GHSL as it is derived from 
the analysis of GHSL datasets in combination with other free and open datasets. 
```

#### [D6-F1] FIGURE — page 11
caption_verbatim:
```text
Figure 1 GHSL Data Anatomy and upstream GHSL products for the production of the GHS-UCDB 
```
printed_text_in_figure_area_verbatim:
```text
The production of the GHS-UCDB is based on two main processes (Figure 2): the delineation of the 
urban centres (the AOIs), and the characterisation of such spatial units with multi-thematic and multi-
dimensional attributes. 
The delineation of the urban centres is obtained from the GHS-SMOD product (European 
Commission. Joint Research Centre. 2023), that implements the Degree of Urbanisation method – a 
standardised definition of urban and rural areas recommended by the UN Statistical Commission for 
international statistical comparison. From the GHS-SMOD Level 1 the class 3 (urban centres) is 
extracted and retained as AOI. There are two approaches to delineate urban centres. One keeping the 
2025 boundaries fixed (addressed in 2.1.6). Another tracking the evolution of the urban centres over 
time (addressed in 2.1.7). 
The geospatial data integration is carried out with GIS techniques to obtain specific attributes 
belonging to an indicator group and to a thematic area for each of the urban centres. 
```
[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]

### [D6-p12]

```text

```

#### [D6-F2] FIGURE — page 12
caption_verbatim:
```text
Figure 2 Logical workflow for the delineation of urban centres spatial entities by applying to raster grids the population density, size and 
```
printed_text_in_figure_area_verbatim:
```text
2.1 Definitions 
Sub-section 2.1.1 to 2.1.5 refers to the fixed boundary database only. 
2.1.1 Thematic Domain 
grid cell contiguity rules of the Degree of Urbanisation method. 
Refers to one of the 15 broad topics covered by the GHS-UCDB. An example of such thematic domain 
is Exposure. Under exposure the GHS-UCDB groups a variety of families and indicators, further divided 
in specific attributes. 
2.1.2 Indicator groups 
Refers to the 63 upper classifications within each thematic domain. An example of such family is 
Flood. Under the families there are several indicators, each further subdivided into attributes. 
2.1.3 Indicator 
Refers to the classification of an indicator group into 473 subdivisions (indicators) in the GHS-UCDB. 
An example of an indicator is Total Population exposed to 100 years return period floods. Each 
indicator is further divided into attributes. 
2.1.4 Attribute 
Refers to the most specific level of the GHS-UCDB in the form of 2602 specific columns of the 
database (attributes). An example of an attribute is Total Population 1995 exposed to 100 year return 
period Flood. 
2.1.5 value 
Refers to the individual value in the GHS-UCDB as intersection of the individual urban centre record 
for the specific attribute. The UCDB has more than 23.5 million data records. For example, 
7568580.457 is the total 1995 population exposed to a flood (100 year return period) in Dhaka 
(Bangladesh). 
```
[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]

### [D6-p13]

```text
2.1.6 Fixed Boundary 

Refers to the concept of a static definition of the urban centre spatial extent. This extent is delineated 
in 2025 and kept fixed (back and forward) in time. 

2.1.7 Multi-temporal Boundary 

Refers to the concept of tracking the urban centres delineated in 2025 and linking its changing 
boundaries through time (i.e. at each epoch urban centre boundaries are linked to each of the 2025 
urban centres, see section delineation). Therefore, urban centres identified in 2025 maintain their ID 
in the other epochs and are subject to changes in their boundaries. This term introduces also birth 
dates of an urban centre, that is the first year in the database when a cluster of grid cells meet the 
urban centre definition (i.e. population density ≥ 1,500 inhabitants/km2 and total population ≥ 
50,000 inhabitants), and their death whena cluster of pixels falls below the urban centre definition 
thresholds. 
The Multi-temporal Boundary database has 2 thematic domains, 10 indicator groups, 21 indicators, 
169 attributes and 1.7 million data records (values). 

With respect to 2.1.6 and 2.1.7 the user is warned that the numeric values for a 
specific attribute or field in the fixed boundary and multi-temporal boundary dataset 
are different and not comparable. Only the values for 2025 are comparable between 
the two databases. 

2.2 Improvements compared to the previous release 

The GHS-UCDB R2024 improves its 2019A release in various ways: 

1. New GHSL input, based on the R2023A release with a series of key improvements to the 
GHSL baseline data (BUILT, POP and SMOD) also resulting in an extended time series (1975 
– 2030 with 5 years interval and up to annual coverage); 

2. Refines the delineation of the urban centres with a fixed boundary and multi-temporal 
boundaries approach; 

3. Expands the thematic scope and integrates data from Copernicus Services; 

4. Further improves the quality control of urban centres spatial entities with a data-driven 
decision ensemble methodology (further explained in 2.6); 

5. More flexible and tailored products to user needs by diversifying data format (geospatial, 
spreadsheets) and subsetting the dataset by region of the world or thematic domain;  

6. Contributed dataset product to flexibly incorporate and distribute data produced from the 
crowd. 
```

### [D6-p14]

```text
2.3 Delineation of the Urban Centres – fix boundaries 

The GHS Settlement Model layers (GHS-SMOD) GHS-SMOD_GLOBE_R2023A delineates and classify 
settlement typologies (Figure 5) via a logic of cell clusters population size, population and built-up 
area densities as defined by the stage I of the Degree of Urbanisation (European Commission. 
Statistical Office of the European Union. 2021) and recommended by the UN STAT COM. The GHS-
SMOD is derived from the GHS-POP (GHS-POP_GLOBE_R2023A, version 1.0) and GHS-BUILT-S (GHS-
BUILT-S_GLOBE_R2023A, version 1.0) released within this GHSL Data Package 2023 (GHS P2023). 

“Urban Centre” consists of contiguous grid cells (4-connectivity cluster) with a density of at least 
1,500 inhabitants per km2 of permanent land, and has at least 50,000 inhabitants in the cluster 
with smoothed boundaries (3-by-3 conditional majority filtering3) and <15 km2 holes filled4. The 
urban centre is defined in 2025. The delineation of urban centres is done using a split-by-
country version of the GHS-SMOD R2023A (i.e. clusters are delimited by country boundaries, 
based on GADM 4.1). (Figure 3). The ID of a fixed boundary urban centre constitute the territorial 
extent of the urban centre in 2025, and the database explains the evolution of such territory over 
time. 
```

#### [D6-F3] FIGURE — page 14
caption_verbatim:
```text
Figure 3 - Schematic overview of subset schema to define urban centres from the GHSL SMOD entities workflow logic. 
“pop” represents the population abundance per grid cell; “pop_d” represents the population density on permanent land; 
```
printed_text_in_figure_area_verbatim:
```text
3 Water is excluded and majority is computed among populated or land (land >= 50%) pixels. Cases of draw with even number of pixels are 
taken as positive realisation. 
4 In a few countries with relatively low-density urban development and a strong separation of land use functions, the Degree of 
Urbanisation generates multiple urban centres for a single city. Creating urban centres and dense urban clusters using both 
cells with a density of at least 1,500 inhabitants and cells that have an optimal built-up density on permanent land resolves 
this issue. Such highly built-up cells typically contain office parks, shopping malls or factories and the optimal threshold is 
identified according to the average built-up density (GHS-BUILT-S 2020) in clusters with a density of at least 1,500 inhabitants 
with a minimum population of 50,000 people. 
```
[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]

### [D6-p15]

```text
“bu” represents the built-up share per grid cell; “bu_d” represents the built-up density on permanent land. “DENSITY ON 
LAND” process fill built-up cells on water with max between 50% and built-up share value and population on water with 
global average built-up per capita. (*) this procedure of enforcement logic allows the delineation of Urban Clusters Entities 

which contains by definition the Urban Centres and all 2X classes. Each entity has a corresponding vector boundary. 

2.4 Delineation of the Urban Centres – multi-temporal boundaries 

The Multi-temporal dynamic of the Urban Centres (GHS_UCDB_MTUC_GLOBE_R2024A) addresses 
these behaviours by setting a reference epoch to define the list entity IDs to follow, adding future (i.e. 
those yet to be born in reference year) or past entities (i.e. those died before reference year), and 
linking boundaries across epochs. The linking methodology relies on the idea that a pair of entities of 
two epochs in a time interval of 5 to 10 years has a spatial overlap and represent the same urban 
centres across time. Not all overlaps can be considered significative (e.g. is a single pixel overlap 
enough to link boundaries?), therefore we defined a set of alternative (i.e. ‘or’) criteria based on the 
population size in the overlap (≥50,000, i.e. the overlap matches itself the UC thresholds) and its 
share of total urban centre population in the two epochs (≥50%). These three rules allow to keep 
track of ‘shrinking’ cities (i), ‘expanding’ cities (ii) and ‘moving’ (i.e. shrinking on one side and expanding 
in another) cities (iii); dropping minor overlaps at fringes of neighbouring urban centres with few 
inhabitants. Between two epochs, entities can have ‘many–to-one’, ‘one-to-many’ or ‘many-to-many’ 
relationships due to significative overlaps. The assumption of a defined list of urban centres implies 
that all these relationships have to be simplified into ‘one-to-one’. The ‘many-to-one’ relationships 
(i.e. many entities in past or future years having overlapping boundaries with one entity in the 
reference year) are considered as spatial dynamics of a single urban centre: one urban centre in the 
reference epoch that originated from a merge of many entities in the past, or that will split in the 
future. In both cases the ID of the urban centre in the reference epoch is assigned to all entities of 
the ‘many-to-one’ relationship. The ‘one-to-many’ and ‘many-to-many’ relationships (i.e. many 
entities in past or future years having overlapping boundaries with many entities in the reference 
year) are solved by splitting single entities into parts each one assigned to an urban centre of the 
reference epoch. The split is performed by assigning each pixel of an entity to the most attracting 
urban centre. The attracting intensity (inspired by the electric field strength due to a dipole) of the 
urban centre U on the pixel i is computed as follow: 

𝐼𝑖,𝑈= ∑
𝑃𝑂𝑃𝑗
𝑑𝑖𝑠𝑡(𝑖, 𝑗)3
𝑗∈𝑈

where POPj represents the population in the pixel j (belonging to the urban centre U), and dist(i,j) the 
distance between pixels i, and j. Distances are computed as shortest path on a graph built with 
pixels centres as nodes having arcs with all the 8 adjacent pixels. Each arc has a cost equal to the 
planar distance between nodes. To enforce spatial contiguity distances are bounded within the 
dissolved boundary of all entities involved in the split (i.e. costs of arcs crossing the boundaries are 
set to infinite). 

The MTUC layer released within the GHS-SMOD R2023 dataset is obtained by setting as reference 
year the 2020 and stepwise moving backward to 1975 and forward to 2030 (i.e. first step: 
reference year 2020, comparison year 2015, the 2020 ID are linked and transferred to 2015 
entities; second step: reference year 2015 with IDs at previous step, comparison year 2010; and so 
on). The list of urban centres across time is fixed and determined by the GHS-SMOD urban centres 
of 2020, plus those that died before 2020 or will be born after 2020. Each of these has a unique 
identifier, was born in a given year (i.e. first appearance), or already there in the first GHSL epoch 
(1975); and it changes boundaries until its death (i.e. last appearance), or is still present in 2030 
(Figure 4). 
```

### [D6-p16]

```text

```

#### [D6-F4] FIGURE — page 16
caption_verbatim:
```text
Figure 4 Schema of the MTUC model: starting from the reference year (ref year) 2025 the model analyse the overlaps between urban 
centre (ref year) and those of the previous epoch (-5 years; the processing is repeated for future starting from 2025 and comparing +5 
years). Significative overlaps (i.e. overlaps hosting [A] population >= 50,000 or [B] >= 50% of ref year urban centre population or [C] >= 
```
printed_text_in_figure_area_verbatim:
```text
50% of +-5-years urban centre population) are kept. Four possible cases of relationships (+-5-years to ref year) are identified: (1) 'No 
overlaps', BIRTH (when comparing -5-years layer) or DEATH (when comparing +5-years layer); (2) 'one to one' relationships, LINK (the ID 
of ref year is inherited in the +- 5-years layer), (3) 'many to 1', MERGE (all the 'many' boundaries in the +-5-years layer inherit the ref 
year ID); (4)0 'one or many to many', SPLIT (areas of the +-5-years layer are split according to a maximum potential function computed in 
each pixel of the areas to be split from all the 'many' urban centres of the ref year; each split area inherit the ID of the ref year urban 
centre with the highest potential). The set of the new defined IDs it is used as input as ref year for the subsequent epoch analysis (e.g. 
completing ref year 2025 and -5-year 2020, at next iteration the newly defined 2020 IDs are used as ref year to link the 2015). 
```
[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]

### [D6-p17]

```text

```

#### [D6-F5] FIGURE — page 17
caption_verbatim:
```text
Figure 5 Comparison of the 'fixed boundary' and the 'multi-temporal boundary' approaches. The 'fixed boundary' (A, C) 
```
printed_text_in_figure_area_verbatim:
```text
computes statistics of the GHS-UCDB across all epochs (1975-2030) based on the fixed 2025 boundaries; the 'multi-
temporal boundary' approach assign a different boundary to each epoch allowing to follow the urban centre growth (B) 
and the urban centre shrinkage (D), and computing statistics of each epoch within the relevant boundary. 
2.5 Geospatial data integration 
The GHS-UCDB is produced in GIS (Geographic Information System) environment by geospatial data 
integration of large volume of geospatial data. Geospatial data across the 15 thematic domains are 
linked to urban centres entities mainly via GIS operations. Most of the attributes are generated with 
zonal statistics (i.e. sum or average of source data within each urban centre spatial extent). 
For example, population data for a specific year (as input value raster) are summed within the urban 
centre extent 2025 (as zone field) for the fixed boundary dataset, or in the spatial extent of that 
urban centre ID in the specific year. 
```
[AMBIGUOUS: printed labels transcribed as text lines; label-to-value pairing not machine-resolved]

### [D6-p18]

```text
Other indicators and attributes are computed with spatial join operations. For example, most of the 
location variables such as country, geographic region, are obtained using the urban centres as target 
features, and the spatial delineation of the attribute as join features. 

The documentation of specific indicators is contained in the fact sheets section (2.9 and 2.10).  

2.6 Quality control of the urban centres 

The purpose of the quality control is to assess the plausibility of the ‘Urban Centres’ (UC) entities 
included in the GHS-UCDB database. These entities were identified in the GHSL data by applying a 
set of rules defined by the DEGURBA methodology (Dijkstra et al. 2021; European Commission. 
Statistical Office of the European Union. 2021). Within this method, a UC is defined in a uniform grid 
sampling space of 1 km² as a connected component with a population density greater than 1500 
inhabitants/km² and a total population exceeding 50,000 inhabitants. These criteria are referred to 
as the ‘canonical principles’ of the UC abstract definition. 

A plausibility test model was developed using a data-driven decision ensemble methodology. This 
ensemble is supported by univariate linear regression, stratified by World Bank Income Group 
(WBincomeGroup) and by year. The predictors are the total sum per UC of modelled population grids 
and land use grids, which are independently produced with respect to the Global Human Settlement 
Population (GHS_POP) and the Global Human Settlement Model (GHS_SMOD), forming the basis for 
the UCDB. 

The objective of the model is to determine the plausibility that the positive occurrences of the UCs 
reflect true data cases and are not artefacts in the input data. These artefacts may be generated by 
residual erroneous values in the input census data or erroneous spatial encoding of the input census 
tracts, leading to misplacement of population information. 

The plausibility of each UC occurrence in any given year, supported by the GHSL data, is measured by 
a voting schema. This ensures that the majority of independent sources corroborate the finding that 
these UCs align with the ‘canonical principles’ internationally agreed upon to define the UC 
abstraction. 

A list of nine predictors was selected, including three population raster grids and six land use raster 
grids. To approximate the residential surface, the non-GHSL land use predictors that do not 
discriminate between residential (RES) and non-residential (NRES) built-up surfaces were factorized 
by the residential surface (RS) share of the single UC, as predicted by the GHSL (time-variant). 

1. POP: GHS_POP resident population (time-variant) 

2. POP: LANDSCAN ambient population (2020) 

3. POP: WorldPop constraint UN aligned (2020) 

4. LANDUSE: ESRI urban surface (2019-2020) * RS 

5. LANDUSE: Copernicus Global Land Cover (CGLC) urban surface (2018-2020) * RS 

6. LANDUSE: GHS_BURES = GHS_BUILT - GHS_BUILT_NRES (time-variant) 

7. LANDUSE: ESA World Cover urban surface (2020-2021) * RS 

8. LANDUSE: WSF2019 settlement footprint surface (2018-2019) * RS 

9. LANDUSE: WSF2015v2 settlement footprint surface (2014-2015) * RS 
```

### [D6-p19]

```text
Each predictor was tested using the Pearson Correlation coefficient for each stratum defined by 
WBincomeGroup and year (1975-2025). A balanced set of the best six predictors (three POP, three 
LANDUSE), including the GHS_POP, was selected for each stratum. 

Consequently, the voting schema may provide from one to six votes. One vote indicates a strong 
failure, while two votes indicate a mild failure. The implications of three to six votes provide a measure 
of confidence that we can reject the hypothesis that the UC is an artefact of GHS_POP data or an 
artefact of the SMOD implementation, which relaxes the UC canonical rules internationally agreed 
upon (relaxed density criteria, gap filling, smoothing of the UC perimeter). 

The model development experimented with various options. The most accurate model, based on the 
composite of expert opinions in a random sample of 778 UCs, was selected. The chosen model 
architecture applies a positive boosting factor proportional to one epsilon error, reducing the 
probability of false alarms in detecting strong failures. Moreover, the selected model architecture 
exclusively applies the canonical rules of “POP size AND density over LAND” for assessing the UC. In 
the sampled universe, the model prediction is three times more conservative than the composite of 
expert opinions in determining a strong failure rate. The vote scores collected by the UC in the various 
years were finally composed using two alternative strategies: ‘VOTE_AVERAGE’ and ‘VOTE_MAX’. The 
latter, consistent with the necessity to provide the most conservative fail rate, was selected. 

Final decisions based on the voting schema were implemented in the GHS-UCDB data as follows and 
results in 11,422 entities: 

1. GHS-SMOD class 30 entities with VOTE_MAX = 1 were excluded from the database. 264 class 
30 entities did not enter the GHS-UCDB as they did not pass the plausibility test 

2. GHS-SMOD class 30 entities with VOTE_MAX = 2 were encoded as ‘low plausibility’. 266 urban 
centres 

3. GHS-SMOD class 30 entities with VOTE_MAX = 3 were encoded as ‘medium plausibility’. 304 
urban centres 

4. GHS-SMOD class 30 entities with VOTE_MAX ≥ 4 were encoded as ‘high plausibility’. 10852 
urban centres 

2.7 User guide 

This section explains with screenshots and step by step guidelines how to open the GHS-UCDB 
geopackage in different GIS environments. 

2.7.1 ArcGIS Pro 

Full detail about how to import GeoPackage files can be found here: 

https://pro.arcgis.com/en/pro-app/latest/help/data/databases/work-with-sqlite-databases-in-arcgis-
pro.htm 

1. Connect to a folder that contains the GHS-UCDB GeoPackage (e.g. “Download/GHS_UCDB”) 
```

### [D6-p20]

```text
2. In the Catalog panel, browse to the folder to which you connected in the previous step. Browse to 
the SQLite database or GeoPackage to start using its items. 

3. To use the exposure data drag it to the Contents pane 
```

### [D6-p21]

```text
4. Right click on the layer and select “Attribute Table”: the fields view will open and show the table 
columns and values 
```

### [D6-p22]

```text
2.7.2 QGIS 

1. Drag and drop the GHS-UCDB GeoPackage file from Windows File Explorer in the Layers panel in 
QGIS 

2. Double click the layer of interest, e.g. the exposure one 
```

### [D6-p23]

```text
3. Right click on the layer and select “Open Attribute Table” to see all fields values 
```

### [D6-p24]

```text
2.8 Fact sheets Specimen 

The documentation of the GHS-UCDB entries is based on fact sheets that follow a harmonised 
template. 

Each attribute in the database has a unique identifier based on a 2 + 3 + 3 + 4 characters in the 
format below: 

<thematic area>_<indicator group>_<attribute identifier>_<year> 

For example, EX_L10_BUS_2000 corresponds to: built-up surface in Low Elevated Coastal Zones 10m 
in 2000 and this attribute belongs to the Exposure thematic area. 
```

### [D6-p25]

```text
Refers to the source of the processed data 

Indicator description  

Refers to a short description of the indicator to clarify the meaning, can be the same of the 
indicator name if self-explanatory 

Methodology 

Refers to an explanation of the processing workflow and the calculations performed to obtain the 
attribute  

Methodology Short 

Refers the geospatial processing or calculations performed 

Temporal Coverage 

Refers to the years or epochs for the indicator covers 

Uncertainties & Best practices  

Refers –when available- to disclaimers, limitations, user awareness or best practices for the best 
use of the indicator 
```

#### [D6-T2] TABLE — page 25
title_verbatim:
```text
Table 2 GHS-UCDB Indicator fact sheet specimen with explanation of the fields 
```
table_flags: [AMBIGUOUS: header extent — no numeric rows; first printed line taken as header]; 8 wrapped printed lines joined into their row's cells (line pitch tighter than the table's row pitch; text verbatim, joined with a space); [AMBIGUOUS: no column structure detected — content kept as single-column rows]

| Indicator thematic area |
|---|
| The field refers to which of the 15 thematic domains the indicator belongs to Indicator group The field refers to the group of single attributes that the indicator contains Attribute ID Refers to the unique Identifier of the specific attribute Indicator Name Refers to the descriptive name of the indicator Units Refers to the unit of measure of the attribute |

[D6-T2-fn1]
```text
Data Source 
```

### [D6-p26]

```text
2.9 GHS-UCDB indicator fact sheets – fixed boundary 

This section contains the individual indicator fact sheets organised by the 15 thematic domains. 

2.9.1 General Characteristics 

Indicator thematic area 

General Characteristics 

Indicator group 

Urban center Name 

Attribute ID 

GC_UCN_MAI_XXXX 

Indicator Name 

Urban center Main Name 

Units 

Dimensionless 

Data Source 

Open Street Maps  

GISCO 

WUP 2018 

Indicator description  

Name of the main city inside the urban center.  

Methodology 

The urban centres are named using an algorithm that automatically queries the GISCO, the full 
OpenStreetMap datasets and WUP 2018 (extended unpublished version, with point locations 
corrected through geocoding and reverse geocoding). 

Methodology Short 

Geoencoding 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p27]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban center Name 

Attribute ID 

GC_UCN_LIS_XXXX 

Indicator Name 

Urban center List Name 

Units 

Dimensionless 

Data Source 

Open Street Maps  

GISCO 

WUP 2018 

Indicator description  

List of names of the all cities inside the urban center.  

Methodology 

The urban centres are named using an algorithm that automatically queries the GISCO, the full 
OpenStreetMap datasets and WUP 2018 (extended unpublished version, with point locations 
corrected through geocoding and reverse geocoding). 

Methodology Short 

Geoencoding 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p28]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Country Name 

Attribute ID 

GC_CNT_GAD_XXXX 

Indicator Name 

Country Name 

Units 

Dimensionless 

Data Source 

GADM version 4.1, released on 16 July 2022 https://gadm.org/data.html  

Indicator description  

Country named based on GADM dataset 

Methodology 

Spatial join of the urban centers and the GADM country layer adapted for GHSL.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p29]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Country Name 

Attribute ID 

GC_CNT_UNN_XXXX 

Indicator Name 

Country Name 

Units 

Dimensionless 

Data Source 

World Population Prospects 2022 (WPP2022) 

Indicator description  

Country named based on WPP2022. 

Methodology 

Merging GADM countries according to WPP2022 notes. 

Methodology Short 

Spatial join  

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p30]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Area 

Attribute ID 

GC_UCA_KM2_XXXX 

Indicator Name 

Urban Centre Area 

Units 

Km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Urban Centre Area 

Methodology 

Calculate area (geometry) of the urban centre. 

Methodology Short 

Area 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p31]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Population 

Attribute ID 

GC_POP_TOT_XXXX 

Indicator Name 

Total Population in the Urban Centre 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total population allocated inside of the UC in number of inhabitants. 

Methodology 

Zonal sum of the GHS-POP R2023A layer pixel values inside the urban centre. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p32]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Development 

Attribute ID 

GC_DEV_WIG_XXXX 

Indicator Name 

World Bank Income Group 

Units 

Categorical 

Data Source 

The World Bank https://datahelpdesk.worldbank.org/knowledgebase/articles/906519  

Indicator description  

The World Bank income group classification provides a complete list of economies classified by 
income, region, and World Bank lending status. This table is updated to year 2022. 

Methodology 

Join by attribute (by country). 

Methodology Short 

Join by attribute 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p33]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Development 

Attribute ID 

GC_DEV_USR_XXXX 

Indicator Name 

UN SDG Region 

Units 

Categorical 

Data Source 

 UN https://unstats.un.org/sdgs/indicators/regional-groups/ 

Indicator description  

Country grouping in geographic regions based on the 2016 Sustainable Development Goals 
Report and the progress reports on the Millennium Development Goals. 

Methodology 

Join by attribute (by country) 

Methodology Short 

Join by attribute 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p34]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Plausibility 

Attribute ID 

GC_PLS_SCR_XXXX 

Indicator Name 

Plausibility 

Units 

Categorical 

Data Source 

Melchiorri Michele; Marí Rivero Inés, Florio Pietro, Uhl Johannes, Krasnodębska Katarzyna, 
Pesaresi Martino, Politis Pangliotis, Schiavina Marcello, Maffenini Luca, Tommasi Pierpaolo, Carioli 
Alessandra, Ehrlich Daniele, Crippa Monica, Guizzardi Diego, Pisoni Enrico, Bellis Claudio, Sulis 
Patrizia, Oom Duarte, Branco Alfredo, Kemper Thomas. Stats in the City –the GHSL Urban Centre 
Database 2025.Publications Office of the European Union, Luxembourg, 2024. ISBN 978-92-68-
21609-5, doi: 10.2760/3046391, JRC139768 

Indicator description  

The score indicates the plausibility/quality of the modelled urban centre. 

Methodology 

A plausibility test model was developed using a data-driven decision ensemble methodology. This 
ensemble is supported by univariate linear regression, stratified by World Bank Income Group 
(WB Income Group) and by year. The predictors are the total sum per UC of modelled population 
grids and land use grids, which are independently produced with respect to the Global Human 
Settlement Population (GHS-POP R2023A) and the Global Human Settlement Model (GHS-SMOD 
R2023A) 

Methodology Short 

Data-driven decision 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p35]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban centre birth 

Attribute ID 

GC_UCB_YOB _XXXX 

Indicator Name 

Year of Birth 

Units 

year 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

European Commission, and Statistical Office of the European Union, 2021 
Applying the Degree of Urbanisation — A methodological manual to define cities, towns and rural 
areas for international comparisons — 2021 edition. Publications Office of the European Union, 
2021; ISBN 978-92-76-20306-3 
10.2785/706535 

Indicator description  

Indicates the year in the multitemporal series GHS-SMOD R2023A, the cells reach the conditions 
to be classified as urban centre. 

Methodology 

The methodology to classify the urban centres is described in “Applying the Degree of 
Urbanisation — A methodological manual to define cities, towns and rural areas for international 
comparisons —“. 

Methodology Short 

Modelled 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p36]

```text
The DEGURBA model considers data only from 1975 to 2030, cities born in 1975 should be 
considered as born in 1975 or earlier, and cities death in 2030 should be considered as death on 
2030 or later 
```

### [D6-p37]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban centre death 

Attribute ID 

GC_UCB_YOD _XXXX 

Indicator Name 

Year of Death 

Units 

year 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

European Commission, and Statistical Office of the European Union, 2021 
Applying the Degree of Urbanisation — A methodological manual to define cities, towns and rural 
areas for international comparisons — 2021 edition. Publications Office of the European Union, 
2021; ISBN 978-92-76-20306-3 
10.2785/706535 

Indicator description  

Indicates weather an urban centre is projected to be a urban centre in 2030 or ‘dies’ (doesn’t 
reach the conditions to be a urban centre) in 2030. 

Methodology 

The methodology to classify the urban centres is described in “Applying the Degree of 
Urbanisation — A methodological manual to define cities, towns and rural areas for international 
comparisons —". 

Methodology Short 

Modelled 

Temporal Coverage 

2025, 2030 

Uncertainties & Best practices  
```

### [D6-p38]

```text
The DEGURBA model considers data only from 1975 to 2030, cities born in 1975 should be 
considered as born in 1975 or earlier, and cities death in 2030 should be considered as death on 
2030 or later 
```

### [D6-p39]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban centre municipality 

Attribute ID 

GC_UCM_CAP_XXXX 

Indicator Name 

Capital city 

Units 

Boolean (yes/no) 

Data Source 

Wikipedia 

GoogleMaps 

Indicator description  

Indicates weather an urban centre is the capital city. 

Methodology 

Nation capitals are flagged by retrieving the information about name on Wikipedia.org and 
location with Geocoding on GoogleMaps. When information retrieved provide multiple capitals: (1) 
'de jure' is preferred over 'de facto'; 'legislative' is preferred over others (e.g. 'royal', 
'administrative', 'executive', etc.). Value 0 indicates no capital city and value 1 indicates Capital 
City)  

Methodology Short 

Geocoding 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p40]

```text
2.9.2 GHSL 

Indicator thematic area 

GHSL 

Indicator group 

Population 

Attribute ID 

GH_POP_TOT_XXXX 

Indicator Name 

Total Population 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total population allocated inside of the UC in number of inhabitants. 

Methodology 

Zonal sum of the GHS-POP R2023A layer pixel values inside the urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p41]

```text
Indicator thematic area 

GHSL 

Indicator group 

Population 

Attribute ID 

GH_POP_CAG_XXXX 

Indicator Name 

Population Compound Annual Growth Rate 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Compound annual growth rate of the total population allocated inside of the UC in percentage. 

Methodology 

𝐶𝐴𝐺𝑅= ((𝑣𝑎𝑙𝑢𝑒𝑡1

𝑣𝑎𝑙𝑢𝑒𝑡0

Methodology Short 

Compound annual growth rate 

Temporal Coverage 

1 𝑡1−𝑡0
⁄

−1) × 100 

)

1975-1980, 1980-1985, 1985-1990, 1990-1995, 1995-2000, 2000-2005, 2005-2010, 2010-
2015, 2015-2020, 2020-2025 

Uncertainties & Best practices  
```

### [D6-p42]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up surface 

Attribute ID 

GH_BUS_TOT_XXXX 

Indicator Name 

Total Built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Total built-up area of the UC in square meters  

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall perimeter. 
```

### [D6-p43]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up surface 

Attribute ID 

GH_BUS_NRE_XXXX 

Indicator Name 

Non-Residential Built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Non-residential built-up area of the UC in square meters  

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall 
perimeter. 
```

### [D6-p44]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up surface 

Attribute ID 

GH_BUS_RES_XXXX 

Indicator Name 

Residential Built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Residential built-up area of the UC in square meters  

Methodology 

Subtraction of the non-residential built-up in a urban centre from the total built-up.  

Methodology Short 

Subtraction 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall 
perimeter. 
```

### [D6-p45]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up per capita 

Attribute ID 

GH_BPC_TOT_XXXX 

Indicator Name 

Total built-up per capita 

Units 

m2/person 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total built-up area per capita in the urban centre  

Methodology 

Total built-up area divided by total population 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Values bellow 1 m2/person and above 600 m2/person are excluded from the data set.  
```

### [D6-p46]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up per capita 

Attribute ID 

GH_BPC_NRE_XXXX 

Indicator Name 

Non-residential built-up per capita 

Units 

m2/person 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
```

### [D6-p47]

```text
Indicator description  

Non-residential built-up area per capita in the urban centre  

Methodology 

Non-residential built-up area divided by total population 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Values above 600 m2/person are excluded from the data set.  
```

### [D6-p48]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up per capita 

Attribute ID 

GH_BPC_RES_XXXX 

Indicator Name 

Residential built-up per capita 

Units 

m2/person 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Residential built-up area per capita in the urban centre  

Methodology 

Residential built-up area divided by total population 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Values bellow 1 m2/person and above 600 m2/person are excluded from the data set. 
```

### [D6-p49]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up volume 

Attribute ID 

GH_BUV_TOT_XXXX 

Indicator Name 

Total built-up volume 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Indicator description  

Total built-up volume in the urban centre  

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre.  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall 
perimeter. 
```

### [D6-p50]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up volume 

Attribute ID 

GH_BUV_NRE_XXXX 

Indicator Name 

Non-residential built-up volume 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Indicator description  

Non-residential built-up volume in the urban centre  

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V-NRES R2023A pixel values inside the urban centre.  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall 
perimeter. 
```

### [D6-p51]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up volume 

Attribute ID 

GH_BUV_RES_XXXX 

Indicator Name 

Residential built-up volume 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Indicator description  

Residential built-up volume in the urban centre  

Methodology 

Subtraction of the non-residential volume from the total volume for each urban centre.  

Methodology Short 

Subtraction 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

The Built-up indicators express quantities In line with the semantic of GHS-BUILT that 
defines ‘building’ as any roofed structure erected above ground for any human use, including 
structures in slums, informal settlements, and refugees/IDP camps and ‘built-up surface’ as the 
gross building surface (including the thickness of the walls) bounded by the building wall 
perimeter. 
```

### [D6-p52]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up height 

Attribute ID 

GH_BUH_AVG_XXXX 

Indicator Name 

Average built-up height 

Units 

m 

Data Source 

Pesaresi, M.; Politis, P. (2023): 
GHS-BUILT-H R2023A - GHS building height, derived from AW3D30, SRTM30, and Sentinel2 
composite (2018).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/85005901-3a49-48dd-9d19-6261354f56fe, 
doi:10.2905/85005901-3A49-48DD-9D19-6261354F56FE 

Indicator description  

Average of the values inside the urban centre of the average height of the built surfaces in a 100 
m pixel. 

Methodology 

Zonal statistics (average) of the GHS-BUILT-H R2023A pixel values inside the urban centre. 

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p53]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up height 

Attribute ID 

GH_BUH_STD_XXXX 

Indicator Name 

Average built-up height 

Units 

m 

Data Source 

Pesaresi, M.; Politis, P. (2023): 
GHS-BUILT-H R2023A - GHS building height, derived from AW3D30, SRTM30, and Sentinel2 
composite (2018).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/85005901-3a49-48dd-9d19-6261354f56fe, 
doi:10.2905/85005901-3A49-48DD-9D19-6261354F56FE 

Indicator description  

Standard deviation of the values inside the urban centre of the average height of the built 
surfaces in a 100 m pixel. 

Methodology 

Zonal statistics (standard deviation) of the GHS-BUILT-H R2023A pixel values inside the urban 
centre. 

Methodology Short 

Zonal statistics (standard deviation) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p54]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up height 

Attribute ID 

GH_BUH_MAX_XXXX 

Indicator Name 

Average built-up height 

Units 

m 

Data Source 

Pesaresi, M.; Politis, P. (2023): 
GHS-BUILT-H R2023A - GHS building height, derived from AW3D30, SRTM30, and Sentinel2 
composite (2018).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/85005901-3a49-48dd-9d19-6261354f56fe, 
doi:10.2905/85005901-3A49-48DD-9D19-6261354F56FE 

Indicator description  

Maximum of the values inside the urban centre of the average height of the built surfaces in a 
100 m pixel. 

Methodology 

Zonal statistics (maximum) of the GHS-BUILT-H R2023A pixel values inside the urban centre. 

Methodology Short 

Zonal statistics (maximum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p55]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P11_XXXX 

Indicator Name 

Population living in residential prevalent 1-2 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as residential prevalent 1-2 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 11 (residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p56]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P12_XXXX 

Indicator Name 

Population living in residential prevalent 3-7 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as residential prevalent 3-7 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 12 (residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p57]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P13_XXXX 

Indicator Name 

Population living in residential prevalent >8 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as residential prevalent >8 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 13 (residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p58]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P21_XXXX 

Indicator Name 

Population living in non-residential prevalent 1-2 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as non-residential prevalent 1-2 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 21 (non-residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p59]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P22_XXXX 

Indicator Name 

Population living in non-residential prevalent 3-7 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as non-residential prevalent 3-7 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 22 (non-residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p60]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_P23_XXXX 

Indicator Name 

Population living in non-residential prevalent >8 floors built-up 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Total population inside the built-up in the urban centre classified as non-residential prevalent >8 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
built-up type class 23 (non-residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p61]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S11_XXXX 

Indicator Name 

Built-up surface in residential prevalent 1-2 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as residential prevalent 1-2 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 11 (residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p62]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S12_XXXX 

Indicator Name 

Built-up surface in residential prevalent 3-7 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID:http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as residential prevalent 3-7 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 12 (residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p63]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S13_XXXX 

Indicator Name 

Built-up surface in residential prevalent >8 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID:http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as residential prevalent >8 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 13 (residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p64]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S21_XXXX 

Indicator Name 

Built-up surface in non-residential prevalent 1-2 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID:http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as non-residential prevalent 1-2 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 21 (non-residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p65]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S22_XXXX 

Indicator Name 

Built-up surface in non-residential prevalent 3-7 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID:http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as non-residential prevalent 3-7 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 22 (non-residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p66]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_S23_XXXX 

Indicator Name 

Built-up surface in non-residential prevalent >8 floors built-up 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID:http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up surface of the built-up in the urban centre classified as non-residential prevalent >8 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as built-up type class 23 (non-residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p67]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V11_XXXX 

Indicator Name 

Built-up volume in residential prevalent 1-2 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as residential prevalent 1-2 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 11 (residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p68]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V12_XXXX 

Indicator Name 

Built-up volume in residential prevalent 3-7 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as residential prevalent 3-7 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 12 (residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p69]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V13_XXXX 

Indicator Name 

Built-up volume in residential prevalent >8 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as residential prevalent >8 floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 13 (residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p70]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V21_XXXX 

Indicator Name 

Built-up volume in non-residential prevalent 1-2 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as non-residential prevalent 1-2 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 21 (non-residential prevalent 1-2 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p71]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V22_XXXX 

Indicator Name 

Built-up volume in non-residential prevalent 3-7 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as non-residential prevalent 3-7 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 22 (non-residential prevalent 3-7 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p72]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up type 

Attribute ID 

GH_BUT_V23_XXXX 

Indicator Name 

Built-up volume in non-residential prevalent >8 floors built-up 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., … Kemper, T. (2024). 
Advances on the Global Human Settlement Layer by joint assessment of Earth Observation and 
population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Indicator description  

Built-up volume of the built-up in the urban centre classified as non-residential prevalent >8 
floors. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as built-up type class 23 (non-residential prevalent >8 floors). 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p73]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S75_XXXX 

Indicator Name 

Share of BU surface in temporal dominant before 1975 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up before 1975 over total 
built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built before 1975 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p74]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S85_XXXX 

Indicator Name 

Share of BU surface in temporal dominant between 1975 and 1985 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up between 1975 and 1985 
over total built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built between 1975 and 1985 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p75]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S95_XXXX 

Indicator Name 

Share of BU surface in temporal dominant between 1985 and 1995 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up between 1985 and 1995 
over total built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built between 1985 and 1995 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p76]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S05_XXXX 

Indicator Name 

Share of BU surface in temporal dominant between 1995 and 2005 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up between 1995 and 2005 
over total built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built between 1995 and 2005 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p77]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S15_XXXX 

Indicator Name 

Share of BU surface in temporal dominant between 2005 and 2015 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up between 2005 and 2015 
over total built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built between 2005 and 2015 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p78]

```text
Indicator thematic area 

GHSL 

Indicator group 

Built-up Age (Temporal Domain) 

Attribute ID 

GH_AGE_S25_XXXX 

Indicator Name 

Share of BU surface in temporal dominant between 2015 and 2025 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

UHL, J.H., POLITIS, P. and PESARESI, M., GHS-AGE: Global gridded estimates of the dominant age 
of the built stock (1975-2020), Publications Office of the European Union, Luxembourg, 2025, 
https://data.europa.eu/doi/10.2760/6443992, JRC141711. 

Uhl, J.H., Pesaresi, M., Politis, P., Krasnodębska, K., Florio, P., Kemper, T. (2024). GHS-AGE: 
Characterizing settlement age at planetary scale using the Global Human Settlement Layer 
(forthcoming). 

Indicator description  

Share of the built-up surface in the urban centre classified as built-up between 2015 and 2025 
over total built-up in the urban centre. 

Methodology 

Ratio of the sum of the GHS-BUILT-S R2023A pixel values inside the urban centre classified as 
built between 2015 and 2025 and the total built-up in the urban centre. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p79]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface 

Attribute ID 

GH_XST_S11_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 11 (very low density) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030) European Commission, Joint 
Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as very low density (DoU class 11) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 11 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p80]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S12_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 12 (low density rural) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030) European Commission, Joint 
Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as low density rural (DoU class 12) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 12 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p81]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S13_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 13 (rural cluster) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as rural cluster (DoU class 13) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 13 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p82]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S21_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 21 (suburban) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as suburban (DoU class 21) within the urban centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 21 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p83]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S22_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 22 (semi dense urban 
cluster) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030) European Commission, Joint 
Research Centre (JRC) PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as semi dense urban cluster (DoU class 22) within the urban 
centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 22 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p84]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S23_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 23 (dense urban cluster) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030) European Commission, Joint 
Research Centre (JRC) PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as dense urban cluster (DoU class 23) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 23 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p85]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up surface  

Attribute ID 

GH_XST_S30_XXXX 

Indicator Name 

Built-up surface within the Degree of Urbanisation Classification class 30 (urban centre) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030) European Commission, Joint 
Research Centre (JRC) PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up surface in cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-S R2023A pixel values inside the urban centre classified 
as class 30 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p86]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume 

Attribute ID 

GH_XST_V11_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 11 (very low density) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as very low density (DoU class 11) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 11 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p87]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume  

Attribute ID 

GH_XST_V12_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 12 (low density rural) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-V R2023A - GHS built-up volume grids derived from 
joint assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-
2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as low density rural (DoU class 12) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 12 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p88]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume 

Attribute ID 

GH_XST_V13_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 13 (rural cluster) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-V R2023A - GHS built-up volume grids derived from 
joint assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-
2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as rural cluster (DoU class 13) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 13 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p89]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume  

Attribute ID 

GH_XST_V21_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 21 (suburban) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-V R2023A - GHS built-up volume grids derived from 
joint assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-
2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as suburban (DoU class 21) within the urban centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 21 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p90]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume 

Attribute ID 

GH_XST_V22_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 22 (semi dense urban 
cluster) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): GHS-BUILT-V R2023A - GHS built-up volume grids derived from 
joint assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-
2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as semi dense urban cluster (DoU class 22) within the urban 
centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 22 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p91]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume  

Attribute ID 

GH_XST_V23_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 23 (dense urban cluster) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023):GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint 
assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-2030).European 
Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as dense urban cluster (DoU class 23) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 23 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p92]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Built-up volume  

Attribute ID 

GH_XST_V30_XXXX 

Indicator Name 

Built-up volume within the Degree of Urbanisation Classification class 30 (urban centre) 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283  

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Built-up volume in cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-BUILT-V R2023A pixel values inside the urban centre classified 
as class 30 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p93]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area 

Attribute ID 

GH_XST_A11_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 11 (very low density) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as very low density (DoU class 11) within the urban centre boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 11 in the 
corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p94]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area  

Attribute ID 

GH_XST_A12_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 12 (low density rural) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as low density rural (DoU class 12) within the urban centre boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 12 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p95]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area 

Attribute ID 

GH_XST_A13_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 13 (rural cluster) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as rural cluster (DoU class 13) within the urban centre boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 13 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p96]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area  

Attribute ID 

GH_XST_A21_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 21 (suburban) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as suburban (DoU class 21) within the urban centre boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 21 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p97]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area 

Attribute ID 

GH_XST_A22_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 22 (semi dense urban cluster) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as semi dense urban cluster (DoU class 22) within the urban centre 
boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 22 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p98]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area  

Attribute ID 

GH_XST_A23_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 23 (dense urban cluster) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as dense urban cluster (DoU class 23) within the urban centre 
boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 23 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p99]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Area  

Attribute ID 

GH_XST_A30_XXXX 

Indicator Name 

Area within the Degree of Urbanisation Classification class 30 (urban centre) 

Units 

km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Area of the cells classified as urban centre (DoU class 30) within the urban centre boundary. 

Methodology 

Zonal statistics (count) of the pixels inside the urban centre classified as class 30 in the 
corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p100]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population 

Attribute ID 

GH_XST_P11_XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 11 (very low density) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as very low density (DoU class 11) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 11 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p101]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population  

Attribute ID 

GH_XST_P12_XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 12 (low density rural) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as low density rural (DoU class 12) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 12 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p102]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population 

Attribute ID 

GH_XST_P13_XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 13 (rural cluster) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as rural cluster (DoU class 13) within the urban centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 13 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p103]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population  

Attribute ID 

GH_XST_P21_XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 21 (suburban) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as suburban (DoU class 21) within the urban centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 21 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p104]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population 

Attribute ID 

GH_XST_ P22 _XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 22 (semi dense urban cluster) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid 
multitemporal (1975-2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as semi dense urban cluster (DoU class 22) within the urban 
centre boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 22 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p105]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population  

Attribute ID 

GH_XST_ P23 _XXXX 

Indicator Name 

Population within the Degree of Urbanisation Classification class 23 (dense urban cluster) 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as dense urban cluster (DoU class 23) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 23 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p106]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population  

Attribute ID 

GH_XST_ P30 _XXXX 

Indicator Name 

Population 

Units 

inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population in the cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Zonal statistics (sum) of the GHS-POP R2023A pixel values inside the urban centre classified as 
class 30 in the corresponding year. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p107]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density  

Attribute ID 

GH_XST_D11_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 11 (very low density) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as very low density (DoU class 11) within the urban 
centre boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 11 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p108]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density 

Attribute ID 

GH_XST_D12_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 12 (low density rural) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as low density rural (DoU class 12) within the urban 
centre boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 12 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p109]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density  

Attribute ID 

GH_XST_P13_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 13 (rural cluster) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid 
multitemporal (1975-2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as rural cluster (DoU class 13) within the urban centre 
boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 13 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p110]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density  

Attribute ID 

GH_XST_D21_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 21 (suburban) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid 
multitemporal (1975-2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as suburban (DoU class 21) within the urban centre 
boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 21 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p111]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density 

Attribute ID 

GH_XST_D22_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 22 (semi dense urban 
cluster) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as semi dense urban cluster (DoU class 22) within the 
urban centre boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 22 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p112]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density 

Attribute ID 

GH_XST_D23_XXXX 

Indicator Name 

Population density within the Degree of Urbanisation Classification class 23 (dense urban cluster) 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid 
multitemporal (1975-2030).European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): GHS-SMOD R2023A - GHS settlement layers, 
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-
BUILT-S R2023A, multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as dense urban cluster (DoU class 23) within the urban 
centre boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 23 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p113]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Population density  

Attribute ID 

GH_XST_D30_XXXX 

Indicator Name 

Population density 

Units 

Inhabitants/km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Population density of the cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Population divided by the land area, both inside the urban centre classified as class 30 in the 
corresponding year. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p114]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Land Area  

Attribute ID 

GH_XST_L30_XXXX 

Indicator Name 

Land Area in the Urban Centre  

Units 

km2 

Data Source 

Pesaresi M., Politis P. (2022): 
GHS-LAND R2022A - Land fraction as derived from Sentinel2 image composite (2018) and OSM 
data. PID: http://data.europa.eu/89h/ab7ad451-5ed5-44a6-a4d0-9f7a4e848ceeEuropean 
Commission, Joint Research Centre (JRC) 
PID: https://doi.org/10.2905/AB7AD451-5ED5-44A6-A4D0-9F7A4E848CEE, 
doi:10.2905/AB7AD451-5ED5-44A6-A4D0-9F7A4E848CEE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Land surface of the cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Zonal statistics (count) of the GHS-LAND R2022A pixels (when the value identifies land surface) 
inside the urban centre classified as class 30 in the corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p115]

```text
Indicator thematic area 

GHSL 

Indicator group 

Cross statistics with DoU: Water Area  

Attribute ID 

GH_XST_W30_XXXX 

Indicator Name 

Water Area in the Urban Centre  

Units 

km2 

Data Source 

Pesaresi M., Politis P. (2022): 
GHS-LAND R2022A - Land fraction as derived from Sentinel2 image composite (2018) and OSM 
data. PID: http://data.europa.eu/89h/ab7ad451-5ed5-44a6-a4d0-9f7a4e848ceeEuropean 
Commission, Joint Research Centre (JRC) 
PID: https://doi.org/10.2905/AB7AD451-5ED5-44A6-A4D0-9F7A4E848CEE, 
doi:10.2905/AB7AD451-5ED5-44A6-A4D0-9F7A4E848CEE 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Water surface of the cells classified as urban centre (DoU class 30) within the urban centre 
boundary. 

Methodology 

Zonal statistics (count) of the GHS-LAND R2022A pixels (when the value identifies water surface) 
inside the urban centre classified as class 30 in the corresponding year. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

2025 

Uncertainties & Best practices  

Water Area can include marine water for coastal urban centres.  
```

### [D6-p116]

```text
2.9.3 Socioeconomic 

Indicator thematic area 

Socioeconomic 

Indicator Group 

GDP 

Attribute ID 

SC_GDP_AVG_XXXX 

Indicator Name 

Average Gross Domestic Product 

Units 

PPP 

Data Source 

Matti Kummu, Maria Kosonen, Sina Masoumzadeh Sayyar et al. Downscaled gridded global 
dataset for Gross Domestic Product (GDP) per capita PPP over 1990-2022, 29 April 2024, 
PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-4321741/v1] 

Indicator description  

Average of the GDP pixel value in the urban center 

Methodology 

Zonal average of the GDP layer pixel values inside the urban center. 

Methodology Short 

Zonal Statistics (average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p117]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

GDP 

Attribute ID 

SC_GDP_SUM_XXXX 

Indicator Name 

Total Gross Domestic Product 

Units 

PPP 

Data Source 

Matti Kummu, Maria Kosonen, Sina Masoumzadeh Sayyar et al. Downscaled gridded global 
dataset for Gross Domestic Product (GDP) per capita PPP over 1990-2022, 29 April 2024, 
PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-4321741/v1] 

Indicator description  

Sum of the GDP pixel values in the urban center 

Methodology 

Zonal sum of the GDP layer pixel values inside the urban center. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p118]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Population distribution 

Attribute ID 

SC_SEC_PCF_XXXX 

Indicator Name 

Percentage of female population 

Units 

% 

Data Source 

Tatem, A. WorldPop, open data for spatial demography. Sci Data 4, 170004 (2017). 
https://doi.org/10.1038/sdata.2017.4 

https://www.worldpop.org/ 

Indicator description  

Percentage of female population 

Methodology 

Percentage of the sum of female population data inside the urban center polygon by total 
population (sum of female and male) 

Methodology Short 

Ratio 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Do not use this indicator to calculate number of inhabitants. Socioeconomic indicators based on 
WorldPop cannot be compared with population indicators based on GHSL data in statistical 
analysis. 
```

### [D6-p119]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Population distribution 

Attribute ID 

SC_SEC_PCM_XXXX 

Indicator Name 

Percentage of male population 

Units 

% 

Data Source 

Tatem, A. WorldPop, open data for spatial demography. Sci Data 4, 170004 (2017). 
https://doi.org/10.1038/sdata.2017.4 

https://www.worldpop.org/ 

Indicator description  

Percentage of male population 

Methodology 

Percentage of the sum of male population data inside the urban center polygon by total 
population (sum of female and male) 

Methodology Short 

Ratio 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Do not use this indicator to calculate number of inhabitants. Socioeconomic indicators based on 
WorldPop cannot be compared with population indicators based on GHSL data in statistical 
analysis. 
```

### [D6-p120]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Population distribution 

Attribute ID 

SC_SEC_PCY_XXXX 

Indicator Name 

Percentage of young population 

Units 

% 

Data Source 

Tatem, A. WorldPop, open data for spatial demography. Sci Data 4, 170004 (2017). 
https://doi.org/10.1038/sdata.2017.4 

https://www.worldpop.org/ 

Indicator description  

Percentage of young population (0 to 14 years) 

Methodology 

Percentage of the sum of total population younger than 14 years old data inside the urban center 
polygon by total population (all years). 

Methodology Short 

Ratio 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Do not use this indicator to calculate number of inhabitants. Socioeconomic indicators based on 
WorldPop cannot be compared with population indicators based on GHSL data in statistical 
analysis. 
```

### [D6-p121]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Population distribution 

Attribute ID 

SC_SEC_PCA_XXXX 

Indicator Name 

Percentage of adult population 

Units 

% 

Data Source 

Tatem, A. WorldPop, open data for spatial demography. Sci Data 4, 170004 (2017). 
https://doi.org/10.1038/sdata.2017.4 

https://www.worldpop.org/ 

Indicator description  

Percentage of adult population (15 to 64 years) 

Methodology 

Percentage of the sum of total population older than 15 and younger than 64 years old data 
inside the urban center polygon by total population (all years). 

Methodology Short 

Ratio 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Do not use this indicator to calculate number of inhabitants. Socioeconomic indicators based on 
WorldPop cannot be compared with population indicators based on GHSL data in statistical 
analysis. 
```

### [D6-p122]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Population distribution 

Attribute ID 

SC_SEC_PCO_XXXX 

Indicator Name 

Percentage of older population 

Units 

% 

Data Source 

Tatem, A. WorldPop, open data for spatial demography. Sci Data 4, 170004 (2017). 
https://doi.org/10.1038/sdata.2017.4 

https://www.worldpop.org/ 

Indicator description  

Percentage of older population (more than 65 years) 

Methodology 

Percentage of the sum of total population older than 65 years old data inside the urban center 
polygon by total population (all years). 

Methodology Short 

Ratio 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Do not use this indicator to calculate number of inhabitants. Socioeconomic indicators based on 
WorldPop cannot be compared with population indicators based on GHSL data in statistical 
analysis. 
```

### [D6-p123]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Human Development Index 

Attribute ID 

SC_SEC_HDI_XXXX 

Indicator Name 

Human Development Index 

Units 

Dimensionless 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019). 

https://hdr.undp.org/data-center/human-development-index#/indicies/HDI 

Indicator description  

Human Development Index at subnational level based on the UNDP’s official HDI. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region.  

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p124]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gender Development Index 

Attribute ID 

SC_SEC_GDI_XXXX 

Indicator Name 

Gender Development Index 

Units 

Dimensionless 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019). 

https://hdr.undp.org/gender-development-index#/indicies/GDI 

Indicator description  

Gender Development Index at subnational level based on the UNDP’s official GDI. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p125]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gender Development Index 

Attribute ID 

SC_SEC_GDF_XXXX 

Indicator Name 

Female Gender Development Index 

Units 

Dimensionless 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

https://hdr.undp.org/gender-development-index#/indicies/GDI 

Indicator description  

Female Gender Development Index at subnational level based on the UNDP’s official GDI. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p126]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gender Development Index 

Attribute ID 

SC_SEC_GDM_XXXX 

Indicator Name 

Male Gender Development Index 

Units 

Dimensionless 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

https://hdr.undp.org/gender-development-index#/indicies/GDI 

Indicator description  

Male Gender Development Index at subnational level based on the UNDP’s official GDI. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p127]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Life Expectancy 

Attribute ID 

SC_SEC_LET_XXXX 

Indicator Name 

Life Expectancy 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years newborn children would live if subject to the mortality risks prevailing for the 
cross-section of population at the time of their birth. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p128]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Life Expectancy 

Attribute ID 

SC_SEC_LEF_XXXX 

Indicator Name 

Female Life Expectancy 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years female newborn children would live if subject to the mortality risks prevailing 
for the cross-section of population at the time of their birth. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p129]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Life Expectancy 

Attribute ID 

SC_SEC_LEM_XXXX 

Indicator Name 

Male Life Expectancy 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years male newborn children would live if subject to the mortality risks prevailing for 
the cross-section of population at the time of their birth. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p130]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Expected years of Schooling 

Attribute ID 

SC_SEC_SET_XXXX 

Indicator Name 

Expected years of Schooling 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years of schooling a child of school entrance age can expect to receive, if prevailing 
patterns of age-specific enrolment rates persist throughout the child’s schooling life. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p131]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Expected years of Schooling 

Attribute ID 

SC_SEC_SEF_XXXX 

Indicator Name 

Female Expected years of Schooling 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years of schooling a female child of school entrance age can expect to receive, if 
prevailing patterns of age-specific enrolment rates persist throughout the child’s schooling life. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p132]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Expected years of Schooling 

Attribute ID 

SC_SEC_SEM_XXXX 

Indicator Name 

Male Expected years of Schooling 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Number of years of schooling a male child of school entrance age can expect to receive, if 
prevailing patterns of age-specific enrolment rates persist throughout the child’s schooling life. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p133]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Mean years of Schooling 

Attribute ID 

SC_SEC_SYT_XXXX 

Indicator Name 

Mean years of Schooling of adults aged 25+ 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Average years of schooling for the population aged 25 or more years. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p134]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Mean years of Schooling 

Attribute ID 

SC_SEC_SYF_XXXX 

Indicator Name 

Mean years of Schooling of female adults aged 25+ 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Average years of schooling for the female population aged 25 or more years. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p135]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Mean years of Schooling 

Attribute ID 

SC_SEC_SYM_XXXX 

Indicator Name 

Mean years of Schooling of male adults aged 25+ 

Units 

Number of years 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

Average years of schooling for the male population aged 25 or more years. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p136]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gross national income per capita 

Attribute ID 

SC_SEC_GIT_XXXX 

Indicator Name 

(Log of) Gross national income per capita 

Units 

US$ 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

(Log of) Sum of value added by all resident producers plus any product taxes (less subsidies) not 
included in the valuation of output plus net receipts of primary income (compensation of 
employees and property income) from abroad. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p137]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gross national income per capita 

Attribute ID 

SC_SEC_GIF_XXXX 

Indicator Name 

(Log of) Gross national income per female capita 

Units 

US$ 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

(Log of) Sum of value added by female resident producers plus any product taxes (less subsidies) 
not included in the valuation of output plus net receipts of primary income (compensation of 
employees and property income) from abroad. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p138]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Gross national income per capita 

Attribute ID 

SC_SEC_GIM_XXXX 

Indicator Name 

(Log of) Gross national income per male capita 

Units 

US$ 

Data Source 

Data retrieved from the Subnational HDI Database of the Global Data 
Lab, https://globaldatalab.org/shdi/, version v7.0. 

Smits, J. and Permanyer, I. The Subnational Human Development Database. Sci. Data. 
6:190038 https://www.nature.com/articles/sdata201938 (2019).  

Indicator description  

(Log of) Sum of value added by male resident producers plus any product taxes (less subsidies) 
not included in the valuation of output plus net receipts of primary income (compensation of 
employees and property income) from abroad. 

Methodology 

Overlaying urban centers’ polygons with the Subnational Human Development Database layer. 
Calculate the weighted average of the overlaid polygons for each UC falling into more than one 
subnational region. 

Methodology Short 

Zonal Statistics (weighted average) 

Temporal Coverage 

1990, 1995, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

The index is constant through the urban centers located in the same subnational division. The 
results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p139]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_DSF_XXXX 

Indicator Name 

Average download speed fixed 

Units 

Mbps 

Data Source 

Speedtest by Ookla 

Indicator description  

Average download speed for the fixed network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p140]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_DSF_XXXX 

Indicator Name 

Average download speed mobile 

Units 

Mbps 

Data Source 

Speedtest by Ookla 

Indicator description  

Average download speed for the mobile network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020 -2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p141]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_USF_XXXX 

Indicator Name 

Average upload speed fixed 

Units 

Mbps 

Data Source 

Speedtest by Ookla 

Indicator description  

Average upload speed for the fixed network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p142]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_USM_XXXX 

Indicator Name 

Average upload speed mobile 

Units 

Mbps 

Data Source 

Speedtest by Ookla 

Indicator description  

Average upload speed for the mobile network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p143]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_ALF_XXXX 

Indicator Name 

Average latency fixed 

Units 

ms 

Data Source 

Speedtest by Ookla 

Indicator description  

Average latency for the fixed network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p144]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_ALM_XXXX 

Indicator Name 

Average latency mobile 

Units 

ms 

Data Source 

Speedtest by Ookla 

Indicator description  

Average latency for the mobile network. 

Methodology 

Zonal Statistics (weighted average) 

Methodology short 

Zonal Statistics (weighted average) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p145]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_NDF_XXXX 

Indicator Name 

Number of unique devices fixed 

Units 

Number of devices 

Data Source 

Speedtest by Ookla 

Indicator description  

Number of devices measuring the fixed network performance through the app. 

Methodology 

Zonal Statistics (sum) 

Methodology short 

Zonal Statistics (sum) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p146]

```text
Indicator thematic area 

Socioeconomic 

Indicator Group 

Connectivity  

Attribute ID 

SC_CON_NDM_XXXX 

Indicator Name 

Number of unique devices mobile 

Units 

Number of devices 

Data Source 

Speedtest by Ookla 

Indicator description  

Number of devices measuring the mobile network performance through the app. 

Methodology 

Zonal Statistics (sum) 

Methodology short 

Zonal Statistics (sum) 

Temporal Coverage 

2020, 2021, 2022, 2023 

Uncertainties & Best practices  

Network performance is measured via users through the Speedtest app. Therefore, information is 
missing for areas where no users is actively testing the network performance.  
```

### [D6-p147]

```text
2.9.4 Land Use Land Cover 

Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_020_XXXX 

Indicator Name 

Shrubs land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Shrubs (woody perennial plants with persistent and woody stems and without any defined main 
stem being less than 5 m tall) total area inside the urban center  

Methodology 

Sum of the pixels’ area classified as shrub (class 20) that overlay the urban center. 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p148]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_030_XXXX 

Indicator Name 

Herbaceous vegetation land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Herbaceous vegetation (plants without persistent stem or shoots above ground and lacking 
definite firm structure) total area inside the urban center  

Methodology 

Sum of the pixels’ area classified as herbaceous vegetation (class 30) that overlay the urban 
center. 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p149]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_040_XXXX 

Indicator Name 

Cultivated and managed vegetation / agriculture land use area 

Units 

Hectares 

Data Source 

Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Cultivated and managed vegetation / agriculture (lands covered with temporary crops followed by 
harvest and a bare soil period) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as cultivated and managed vegetation / agriculture (class 40) 
that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p150]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_050_XXXX 

Indicator Name 

Buildings and other man-made structures land use area 

Units 

Hectares 

Data Source 

Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Total area of land covered by buildings and other man-made structures inside the urban center. 

Methodology 

Sum of the pixels’ area classified as urban / built (class 50) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p151]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_060_XXXX 

Indicator Name 

Bare / sparse vegetation land cover area 

Units 

hectares 

Data Source 

Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Bare / sparse vegetation (lands with exposed soil, sand, or rocks and never has more than 10 % 
vegetated cover during any time of the year) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified bare / sparse vegetation (class 60) that overlay the urban 
center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p152]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_070_XXXX 

Indicator Name 

Snow and ice land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Snow and ice land cover (lands with exposed soil, sand, or rocks and never has more than 10 % 
vegetated cover during any time of the year) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as snow and ice land cover (class 70) that overlay the urban 
center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p153]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_080_XXXX 

Indicator Name 

Permanent water bodies land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Permanent water bodies (lakes, reservoirs, and rivers - can be either fresh or salt-water bodies -) 
total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as permanent water bodies (class 80) that overlay the urban 
center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p154]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_090_XXXX 

Indicator Name 

Herbaceous wetland land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Herbaceous wetland (lands with a permanent mixture of water and herbaceous or woody 
vegetation; the vegetation can be present in either salt, brackish, or fresh water) total area inside 
the urban center. 

Methodology 

Sum of the pixels’ area classified as herbaceous wetland (class 90) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p155]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_100_XXXX 

Indicator Name 

Moss and lichen land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Moss and lichen total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as moss and lichen (class 100) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p156]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_111_XXXX 

Indicator Name 

Closed forest, evergreen needle leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description (xxx max words) 

Closed forest, evergreen needle leaf (tree canopy >70 %, almost all needle leaf trees remain 
green all year; canopy is never without green foliage) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 111) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p157]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_112_XXXX 

Indicator Name 

Closed forest, evergreen broad leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Closed forest, evergreen broad leaf (tree canopy >70 %, almost all broadleaf trees remain green 
year round; canopy is never without green foliage) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 112) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p158]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_113_XXXX 

Indicator Name 

Closed forest, deciduous needle leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Closed forest, deciduous needle leaf (tree canopy >70 %, consists of seasonal needle leaf tree 
communities with an annual cycle of leaf-on and leaf-off periods) total area inside the urban 
center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 113) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p159]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_114_XXXX 

Indicator Name 

Closed forest, deciduous broad leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Closed forest, deciduous broad leaf (tree canopy >70 %, consists of seasonal broadleaf tree 
communities with an annual cycle of leaf-on and leaf-off periods) total area inside the urban 
center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 114) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p160]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_115_XXXX 

Indicator Name 

Closed forest (mixed) land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Closed forest (mixed) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 115) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p161]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_116_XXXX 

Indicator Name 

Closed forest (other) land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Closed forest (other) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as closed forest (class 116) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p162]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_121_XXXX 

Indicator Name 

Open forest, evergreen needle leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest, evergreen needle leaf (top layer- trees 15-70 % and second layer- mixed of shrubs 
and grassland, almost all needle leaf trees remain green all year; canopy is never without green 
foliage) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 121) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p163]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_122_XXXX 

Indicator Name 

Open forest, evergreen broad leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest, evergreen broad leaf (top layer- trees 15-70 % and second layer- mixed of shrubs 
and grassland, almost all broadleaf trees remain green year round; canopy is never without green 
foliage) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 122) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p164]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_123_XXXX 

Indicator Name 

Open forest, deciduous needle leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest, deciduous needle leaf (top layer- trees 15-70 % and second layer- mixed of shrubs 
and grassland, consists of seasonal needle leaf tree communities with an annual cycle of leaf-on 
and leaf-off periods) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 123) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p165]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_124_XXXX 

Indicator Name 

Open forest, deciduous broad leaf land cover area 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest, deciduous broad leaf (top layer- trees 15-70 % and second layer- mixed of shrubs 
and grassland, consists of seasonal broadleaf tree communities with an annual cycle of leaf-on 
and leaf-off periods) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 124) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p166]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_125_XXXX 

Indicator Name 

Open forest (mixed) 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest (mixed) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 125) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p167]

```text
Indicator thematic area 

Land Use Land Cover 

Indicator group 

Land Use Land Cover 

Attribute ID 

LU_HEC_126_XXXX 

Indicator Name 

Open forest (other) 

Units 

Hectares 

Data Source 

Buchhorn, M.; Lesiv, M.; Tsendbazar, N. - E.; Herold, M.; Bertels, L.; Smets, B. Copernicus Global 
Land Cover Layers-Collection 2. Remote Sensing 2020, 12Volume 108, 
1044. doi:10.3390/rs12061044 

Indicator description  

Open forest (other) total area inside the urban center. 

Methodology 

Sum of the pixels’ area classified as open forest (class 126) that overlay the urban center 

Methodology short 

Area 

Temporal Coverage 

2015, 2019 

Uncertainties & Best practices  
```

### [D6-p168]

```text
2.9.5 Exposure 

Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_POP_XXXX 

Indicator Name 

People exposed to floods (10 years return period) 

Units 

number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Number of people exposed to floods (10 years return period) 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center, masked by the 10 yrp 
flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p169]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_POP_XXXX 

Indicator Name 

People exposed to floods (100 years return period) 

Units 

number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Number of people exposed to floods (100 years return period) 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center, masked by the 100 yrp 
flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p170]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_SHP_XXXX 

Indicator Name 

Share of People exposed to floods (100 years return period) 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of people exposed to floods (10 years return period) over the total urban center population 

Methodology 

Percentage of population exposed over total population in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p171]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_SHP_XXXX 

Indicator Name 

Share of People exposed to floods (10 years return period) 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of people exposed to floods (100 years return period) over the total urban center 
population 

Methodology 

Percentage of population exposed over total population in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p172]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_BUS_XXXX 

Indicator Name 

Built-up surface exposed to floods (10 years return period) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Built-up surface exposed to floods (10 years return period) 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center, masked by the 10 
yrp flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p173]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_BUS_XXXX 

Indicator Name 

Built-up surface exposed to floods (100 years return period) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Built-up surface exposed to floods (100 years return period) 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center, masked by the 100 
yrp flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p174]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_SHB_XXXX 

Indicator Name 

Share of built-up surface exposed to floods (10 years return period) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of built-up surface exposed to floods (10 years return period) over the total urban center 
built-up surface 

Methodology 

Percentage of built-up surface exposed over total built-up in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p175]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_SHB_XXXX 

Indicator Name 

Share of built-up surface exposed to floods (100 years return period) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of built-up surface exposed to floods (100 years return period) over the total urban center 
built-up surface 

Methodology 

Percentage of built-up surface exposed over total built-up in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p176]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_NRE_XXXX 

Indicator Name 

Non-residential built-up surface exposed to floods (10 years return period) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Non-residential built-up surface exposed to floods (10 years return period) 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center, masked by the 
10 yrp flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p177]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_NRE_XXXX 

Indicator Name 

Non-residential built-up surface exposed to floods (100 years return period) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Non-residential built-up surface exposed to floods (100 years return period) 

Methodology 

Zonal sum of the GHS-BUILT-S-NRE R2023A pixel values inside the urban center, masked by the 
100 yrp flood hazard map (1 - flood, 0 - no flood). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p178]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_010_SNR_XXXX 

Indicator Name 

Share of non-residential built-up surface exposed to floods (10 years return period) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of non-residential built-up surface exposed to floods (10 years return period) over the 
urban center non-residential built-up surface 

Methodology 

Percentage of non-residential built-up surface exposed over non-residential built-up in the urban 
center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p179]

```text
Indicator thematic area 

Exposure 

Indicator group 

Floods 

Attribute ID 

EX_100_SNR_XXXX 

Indicator Name 

Share of non-residential built-up surface exposed to floods (100 years return period) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Baugh, Calum; Colonese, Juan; D'Angelo, Claudia; Francesco, Dottori; Neal, Jeffrey; Prudhomme; 
Christe; Salamon, Peter (2024): Modelled flood inundation for different return period scenarios at 
the global scale. European Commission, Joint Research Centre (JRC) 
https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-GLOFAS/flood_hazard/ 

Indicator description  

Share of non-residential built-up surface exposed to floods (100 years return period) over the l 
urban center non-residential built-up surface 

Methodology 

Percentage of non-residential built-up surface exposed over non-residential built-up in the urban 
center. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p180]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E01_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 1 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 1 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 1MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p181]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E02_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 2-3 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 2-3 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 2-3 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p182]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E04_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 4 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 4 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 4 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p183]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E05_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 5 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 5 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 5 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p184]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E06_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 6 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 6 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 6 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p185]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E07_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 7 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 7 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 7 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p186]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E08_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 8 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 8 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 8 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p187]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E09_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 9 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 9 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 9 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p188]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E10_POP_XXXX 

Indicator Name 

Population exposed to earthquakes (class 10 MMI) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Population exposed to earthquakes (class 10 MMI)  

Methodology 

Zonal statistics (sum) of GHS-POP R2023A inside the urban center affected by seismic hazard 
class 10 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p189]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_SHA_POP_XXXX 

Indicator Name 

Share of population exposed to earthquakes (class equal or greater than 6 MMI) 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Share of population exposed to earthquakes (class equal or greater than 6 MMI)  

Methodology 

Percentage of population exposed to earthquakes (class equal or greater than 6 MMI) over the 
total population of the urban center.  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p190]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E01_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 1 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 1 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 1 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p191]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E02_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 2-3 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 2-3 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 2-3 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p192]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E04_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 4 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 4 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 4 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p193]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E05_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 5 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 5 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 5 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p194]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E06_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 6 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 6 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 6 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p195]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E07_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 7 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 7 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 7 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p196]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E08_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 8 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 8 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 8 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p197]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E09_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 9 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 9 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 9 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p198]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E10_BUS_XXXX 

Indicator Name 

Total built-up exposed to earthquakes (class 10 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Built-up exposed to earthquakes (class 10 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S R2023A inside the urban center affected by seismic 
hazard class 10 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p199]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_SHA_BUS_XXXX 

Indicator Name 

Share of total built-up exposed to earthquakes (class equal or greater than 6 MMI) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Share of total built-up exposed to earthquakes (class equal or greater than 6 MMI)  

Methodology 

Percentage of total built-up exposed to earthquakes (class equal or greater than 6 MMI) over the 
total built-up of the urban center.  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p200]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E01_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 1 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 1 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 1 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p201]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E02_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 2-3 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 2-3 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard classes 2-3 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p202]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E04_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 4 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 4 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 4 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p203]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E05_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 5 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 5 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 5 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p204]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E06_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 6 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 6 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 6 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p205]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E07_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 7 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 7 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 7 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p206]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E08_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 8 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 8 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 8 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p207]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E09_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 9 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 9 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 9 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p208]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_E10_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to earthquakes (class 10 MMI) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Non-residential built-up exposed to earthquakes (class 10 MMI)  

Methodology 

Zonal statistics (sum) of GHS-BUILT-S-NRES R2023A inside the urban center affected by seismic 
hazard class 10 MMI  

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p209]

```text
Indicator thematic area 

Exposure 

Indicator group 

Earthquake 

Attribute ID 

EX_SHA_RES_XXXX 

Indicator Name 

Share of non-residential built-up exposed to earthquakes (class equal or greater than 6 MMI) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

GEM GLOBAL SEISMIC HAZARD MAP version 2023.1 

K. Johnson, M. Villani, K. Bayliss, C. Brooks, S. Chandrasekhar, T. Chartier, Y. Chen, J. Garcia-Pelaez, 
R. Gee, R. Styron, A. Rood, M. Simionato, M. Pagani (2023). Global Earthquake Model (GEM) 
Seismic Hazard Map (version 2023.1 - June 2023), DOI: https://doi.org/10.5281/zenodo.8409647 

Indicator description  

Share of non-residential built-up exposed to earthquakes (class equal or greater than 6 MMI)  

Methodology 

Percentage of non-residential built-up exposed to earthquakes (class equal or greater than 6 
MMI) over the total built-up of the urban center.  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p210]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_POP_XXXX 

Indicator Name 

Population living below 5 m LECZ 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in the areas of the urban center which elevation is 5 m above the sea level 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the LECZ 
layer (5 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p211]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_POP_XXXX 

Indicator Name 

Population living between 5 and 10 m LECZ 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in the areas of the urban center which elevation is between 5 and 10m above 
the sea level 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the LECZ 
layer (10 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p212]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_SHP_XXXX 

Indicator Name 

Share of population living below 5 m LECZ 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of population living in the areas of the urban center which elevation is 5 m above the sea 
level 

Methodology 

Percentage of population living inside the urban center area situated 5 m above the sea level 
over the total urban center population. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p213]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_SHP_XXXX 

Indicator Name 

Share of population living between 5 and 10 m LECZ 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of population living in the areas of the urban center which elevation is between 5 and 10 
m above the sea level 

Methodology 

Percentage of population living inside the urban center area situated between 5 and 10 m above 
the sea level over the total urban center population. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p214]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_LEC_SHP_XXXX 

Indicator Name 

Share of population living below 10 m LECZ 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of population living in the areas of the urban center which elevation is below 10 m above 
the sea level. 

Methodology 

Percentage of population living inside the urban center area situated below 10 m above the sea 
level over the total urban center population. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p215]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_BUS_XXXX 

Indicator Name 

Total Built-up situated below 5 m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up area in the areas of the urban center which elevation is below 5m above the sea 
level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the LECZ 
layer (5 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p216]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_BUS_XXXX 

Indicator Name 

Total Built-up situated between 5 and 10m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up area in the areas of the urban center which elevation is between 5 and 10m above 
the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the LECZ 
layer (10 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p217]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_SHB_XXXX 

Indicator Name 

Share of total built-up below 5 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of total built-up in the areas of the urban center which elevation is below 5 m above the 
sea level. 

Methodology 

Percentage of total built-up in the urban center area situated below 5 m above the sea level over 
the total urban center built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p218]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_SHB_XXXX 

Indicator Name 

Share of total built-up between 5 and 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of total built-up in the areas of the urban center which elevation is between 5 and 10 m 
above the sea level. 

Methodology 

Percentage of total built-up in the urban center area situated between 5 and 10 m above the sea 
level over the total urban center built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p219]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_LEC_SHB_XXXX 

Indicator Name 

Share of total built-up below 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of total built-up in the areas of the urban center which elevation is below 10 m above the 
sea level. 

Methodology 

Percentage of total built-up in the urban center area situated below 10 m above the sea level 
over the total urban center built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p220]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_NRE_XXXX 

Indicator Name 

Non-residential Built-up situated below 5 m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Non-residential built-up area in the areas of the urban center which elevation is below 5m above 
the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p221]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_NRE_XXXX 

Indicator Name 

Non-residential built-up situated between 5 and 10m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Non-residential built-up area in the areas of the urban center which elevation is between 5 and 
10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
LECZ layer (10 m above the sea level). 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p222]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_SNR_XXXX 

Indicator Name 

Share of non-residential built-up below 5 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of non-residential built-up in the areas of the urban center which elevation is below 5 m 
above the sea level. 

Methodology 

Percentage of non-residential built-up in the urban center area situated below 5 m above the sea 
level over the total urban center non-residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p223]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_SNR_XXXX 

Indicator Name 

Share of non-residential built-up between 5 and 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of non-residential built-up in the areas of the urban center which elevation is between 5 
and 10 m above the sea level. 

Methodology 

Percentage of non-residential built-up in the urban center area situated between 5 and 10 m 
above the sea level over the total urban center non-residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p224]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_LEC_SNR_XXXX 

Indicator Name 

Share of non-residential built-up below 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of non-residential built-up in the areas of the urban center which elevation is below 10 m 
above the sea level. 

Methodology 

Percentage of non-residential built-up in the urban center area situated below 10 m above the 
sea level over the total urban center non-residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p225]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_RES_XXXX 

Indicator Name 

Residential Built-up situated below 5 m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Residential built-up area in the areas of the urban center which elevation is below 5m above the 
sea level. 

Methodology 

Subtraction total built-up in LECZ (5m above the sea level) minus non-residential built-up in LECZ 
(5m above the sea level) 

Methodology Short 

Subtraction 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p226]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_NRE_XXXX 

Indicator Name 

Residential built-up situated between 5 and 10m LECZ 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Non-residential built-up area in the areas of the urban center which elevation is between 5 and 
10m above the sea level. 

Methodology 

Subtraction total built-up in LECZ (10 m above the sea level) minus non-residential built-up in 
LECZ (10 m above the sea level) 

Methodology Short 

Subtraction 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p227]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_SHR_XXXX 

Indicator Name 

Share of residential built-up below 5 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of residential built-up in the areas of the urban center which elevation is below 5 m above 
the sea level. 

Methodology 

Percentage of residential built-up in the urban center area situated below 5 m above the sea 
level over the total urban center residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p228]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_SHR_XXXX 

Indicator Name 

Share of non-residential built-up between 5 and 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of residential built-up in the areas of the urban center which elevation is between 5 and 10 
m above the sea level. 

Methodology 

Percentage of residential built-up in the urban center area situated between 5 and 10 m above 
the sea level over the total urban center residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p229]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_LEC_SHR_XXXX 

Indicator Name 

Share of residential built-up below 10 m LECZ 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Share of residential built-up in the areas of the urban center which elevation is below 10 m 
above the sea level. 

Methodology 

Percentage of residential built-up in the urban center area situated below 10 m above the sea 
level over the total urban center residential built-up. 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p230]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P11_XXXX 

Indicator Name 

Population living in BUTYPE 11 (residential prevalent 1-2 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023):  

GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 11 (residential prevalent 1-2 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 11 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p231]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p232]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P12_XXXX 

Indicator Name 

Population living in BUTYPE 12 (residential prevalent 3-7 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 12 (residential prevalent 3-7 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 12 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p233]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p234]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P13_XXXX 

Indicator Name 

Population living in BUTYPE 13 (residential prevalent > 8 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 13 (residential prevalent > 8 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 13 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p235]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p236]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P21_XXXX 

Indicator Name 

Population living in BUTYPE 21 (non-residential prevalent 1-2 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 21 (non-residential prevalent 1-2 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 21 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p237]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p238]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P22_XXXX 

Indicator Name 

Population living in BUTYPE 22 (non-residential prevalent 3-7 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 22 (non-residential prevalent 3-7 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 22 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p239]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p240]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_P23_XXXX 

Indicator Name 

Population living in BUTYPE 23 (non-residential prevalent >8 floors) in LECZ (below 5m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 23 (non-residential prevalent >8 floors) which elevation is 5 m 
above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 23 and the LECZ layer (5 m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p241]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p242]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P11_XXXX 

Indicator Name 

Population living in BUTYPE 11 (residential prevalent 1-2 floors) in LECZ (between 5 and 10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 11 (residential prevalent 1-2 floors) which elevation is between 
5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 11 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p243]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p244]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P12_XXXX 

Indicator Name 

Population living in BUTYPE 12 (residential prevalent 3-7 floors) in LECZ (between 5 and 10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 12 (residential prevalent 3-7 floors) which elevation is between 
5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 12 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p245]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p246]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P13_XXXX 

Indicator Name 

Population living in BUTYPE 13 (residential prevalent > 8 floors) in LECZ (between 5 and 10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 13 (residential prevalent > 8 floors) which elevation is between 
5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 13 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p247]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p248]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P21_XXXX 

Indicator Name 

Population living in BUTYPE 21 (non-residential prevalent 1-2 floors) in LECZ (between 5 and 
10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 21 (non-residential prevalent 1-2 floors) which elevation is 
between 5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 21 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 
```

### [D6-p249]

```text
Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p250]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P22_XXXX 

Indicator Name 

Population living in BUTYPE 22 (non-residential prevalent 3-7 floors) in LECZ (between 5 and 
10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 22 (non-residential prevalent 3-7 floors) which elevation is 
between 5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 22 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 
```

### [D6-p251]

```text
Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p252]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_P23_XXXX 

Indicator Name 

Population living in BUTYPE 23 (non-residential prevalent >8 floors) in LECZ (between 5 and 10m) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Population living in BUTYPE class 23 (non-residential prevalent >8 floors) which elevation is 
between 5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the BUTYPE 
layer class 23 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p253]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p254]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B11_XXXX 

Indicator Name 

Total built-up in BUTYPE 11 (residential prevalent 1-3 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 11 (residential prevalent 1-3 floors) which elevation is below 5m 
above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 11 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p255]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p256]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B12_XXXX 

Indicator Name 

Total built-up in BUTYPE 12 (residential prevalent 3-7 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 12 (residential prevalent 3-7 floors) which elevation is below 5m 
above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 12 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p257]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p258]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B13_XXXX 

Indicator Name 

Total built-up in BUTYPE 13 (residential prevalent >8 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 13 (residential prevalent >8 floors) which elevation is below 5m 
above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 13 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p259]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p260]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B21_XXXX 

Indicator Name 

Total built-up in BUTYPE 21 (non-residential prevalent 1-3 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 21 (non-residential prevalent 1-3 floors) which elevation is below 
5m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 21 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p261]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p262]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B22_XXXX 

Indicator Name 

Total built-up in BUTYPE 22 (non-residential prevalent 3-7 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 22 (non-residential prevalent 3-7 floors) which elevation is below 
5m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 22 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p263]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p264]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L05_B23_XXXX 

Indicator Name 

Total built-up in BUTYPE 23 (non-residential prevalent >8 floors) in LECZ (below 5m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 23 (non-residential prevalent >8 floors) which elevation is below 
5m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 23 and the LECZ layer (below 5m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p265]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p266]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B11_XXXX 

Indicator Name 

Total built-up in BUTYPE 11 (residential prevalent 1-3 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 11 (residential prevalent 1-3 floors) which elevation is between 5 
and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 11 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p267]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p268]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B12_XXXX 

Indicator Name 

Total built-up in BUTYPE 12 (residential prevalent 3-7 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 12 (residential prevalent 3-7 floors) which elevation is between 5 
and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 12 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p269]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p270]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B13_XXXX 

Indicator Name 

Total built-up in BUTYPE 13 (residential prevalent >8 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 13 (residential prevalent >8 floors) which elevation is between 5 
and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 13 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p271]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p272]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B21_XXXX 

Indicator Name 

Total built-up in BUTYPE 21 (non-residential prevalent 1-3 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 21 (non-residential prevalent 1-3 floors) which elevation is 
between 5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 21 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p273]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p274]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B22_XXXX 

Indicator Name 

Total built-up in BUTYPE 22 (non-residential prevalent 3-7 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 22 (non-residential prevalent 3-7 floors) which elevation is below 
between 5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 22 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p275]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p276]

```text
Indicator thematic area 

Exposure 

Indicator group 

Low elevated coastal Zones (LECZ) 

Attribute ID 

EX_L10_B23_XXXX 

Indicator Name 

Total built-up in BUTYPE 23 (non-residential prevalent >8 floors) in LECZ (between 5 and 10m) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Pesaresi, M., Schiavina, M., Politis, P., Freire, S., Krasnodębska, K., Uhl, J. H., Alessandra Carioli, 
Christina Corbane, Lewis Dijkstra, Pietro Florio, Hannah K. Friedrich, Jing Gao, Stefan Leyk, Linlin 
Lu, Luca Maffenini, Ines Mari-Rivero, Michele Melchiorri, Vasileios Syrris, Jamon Van Den Hoek & 
Kemper, T. (2024). Advances on the Global Human Settlement Layer by joint assessment of Earth 
Observation and population survey data. International Journal of Digital Earth, 17(1). 
https://doi.org/10.1080/17538947.2024.2390454 

Center for International Earth Science Information Network (CIESIN), Columbia University, and 
CUNY Institute for Demographic Research (CIDR), City University of New York. 2021. Low 
Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 3. 
Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
https://doi.org/10.7927/d1x1-d702. Accessed 18/05/2021. 

Indicator description  

Total built-up in BUTYPE class 23 (non-residential prevalent >8 floors) which elevation is between 
5 and 10m above the sea level. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
BUTYPE layer class 23 and the LECZ layer (between 5 and 10m above the sea level). 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p277]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p278]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_020_S1P_XXXX 

Indicator Name 

Population exposed to cyclone wind 20 yrp (wind speed classes 1-2) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  
Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Population exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 20 yrp. 

Methodology 

Zonal sum of the GHS- POP R2023A pixel values inside the urban center masked by the cyclone 
layer 20 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p279]

```text
DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p280]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_100_S1P_XXXX 

Indicator Name 

Population exposed to cyclone wind 100 yrp (wind speed classes 1-2) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  
Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Population exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 100 yrp. 

Methodology 

Zonal sum of the GHS- POP R2023A pixel values inside the urban center masked by the cyclone 
layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p281]

```text
DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p282]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S1P_XXXX 

Indicator Name 

Population exposed to cyclone wind 400 yrp (wind speed classes 1-2) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  
Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Population exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS- POP R2023A pixel values inside the urban center masked by the cyclone 
layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p283]

```text
DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p284]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S3P_XXXX 

Indicator Name 

Population exposed to cyclone wind 400 yrp (wind speed classes 3-5) 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  
Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU. ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Population exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS- POP R2023A pixel values inside the urban center masked by the cyclone 
layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p285]

```text
DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. There is population exposed only to classes 3-5 for 400 yrp 
cyclone wind  
```

### [D6-p286]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_020_S1B_XXXX 

Indicator Name 

Total built-up exposed to cyclone wind 20 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Total built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 20 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
cyclone layer 20 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p287]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p288]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_100_S1B_XXXX 

Indicator Name 

Total built-up exposed to cyclone wind 100 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Total built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 100 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p289]

```text
DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p290]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S1B_XXXX 

Indicator Name 

Total built-up exposed to cyclone wind 400 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Total built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS- BUILT-S R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p291]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p292]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S3P_XXXX 

Indicator Name 

Total built-up exposed to cyclone wind 400 yrp (wind speed classes 3-5) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Total built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson Hurricane Wind 
Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p293]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 

There is built-up exposed only to classes 3-5 for 400 yrp cyclone wind  
```

### [D6-p294]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_020_S1N_XXXX 

Indicator Name 

Non-residential built-up exposed to cyclone wind 20 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Non-residential built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson 
Hurricane Wind Scale) for a 20 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
cyclone layer 20 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p295]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p296]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_100_S1N_XXXX 

Indicator Name 

Non-residential built-up exposed to cyclone wind 100 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Non-residential built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson 
Hurricane Wind Scale) for a 100 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
```

### [D6-p297]

```text
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p298]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S1N_XXXX 

Indicator Name 

Non-residential built-up exposed to cyclone wind 400 yrp (wind speed classes 1-2) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Non-residential built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson 
Hurricane Wind Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS- BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
```

### [D6-p299]

```text
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 
```

### [D6-p300]

```text
Indicator thematic area 

Exposure 

Indicator group 

Cyclone wind 

Attribute ID 

EX_400_S3N_XXXX 

Indicator Name 

Non-residential built-up exposed to cyclone wind 400 yrp (wind speed classes 3-5) 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. Generation of a global synthetic tropical cyclone 
hazard dataset using STORM. Sci Data 7, 40 (2020). https://www.nature.com/articles/s41597-
020-0381-2  

Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts, J.C.J.H. (Jeroen) (2023): 
STORM tropical cyclone wind speed return periods. Version 4. 4TU.ResearchData. dataset. 
https://doi.org/10.4121/12705164.v4  

Indicator description  

Non-residential built-up exposed to cyclone wind classes 1-2 (category 1-2 Saffir-Simpson 
Hurricane Wind Scale) for a 400 yrp. 

Methodology 

Zonal sum of the GHS-BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
cyclone layer 100 yrp classes 1-2 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses tropical cyclone maximum wind speed return periods, generated using 
the Synthetic Tropical cyclOne geneRation Model (STORM). Input TC data are extracted from the 
```

### [D6-p301]

```text
International Best Track Archive for Climate Stewardship (IBTrACS) dataset (1980–2018). 
Comparison between the TC characteristics from the IBTrACS dataset to those generated by 
STORM shows that the STORM dataset performs sufficiently to be used for TC risk assessments 
and TC hazard analyses. The STORM model does not distinguish between tropical and 
extratropical systems. Therefore, TCs with extratropical nature in higher latitudes are not 
considered in our TC-related analysis. 

There is built-up exposed only to classes 3-5 for 400 yrp cyclone wind  
```

### [D6-p302]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_POP_XXXX 

Indicator Name 

Population exposed to coastal floods 20 yrp 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Population exposed to coastal floods (20 yrp). 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the coastal 
flood layer 20 yrp 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p303]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p304]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_POP_XXXX 

Indicator Name 

Population exposed to coastal floods 100 yrp 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 
Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 
Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4 
Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Population exposed to coastal floods (100 yrp). 

Methodology 

Zonal sum of the GHS-POP R2023A pixel values inside the urban center masked by the coastal 
flood layer 100 yrp 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p305]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p306]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_BUS_XXXX 

Indicator Name 

Built-up exposed to coastal floods 20 yrp 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Total built-up exposed to coastal floods (20 yrp). 

Methodology 

Zonal sum of the GHS- BUILT-S R2023A pixel values inside the urban center masked by the 
coastal flood layer 20 yrp 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p307]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p308]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_BUS_XXXX 

Indicator Name 

Built-up exposed to coastal floods 100 yrp 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Total built-up exposed to coastal floods (100 yrp). 

Methodology 

Zonal sum of the GHS- BUILT-S R2023A pixel values inside the urban center masked by the 
coastal flood layer 100 yrp 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p309]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p310]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to coastal floods 20 yrp 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 
Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Non-residential built-up exposed to coastal floods (20 yrp). 

Methodology 

Zonal sum of the GHS- BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
coastal flood layer 20 yrp 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p311]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p312]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_NRE_XXXX 

Indicator Name 

Non-residential built-up exposed to coastal floods 100 yrp 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4.  
Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Non-residential built-up exposed to coastal floods (100 yrp). 

Methodology 

Zonal sum of the GHS- BUILT-S-NRES R2023A pixel values inside the urban center masked by the 
coastal flood layer 100 yrp 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p313]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p314]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_SHP_XXXX 

Indicator Name 

Share of population exposed to coastal floods 20 yrp 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of population exposed to coastal floods (20 yrp). 

Methodology 

Percentage of population exposed to coastal floods (20yrp) over total population in urban center.  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p315]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p316]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_SHP_XXXX 

Indicator Name 

Share of population exposed to coastal floods 100 yrp 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of population exposed to coastal floods (100 yrp). 

Methodology 

Percentage of population exposed to coastal floods (100yrp) over total population in urban 
center.  

Methodology Short 

Ratio 
```

### [D6-p317]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p318]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_SHB_XXXX 

Indicator Name 

Share of built-up exposed to coastal floods 20 yrp 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of total built-up exposed to coastal floods (20 yrp). 

Methodology 

Percentage of total built-up exposed to coastal floods (20yrp) over total built-up in urban center.  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 
```

### [D6-p319]

```text
Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p320]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_SHB_XXXX 

Indicator Name 

Share of built-up exposed to coastal floods 100 yrp 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of total built-up exposed to coastal floods (100 yrp). 

Methodology 

Percentage of total built-up exposed to coastal floods (100yrp) over total built-up in urban 
center.  

Methodology Short 

Ratio 

Temporal Coverage 
```

### [D6-p321]

```text
1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p322]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF2_SNR_XXXX 

Indicator Name 

Share of non-residential built-up exposed to coastal floods 20 yrp 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of non-residential built-up exposed to coastal floods (20 yrp). 

Methodology 

Percentage of non-residential built-up exposed to coastal floods (20yrp) over non-residential 
built-up in urban center.  

Methodology Short 

Ratio 
```

### [D6-p323]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p324]

```text
Indicator thematic area 

Exposure 

Indicator group 

Coastal flood 

Attribute ID 

EX_CF1_SNR_XXXX 

Indicator Name 

Share of non-residential built-up exposed to coastal floods 100 yrp 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030)European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Verlaan, M., Jevrejeva, S., Jackson, L.P., Feyen, L., 
2018. Global probabilistic projections of extreme sea levels show intensification of coastal flood 
hazard. Nat. Commun. 9, 2360. https://doi.org/10.1038/s41467-018-04692-w. 

Vousdoukas, M.I., Mentaschi, L., Voukouvalas, E., Bianchi, A., Dottori, F., Feyen, L.,2018. Climatic 
and socioeconomic controls of future coastal flood risk in Europe. Nat. Clim. Change. 89 (8), 776–
780. https://doi.org/10.1038/s41558-018-0260-4. 

Dottori, F., Salamon, P., Bianchi, A., Alfieri, L., Hirpa, F.A., Feyen, L., 2016. Development and 
evaluation of a framework for global flood hazard mapping. Adv. Water Resour. 94, 87–102. 
https://doi.org/10.1016/j.advwatres.2016.05.002.  

Indicator description  

Share of non-residential built-up exposed to coastal floods (100 yrp). 

Methodology 

Percentage of non-residential built-up exposed to coastal floods (100yrp) over non-residential 
built-up in urban center.  

Methodology Short 

Ratio 
```

### [D6-p325]

```text
Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

DRMKC (JRC) team uses the coastal flood extent which is estimated by the JRC LISFLOOD-FP 
numerical model and derived by the various design return periods of the total water level. The 
extreme total water level describes the contribution of the mean sea level, tides and extreme 
episodic water level variations (storm surges and waves), without considering the non-linear 
interactions between the hydrodynamic components. Although the episodic offshore water level 
has been validated with tide gauge and wave buoy records, uncertainties of the derived 
inundation extent may arise due to the performance skill of the utilized hydrodynamic numerical 
models, in the absence of high resolution and accurate nearshore topobathy data, especially in 
locations with complex morphology.  
```

### [D6-p326]

```text
2.9.6 Hazards 

Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_VAC_XXXX 

Indicator Name 

Number of event type 'violence against civilians' 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as 'violence against civilians' 

Methodology 

Zonal count of point-based ACLED data where violence type is 'violence against civilians'. The 
total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p327]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_BAT_XXXX 

Indicator Name 

Number of event type ‘battles’ 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as ‘battles’ 

Methodology 

Zonal count of point-based ACLED data where violence type is ‘battles’. The total number 
corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p328]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_SDV_XXXX 

Indicator Name 

Number of event type ‘Strategic Developments’ 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as ‘Strategic Developments’ 

Methodology 

Zonal count of point-based ACLED data where violence type is ‘Strategic Developments’. The total 
number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p329]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_RIO_XXXX 

Indicator Name 

Number of event type ‘riots’ 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as ‘riots’ 

Methodology 

Zonal count of point-based ACLED data where violence type is ‘riots’. The total number 
corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p330]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_PRO_XXXX 

Indicator Name 

Number of event type ‘protests’ 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as ‘protests’ 

Methodology 

Zonal count of point-based ACLED data where violence type is ‘protests’. The total number 
corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p331]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_ERV_XXXX 

Indicator Name 

Number of event type ‘explosions or remote violence’ 

Units 

Number of events 

Data Source 

ACLED dataset. Published on: 25 October 2023 | Last updated: 29 November 2023. Last complete 
ACLED download on 2023-09-26 10:10:29 

Indicator description  

Count of numbers of events in the urban center classified as ‘explosions or remote violence’ 

Methodology 

Zonal count of point-based ACLED data where violence type is ‘explosions or remote violence’. 
The total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

https://acleddata.com/knowledge-base/how-does-acled-code-and-review-data-to-ensure-quality/ 
```

### [D6-p332]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_TOT_XXXX 

Indicator Name 

Total number of events 

Units 

Number of events 

Data Source 

Sundberg, Ralph, and Erik Melander, 2013, “Introducing the UCDP Georeferenced Event Dataset”, 
Journal of Peace Research, vol.50, no.4, 523-532. Download on 2023-08-22 15:00:27. Includes 
the following versions: 23.1, 23.01.23.06, 23.0.7 

Indicator description  

Count of total number of events in the urban center  

Methodology 

Zonal count of point-based UCDP GED event data. The total number corresponds to the previous 
year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Högbladh Stina, 2023, “UCDP GED Codebook version 23.1”, Department of Peace and Conflict 
Research, Uppsala University https://ucdp.uu.se/downloads/ged/ged231.pdf 
```

### [D6-p333]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_SBC_XXXX 

Indicator Name 

Number of state-based-conflict 

Units 

Number of events 

Data Source 

Sundberg, Ralph, and Erik Melander, 2013, “Introducing the UCDP Georeferenced Event Dataset”, 
Journal of Peace Research, vol.50, no.4, 523-532. Download on 2023-08-22 15:00:27. Includes 
the following versions: 23.1, 23.01.23.06, 23.0.7 

Indicator description  

Count of state-based-conflict events in the urban center  

Methodology 

Zonal count of point-based UCDP GED event data when the event type is ‘state-based-conflict’. 
The total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Högbladh Stina, 2023, “UCDP GED Codebook version 23.1”, Department of Peace and Conflict 
Research, Uppsala University https://ucdp.uu.se/downloads/ged/ged231.pdf 
```

### [D6-p334]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_NSC_XXXX 

Indicator Name 

Number of non-state-conflict 

Units 

Number of events 

Data Source 

Sundberg, Ralph, and Erik Melander, 2013, “Introducing the UCDP Georeferenced Event Dataset”, 
Journal of Peace Research, vol.50, no.4, 523-532. Download on 2023-08-22 15:00:27. Includes 
the following versions: 23.1, 23.01.23.06, 23.0.7 

Indicator description  

Count of non-state-conflict events in the urban center  

Methodology 

Zonal count of point-based UCDP GED event data when the event type is ‘non-state-conflict’. The 
total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Högbladh Stina, 2023, “UCDP GED Codebook version 23.1”, Department of Peace and Conflict 
Research, Uppsala University https://ucdp.uu.se/downloads/ged/ged231.pdf 
```

### [D6-p335]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_OSV_XXXX 

Indicator Name 

Number of one-sided violence 

Units 

Number of events 

Data Source 

Sundberg, Ralph, and Erik Melander, 2013, “Introducing the UCDP Georeferenced Event Dataset”, 
Journal of Peace Research, vol.50, no.4, 523-532. Download on 2023-08-22 15:00:27. Includes 
the following versions: 23.1, 23.01.23.06, 23.0.7 

Indicator description  

Count of one-sided violence events in the urban center  

Methodology 

Zonal count of point-based UCDP GED event data when the event type is ‘one-sided violence’. The 
total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Högbladh Stina, 2023, “UCDP GED Codebook version 23.1”, Department of Peace and Conflict 
Research, Uppsala University https://ucdp.uu.se/downloads/ged/ged231.pdf 
```

### [D6-p336]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Conflicts 

Attribute ID 

HZ_CON_FAT_XXXX 

Indicator Name 

Number of fatalities 

Units 

Number of fatalities 

Data Source 

Sundberg, Ralph, and Erik Melander, 2013, “Introducing the UCDP Georeferenced Event Dataset”, 
Journal of Peace Research, vol.50, no.4, 523-532. Download on 2023-08-22 15:00:27. Includes 
the following versions: 23.1, 23.01.23.06, 23.0.7 

Indicator description  

Count of one-sided violence events in the urban center  

Methodology 

Zonal count of point-based UCDP GED number of fatalities data. The total number corresponds to 
the previous year, the precedent year and the next year. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  

Högbladh Stina, 2023, “UCDP GED Codebook version 23.1”, Department of Peace and Conflict 
Research, Uppsala University https://ucdp.uu.se/downloads/ged/ged231.pdf 
```

### [D6-p337]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Wildfires 

Attribute ID 

HZ_WLF_NUM_XXXX 

Indicator Name 

Accumulate number of wildfires 

Units 

Number of wildfires 

Data Source 

San-Miguel-Ayanz, J., Houston Durrant, T., Boca, R., Libertà, G., Branco, A., de Rigo, D., Ferrari, D., 
Maianti, P., Artés Vivancos, T., Schulte, E., Loffler, P., Benchikha, A., Abbas, M., Humer, F., 
Konstantinov, V., Pešut, I., Petkoviček, S., Papageorgiou, K., Toumasis, I., Kütt, V., Kõiv, K., Ruuska, 
R., Anastasov, T., Timovska, M., Michaut, P., Joannelle, P., Lachmann, M., Pavlidou, K., Debreceni, P., 
Nagy, D., Nugent, C., Di Fonzo, M., Leisavnieks, E., Jaunķiķis, Z., Mitri, G., Repšienė, S., Assali, F., 
Mharzi Alaoui, H., Botnen, D., Piwnicki, J., Szczygieł, R., Janeira, M., Borges, A., Sbirnea, R., Mara, S., 
Eritsov, A., Longauerová, V., Jakša, J., Enriquez, E., Lopez, A., Sandahl, L., Reinhard, M., Conedera, 
M., Pezzatti, B., Dursun, K. T., Baltaci, U., Moffat, A., 2017. Forest fires in Europe, Middle East and 
North Africa 2016. Publications Office of the European Union, Luxembourg. ISBN:978-92-79-
71292-0, https://doi.org/10.2760/17690 
Goldammer, J. G., Mangeon, S., Keywood, M., Kaiser, J. W., de Groot, W. J., Gunawan, D., Gan, C., 
Field, R., Sofiev, M., Baklanov, A., 2018. Vegetation Fire and Smoke Pollution Warning and Advisory 
System (VFSP-WAS): concept note and expert recommendations. Vol. 235 of GAW Report series. 
World Meteorological Organization, Geneva, 
Switzerland. https://library.wmo.int/doc_num.php?explnum_id=4519 
Giglio, L., Boschetti, L., Roy, D., Humber, M., Justice, C.O., The Collection 6 MODIS Burned Area 
Mapping Algorithm and Product. Remote Sensing of Environment (submitted June 2018). 

https://data.jrc.ec.europa.eu/dataset/e6f7a4e7-1f64-4ba9-9363-6bc864ab4666 

Indicator description  

Accumulate number of wildfires  

Methodology 

Zonal count of wildfires occurred inside the urban center. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 
```

### [D6-p338]

```text
2015, 2020, 2024 

Uncertainties & Best practices  

The accumulate periods are the following: 2012-2015 for the year 2015, 2016-2020 for the 
year 2020 and 2020-2024 for the year 2024 
```

### [D6-p339]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Wildfires 

Attribute ID 

HZ_WLF_BHA_XXXX 

Indicator Name 

Accumulate burnt area 

Units 

hectares 

Data Source 

San-Miguel-Ayanz, J., Houston Durrant, T., Boca, R., Libertà, G., Branco, A., de Rigo, D., Ferrari, D., 
Maianti, P., Artés Vivancos, T., Schulte, E., Loffler, P., Benchikha, A., Abbas, M., Humer, F., 
Konstantinov, V., Pešut, I., Petkoviček, S., Papageorgiou, K., Toumasis, I., Kütt, V., Kõiv, K., Ruuska, 
R., Anastasov, T., Timovska, M., Michaut, P., Joannelle, P., Lachmann, M., Pavlidou, K., Debreceni, P., 
Nagy, D., Nugent, C., Di Fonzo, M., Leisavnieks, E., Jaunķiķis, Z., Mitri, G., Repšienė, S., Assali, F., 
Mharzi Alaoui, H., Botnen, D., Piwnicki, J., Szczygieł, R., Janeira, M., Borges, A., Sbirnea, R., Mara, S., 
Eritsov, A., Longauerová, V., Jakša, J., Enriquez, E., Lopez, A., Sandahl, L., Reinhard, M., Conedera, 
M., Pezzatti, B., Dursun, K. T., Baltaci, U., Moffat, A., 2017. Forest fires in Europe, Middle East and 
North Africa 2016. Publications Office of the European Union, Luxembourg. ISBN:978-92-79-
71292-0, https://doi.org/10.2760/17690 
Goldammer, J. G., Mangeon, S., Keywood, M., Kaiser, J. W., de Groot, W. J., Gunawan, D., Gan, C., 
Field, R., Sofiev, M., Baklanov, A., 2018. Vegetation Fire and Smoke Pollution Warning and Advisory 
System (VFSP-WAS): concept note and expert recommendations. Vol. 235 of GAW Report series. 
World Meteorological Organization, Geneva, 
Switzerland. https://library.wmo.int/doc_num.php?explnum_id=4519 
Giglio, L., Boschetti, L., Roy, D., Humber, M., Justice, C.O., The Collection 6 MODIS Burned Area 
Mapping Algorithm and Product. Remote Sensing of Environment (submitted June 2018). 

https://data.jrc.ec.europa.eu/dataset/e6f7a4e7-1f64-4ba9-9363-6bc864ab4666 

Indicator description  

Accumulate burnt area due to wildfires  

Methodology 

Zonal sum of the burnt area due to wildfires inside the urban center. 

Methodology Short 

Zonal Statistics (count) 
```

### [D6-p340]

```text
Temporal Coverage 

2015, 2020, 2024 

Uncertainties & Best practices  

The accumulate periods are the following: 2012-2015 for the year 2015, 2016-2020 for the 
year 2020 and 2020-2024 for the year 2024 
```

### [D6-p341]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_TEV_XXXX 

Indicator Name 

Total number of events 

Units 

Number of events 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of events 

Methodology 

Spatial join and count of the events (1 event has 1 or multiple hazards) that overlay the urban 
center. The total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p342]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_THZ_XXXX 

Indicator Name 

Total number of hazards 

Units 

Number of hazards 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards 

Methodology 

Spatial join and count of the hazards (1 hazards can happen more than once during an event and 
in multiple events) that overlay the urban center. The total number corresponds to the previous 
year, the precedent year and the next year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p343]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_EAR_XXXX 

Indicator Name 

Earthquakes occurrence 

Units 

Number of hazards type earthquakes 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type earthquakes 

Methodology 

Spatial join and count of the hazards (when hazard is classified as earthquakes) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p344]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_EWI_XXXX 

Indicator Name 

Extreme wind occurrence 

Units 

Number of hazards type extreme wind 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type extreme wind 

Methodology 

Spatial join and count of the hazards (when hazard is classified as extreme wind) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p345]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_TSU_XXXX 

Indicator Name 

Tsunami occurrence 

Units 

Number of hazards type extreme wind 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type tsunami 

Methodology 

Spatial join and count of the hazards (when hazard is classified as tsunami) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p346]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_HEW_XXXX 

Indicator Name 

Heatwaves occurrence 

Units 

Number of hazards type heatwaves 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type heatwaves 

Methodology 

Spatial join and count of the hazards (when hazard is classified as heatwave) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p347]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_DRO_XXXX 

Indicator Name 

Droughts occurrence 

Units 

Number of hazards type drought 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type drought 

Methodology 

Spatial join and count of the hazards (when hazard is classified as drought) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p348]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_FLO_XXXX 

Indicator Name 

Floods occurrence 

Units 

Number of hazards type flood 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type flood 

Methodology 

Spatial join and count of the hazards (when hazard is classified as flood) that overlay the urban 
center. The total number corresponds to the previous year, the precedent year and the next year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p349]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_TCY_XXXX 

Indicator Name 

Tropical Cyclones occurrence 

Units 

Number of hazards type tropical cyclones 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type tropical cyclones 

Methodology 

Spatial join and count of the hazards (when hazard is classified as tropical cyclones) that overlay 
the urban center. The total number corresponds to the previous year, the precedent year and the 
next year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p350]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_VOL_XXXX 

Indicator Name 

Volcanic eruptions occurrence 

Units 

Number of hazards type volcanic eruption 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type volcanic eruption 

Methodology 

Spatial join and count of the hazards (when hazard is classified as volcano) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p351]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_LAN_XXXX 

Indicator Name 

Landslide occurrence 

Units 

Number of hazards type landslide 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type landslide 

Methodology 

Spatial join and count of the hazards (when hazard is classified as landslide) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p352]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_COW_XXXX 

Indicator Name 

Cold wave occurrence 

Units 

Number of hazards type cold wave 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type cold wave 

Methodology 

Spatial join and count of the hazards (when hazard is classified as cold wave) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p353]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_WLF_XXXX 

Indicator Name 

Wildfire occurrence 

Units 

Number of hazards type wildfire 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Total number of hazards type wildfire 

Methodology 

Spatial join and count of the hazards (when hazard is classified as wildfire) that overlay the 
urban center. The total number corresponds to the previous year, the precedent year and the next 
year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p354]

```text
Indicator thematic area 

Hazard and Risk 

Indicator group 

Combined events 

Attribute ID 

HZ_CEV_MHZ_XXXX 

Indicator Name 

Maximum number of hazards per event 

Units 

Maximum number of hazards per event 

Data Source 

Claassen, J.N., Ward, P.J., Daniell, J. et al. A new method to compile global multi-hazard event 
sets. Sci Rep 13, 13808 (2023). https://doi.org/10.1038/s41598-023-40400-5 

MYRIAD – Hazard Event Sets (MYRIAD-HES) https://zenodo.org/records/8269680  

Indicator description  

Maximum number of hazards per event 

Methodology 

Spatial join and count of the number of hazards per event that overlay the urban center. 
Selection of the maximum number. The total number corresponds to the previous year, the 
precedent year and the next year. 

Methodology Short 

Spatial join 

Temporal Coverage 

2005, 2010, 2015 

Uncertainties & Best practices  
```

### [D6-p355]

```text
2.9.7 SDGs 

Indicator thematic area 

SDG 

Indicator group 

Land Use efficiency 

Attribute ID 

SD_LUE_LPR_XXXX_YYYY 

Indicator Name 

Land Use Efficiency 

Units 

Dimensionless 

Data Source 

Melchiorri, M.; Pesaresi, M.; Florczyk, A.J.; Corbane, C.; Kemper, T. Principles and Applications of the 
Global Human Settlement Layer as Baseline for the Land Use Efficiency Indicator—SDG 
11.3.1. ISPRS Int. J. Geo-Inf. 2019, 8, 96. https://doi.org/10.3390/ijgi8020096 

SDG indicator metadata (Harmonized metadata template - format version 1.1), Metadata-11-03-
01.pdf (un.org) 

Indicator description  

Land Use efficiency is the ratio between the Land Consumption Rate and the Population Growth 
Rate 

Methodology 

𝐿𝑈𝐸= 𝐿𝑎𝑛𝑑 𝐶𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛 𝑟𝑎𝑡𝑒

Methodology Short 

Definition formula 

Temporal Coverage 

𝑃𝑜𝑝𝑢𝑙𝑎𝑡𝑖𝑜𝑛 𝐺𝑟𝑜𝑤𝑡ℎ 𝑟𝑎𝑡𝑒 

1975-1980, 1980-1990, 1990-2000, 2000-2010, 2010-2020, 2020-2030, 1975-2020, 1990-
2020, 2000-2020 

Uncertainties & Best practices  

Values less than -5 are indicated as ‘< -5’ and values greater than 5 are indicated as ‘>5’ in the 
dataset. 
```

### [D6-p356]

```text
Indicator thematic area 

SDG 

Indicator group 

Land Use Efficiency 

Attribute ID 

SD_LUE_LCR_XXXX_YYYY 

Indicator Name 

Land Consumption Rate 

Units 

Dimensionless 

Data Source 

Melchiorri, M.; Pesaresi, M.; Florczyk, A.J.; Corbane, C.; Kemper, T. Principles and Applications of the 
Global Human Settlement Layer as Baseline for the Land Use Efficiency Indicator—SDG 
11.3.1. ISPRS Int. J. Geo-Inf. 2019, 8, 96. https://doi.org/10.3390/ijgi8020096 

SDG indicator metadata (Harmonized metadata template - format version 1.1), Metadata-11-03-
01.pdf (un.org) 

Indicator description  

Land Consumption Rate is defined as the share of the difference between total built-up in two 
years over the total built-up in the past year, divided by the difference between the two years. 
The total built-up is calculated as total built-up in the urban center. 

Methodology 

𝐿𝐶𝑅= 𝐵𝑈_𝑇𝑂𝑇𝑡−𝐵𝑈_𝑇𝑂𝑇𝑡−𝑛

Methodology Short 

Definition formula  

Temporal Coverage 

 × 1

𝑛 

𝐵𝑈_𝑇𝑂𝑇𝑡−𝑛

1975-1980, 1980-1990, 1990-2000, 2000-2010, 2010-2020, 2020-2030, 1975-2020, 1990-
2020, 2000-2020 

Uncertainties & Best practices  

Values less than -5 are indicated as ‘< -5’ and values greater than 5 are indicated as ‘>5’ in the 
dataset. 
```

### [D6-p357]

```text
Indicator thematic area 

SDG 

Indicator group 

Land Use Efficiency 

Attribute ID 

SD_LUE_PGR_XXXX_YYYY 

Indicator Name 

Population Growth Rate 

Units 

Dimensionless 

Data Source 

Melchiorri, M.; Pesaresi, M.; Florczyk, A.J.; Corbane, C.; Kemper, T. Principles and Applications of the 
Global Human Settlement Layer as Baseline for the Land Use Efficiency Indicator—SDG 
11.3.1. ISPRS Int. J. Geo-Inf. 2019, 8, 96. https://doi.org/10.3390/ijgi8020096 

SDG indicator metadata (Harmonized metadata template - format version 1.1), Metadata-11-03-
01.pdf (un.org) 

Indicator description  

Population Growth Rate is defined as logarithm of the fraction between of the total population in 
the current year and the total population in the past year, divided by the difference between the 
two years. The total population is calculated as total built-up in the urban center. 

Methodology 

𝐿𝐶𝑅= ln ( 𝑃𝑂𝑃_𝑇𝑂𝑇𝑡

Methodology Short 

Definition formula 

Temporal Coverage 

) × 1

𝑛 

𝑃𝑂𝑃_𝑇𝑂𝑇𝑡−𝑛

1975-1980, 1980-1990, 1990-2000, 2000-2010, 2010-2020, 2020-2030, 1975-2020, 1990-
2020, 2000-2020 

Uncertainties & Best practices  

Values less than -5 are indicated as ‘< -5’ and values greater than 5 are indicated as ‘>5’ in the 
dataset. 
```

### [D6-p358]

```text
Indicator thematic area 

SDG 

Indicator group 

Open Green Space 

Attribute ID 

SD_POP_HGR_XXXX 

Indicator Name 

Share of the Urban Centre population living in area of high greenness 

Units 

% 

Data Source 

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): GHS-POP R2023A - GHS population grid 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) PID: 
http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, doi:10.2905/2FF68A52-
5B5B-4A22-8F40-C41DA8332CFE 

Pesaresi M., Politis P. (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from 
Sentinel2 composite and Landsat, multitemporal (1975-2030). European Commission, Joint 
Research Centre (JRC) PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Indicator description  

Share of the Urban Centre population living in area of high greenness for the corresponding year 

Methodology 

Sequence of masking and zonal statistics. 300m buffering of the built-up domain, masking of the 
built-up and population grid with 3 years average NDVI (greater equal than threshold); zonal 
statistics of the population in the obtained mask; ratio between zonal statistics population and 
urban centre population. Thresholds for high greenness are estimated by UN-Habitat for agro-
ecological-zones, from a sample of 700 cities. Agro-ecological zone values are obtained by 
averaging observations within the cities in each zone. 
```

### [D6-p359]

```text
Methodology Short 

Zonal Statistics (sum), ratio 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p360]

```text
2.9.8 Climate 

Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_CUR_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (reanalysis data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (reanalysis data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  
```

### [D6-p361]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_P45_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (projection rcp 4.5 data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (projection rcp 4.5 data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p362]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_P85_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (projection rcp 8.5 data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (projection rcp 8.5 data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p363]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B04_CUR_XXXX 

Indicator Name 

Temperature Seasonality (standard deviation ×100) - reanalysis data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Seasonality (standard deviation ×100) - reanalysis data 

Methodology 

Zonal average of the Temperature Seasonality pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  
```

### [D6-p364]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B04_P45_XXXX 

Indicator Name 

Temperature Seasonality (standard deviation ×100) - projection rcp 4.5 data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Seasonality (standard deviation ×100) - projection rcp 4.5 data 

Methodology 

Zonal average of the Temperature Seasonality pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p365]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B04_P85_XXXX 

Indicator Name 

Temperature Seasonality (standard deviation ×100) - projection rcp 8.5 data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Seasonality (standard deviation ×100) - projection rcp 8.5 data 

Methodology 

Zonal average of the Temperature Seasonality pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p366]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B07_CUR_XXXX 

Indicator Name 

Temperature Annual Range - reanalysis data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Annual Range - reanalysis data 

Methodology 

Zonal average of the Temperature Annual Range pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  
```

### [D6-p367]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B07_P45_XXXX 

Indicator Name 

Temperature Annual Range - projection rcp 4.5 data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Annual Range - projection rcp 4.5 data 

Methodology 

Zonal average of the Temperature Annual Range pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p368]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B07_P85_XXXX 

Indicator Name 

Temperature Annual Range - projection rcp 8.5 data 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Temperature Annual Range - projection rcp 8.5 data 

Methodology 

Zonal average of the Temperature Annual Range pixels values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p369]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B12_CUR_XXXX 

Indicator Name 

Annual Precipitation mean in the decade - reanalysis data 

Units 

mm year-1 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Precipitation mean in the decade - reanalysis data 

Methodology 

Zonal average of the Annual Precipitation mean in the decade pixel values touching the urban 
center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  
```

### [D6-p370]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B12_P45_XXXX 

Indicator Name 

Annual Precipitation mean in the decade - projection rcp 4.5 data 

Units 

mm year-1 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Precipitation mean in the decade - projection rcp 4.5 data 

Methodology 

Zonal average of the Annual Precipitation mean in the decade pixel values touching the urban 
center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p371]

```text
Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B12_P85_XXXX 

Indicator Name 

Annual Precipitation mean in the decade - projection rcp 8.5 data 

Units 

mm year-1 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Precipitation mean in the decade - projection rcp 8.5 data 

Methodology 

Zonal average of the Annual Precipitation mean in the decade pixels values touching the urban 
center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions for projections: temperature averages between models 'access1_0', 
'bcc_csm1_1_m', 'gfdl_esm2m', 'hadgem2_cc', 'ipsl_cm5a_lr', 'noresm1_m', with ensemble 
members r1i1p1 
```

### [D6-p372]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_CUR_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - current conditions 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - current conditions 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p373]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_119_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 119 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 119 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p374]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_126_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 126 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 126 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p375]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_245_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 245 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 245 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p376]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_370_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 370 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 370 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p377]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_434_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 434 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 434 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p378]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_460_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 460 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 460 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p379]

```text
Indicator thematic area 

Climate 

Indicator group 

Climate classification 

Attribute ID 

CL_KOP_585_XXXX 

Indicator Name 

Köppen-Geiger classification of the majority of UC surface - projection ssp 585 

Units 

categorical 

Data Source 

Beck, H., Zimmermann, N., McVicar, T. et al. Present and future Köppen-Geiger climate 
classification maps at 1-km resolution. Sci Data 5, 180214 (2018). 
https://doi.org/10.1038/sdata.2018.214  

Indicator description  

Köppen-Geiger classification of the majority of UC surface - projection ssp 585 

Methodology 

Spatial join of the Köppen-Geiger classification layer. The classification covering the greater area 
of the urban center is considered as the indicator value.  

Methodology Short 

Spatial join 

Temporal Coverage 

2040, 2070 

Uncertainties & Best practices  
```

### [D6-p380]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_PVO_XXXX 

Indicator Name 

Average daily PV potential 

Units 

kWh/kWp 

Data Source 

Photovoltaic power potential obtained from the “Global Solar Atlas 2.0, a free, web-based 
application is developed and operated by the company Solargis s.r.o. on behalf of the World Bank 
Group, utilizing Solargis data, with funding provided by the Energy Sector Management 
Assistance Program (ESMAP). For additional information: https://globalsolaratlas.info. Access 
21/06/2024    

Indicator description  

Average daily PV potential 

Methodology 

Zonal average of the Photovoltaic power potential layer in the decade pixels values touching the 
urban center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p381]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_W01_XXXX 

Indicator Name 

Mean wind speed at 10 m above ground 

Units 

m/s 

Data Source 

Neil N. Davis, Jake Badger, Andrea N. Hahmann, Brian O. Hansen, Niels G. Mortensen, Mark Kelly, 
Xiaoli G. Larsén, Bjarke T. Olsen, Rogier Floors, Gil Lizcano, Pau Casso, Oriol Lacave, Albert Bosch, 
Ides Bauwens, Oliver James Knight, Albertine Potter van Loon, Rachel Fox, Tigran Parvanyan, 
Søren Bo Krohn Hansen, Duncan Heathfield, Marko Onninen, Ray Drummond; The Global Wind 
Atlas: A high-resolution dataset of climatologies and associated web-based application; Bulletin 
of the American Meteorological Society, Volume 104: Issue 8, Pages E1507-E1525, August 2023, 
DOI: https://doi.org/10.1175/BAMS-D-21-0075.1 

Global Wind Speed obtained from the Global Wind Atlas version 3.3, a free, web-based 
application developed, owned and operated by the Technical University of Denmark (DTU). The 
Global Wind Atlas version 3.3 is released in partnership with the World Bank Group, utilizing data 
provided by Vortex, using funding provided by the Energy Sector Management Assistance 
Program (ESMAP). For additional information: https://globalwindatlas.info.  

Indicator description  

Mean wind speed at 10 m above ground 

Methodology 

Zonal average of wind speed at 10 m layer in the decade pixels values touching the urban center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p382]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_W05_XXXX 

Indicator Name 

Mean wind speed at 50 m above ground 

Units 

m/s 

Data Source 

Neil N. Davis, Jake Badger, Andrea N. Hahmann, Brian O. Hansen, Niels G. Mortensen, Mark Kelly, 
Xiaoli G. Larsén, Bjarke T. Olsen, Rogier Floors, Gil Lizcano, Pau Casso, Oriol Lacave, Albert Bosch, 
Ides Bauwens, Oliver James Knight, Albertine Potter van Loon, Rachel Fox, Tigran Parvanyan, 
Søren Bo Krohn Hansen, Duncan Heathfield, Marko Onninen, Ray Drummond; The Global Wind 
Atlas: A high-resolution dataset of climatologies and associated web-based application; Bulletin 
of the American Meteorological Society, Volume 104: Issue 8, Pages E1507-E1525, August 2023, 
DOI: https://doi.org/10.1175/BAMS-D-21-0075.1 

Global Wind Speed obtained from the Global Wind Atlas version 3.3, a free, web-based 
application developed, owned and operated by the Technical University of Denmark (DTU). The 
Global Wind Atlas version 3.3 is released in partnership with the World Bank Group, utilizing data 
provided by Vortex, using funding provided by the Energy Sector Management Assistance 
Program (ESMAP). For additional information: https://globalwindatlas.info.  

Indicator description  

Mean wind speed at 50 m above ground 

Methodology 

Zonal average of wind speed at 50 m layer in the decade pixels values touching the urban center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p383]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_W10_XXXX 

Indicator Name 

Mean wind speed at 100 m above ground 

Units 

m/s 

Data Source 

Neil N. Davis, Jake Badger, Andrea N. Hahmann, Brian O. Hansen, Niels G. Mortensen, Mark Kelly, 
Xiaoli G. Larsén, Bjarke T. Olsen, Rogier Floors, Gil Lizcano, Pau Casso, Oriol Lacave, Albert Bosch, 
Ides Bauwens, Oliver James Knight, Albertine Potter van Loon, Rachel Fox, Tigran Parvanyan, 
Søren Bo Krohn Hansen, Duncan Heathfield, Marko Onninen, Ray Drummond; The Global Wind 
Atlas: A high-resolution dataset of climatologies and associated web-based application; Bulletin 
of the American Meteorological Society, Volume 104: Issue 8, Pages E1507-E1525, August 2023, 
DOI: https://doi.org/10.1175/BAMS-D-21-0075.1 

Global Wind Speed obtained from the Global Wind Atlas version 3.3, a free, web-based 
application developed, owned and operated by the Technical University of Denmark (DTU). The 
Global Wind Atlas version 3.3 is released in partnership with the World Bank Group, utilizing data 
provided by Vortex, using funding provided by the Energy Sector Management Assistance 
Program (ESMAP). For additional information: https://globalwindatlas.info.  

Indicator description  

Mean wind speed at 100 m above ground 

Methodology 

Zonal average of wind speed at 100 m layer in the decade pixels values touching the urban 
center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p384]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_W15_XXXX 

Indicator Name 

Mean wind speed at 150 m above ground 

Units 

m/s 

Data Source 

Neil N. Davis, Jake Badger, Andrea N. Hahmann, Brian O. Hansen, Niels G. Mortensen, Mark Kelly, 
Xiaoli G. Larsén, Bjarke T. Olsen, Rogier Floors, Gil Lizcano, Pau Casso, Oriol Lacave, Albert Bosch, 
Ides Bauwens, Oliver James Knight, Albertine Potter van Loon, Rachel Fox, Tigran Parvanyan, 
Søren Bo Krohn Hansen, Duncan Heathfield, Marko Onninen, Ray Drummond; The Global Wind 
Atlas: A high-resolution dataset of climatologies and associated web-based application; Bulletin 
of the American Meteorological Society, Volume 104: Issue 8, Pages E1507-E1525, August 2023, 
DOI: https://doi.org/10.1175/BAMS-D-21-0075.1 

Global Wind Speed obtained from the Global Wind Atlas version 3.3, a free, web-based 
application developed, owned and operated by the Technical University of Denmark (DTU). The 
Global Wind Atlas version 3.3 is released in partnership with the World Bank Group, utilizing data 
provided by Vortex, using funding provided by the Energy Sector Management Assistance 
Program (ESMAP). For additional information: https://globalwindatlas.info.  

Indicator description  

Mean wind speed at 150 m above ground 

Methodology 

Zonal average of wind speed at 150 m layer in the decade pixels values touching the urban 
center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p385]

```text
Indicator thematic area 

Climate 

Indicator group 

Renewable potential 

Attribute ID 

CL_REN_W20_XXXX 

Indicator Name 

Mean wind speed at 200 m above ground 

Units 

m/s 

Data Source 

Neil N. Davis, Jake Badger, Andrea N. Hahmann, Brian O. Hansen, Niels G. Mortensen, Mark Kelly, 
Xiaoli G. Larsén, Bjarke T. Olsen, Rogier Floors, Gil Lizcano, Pau Casso, Oriol Lacave, Albert Bosch, 
Ides Bauwens, Oliver James Knight, Albertine Potter van Loon, Rachel Fox, Tigran Parvanyan, 
Søren Bo Krohn Hansen, Duncan Heathfield, Marko Onninen, Ray Drummond; The Global Wind 
Atlas: A high-resolution dataset of climatologies and associated web-based application; Bulletin 
of the American Meteorological Society, Volume 104: Issue 8, Pages E1507-E1525, August 2023, 
DOI: https://doi.org/10.1175/BAMS-D-21-0075.1 

Global Wind Speed obtained from the Global Wind Atlas version 3.3, a free, web-based 
application developed, owned and operated by the Technical University of Denmark (DTU). The 
Global Wind Atlas version 3.3 is released in partnership with the World Bank Group, utilizing data 
provided by Vortex, using funding provided by the Energy Sector Management Assistance 
Program (ESMAP). For additional information: https://globalwindatlas.info.  

Indicator description  

Mean wind speed at 200 m above ground 

Methodology 

Zonal average of wind speed at 200 m layer in the decade pixels values touching the urban 
center 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p386]

```text
Indicator thematic area 

Climate 

Indicator group 

Warm Days 

Attribute ID 

CL_WDS_CUR_XXXX 

Indicator Name 

Percentage of days with maximum temperature - reanalysis data 

Units 

% 

Data Source 

Sandstad, M., Schwingshackl, C., Iles, C., (2022): Climate extreme indices and heat stress 
indicators derived from CMIP6 global climate projections. Copernicus Climate Change Service 
(C3S) Climate Data Store (CDS). DOI: 10.24381/cds.776e08bd (Accessed on 29-August-2024) 

Indicator description  

Percentage of days with maximum temperature above the corresponding calendar day 90th 
percentile of maximum temperature for a 5-day moving window in the base period 1961-1990 - 
reanalysis data 

Methodology 

Zonal average of the data layer pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  

Assumptions: model 'ec_earth3', with ensemble members r1i1p1f1 
```

### [D6-p387]

```text
Indicator thematic area 

Climate 

Indicator group 

Warm Days 

Attribute ID 

CL_WDS_126_XXXX 

Indicator Name 

Percentage of days with maximum temperature - projection ssp 126 

Units 

% 

Data Source 

Sandstad, M., Schwingshackl, C., Iles, C., (2022): Climate extreme indices and heat stress 
indicators derived from CMIP6 global climate projections. Copernicus Climate Change Service 
(C3S) Climate Data Store (CDS). DOI: 10.24381/cds.776e08bd (Accessed on 29-August-2024) 

Indicator description  

Percentage of days with maximum temperature above the corresponding calendar day 90th 
percentile of maximum temperature for a 5-day moving window in the base period 1961-1990 - 
projection ssp 126 

Methodology 

Zonal average of the data layer pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions: model 'ec_earth3', with ensemble members r1i1p1f1 
```

### [D6-p388]

```text
Indicator thematic area 

Climate 

Indicator group 

Warm Days 

Attribute ID 

CL_WDS_245_XXXX 

Indicator Name 

Percentage of days with maximum temperature - projection ssp 245 

Units 

% 

Data Source 

Sandstad, M., Schwingshackl, C., Iles, C., (2022): Climate extreme indices and heat stress 
indicators derived from CMIP6 global climate projections. Copernicus Climate Change Service 
(C3S) Climate Data Store (CDS). DOI: 10.24381/cds.776e08bd (Accessed on 29-August-2024) 

Indicator description  

Percentage of days with maximum temperature above the corresponding calendar day 90th 
percentile of maximum temperature for a 5-day moving window in the base period 1961-1990 - 
projection ssp 245 

Methodology 

Zonal average of the data layer pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions: model 'ec_earth3', with ensemble members r1i1p1f1 
```

### [D6-p389]

```text
Indicator thematic area 

Climate 

Indicator group 

Warm Days 

Attribute ID 

CL_WDS_370_XXXX 

Indicator Name 

Percentage of days with maximum temperature - projection ssp 370 

Units 

% 

Data Source 

Sandstad, M., Schwingshackl, C., Iles, C., (2022): Climate extreme indices and heat stress 
indicators derived from CMIP6 global climate projections. Copernicus Climate Change Service 
(C3S) Climate Data Store (CDS). DOI: 10.24381/cds.776e08bd (Accessed on 29-August-2024) 

Indicator description  

Percentage of days with maximum temperature above the corresponding calendar day 90th 
percentile of maximum temperature for a 5-day moving window in the base period 1961-1990 - 
projection ssp 370 

Methodology 

Zonal average of the data layer pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions: model 'ec_earth3', with ensemble members r1i1p1f1 
```

### [D6-p390]

```text
Indicator thematic area 

Climate 

Indicator group 

Warm Days 

Attribute ID 

CL_WDS_585_XXXX 

Indicator Name 

Percentage of days with maximum temperature - projection ssp 585 

Units 

% 

Data Source 

Sandstad, M., Schwingshackl, C., Iles, C., (2022): Climate extreme indices and heat stress 
indicators derived from CMIP6 global climate projections. Copernicus Climate Change Service 
(C3S) Climate Data Store (CDS). DOI: 10.24381/cds.776e08bd (Accessed on 29-August-2024) 

Indicator description  

Percentage of days with maximum temperature above the corresponding calendar day 90th 
percentile of maximum temperature for a 5-day moving window in the base period 1961-1990 - 
projection ssp 585 

Methodology 

Zonal average of the data layer pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

2020, 2030 

Uncertainties & Best practices  

Assumptions: model 'ec_earth3', with ensemble members r1i1p1f1 
```

### [D6-p391]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A01_XXXX 

Indicator Name 

Share of urban center area in “compact highrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “compact highrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “compact highrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p392]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A02_XXXX 

Indicator Name 

Share of urban center area in “compact midrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “compact midrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “compact midrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p393]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A03_XXXX 

Indicator Name 

Share of urban center area in “compact lowrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “compact lowrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “compact lowrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p394]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A04_XXXX 

Indicator Name 

Share of urban center area in “open highrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “open highrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “open highrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p395]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A05_XXXX 

Indicator Name 

Share of urban center area in “open midrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “open midrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “open midrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p396]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A06_XXXX 

Indicator Name 

Share of urban center area in “open lowrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “open lowrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “open lowrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p397]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A07_XXXX 

Indicator Name 

Share of urban center area in “lightweight lowrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “lightweight lowrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “lightweight lowrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p398]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A08_XXXX 

Indicator Name 

Share of urban center area in “large lowrise” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “large lowrise” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “large lowrise” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p399]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A09_XXXX 

Indicator Name 

Share of urban center area in “sparsely built” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “sparsely built” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “sparsely built” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p400]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A10_XXXX 

Indicator Name 

Share of urban center area in “heavy industry” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “heavy industry” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “heavy industry” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p401]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A11_XXXX 

Indicator Name 

Share of urban center area in “dense trees” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “dense trees” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “dense trees” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p402]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A12_XXXX 

Indicator Name 

Share of urban center area in “scattered trees” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “scattered trees” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “scattered trees” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p403]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A13_XXXX 

Indicator Name 

Share of urban center area in “bush, scrub” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “bush, scrub” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “bush, scrub” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p404]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A14_XXXX 

Indicator Name 

Share of urban center area in “low plants” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “low plants” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “low plants” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p405]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A15_XXXX 

Indicator Name 

Share of urban center area in “bare rock or paved” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “bare rock or paved” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “bare rock or paved” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p406]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A16_XXXX 

Indicator Name 

Share of urban center area in “bare soil or sand” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “bare soil or sand” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “bare soil or sand” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p407]

```text
Indicator thematic area 

Climate 

Indicator group 

Local climate Zone 

Attribute ID 

CL_LCZ_A17_XXXX 

Indicator Name 

Share of urban center area in “water” Local Climate Zone 

Units 

Categorical 

Data Source 

Demuzere M, Kittner J, Martilli A, et al. A global map of local climate zones to support earth 
system modelling and urban-scale environmental science. Earth Syst Sci Data. 2022a; 
14(8):3835-3873. doi:10.5194/essd-14-3835-2022. 
https://essd.copernicus.org/articles/14/3835/2022/  

Demuzere M, Kittner J, Martilli A, et al. Global Local Climate Zone map. Zenodo (2022b) 

doi:10.5281/zenodo.6364594. https://zenodo.org/records/8419340  

Indicator description  

Share of urban center area that is classified as “water” Local Climate Zone 

Methodology 

Share of area of the urban center classified as “water” over total urban center area.  

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p408]

```text
Indicator thematic area 

Climate 

Indicator group 

Universal thermal climate indicators 

Attribute ID 

CL_UTC_T32_XXXX 

Indicator Name 

Annual mean number of days in the decade that Universal thermal climate index has exceeded 
32 degrees based on daily maxima. 

Units 

Number of days 

Data Source 

Di Napoli C., Barnard C., Prudhomme C., Cloke HL and Pappenberger F. (2020): Thermal comfort 
indices derived from ERA5 reanalysis. Copernicus Climate Change Service (C3S) Climate Data 
Store (CDS). DOI: 10.24381/cds.553b7518  (Accessed on 24-January-2025) 

Indicator description  

Annual mean number of days in the decade that Universal thermal climate index has exceeded 
32 degrees based on daily maxima. 

Methodology 

Zonal average (count) of the number of pixels exceeding the threshold value (32 degrees) 
touching the urban center. 

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010, 2020 

Uncertainties & Best practices  
```

### [D6-p409]

```text
2.9.9 Emissions 
```

### [D6-p410]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_AGR_XXXX 

Indicator Name 

Total CO2 emissions in agriculture sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets).  

https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total CO2 emissions in agriculture sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 
```

### [D6-p411]

```text
Uncertainties & Best practices  
```

### [D6-p412]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_ENE_XXXX 

Indicator Name 

Total CO2 emissions in the energy sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total CO2 emissions in the energy sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 
```

### [D6-p413]

```text
Uncertainties & Best practices  
```

### [D6-p414]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_IND_XXXX 

Indicator Name 

Total CO2 emissions in the industry sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total CO2 emissions in the industry sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 
```

### [D6-p415]

```text
Uncertainties & Best practices  
```

### [D6-p416]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_RES_XXXX 

Indicator Name 

Total CO2 emissions in residential sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total CO2 emissions in residential sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p417]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p418]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_TRA_XXXX 

Indicator Name 

Total CO2 emissions in transport sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total CO2 emissions in transport sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 
```

### [D6-p419]

```text
Uncertainties & Best practices  
```

### [D6-p420]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_CO2_WAS_XXXX 

Indicator Name 

Total CO2 emissions in waste sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total CO2 emissions in waste sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p421]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p422]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_AGR_XXXX 

Indicator Name 

Total GHG emissions in agriculture sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total GHG emissions in agriculture sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p423]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p424]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_ENE_XXXX 

Indicator Name 

Total GHG emissions in the energy sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total GHG emissions in the energy sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p425]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p426]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_IND_XXXX 

Indicator Name 

Total GHG emissions in the industry sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total GHG emissions in the industry sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p427]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p428]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_RES_XXXX 

Indicator Name 

Total GHG emissions in residential sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total GHG emissions in residential sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p429]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p430]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_TRA_XXXX 

Indicator Name 

Total GHG emissions in transport sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total GHG emissions in transport sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal Statistics (sum) 
```

### [D6-p431]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p432]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_GHG_WAS_XXXX 

Indicator Name 

Total GHG emissions in waste sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total GHG emissions in waste sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p433]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p434]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_AGR_XXXX 

Indicator Name 

Total NOx emissions in agriculture sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total NOx emissions in agriculture sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p435]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p436]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_ENE_XXXX 

Indicator Name 

Total NOx emissions in the energy sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total NOx emissions in the energy sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p437]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p438]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_IND_XXXX 

Indicator Name 

Total NOx emissions in the industry sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total NOx emissions in the industry sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p439]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p440]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_RES_XXXX 

Indicator Name 

Total NOx emissions in residential sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total NOx emissions in residential sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p441]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p442]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_TRA_XXXX 

Indicator Name 

Total NOx emissions in transport sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total NOx emissions in transport sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p443]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p444]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_NOX_WAS_XXXX 

Indicator Name 

Total NOx emissions in waste sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total NOx emissions in waste sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p445]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p446]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_AGR_XXXX 

Indicator Name 

Total PM2.5 emissions in agriculture sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total PM2.5 emissions in agriculture sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p447]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p448]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_ENE_XXXX 

Indicator Name 

Total PM2.5 emissions in the energy sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total PM2.5 emissions in the energy sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p449]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p450]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_IND_XXXX 

Indicator Name 

Total PM2.5 emissions in the industry sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total PM2.5 emissions in the industry sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p451]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p452]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_RES_XXXX 

Indicator Name 

Total PM2.5 emissions in residential sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total PM2.5 emissions in residential sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p453]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p454]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_TRA_XXXX 

Indicator Name 

Total PM2.5 emissions in transport sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total PM2.5 emissions in transport sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p455]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p456]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance and sector 

Attribute ID 

EM_PM2_WAS_XXXX 

Indicator Name 

Total PM2.5 emissions in waste sector 

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.  

Indicator description  

Total PM2.5 emissions in waste sector 

Methodology 

Zonal statistics (sum) of the EDGAR gridded emissions (with a resolution of 0.01x0.01 degree) 
and the urban centres polygons. If a cell is fully inside a polygon, the 100% of emissions of that 
cell is allocated to the polygon itself. If a cell is partly inside / partly outside a polygon, the % of 
urban population of that cell is population belonging to the urban polygon applied to allocate a 
fraction of the grid emissions to that polygon. 

Methodology Short 

Zonal statistics (sum) 
```

### [D6-p457]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p458]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance 

Attribute ID 

EM_CO2_TOT_XXXX 

Indicator Name 

Total CO2 emissions in all sectors  

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total CO2 emissions in all sectors 

Methodology 

Sum of the CO2 emissions in all sectors  

Methodology Short 

Sum 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p459]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance 

Attribute ID 

EM_GHG_TOT_XXXX 

Indicator Name 

Total GHG emissions in all sectors  

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total GHG emissions in all sectors 

Methodology 

Sum of the GHG emissions in all sectors  

Methodology Short 

Sum 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p460]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance 

Attribute ID 

EM_NOX_TOT_XXXX 

Indicator Name 

Total NOx emissions in all sectors  

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total NOx emissions in all sectors 

Methodology 

Sum of the NOx emissions in all sectors  

Methodology Short 

Sum 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p461]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Total emissions per substance 

Attribute ID 

EM_PM2_TOT_XXXX 

Indicator Name 

Total PM2.5 emissions in all sectors  

Units 

ton/year 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Total PM2.5 emissions in all sectors 

Methodology 

Sum of the PM2.5 emissions in all sectors  

Methodology Short 

Sum 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p462]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_SAG_XXXX 

Indicator Name 

Share of CO2 agricultural emissions over total CO2 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81 

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of CO2 agricultural emissions over total CO2 emissions 

Methodology 

Ratio between CO2 agricultural emissions and total CO2 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p463]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_SEN_XXXX 

Indicator Name 

Share of CO2 energy emissions over total CO2 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Daabase for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of CO2 energy emissions over total CO2 emissions 

Methodology 

Ratio between CO2 energy emissions and total CO2 emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p464]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_SIN_XXXX 

Indicator Name 

Share of CO2 industry emissions over total CO2 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of CO2 industry emissions over total CO2 emissions 

Methodology 

Ratio between CO2 industry emissions and total CO2 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p465]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_SRE_XXXX 

Indicator Name 

Share of residential CO2 emissions over total CO2 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of residential CO2 emissions over total CO2 emissions 

Methodology 

Ratio between residential CO2 emissions and total CO2 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p466]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_STR_XXXX 

Indicator Name 

Share of CO2 transport emissions over total CO2 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81 

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of CO2 transport emissions over total emissions 

Methodology 

Ratio between CO2 transport emissions and total CO2 emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p467]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_CO2_SWA_XXXX 

Indicator Name 

Share of CO2 waste emissions over CO2 total emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of CO2 waste emissions over total CO2 emissions 

Methodology 

Ratio between CO2 waste emissions and total CO2 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p468]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_SAG_XXXX 

Indicator Name 

Share of GHG agricultural emissions over total GHG emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of GHG agricultural emissions over total GHG emissions 

Methodology 

Ratio between GHG agricultural emissions and total GHG emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p469]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_SEN_XXXX 

Indicator Name 

Share of GHG energy emissions over total GHG emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of GHG energy emissions over total GHG emissions 

Methodology 

Ratio between GHG energy emissions and total GHG emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p470]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_SIN_XXXX 

Indicator Name 

Share of GHG industry emissions over total GHG emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of GHG industry emissions over total GHG emissions 

Methodology 

Ratio between GHG industry emissions and total GHG emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p471]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_SRE_XXXX 

Indicator Name 

Share of GHG residential emissions over total GHG emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of residential GHG emissions over total GHG emissions 

Methodology 

Ratio between residential GHG emissions and total GHG emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p472]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_STR_XXXX 

Indicator Name 

Share of GHG transport emissions over total GHG emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of GHG transport emissions over total GHG emissions 

Methodology 

Ratio between GHG transport emissions and total GHG emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p473]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_GHG_SWA_XXXX 

Indicator Name 

Share of GHG waste emissions over GHG total emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of GHG waste emissions over total GHG emissions 

Methodology 

Ratio between GHG waste emissions and total GHG emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p474]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_SAG_XXXX 

Indicator Name 

Share of NOx agricultural emissions over total NOx emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–2830, 
doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of NOx agricultural emissions over total NOx emissions 

Methodology 

Ratio between NOx agricultural emissions and total NOx emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p475]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_SEN_XXXX 

Indicator Name 

Share of NOx energy emissions over total NOx emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of NOx energy emissions over total NOx emissions 

Methodology 

Ratio between NOx energy emissions and total NOx emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p476]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_SIN_XXXX 

Indicator Name 

Share of NOx industry emissions over total NOx emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of NOx industry emissions over total NOx emissions 

Methodology 

Ratio between NOx industry emissions and total NOx emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p477]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_SRE_XXXX 

Indicator Name 

Share of NOx residential emissions over total NOx emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of residential NOx emissions over total NOx emissions 

Methodology 

Ratio between residential NOx emissions and total NOx emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p478]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_STR_XXXX 

Indicator Name 

Share of NOx transport emissions over total NOx emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of NOx transport emissions over total NOx emissions 

Methodology 

Ratio between NOx transport emissions and total NOx emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p479]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_NOX_SWA_XXXX 

Indicator Name 

Share of NOx waste emissions over NOx total emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of NOx waste emissions over total NOx emissions 

Methodology 

Ratio between NOx waste emissions and total NOx emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p480]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_SAG_XXXX 

Indicator Name 

Share of PM2.5 agricultural emissions over total PM2.5 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of PM2.5 agricultural emissions over total PM2.5 emissions 

Methodology 

Ratio between PM2.5 agricultural emissions and total PM2.5 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p481]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_SEN_XXXX 

Indicator Name 

Share of PM2.5 energy emissions over total PM2.5 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of PM2.5 energy emissions over total PM2.5 emissions 

Methodology 

Ratio between PM2.5 energy emissions and total PM2.5 emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p482]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_SIN_XXXX 

Indicator Name 

Share of PM2.5 industry emissions over total PM2.5 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of PM2.5 industry emissions over total PM2.5 emissions 

Methodology 

Ratio between PM2.5 industry emissions and total PM2.5 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p483]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_SRE _XXXX 

Indicator Name 

Share of PM2.5 residential emissions over total PM2.5 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of residential PM2.5 emissions over total PM2.5 emissions 

Methodology 

Ratio between residential PM2.5 emissions and total PM2.5 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p484]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_STRA_ XXXX 

Indicator Name 

Share of PM2.5 transport emissions over total PM2.5 emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of PM2.5 transport emissions over total PM2.5 emissions 

Methodology 

Ratio between PM2.5 transport emissions and total PM2.5 emissions 

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p485]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Share of emissions per sector 

Attribute ID 

EM_PM2_SWA_XXXX 

Indicator Name 

Share of PM2.5 waste emissions over PM2.5 total emissions  

Units 

% 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Indicator description  

Share of PM2.5 waste emissions over total PM2.5 emissions 

Methodology 

Ratio between PM2.5 waste emissions and total PM2.5 emissions  

Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020, 2022 

Uncertainties & Best practices  
```

### [D6-p486]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Emissions per capita 

Attribute ID 

EM_CO2_PEC_XXXX 

Indicator Name 

CO2 emissions per capita  

Units 

ton year-1 inhabitant-1 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets).  

https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

CO2 emissions per capita  

Methodology 

Ration between CO2 emissions and total population in the urban centre. 

Methodology Short 

Ratio 
```

### [D6-p487]

```text
Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  
```

### [D6-p488]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Emissions per capita 

Attribute ID 

EM_GHG_PEC_XXXX 

Indicator Name 

GHG emissions per capita  

Units 

ton year-1 inhabitant-1 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

GHG emissions per capita  

Methodology 

Ration between GHG emissions and total population in the urban centre. 
```

### [D6-p489]

```text
Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  
```

### [D6-p490]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Emissions per capita 

Attribute ID 

EM_NOX_PEC_XXXX 

Indicator Name 

NOX emissions per capita  

Units 

ton year-1 inhabitant-1 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

NOX emissions per capita  

Methodology 

Ration between NOX emissions and total population in the urban centre. 
```

### [D6-p491]

```text
Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  
```

### [D6-p492]

```text
Indicator thematic area 

Emissions 

Indicator Group 

Emissions per capita 

Attribute ID 

EM_PM2_PEC_XXXX 

Indicator Name 

PM 2.5 emissions per capita  

Units 

ton year-1 inhabitant-1 

Data Source 

EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database, a 
collaboration between the European Commission, Joint Research Centre (JRC), the International 
Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES 
version 8.0, (2023) European Commission, JRC (Datasets). 
https://edgar.jrc.ec.europa.eu/report_2023, https://edgar.jrc.ec.europa.eu/dataset_ghg80 

EDGAR v8.1 air pollutant emissions: https://edgar.jrc.ec.europa.eu/dataset_ap81  

Crippa, M., Guizzardi, D., Pagani, F., Schiavina, M., Melchiorri, M., Pisoni, E., Graziosi, F., Muntean, M., 
Maes, J., Dijkstra, L., Van Damme, M., Clarisse, L., and Coheur, P.: Insights into the spatial 
distribution of global, national, and subnational greenhouse gas emissions in the Emissions 
Database for Global Atmospheric Research (EDGAR v8.0), Earth Syst. Sci. Data, 16, 2811–
2830, doi:10.5194/essd-16-2811-2024, 2024.   

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

PM 2.5 emissions per capita  

Methodology 

Ration between PM 2.5 emissions and total population in the urban centre. 
```

### [D6-p493]

```text
Methodology Short 

Ratio 

Temporal Coverage 

1975, 1990, 2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  
```

### [D6-p494]

```text
Indicator Group 

Emissions 

Indicator Type 

Concentrations 

Indicator Code 

EM_PM2_CON_XXXX 

Indicator Name 

PM2.5 population weighted average concentrations 

Units 

µg/m3 

Data Source 

Shen, S. Li, C. van Donkelaar, A. Jacobs, N. Wang, C. Martin, R. V.: Enhancing Global Estimation of 
Fine Particulate Matter Concentrations by Including Geophysical a Priori Information in Deep 
Learning. (2024) ACS ES&T Air. DOI: 10.1021/acsestair.3c00054 
https://pubmed.ncbi.nlm.nih.gov/38751607/  

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Yearly population weighted average PM2.5 concentrations 

Methodology 

Estimated annual ground-level fine particulate matter (PM2.5) for 2000-2020 as provided at 
https://sites.wustl.edu/acag/datasets/surface-pm2-5/#V6.GL.02. The dataset is produced  

combining Aerosol Optical Depth (AOD) retrievals from the NASA MODIS, MISR, SeaWIFS, and 
VIIRS with the GEOS-Chem chemical transport model, and subsequently calibrating to global 
ground-based observations using a residual Convolutional Neural Network (CNN). Dataset version 
V6.GL.02.02. The dataset (at 1km resolution) is overlapped with the GHSL 1km global population 
(GHS_POP_GLOBE_R2023A) and the UCDB, to compute population weighted PM2.5 
concentrations. 

Methodology Short 
```

### [D6-p495]

```text
Modelled 

Temporal Coverage 

2000, 2005, 2010, 2015, 2020 

Uncertainties & Best practices  
```

### [D6-p496]

```text
Indicator Group 

Emissions 

Indicator Type 

Mortality 

Indicator Code 

EM_PM2_MOR_XXXX 

Indicator Name 

Premature deaths due to PM2.5 concentrations 

Units 

Number of premature deaths 

Data Source 

WHO mortality database: 

https://www.who.int/data/data-collection-tools/who-mortality-database 

Murray, C.J.L. et al., 2020. Global burden of 87 risk factors in 204 countries and territories, 1990 
- 2013;2019: a systematic analysis for the Global Burden of Disease Study 2019. The Lancet 
396:1223-1249. 

https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30752-2/fulltext  

Belis, C.A., Matkovic, V., Ballocci, M., Jevtic, M., Millo, G., Mata, E., Van Dingenen, R., 2023. 
Assessment of health impacts and costs attributable to air pollution in urban areas using two 
different approaches. A case study in the Western Balkans. Environment International 182, 
108347. https://doi.org/10.1016/j.envint.2023.108347 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

PM2.5 related premature deaths 

Methodology 

Estimation of the premature deaths according to integrated exposure response curves (IER) from 
the Global Burden of Disease methodology (Murray et al., 2020) as implemented in the JRC FAst 
Scenario Screening Tool (FASST, Belis et al., 2023) 
```

### [D6-p497]

```text
Premature deaths attributable to PM2.5 were estimated starting from PM2.5 concentrations, city 
population and country mortality rates from WHO mortality database. 

Methodology Short 

Modelled 

Temporal Coverage 

2000, 2020 

Uncertainties & Best practices  
```

### [D6-p498]

```text
2.9.10 Natural Systems 

Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_TPA_PER_ XXXX 

Indicator Name 

Share of Terrestrial Protected Areas  

Units 

% 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

Share of the urban center area covered by terrestrial protected areas over the total urban center 
area.  

Methodology 

Share of the urban center area covered by terrestrial protected areas. The protected areas were 
overlapped with the urban centers to calculate total area overlapping.  

Methodology Short 

Spatial Join, ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p499]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_MPA_PER_ XXXX 

Indicator Name 

Share of Marine Protected Areas  

Units 

% 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

Share of the urban center area covered by marine protected areas over the total urban center 
area.  

Methodology 

Share of the urban center area covered by marine protected areas. The protected areas were 
overlapped with the urban centers to calculate total area overlapping.  

Methodology Short 

Spatial Join, ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The results may differ from V1.0, while the methodology has not change, the indicator has been 
recalculated fixing a bug in the algorithm. 
```

### [D6-p500]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_TPA_NAM_ XXXX 

Indicator Name 

Name of Terrestrial Protected Areas  

Units 

Categorical 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

List of the names of the terrestrial protected areas overlaying the urban center area.  

Methodology 

The protected areas were overlaid with the urban centers to list the names of the protected 
areas.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p501]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_MPA_NAM_ XXXX 

Indicator Name 

Name of Marine Protected Areas  

Units 

Categorical 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

List of the names of the marine protected areas overlaying the urban center area.  

Methodology 

The protected areas were overlaid with the urban centers to list the names of the protected 
areas.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p502]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_TPA_DES_ XXXX 

Indicator Name 

Designation of Terrestrial Protected Areas  

Units 

Categorical 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

List of the terrestrial protected areas designation overlaying the urban center area.  

Methodology 

The protected areas were overlaid with the urban centers to list the designations of the protected 
areas.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p503]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Protected areas 

Attribute ID 

NS_MPA_DES_ XXXX 

Indicator Name 

Designation of Marine Protected Areas  

Units 

Categorical 

Data Source 

UNEP-WCMC and IUCN (2024), Protected Planet: The World Database on Protected Areas (WDPA) 
[Online], May 2024, Cambridge, UK: UNEP-WCMC and IUCN. Available 
at: www.protectedplanet.net. Download data 19/06/2024 

Indicator description  

List of the marine protected areas designation overlaying the urban center area.  

Methodology 

The protected areas were overlaid with the urban centers to list the designations of the protected 
areas.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p504]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_BIO_ XXXX 

Indicator Name 

Biointegrity transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of biointegrity transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the biointegrity transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p505]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_GWA_ XXXX 

Indicator Name 

Groundwater transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of groundwater transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the groundwater transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p506]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_NIT_ XXXX 

Indicator Name 

Nitrogen transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of nitrogen transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the nitrogen transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p507]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_PHO_ XXXX 

Indicator Name 

Phosphorus transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of phosphorus transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the phosphorus transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p508]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_P25_ XXXX 

Indicator Name 

PM2.5 transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of PM2.5 transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the PM2.5 transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p509]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_SLR_ XXXX 

Indicator Name 

Sea level rise transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of sea level rise transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the sea level rise transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p510]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_SWA_ XXXX 

Indicator Name 

Surface water transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of surface water transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the surface water transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p511]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_WET_ XXXX 

Indicator Name 

Wet bulb temperature transgression  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Number of wet bulb transgressions inside the urban center  

Methodology 

Zonal statistics (sum) of the wet bulb transgression layer. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p512]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_MIN_ XXXX 

Indicator Name 

Minimum number of total transgressions  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Minimum number of total transgressions inside the urban center  

Methodology 

Zonal statistics (min) of the total transgression layer. 

Methodology Short 

Zonal statistics (min) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p513]

```text
Indicator thematic area 

Natural Systems 

Indicator group 

Earth Boundaries System 

Attribute ID 

NS_ESB_MAX_ XXXX 

Indicator Name 

Maximum number of total transgressions  

Units 

Number of transgressions 

Data Source 

Rockström, J., Gupta, J., Qin, D. et al. Safe and just Earth system boundaries. Nature 619, 102–
111 (2023). https://doi.org/10.1038/s41586-023-06083-8 

Abrams, Jesse (2022). Transgression map. figshare. Dataset. 
https://doi.org/10.6084/m9.figshare.20079200.v2  

Indicator description  

Maximum number of total transgressions inside the urban center  

Methodology 

Zonal statistics (max) of the total transgression layer. 

Methodology Short 

Zonal statistics (max) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p514]

```text
2.9.11 Health 

Indicator thematic area 

Health 

Indicator group 

Number of facilities 

Attribute ID 

HL_FCL_HOS_XXXX 

Indicator Name 

Number of hospitals 

Units 

Units of facilities 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Indicator description  

Number of health facilities (hospitals) in the urban center. 

Methodology 

Zonal count of the points and polygons. Point and polygon data are compared to exclude 
duplicates; any feature class which attribute contains the word ‘hospital’ is reclassified as 
hospital facility.  

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2024 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p515]

```text
Indicator thematic area 

Health 

Indicator group 

Number of facilities 

Attribute ID 

HL_FCL_PHA_XXXX 

Indicator Name 

Number of pharmacies 

Units 

Units of facilities 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Indicator description  

Number of health facilities (pharmacies) in the urban center. 

Methodology 

Zonal count of the points and polygons. Point and polygon data are compared to exclude 
duplicates; any feature class which attribute contains the word ‘pharmacy’ but not ‘hospital’ is 
reclassified as pharmacy facility.  

Methodology Short 

Zonal Statistics (count) 

Temporal Coverage 

2024 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p516]

```text
Indicator thematic area 

Health 

Indicator group 

Number of facilities per capita 

Attribute ID 

HL_FPC_HOS_XXXX 

Indicator Name 

Number of hospitals per capita 

Units 

Number of facilities per 1000000 inhabitants 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Number of health facilities (hospitals) per capita in the urban center. 

Methodology 

Ratio between the number of facilities and total population in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p517]

```text
Indicator thematic area 

Health 

Indicator group 

Number of facilities per capita 

Attribute ID 

HL_FPC_PHA_XXXX 

Indicator Name 

Number of pharmacies per capita 

Units 

Number of facilities per 1000000 inhabitants 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Number of health facilities (pharmacies) per capita in the urban center. 

Methodology 

Ratio between the number of facilities and total population in the urban center. 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p518]

```text
Indicator thematic area 

Health 

Indicator group 

Facilities density 

Attribute ID 

HL_FDE_HOS_XXXX 

Indicator Name 

Hospitals density 

Units 

Units of facilities per squared kilometer 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Indicator description  

Number of health facilities (hospitals) per urban center area. 

Methodology 

Ratio between the number of facilities and the total area of the urban center (in squared 
kilometers). 

Methodology Short 

Ratio 

Temporal Coverage 

2024 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p519]

```text
Indicator thematic area 

Health 

Indicator group 

Facilities density 

Attribute ID 

HL_FDE_PHA_XXXX 

Indicator Name 

Pharmacies density 

Units 

Units of facilities per squared kilometer 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Indicator description  

Number of health facilities (pharmacies) per urban center area. 

Methodology 

Ratio between the number of facilities and the total area of the urban center (in squared 
kilometers). 

Methodology Short 

Ratio 

Temporal Coverage 

2024 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p520]

```text
Indicator thematic area 

Health 

Indicator group 

Population with access to facilities  

Attribute ID 

HL_POP_HOS_XXXX 

Indicator Name 

Population with access to hospitals  

Units 

Number of inhabitants 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Population living within a kilometer buffer of a hospital facility, inside the urban center. 

Methodology 

Zonal statistics (sum) of the population within a 1 km buffer of a hospital facility, inside the 
urban center. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p521]

```text
Indicator thematic area 

Health 

Indicator group 

Population with access to facilities  

Attribute ID 

HL_POP_PHA_XXXX 

Indicator Name 

Population with access to pharmacies  

Units 

Number of inhabitants 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Population living within a kilometer buffer of a pharmacy facility, inside the urban center. 

Methodology 

Zonal statistics (sum) of the population within a 1 km buffer of a pharmacy facility, inside the 
urban center. 

Methodology Short 

Zonal statistics (sum) 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p522]

```text
Indicator thematic area 

Health 

Indicator group 

Share of population with access to facilities  

Attribute ID 

HL_SHP_HOS_XXXX 

Indicator Name 

Share of population with access to hospitals  

Units 

% 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Share of population living within a kilometer buffer of a hospital facility, inside the urban center 
over total urban centre population. 

Methodology 

Ratio 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p523]

```text
Indicator thematic area 

Health 

Indicator group 

Share of population with access to facilities  

Attribute ID 

HL_SHP_PHA_XXXX 

Indicator Name 

Share of population with access to pharmacies  

Units 

% 

Data Source 

https://www.healthsites.io/map 

Downloaded on 27/06/2024 

World.zip (last update at: Tue Jun 25 2024 00:00:03 GMT+0200 (Central European Summer 
Time)) 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Share of population living within a kilometer buffer of a pharmacy facility, inside the urban 
center over total urban centre population. 

Methodology 

Ratio 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  

The data is derived from OSM. OSM limitations, completeness and accuracy are inherited.  
```

### [D6-p524]

```text
2.9.12 Water 

Indicator thematic area 

Water 

Indicator group 

Groundwater 

Attribute ID 

WA_GWR_GWB_XXXX 

Indicator Name 

Basin Type 

Units 

Categorical 

Data Source 

RICHTS, A., STRUCKMEIER, W. & ZAEPKE, M. (2011): WHYMAP and the Groundwater Resources of 
the World 1:25,000,000. In: Jones J. (Eds.): Sustaining Groundwater Resources. International Year 
of Planet Earth; Springer. doi: 10.1007/978-90-481-3426-7_10 

Indicator description  

Groundwater basin type  

Methodology 

Spatial join of the WHYMAP groundwater recharge type layer with the urban centers. If more than 
one aquifer unit overlays the urban center, the greater area covered by the join in considered to 
classify the aquifers of the urban centers.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p525]

```text
Indicator thematic area 

Water 

Indicator group 

Groundwater 

Attribute ID 

WA_GWR_GWR_XXXX 

Indicator Name 

Groundwater recharge  

Units 

Categorical 

Data Source 

RICHTS, A., STRUCKMEIER, W. & ZAEPKE, M. (2011): WHYMAP and the Groundwater Resources of 
the World 1:25,000,000. In: Jones J. (Eds.): Sustaining Groundwater Resources. International Year 
of Planet Earth; Springer. doi: 10.1007/978-90-481-3426-7_10 

Indicator description  

Groundwater recharge classification  

Methodology 

Spatial join of the WHYMAP groundwater recharge type layer with the urban centers. If more than 
one aquifer unit overlays the urban center, the greater area covered by the join in considered to 
define the aquifers’ recharge of the urban centers.  

Recharge is defined as: 

Major Groundwater Basins  Complex Hydrogeological Structures  

very high (> 300)  
very high (> 300)  

high (100 - 300)  
high (100 - 300)  

medium (20 - 100)  
medium (20 - 100)  

low (2 - 20)  
low - very low (< 20)  

very low (< 2)  
Local and Shallow Aquifers  

very high - high (> 100)  

medium - very low (< 100)  

Methodology Short 

Spatial Join 

Temporal Coverage 
```

### [D6-p526]

```text
2025 

Uncertainties & Best practices  
```

### [D6-p527]

```text
Indicator thematic area 

Water 

Indicator group 

Groundwater 

Attribute ID 

WA_GWS_SAL_XXXX 

Indicator Name 

Aquifer Salinity 

Units 

Boolean (True/False) 

Data Source 

RICHTS, A., STRUCKMEIER, W. & ZAEPKE, M. (2011): WHYMAP and the Groundwater Resources of 
the World 1:25,000,000. In: Jones J. (Eds.): Sustaining Groundwater Resources. International Year 
of Planet Earth; Springer. doi: 10.1007/978-90-481-3426-7_10 

Indicator description  

Groundwater salinity  

Methodology 

Spatial join of the WHYMAP groundwater salinity layer with the urban centers. If the aquifer unit 
overlays the urban center the aquifers are flag as saline (1), else as not saline (0). Saline is 
considered when TDS > 5 g/l  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p528]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_SHT_XXXX 

Indicator Name 

Sea surface height above the sea trend 

Units 

mm/year 

Data Source 

Global Ocean Mean Sea Level trend map from Observations Reprocessing. E.U. Copernicus Marine 
Service Information (CMEMS). Marine Data Store (MDS). DOI: 10.48670/moi-00238 (Accessed on 
26-July-2024) 

Indicator description  

Sea surface height above the sea trend 

Methodology 

Zonal statistics (average) of the Global Ocean Mean Sea Level trend layer 
(omi_climate_sl_global_regional_trends) using a 10 km buffer around the coastal urban centers. 
The data shows the mean sea level trends for the time period 1993 to 2023.  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2023 

Uncertainties & Best practices  
```

### [D6-p529]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_STT_XXXX 

Indicator Name 

Sea surface temperature trend 

Units 

°C/year 

Data Source 

Global Ocean Sea Surface Temperature trend map from Observations Reprocessing. E.U. 
Copernicus Marine Service Information (CMEMS). Marine Data Store (MDS). DOI: 10.48670/moi-
00243 (Accessed on 26-July-2024) 

Indicator description  

Sea surface temperature trend 

Methodology 

Zonal statistics (average) of the Global Ocean Sea Surface Temperature trend layer 
(global_omi_tempsal_sst_trend) using a 10 km buffer around the coastal urban centers. The data 
shows sea surface temperature trends for the time period 1993 to 2021.  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2021 

Uncertainties & Best practices  
```

### [D6-p530]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_SST_XXXX 

Indicator Name 

Sea surface temperature  

Units 

°C 

Data Source 

Global Ocean Physics Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00021 (Accessed on 20-September-2024) 

Indicator description  

Sea surface temperature 

Methodology 

Zonal statistics (average) of the Global Ocean Physics Reanalysis layer 
(cmems_mod_glo_phy_myint_0.083deg_P1M-m) using a 10 km buffer around the coastal urban 
centers. The data shows the yearly averaged sea surface temperature (selecting the depth level 0 
from the data) for each year.  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2021, 2022, 2023, 2024 

Uncertainties & Best practices  
```

### [D6-p531]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W01_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - January - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p532]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W02_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged – February - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p533]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W03_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - March - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p534]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W04_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - April - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p535]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W05_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - May - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p536]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W06_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - June - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p537]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W07_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - July - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p538]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W08_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - August - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p539]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W09_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - September - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p540]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W10_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - October - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p541]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W11_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - November - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p542]

```text
Indicator thematic area 

Water 

Indicator group 

Marine 

Attribute ID 

WA_MAR_W12_XXXX 

Indicator Name 

Wave significant height 

Units 

m 

Data Source 

Global Ocean Waves Reanalysis. E.U. Copernicus Marine Service Information (CMEMS). Marine 
Data Store (MDS). DOI: 10.48670/moi-00022 (Accessed on 29-September-2024) 

Indicator description  

Wave significant height (monthly averaged - December - data over the period 1993 to 2018) 

Methodology 

Zonal statistics (average) of the Global Ocean Waves Reanalysis layer 
(cmems_mod_glo_wav_my_0.2deg-climatology_P1M-m) using a 10 km buffer around the 
coastal urban centers. The data shows the monthly wave significant height averaged over the 
period 1993 to 2018 (included)  

Methodology Short 

Zonal statistics (average) 

Temporal Coverage 

2018 

Uncertainties & Best practices  
```

### [D6-p543]

```text
2.9.13 Infrastructure 

Indicator thematic area 

Infrastructures 

Indicator group 

Roads 

Attribute ID 

IN_ROA_LEN_XXXX 

Indicator Name 

Road length 

Units 

m 

Data Source 

Overture Maps Foundation, overturemaps.org. Accessed on 24/07/2024 

Indicator description  

Total road length inside the urban center  

Methodology 

Length calculation in local geographic projection and sum of the features’ length inside the urban 
center. 

Methodology Short 

Calculate geometry (length) 

Temporal Coverage 

2024 

Uncertainties & Best practices  
```

### [D6-p544]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Roads 

Attribute ID 

IN_ROA_DEN_XXXX 

Indicator Name 

Road density network 

Units 

m/m2 

Data Source 

Overture Maps Foundation, overturemaps.org. Accessed on 24/07/2024 

Indicator description  

Road network density, total road length inside the urban center divided by the urban center area 

Methodology 

Division between total length in the urban center and the urban center area.  

Methodology Short 

Division 

Temporal Coverage 

2024 

Uncertainties & Best practices  
```

### [D6-p545]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_ALL_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Critical Infrastructures Spatial Index is an index that spatially explicit indicates the coverage or 
lack of infrastructures.  

Methodology 

Sum of the CISI score by urban center, normalized by the maximum value for all urban centers 

Methodology Short 

Sum and normalization 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p546]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_ENE_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the energy sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the energy system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p547]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_TRA_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the transportation sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the transportation system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p548]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_WAT_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the water sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the water system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p549]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_WAS_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the waste sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the waste system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p550]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_TEL_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the telecommunications sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the telecommunications system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p551]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_HEA_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the health sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the health system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p552]

```text
Indicator thematic area 

Infrastructures 

Indicator group 

Critical Infrastructures Spatial Index (CISI) 

Attribute ID 

IN_CIS_EDU_XXXX 

Indicator Name 

Critical Infrastructures Spatial Index for the education sector 

Units 

dimensionless 

Data Source 

Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical 
infrastructure. Sci Data 9, 150 (2022). https://doi.org/10.1038/s41597-022-01218-4  

Data: A spatially-explicit harmonized global dataset of critical infrastructure (zenodo.org)  

Indicator description  

Sectorial CISI is an index that spatially explicit indicates the coverage or lack of infrastructures 
per sector.  

Methodology 

Area weighted mean subsector score for the education system. 

Methodology Short 

Area weighted average 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p553]

```text
2.9.14 Geography 

Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A01_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SLC" (Short, Low VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLC" (Short, Low VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SLC" (Short, 
Low VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p554]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A02_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SMC" (Short, Medium VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLC" (Short, Low VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SMC" (Short, 
Medium VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p555]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A03_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SHC" (Short, High VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLC" (Short, Low VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SHC" (Short, 
High VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p556]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A04_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TLC" (Tall, Low VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TLC" (Tall, Low VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TLC" (Tall, 
Low VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p557]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A05_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TMC" (Tall, Medium VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TMC" (Tall, Medium VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TMC" (Tall, 
Medium VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p558]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A06_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "THC" (Tall, High VPI, Cold) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "THC" (Tall, High VPI, Cold) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "THC" (Tall, 
High VPI, Cold) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p559]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A07_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SLD" (Short, Low VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLD" (Short, Low VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SLD" (Short, 
Low VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p560]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A08_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SMD" (Short, Medium VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SMD" (Short, Medium VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SMD" (Short, 
Medium VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p561]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A09_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SHD" (Short, High VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SHD" (Short, High VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SHD" (Short, 
High VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p562]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A10_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TLD" (Tall, Low VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TLD" (Tall, Low VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TLD" (Tall, 
Low VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p563]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A11_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TMD" (Tall, Medium VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TMD" (Tall, Medium VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TMD" (Tall, 
Medium VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p564]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A12_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "THD" (Tall, High VPI, Dry) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "THD" (Tall, High VPI, Dry) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "THD" (Tall, 
High VPI, Dry) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p565]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A13_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SLB" (Short, Low VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLB" (Short, Low VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SLB" (Short, 
Low VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p566]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A14_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SMB" (Short, Medium VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SMB" (Short, Medium VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SMB" (Short, 
Medium VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p567]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A15_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SHB" (Short, High VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SHB" (Short, High VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SHB" (Short, 
High VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p568]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A16_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TLB" (Tall, Low VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TLB" (Tall, Low VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TLB" (Tall, 
Low VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p569]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A17_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TMB" (Tall, Medium VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TMB" (Tall, Medium VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TMB" (Tall, 
Medium VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p570]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A18_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "THB" (Tall, High VPI, Both) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "THB" (Tall, High VPI, Both) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "THB" (Tall, 
High VPI, Both) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p571]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A19_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SLN" (Short, Low VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SLN" (Short, Low VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SLN" (Short, 
Low VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p572]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A20_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SMN" (Short, Medium VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SMN" (Short, Medium VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SMN" (Short, 
Medium VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p573]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A21_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "SHN" (Short, High VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "SMN" (Short, Medium VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "SMN" (Short, 
Medium VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p574]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A22_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TLN" (Tall, Low VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TLN" (Tall, Low VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TLN" (Tall, 
Low VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p575]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A23_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "TMN" (Tall, Medium VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "TMN" (Tall, Medium VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "TMN" (Tall, 
Medium VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p576]

```text
Indicator thematic area 

Geography 

Indicator group 

Biome 

Attribute ID 

GE_BIO_A24_XXXX 

Indicator Name 

Share of Urban Center area classified as Biome class "THN" (Tall, High VPI, Non-seasonal) 

Units 

% 

Data Source 

Higgins, S.I., Buitenwerf, R. and Moncrieff, G.R. (2016), Defining functional biomes and monitoring 
their change globally. Glob Change Biol, 22: 3583-3593. https://doi.org/10.1111/gcb.13367 

Indicator description  

Share of Urban Center area classified as Biome class "THN" (Tall, High VPI, Non-seasonal) 

Methodology 

Share of the total urban center area over the urban area classified as Biome class "THN" (Tall, 
High VPI, Non-seasonal) 

Methodology Short 

Ratio 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p577]

```text
Indicator thematic area 

Geography 

Indicator group 

Ecoregion 

Attribute ID 

GE_ECO_CLA_2025 

Indicator Name 

Ecoregion  

Units 

Categorical 

Data Source 

David M. Olson, Eric Dinerstein, Eric D. Wikramanayake, Neil D. Burgess, George V. N. Powell, 
Emma C. Underwood, Jennifer A. D'amico, Illanga Itoua, Holly E. Strand, John C. Morrison, Colby J. 
Loucks, Thomas F. Allnutt, Taylor H. Ricketts, Yumiko Kura, John F. Lamoreux, Wesley W. 
Wettengel, Prashant Hedao, Kenneth R. Kassem, Terrestrial Ecoregions of the World: A New Map 
of Life on Earth: A new global map of terrestrial ecoregions provides an innovative tool for 
conserving biodiversity, BioScience, Volume 51, Issue 11, November 2001, Pages 933–
938, https://doi.org/10.1641/0006-3568(2001)051[0933:TEOTWA]2.0.CO;2 

Indicator description  

Ecoregion in which the urban center is located. 

Methodology 

Overlap of urban centers with ecoregions layer, in the cases where the urban center falls into two 
or more ecoregions the ecoregion with greater overlapping area is selected. 

Methodology Short 

Overlap 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p578]

```text
Indicator thematic area 

Geography 

Indicator group 

Major River Basin  

Attribute ID 

GE_MRB_MAI_2025 

Indicator Name 

Main Major River Basin  

Units 

Categorical 

Data Source 

Major River Basins of the World (WB) https://datacatalog.worldbank.org/search/dataset/0041426  

Indicator description  

Main Major River Basin  

Methodology 

Overlap of urban centers with the major river basin layer, in the cases where the urban center 
falls into two or more ecoregions the ecoregion with greater overlapping area is selected. 

Methodology Short 

Overlap 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p579]

```text
Indicator thematic area 

Geography 

Indicator group 

Major River Basin  

Attribute ID 

GE_MRB_LIS_2025 

Indicator Name 

List of Major River Basin  

Units 

Categorical 

Data Source 

Major River Basins of the World (WB) https://datacatalog.worldbank.org/search/dataset/0041426  

Indicator description  

List of Major River Basin  

Methodology 

Overlap of urban centers with the major river basin layer and selection of all overlapping basins.  

Methodology Short 

Overlap 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p580]

```text
Indicator thematic area 

Geography 

Indicator group 

Elevation  

Attribute ID 

GE_ELV_AVG_2025 

Indicator Name 

Average Elevation  

Units 

m 

Data Source 

Copernicus GLO-90 dataset https://doi.org/10.5270/ESA-c5d3d65 

Indicator description  

Average elevation in the urban center  

Methodology 

Zonal statistics (avg) of the elevation layer. 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p581]

```text
Indicator thematic area 

Geography 

Indicator group 

Soil Class  

Attribute ID 

GE_SLC_MPC_2025 

Indicator Name 

Most probable soil class  

Units 

Categorical 

Data Source 

SoilGrids250m 2.0 - WRB classes and probabilities. 
https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/c4dc161c-d62d-11ea-a1a3-
292680b15169. Repository: https://files.isric.org/soilgrids/latest/data/wrb/MostProbable/ 

Accessed 25/09/2024 

Indicator description  

Zonal count of the most probable soil class layer. The soil class more present in the urban center 
is selected as the most probable soil class.  

Methodology 

Zonal statistics (count) of the most probable soil class. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p582]

```text
Indicator thematic area 

Geography 

Indicator group 

Soil Class  

Attribute ID 

GE_SLC_LST_2025 

Indicator Name 

List of most probable soil classes  

Units 

Categorical 

Data Source 

SoilGrids250m 2.0 - WRB classes and probabilities. 
https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/c4dc161c-d62d-11ea-a1a3-
292680b15169. Repository: https://files.isric.org/soilgrids/latest/data/wrb/MostProbable/ 

Accessed 25/09/2024 

Indicator description  

Zonal count of the most probable soil class layer. All soil classes present in the urban center are 
listed in the most probable soil classes list.  

Methodology 

Zonal statistics (count) of the most probable soil class. 

Methodology Short 

Zonal statistics (count) 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p583]

```text
2.9.15 Greenness 

Indicator thematic area 

Greenness 

Indicator group 

Tree Canopy Height 

Attribute ID 

GR_CTH_AVG_ XXXX 

Indicator Name 

Average Canopy Top Height in the built-up area  

Units 

m 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Lang, N., Jetz, W., Schindler, K. et al. A high-resolution canopy height model of the Earth. Nat Ecol 
Evol 7, 1778–1789 (2023). https://doi.org/10.1038/s41559-023-02206-6 

Indicator description  

Average Canopy Top Height in the built-up area 

Methodology 

Zonal statistics (average) of canopy top height layer, masked by a 300 m buffer of the GHS-
BUILT-S layer. 

Methodology Short 

Zonal statistics (avg) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p584]

```text
Indicator thematic area 

Greenness 

Indicator group 

Tree Canopy Height 

Attribute ID 

GR_CTH_STD_ XXXX 

Indicator Name 

Standard deviation Canopy Top Height in the built-up area  

Units 

m 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Lang, N., Jetz, W., Schindler, K. et al. A high-resolution canopy height model of the Earth. Nat Ecol 
Evol 7, 1778–1789 (2023). https://doi.org/10.1038/s41559-023-02206-6 

Indicator description  

Standard deviation Canopy Top Height in the built-up area 

Methodology 

Zonal statistics (standard deviation) of canopy top height layer, masked by a 300 m buffer of the 
GHS-BUILT-S layer. 

Methodology Short 

Zonal statistics (stdev) 

Temporal Coverage 

2020 

Uncertainties & Best practices  
```

### [D6-p585]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_AVG_GRN_ XXXX 

Indicator Name 

Mean greenness in the built-up area  

Units 

dimensionless 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Mean greenness (NDVI) in the built-up area (within a 300 m buffer of the built-up cells) 

Methodology 

Sequence of masking and zonal statistics. 300m buffering of the built-up domain, masking of the 
built-up grid with 3 years average NDVI (greater or equal than threshold); zonal statistics of the 
NDVI in the obtained mask. Thresholds for high greenness are estimated by UN-Habitat for agro-
ecological-zones, from a sample of 700 cities. Agro-ecological zone values are obtained by 
averaging observations within the cities in each zone. 

Methodology Short 

Zonal statistics (sum), zonal statistics (avg), mask 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 
```

### [D6-p586]

```text
Uncertainties & Best practices  
```

### [D6-p587]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_SQM_HGR_ XXXX 

Indicator Name 

Built-up area in the highest greenness area 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Total built-up area (within a 300 m buffer of the built-up cells and high greenness threshold) 

Methodology 

Sequence of masking and zonal statistics. 300m buffering of the built-up domain, masking of the 
built-up grid with 3 years average NDVI (greater or equal than threshold); zonal statistics of the 
built-up in the obtained mask. Thresholds for high greenness are estimated by UN-Habitat for 
agro-ecological-zones, from a sample of 700 cities. Agro-ecological zone values are obtained by 
averaging observations within the cities in each zone. 

Methodology Short 

Zonal statistics (sum), zonal statistics (avg), mask 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 
```

### [D6-p588]

```text
Uncertainties & Best practices  
```

### [D6-p589]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_SQM_LGR_ XXXX 

Indicator Name 

Built-up area in the lower greenness area 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Total built-up area (within a 300 m buffer of the built-up cells and low greenness threshold) 

Methodology 

Sequence of masking and zonal statistics. 300m buffering of the built-up domain, masking of the 
built-up grid with 3 years average NDVI (less or equal than threshold); zonal statistics of the 
built-up in the obtained mask. Thresholds for high greenness are estimated by UN-Habitat for 
agro-ecological-zones, from a sample of 700 cities. Agro-ecological zone values are obtained by 
averaging observations within the cities in each zone. 

Methodology Short 

Zonal statistics (sum), zonal statistics (avg), mask 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 
```

### [D6-p590]

```text
Uncertainties & Best practices  
```

### [D6-p591]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_SQM_GRN_ XXXX 

Indicator Name 

Built-up area in the greenness area 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Total built-up area in the greenness area.  

Methodology 

Sum of the built-up in the low and high greennes 

Methodology Short 

Sum 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p592]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_SHB_HGR_ XXXX 

Indicator Name 

Share of Built-up area in the high greenness area over total built-up area in the urban centre. 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Share of built-up area in the high greenness area.  

Methodology 

Ratio of the built-up in the high greenness and the total built-up of the urban centre.  

Methodology Short 

Ratio 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p593]

```text
Indicator thematic area 

Greenness 

Indicator group 

Greenness in the built-up 

Attribute ID 

GR_SHB_GRN_ XXXX 

Indicator Name 

Share of Built-up area in the greenness area over total built-up area in the urban centre. 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA  

Landsat Collection 2 Tier 1 Level 2 8-Day NDVI Composite courtesy of the U.S. Geological Survey  

United Nations Human Settlement Programme (UN-Habitat), Global Urban Indicators Database 
2024 

USGS Earth Resources Observation and Science (EROS) Center. (2021). Landsat 8 Level-2 Science 
Products. Landsat NDVI data from Landsat 8 mission. Retrieved from https://eros.usgs.gov/land-
cover-land-use/landsat-8-level-2-science-products 

Indicator description  

Share of built-up area in the greenness area.  

Methodology 

Ratio of the built-up in the greenness and the total built-up of the urban centre.  

Methodology Short 

Ratio 

Temporal Coverage 

1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025 

Uncertainties & Best practices  
```

### [D6-p594]

```text
2.10 GHS-UCDB indicator fact sheets – multi-temporal boundaries 

This section contains the individual indicator fact sheets organised by the 2 thematic domains 

2.10.1 General Characteristics 

Indicator thematic area 

General Characteristics 

Indicator Group 

Urban center Name 

Attribute ID 

GC_UCN_MAI_XXXX 

Indicator Name 

Urban center Main Name 

Units 

Dimensionless 

Data Source 

Open Street Maps  

GISCO 

WUP 2018 

Indicator description  

Name of the main city inside the urban center.  

Methodology 

The urban centres are named using an algorithm that automatically queries the GISCO, the full 
OpenStreetMap datasets and WUP 2018 (extended unpublished version, with point locations 
corrected through geocoding and reverse geocoding). 

Methodology Short 

Geoencoding 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p595]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban center Name 

Attribute ID 

GC_UCN_LIS_XXXX 

Indicator Name 

Urban center List Name 

Units 

Dimensionless 

Data Source 

Open Street Maps  

GISCO 

WUP 2018 

Indicator description  

List of names of the all cities inside the urban center.  

Methodology 

The urban centres are named using an algorithm that automatically queries the GISCO, the full 
OpenStreetMap datasets and WUP 2018 (extended unpublished version, with point locations 
corrected through geocoding and reverse geocoding). 

Methodology Short 

Geoencoding 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p596]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Country Name 

Attribute ID 

GC_CNT_GAD_XXXX 

Indicator Name 

Country Name 

Units 

Dimensionless 

Data Source 

GADM version 4.1, released on 16 July 2022 https://gadm.org/data.html  

Indicator description  

Country named based on GADM dataset 

Methodology 

Spatial join of the urban centers and the GADM country layer adapted for GHSL.  

Methodology Short 

Spatial Join 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p597]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Development 

Attribute ID 

GC_DEV_USR_XXXX 

Indicator Name 

UN SDG Region 

Units 

Categorical 

Data Source 

 UN https://unstats.un.org/sdgs/indicators/regional-groups/ 

Indicator description  

Country grouping in geographic regions based on the 2016 Sustainable Development Goals 
Report and the progress reports on the Millennium Development Goals. 

Methodology 

Join by attribute (by country) 

Methodology Short 

Join by attribute 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p598]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Development 

Attribute ID 

GC_DEV_WIG_XXXX 

Indicator Name 

World Bank Income Group 

Units 

Categorical 

Data Source 

The World Bank https://datahelpdesk.worldbank.org/knowledgebase/articles/906519  

Indicator description  

The World Bank income group classification provides a complete list of economies classified by 
income, region, and World Bank lending status. This table is updated to year 2022. 

Methodology 

Join by attribute (by country). 

Methodology Short 

Join by attribute 

Temporal Coverage 

2025 

Uncertainties & Best practices  
```

### [D6-p599]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban centre birth 

Attribute ID 

GC_UCB_YOB _XXXX 

Indicator Name 

Year of Birth 

Units 

year 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

European Commission, and Statistical Office of the European Union, 2021 
Applying the Degree of Urbanisation — A methodological manual to define cities, towns and rural 
areas for international comparisons — 2021 edition. Publications Office of the European Union, 
2021; ISBN 978-92-76-20306-3 
10.2785/706535 

Indicator description  

Indicates the year in the multitemporal series GHS-SMOD R2023A, the cells reach the conditions 
to be classified as urban centre. 

Methodology 

The methodology to classify the urban centres is described in “Applying the Degree of 
Urbanisation — A methodological manual to define cities, towns and rural areas for international 
comparisons —“. 

Methodology Short 

Modelled 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p600]

```text
The DEGURBA model considers data only from 1975 to 2030, cities born in 1975 should be 
considered as born in 1975 or earlier, and cities death in 2030 should be considered as death on 
2030 or later 
```

### [D6-p601]

```text
Indicator thematic area 

General Characteristics 

Indicator group 

Urban centre death 

Attribute ID 

GC_UCB_YOD _XXXX 

Indicator Name 

Year of Death 

Units 

year 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

European Commission, and Statistical Office of the European Union, 2021 
Applying the Degree of Urbanisation — A methodological manual to define cities, towns and rural 
areas for international comparisons — 2021 edition. Publications Office of the European Union, 
2021; ISBN 978-92-76-20306-3 
10.2785/706535 

Indicator description  

Indicates weather an urban centre is projected to be a urban centre in 2030 or ‘dies’ (doesn’t 
reach the conditions to be a urban centre) in 2030. 

Methodology 

The methodology to classify the urban centres is described in “Applying the Degree of 
Urbanisation — A methodological manual to define cities, towns and rural areas for international 
comparisons —". 

Methodology Short 

Modelled 

Temporal Coverage 

2025, 2030 

Uncertainties & Best practices  
```

### [D6-p602]

```text
The DEGURBA model considers data only from 1975 to 2030, cities born in 1975 should be 
considered as born in 1975 or earlier, and cities death in 2030 should be considered as death on 
2030 or later 
```

### [D6-p603]

```text
2.10.2 Multi-temporal GHSL 

Indicator thematic area 

Multi-temporal_GHSL 

Indicator group 

Point-in-time Area 

Attribute ID 

MT_UCA_KM2_XXXX 

Indicator Name 

Urban Centre Area 

Units 

Km2 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Urban Centre Area 

Methodology 

Calculate area (geometry) of the urban centre. 

Methodology Short 

Area 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  
```

### [D6-p604]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Population 

Attribute ID 

MT_POP_TOT_XXXX 

Indicator Name 

Total Population 

Units 

Number of inhabitants 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid multi-temporal (1975-2030).European Commission, 
Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description (xxx max words) 

Total population allocated inside of the Multi-temporal UC in number of inhabitants. The 
boundaries of the urban centre are calculated dynamically per each epoch based on its 
population, not anchored in 2025. 

Methodology 

Zonal sum of the GHS-POP R2023A layer pixel values inside the multi-temporal urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p605]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Built-up 

Attribute ID 

MT_BUS_TOT_XXXX 

Indicator Name 

Total Built-up surface 

Units 

m2 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and 
Landsat, multitemporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Total built-up surface of the UC in square meters. The boundaries of the urban centre are 
calculated dynamically per each epoch based on its population, not anchored in 2025.  

Methodology 

Zonal sum of the GHS-BUILT-S R2023A pixel values inside the multi-temporal urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p606]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Built-up 

Attribute ID 

MT_BUV_TOT_XXXX 

Indicator Name 

Total Built-up volume 

Units 

m3 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, multitemporal (1975-2030).European Commission, Joint Research 
Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Indicator description  

Total built-up volume of the UC in square meters. The boundaries of the urban centre are 
calculated dynamically per each epoch based on its population, not anchored in 2025.  

Methodology 

Zonal sum of the GHS-BUILT-V R2023A pixel values inside the multi-temporal urban centre. 

Methodology Short 

Zonal Statistics (sum) 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p607]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Population 

Attribute ID 

MT_POP_DEN_XXXX 

Indicator Name 

Population density 

Units 

Number of inhabitants per km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description (xxx max words) 

Population density in the Multi-temporal UC 

Methodology 

Zonal sum of the GHS-POP R2023A layer pixel values inside the multi-temporal urban centre 
divided by its area. 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p608]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Built-up 

Attribute ID 

MT_BPC_TOT_XXXX 

Indicator Name 

Total built-up per capita 

Units 

m2 per inhabitant 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
Multi-temporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total built-up area per capita in the multi-temporal urban centre  

Methodology 

Total built-up area divided by total population 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p609]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Built-up 

Attribute ID 

MT_BUV_SHR_XXXX 

Indicator Name 

Share of built-up volume being residential 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 
GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel2, 
Landsat, and global DEM data, Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283, 
doi:10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283 

Indicator description  

Share of residential built-up volume over total built-up volume in the multi-temporal urban 
centre  

Methodology 

Residential built-up volume divided by total built-up volume. 1 - GHS-BUILT-V-NRES R2023A/ 
GHS-BUILT-V R2023A 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p610]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Point-in-time Built-up 

Attribute ID 

MT_BUS_SHT_XXXX 

Indicator Name 

Built-up fraction (Share of UC area being built-up) 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
Multi-temporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Share of total built-up surface over UC area in the multi-temporal urban centre  

Methodology 

Total built-up surface divided by UC area 

Methodology Short 

Division 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p611]

```text
Indicator thematic area 

1. Multi-temporal GHSL 

Indicator Group 

Multi-temporal change Population 

Attribute ID 

MT_POP_DIF_XXXX_YYYY 

Indicator Name 

Population relative change 

Units 

% 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total population change over five years as percentage in the multi-temporal urban centre 

Methodology 

Population relative percentage difference (pop t+5 – pop t)/pop t 

Methodology Short 

Relative percentage difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p612]

```text
Indicator thematic area 

Multi-temporal GHSL 

Indicator Group 

Multi-temporal change Population 

Attribute ID 

MT_PDY_DIF_XXXX_YYYY 

Indicator Name 

Population density change 

Units 

Number of inhabitants per km2 

Data Source 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Population density change over five years as delta inhabitants perkm2 in the multi-temporal 
urban centre 

Methodology 

Population density difference pop t+5/area t+5 - pop t/area t 

Methodology Short 

Difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p613]

```text
Indicator thematic area 

1. Multi-temporal GHSL 

Indicator Group 

Multi-temporal change Area 

Attribute ID 

MT_XST_D30_XXXX_YYYY 

Indicator Name 

Change in UC extent 

Units 

% 

Data Source 

Schiavina M., Melchiorri M., Pesaresi M. (2023): 
GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation 
methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-
2030). European Commission, Joint Research Centre (JRC) 
PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea-9bde-563437a6e2ba, 
doi:10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA 

Indicator description  

Total UC area change over five years as percentage in the multi-temporal urban centre 

Methodology 

UC Area relative percentage difference (area t+5 – area t)/area t 

Methodology Short 

Relative percentage difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p614]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Multi-temporal change Built-up 

Attribute ID 

MT_BPC_DIF_XXXX_YYYY 

Indicator Name 

Built-up per capita change 

Units 

m2 per inhabitant 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
Multi-temporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Schiavina M., Freire S., Carioli A., MacManus K. (2023): 
GHS-POP R2023A - GHS population grid Multi-temporal (1975-2030).European Commission, Joint 
Research Centre (JRC) 
PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-8f40-c41da8332cfe, 
doi:10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE 

Indicator description  

Total built-up surface per capita change over five years as delta m2 per inhabitant in the multi-
temporal urban centre  

Methodology 

Built-up per capita difference BUS t+5/pop t+5 - BUS t/pop t 

Methodology Short 

Difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p615]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Multi-temporal change Built-up 

Attribute ID 

MT_BUF_DIF_XXXX_YYYY 

Indicator Name 

Change in the fraction of built-up surface 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
Multi-temporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Share of total built-up surface over UC area change over five years as delta percentage in the 
multi-temporal urban centre  

Methodology 

Built-up fraction difference BUS t+5/area t+5 - BUS t/area t 

Methodology Short 

Difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p616]

```text
Indicator thematic area 

Multi-temporal_GHSL 

Indicator Group 

Multi-temporal change Built-up 

Attribute ID 

MT_BUS_DIF_XXXX_YYYY 

Indicator Name 

Built-up surface relative change 

Units 

% 

Data Source 

Pesaresi M., Politis P. (2023): 

GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, 
Multi-temporal (1975-2030) European Commission, Joint Research Centre (JRC) 

PID: http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea, 
doi:10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA 

Indicator description  

Total built-up surface change over five years as percentage in the multi-temporal urban centre 

Methodology 

Built-up surface relative percentage difference (BUS t+5 – BUS t)/BUS t 

Methodology Short 

Relative percentage difference 

Temporal Coverage 

1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030 

Uncertainties & Best practices  

Please mind that the boundaries of UC in this data stream change according to the population in 
each year. Such data is particularly adapted for population weighted metrics (i.e. per capita) and 
for population density. 
```

### [D6-p617]

```text
2.11 Input Data 

The input data are data from the GHSL P2023 release, plus the corresponding input data for each of 
the indicators contained in section 2.9 and 2.10. 

2.12 Technical Details 

Authors: Marí Rivero Inés, Melchiorri Michele, Florio Pietro, Schiavina Marcello, Krasnodębska 
Katarzyna, Politis Panagliotis, Uhl Johannes, Pesaresi Martino, Maffenini Luca, Sulis Patrizia, Crippa 
Monica, Guizzardi Diego, Pisoni Enrico, Belis Claudio, Oom Duarte, Branco Alfredo, Mwaniki Dennis, 
Kochulem Edwin, Githira Daniel, Carioli Alessandra, Ehrlich Daniele, Tommasi Pierpaolo, Thomas 
Kemper, Lewis Dijkstra.  

Product name: GHS_UCDB_GLOBE_R2024 

Spatial extent: Global 

Temporal extent: from 1975 to 2030, 5 years interval  

Coordinate System: World Mollweide (EPSG: 54009) 

Spatial resolution available: - 

2.12.1 GHS_UCDB_GLOBE_R2024 

Data organisation: Geopackage (.gpkg) database with vector layer of Urban Centre entities boundaries 
(polygons) and centroids (points) and spreadsheet (xlsx) 

Records: 11,422 urban centres 

Attributes: 

• 
2.9.1 General Characteristics; 

• 
2.9.2 GHSL 

• 
2.9.3 Socioeconomic 

• 
2.9.4 Land Use Land Cover 

• 
2.9.5 Exposure 

• 
0  
```

### [D6-p618]

```text
• 
Hazards 

• 
2.9.7 SDGs 

• 
0  
```

### [D6-p619]

```text
• 
Climate 

Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_CUR_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (reanalysis data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (reanalysis data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  

• 
2.9.9 Emissions 

• 
2.9.10 Natural Systems 

• 
2.9.11 Health  

• 
2.9.12 Water  

• 
2.9.13 Infrastructure 

• 
2.9.14 Geography 
```

### [D6-p620]

```text
• 
2.9.15 Greenness 

2.12.2 GHS_UCDB_REGION_GLOBE_R2024A 

Data organisation: Geopackage (.gpkg) database with vector layer of Urban Centre entities boundaries 
(polygons), centroids (points), and tables (csv) 

Records: in individual .gpkg and tables by region  

Regions :  

Region 
UC Count 
Australia and New Zealand 
44 
Central and Southern Asia 
2895 
Eastern and South-Eastern Asia 
3117 
Europe 
1165 
Latin America and the Caribbean 
1089 
Northern Africa and Western Asia 
1038 
Northern America 
398 
Oceania 
18 
Sub-Saharan Africa 
1658 

Attributes: 

• 
2.9.1 General Characteristics; 

• 
2.9.2 GHSL 

• 
2.9.3 Socioeconomic 

• 
2.9.4 Land Use Land Cover 

• 
2.9.5 Exposure 

• 
0  
```

### [D6-p621]

```text
• 
Hazards 

• 
2.9.7 SDGs 

• 
0  
```

### [D6-p622]

```text
• 
Climate 

Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_CUR_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (reanalysis data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (reanalysis data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  

• 
2.9.9 Emissions 

• 
2.9.10 Natural Systems 

• 
2.9.11 Health  

• 
2.9.12 Water  

• 
2.9.13 Infrastructure 

• 
2.9.14 Geography 
```

### [D6-p623]

```text
• 
2.9.15 Greenness 

2.12.3 GHS_UCDB_THEME_GLOBE_R2024A 

Data organisation: Geopackage (.gpkg) database with vector layer of Urban Centre entities boundaries 
(polygons) and centroids (points). 

Records: 11,422 urban centres 

Attributes: in individual csv and xlsx by thematic domain 

• 
2.9.1 General Characteristics; 

• 
2.9.2 GHSL 

• 
2.9.3 Socioeconomic 

• 
2.9.4 Land Use Land Cover 

• 
2.9.5 Exposure 

• 
0  
```

### [D6-p624]

```text
• 
Hazards 

• 
2.9.7 SDGs 

• 
0  
```

### [D6-p625]

```text
• 
Climate 

Indicator thematic area 

Climate 

Indicator group 

Bioclimatic indicators 

Attribute ID 

CL_B01_CUR_XXXX 

Indicator Name 

Annual Mean Temperature in the decade (reanalysis data) 

Units 

°C 

Data Source 

Wouters, H., (2021): Global bioclimatic indicators from 1979 to 2018 derived from reanalysis. 
Copernicus Climate Change Service (C3S) Climate Data Store (CDS). 
DOI: 10.24381/cds.bce175f0 (Accessed on 07-August-2024) 

Indicator description  

Annual Mean Temperature in the decade (reanalysis data) 

Methodology 

Zonal average of the Annual Mean Temperature pixel values touching the urban center. 

Methodology Short 

Zonal Statistics (avg) 

Temporal Coverage 

1970, 1980, 1990, 2000, 2010 

Uncertainties & Best practices  

• 
2.9.9 Emissions 

• 
2.9.10 Natural Systems 

• 
2.9.11 Health  

• 
2.9.12 Water  

• 
2.9.13 Infrastructure 

• 
2.9.14 Geography 
```

### [D6-p626]

```text
• 
2.9.15 Greenness 

2.12.4 GHS_UCDB_CONTRIBUTIONS_R2024A 

Data organisation: tables (csv, xlsx) 

Attributes: 

The UCDB_CONTRIBUTIONS is a living dataset, therefore the entries will be updated with attributes 
and corresponding factsheet in individual folders.  

At the time of the first release, this section contains: 

• 
Completeness of Built-up Area in OpenStreetMap 

• 
Completeness of Road Length in OpenStreetMap 

The first dataset is contributed by: 

João Porto de Albuquerque; Professor (Chair) in Urban Analytics, Deputy Director of the Urban Big 
Data Centre; 

Benjamin Herfort; Heidelberg Institute for Geoinformation Technology, Heidelberg, Germany 

2.12.5 GHS_UCDB_MTUC_GLOBE_R2024A 

Data organisation: Geopackage (.gpkg) database with vector layer of Urban Centre entities boundaries 
(polygons) and centroids (points). 

Records: 11,422 urban centres 

Attributes:  

• 
2.10.1 General Characteristics 

• 
2.10.2 Multi-temporal GHSL 
```

#### [D6-T3] TABLE — page 626
title_verbatim:
```text
Table 3 - Technical details of the datasets in GHS-UCDB_GLOBE_R2024A 
```
table_flags: [AMBIGUOUS: header extent — no numeric rows; first printed line taken as header]; 1 wrapped printed lines joined into their row's cells (line pitch tighter than the table's row pitch; text verbatim, joined with a space)

|  | GHS_SMOD_GLOBE_R2023A |  |
|---|---|---|
| ID | Description | Resolution |
|  |  | (Projection) |
|  | Urban centre database fixed |  |
|  | boundaries, all thematic |  |
| GHS_UCDB_GLOBE_R2024 | domains and all records | World Mollweide |
|  | File format: gpkg, csv, xlsx | ESRI:54009 |
|  | Urban centre database fixed |  |
| GHS_UCDB_REGION_GLOBE_R2024A | boundaries, Region records |  |
|  | and full attributes |  |


### [D6-p627]

```text
GHS_UCDB_THEME_GLOBE_R2024A 

GHS_UCDB_CONTRIBUTIONS_R2024A 

GHS_UCDB_MTUC_GLOBE_R2024A 

2.13 How to cite 

Dataset: 

File format: gpkg, csv, xlsx 

Urban centre database fixed 
boundaries, single thematic 
domains and full attributes 
File format: gpkg, csv, xlsx 

Urban centre database fixed 
boundaries, single attribute 
and full records 
File format: csv 

Urban centre database 
multi-temporal boundaries, 
all thematic domains and all 
records 
File format: gpkg, csv, xlsx 

Marí Rivero Inés, Melchiorri Michele, Florio Pietro, Schiavina Marcello, Krasnodębska Katarzyna, Politis 
Panagliotis, Uhl Johannes, Pesaresi Martino, Maffenini Luca, Sulis Patrizia, Crippa Monica, 
Guizzardi Diego, Pisoni Enrico, Belis Claudio, Oom Duarte, Branco Alfredo, Mwaniki Dennis, Kochulem 
Edwin, Githira Daniel, Carioli Alessandra, Ehrlich Daniele, Tommasi Pierpaolo, Thomas Kemper, Lewis 
Dijkstra. Joint Research Centre (JRC) [Dataset] doi: 10.2905/1A338BE6-7EAF-480C-9664-
3A8ADE88CBCD 

Concept & Methodology: 

Melchiorri, Michele. "The global human settlement layer sets a new standard for global urban data 
reporting with the urban centre database." Frontiers in Environmental Science 10 (2022): 1003862. 
```

### [D6-p628]

```text
3 Conclusions 

The new release of the GHS-UCDB dataset, now presented as Stats in the City, marks a substantial 
improvement and update to the Urban Centre Database product within the GHSL Suite. This significant 
enhancement not only incorporates new data sources but also broadens the thematic scope, 
effectively integrating data from operational Copernicus Services. 

A notable feature of this dataset is its ability to offer user-specific delineation of urban centres, 
adapting to diverse uses and applications. This flexibility and comprehensiveness open up new 
opportunities for the creation of detailed urban centre profiles and multi-thematic studies on cities 
worldwide for broader analyses and more informed decision-making. 

Moreover, the introduction of a new contributors section within the dataset is a forward-thinking 
approach that encourages collaboration and community engagement. This feature enables 
continuous updates and the seamless integration of data from the user community, who can create 
new data for the urban centre spatial units. 
```

### [D6-p629]

```text
References 

Dijkstra, Lewis, Aneta J. Florczyk, Sergio Freire, Thomas Kemper, Michele Melchiorri, Martino 

Pesaresi, and Marcello Schiavina. 2021. “Applying the Degree of Urbanisation to the Globe: 
A New Harmonised Definition Reveals a Different Picture of Global Urbanisation.” Journal of 
Urban Economics 125:103312. https://doi.org/10.1016/j.jue.2020.103312. 
European Commission. Joint Research Centre. 2023. GHSL Data Package 2023. LU: Publications 

Office. https://data.europa.eu/doi/10.2760/098587. 
European Commission. Statistical Office of the European Union. 2021. “Applying the Degree of 

Urbanisation: A Methodological Manual to Define Cities, Towns and Rural Areas for 
International Comparisons : 2021 Edition.” LU: Publications Office of the European Union. 
https://data.europa.eu/doi/10.2785/706535. 
Florczyk, A. J., C. Corbane, D. Ehrlich, S. Freire, T. Kemper, L. Maffenini, M. Melchiorri, et al. 2019. 

GHSL Data Package 2019. JRC117104. Publications Office of the European Union. 
10.2760/729240. 
Melchiorri, Michele. 2022. “The Global Human Settlement Layer Sets a New Standard for Global 

Urban Data Reporting with the Urban Centre Database.” Frontiers in Environmental Science 
10 (October):1003862. https://doi.org/10.3389/fenvs.2022.1003862. 
Melchiorri, Michele, Sergio Freire, Marcello Schiavina, Aneta Florczyk, Christina Corbane, Luca 

Maffenini, Martino Pesaresi, et al. 2024. “The Multi-Temporal and Multi-Dimensional Global 
Urban Centre Database to Delineate and Analyse World Cities.” Scientific Data 11 (1): 82. 
https://doi.org/10.1038/s41597-023-02691-1. 
Melchiorri, Michele, Martino Pesaresi, Aneta J. Florczyk, Christina Corbane, and Thomas Kemper. 2019. 

“Principles and Applications of the Global Human Settlement Layer as Baseline for the Land 
Use Efficiency Indicator—SDG 11.3.1.” ISPRS International Journal of Geo-Information 8 (2): 
96. https://doi.org/10.3390/ijgi8020096. 
```

### [D6-p630]

[LIST/CONTENTS PAGE — transcribed verbatim; used as completeness checklist]

```text
List of Figures 

Figure 1 GHSL Data Anatomy and upstream GHSL products for the production of the GHS-UCDB .... 7 

Figure 2 Logical workflow for the delineation of urban centres spatial entities by applying to raster 
grids the population density, size and grid cell contiguity rules of the Degree of Urbanisation 
method. .................................................................................................................................................... 8 

Figure 3 - Schematic overview of subset schema to define urban centres from the GHSL SMOD 
entities workflow logic. “pop” represents the population abundance per grid cell; “pop_d” represents 
the population density on permanent land; “bu” represents the built-up share per grid cell; “bu_d” 
represents the built-up density on permanent land. “DENSITY ON LAND” process fill built-up cells on 
water with max between 50% and built-up share value and population on water with global 
average built-up per capita. (*) this procedure of enforcement logic allows the delineation of Urban 
Clusters Entities which contains by definition the Urban Centres and all 2X classes. Each entity has a 
corresponding vector boundary. ............................................................................................................ 10 

Figure 4 Schema of the MTUC model: starting from the reference year (ref year) 2025 the model 
analyse the overlaps between urban centre (ref year) and those of the previous epoch (-5 years; the 
processing is repeated for future starting from 2025 and comparing +5 years). Significative 
overlaps (i.e. overlaps hosting [A] population >= 50,000 or [B] >= 50% of ref year urban centre 
population or [C] >= 50% of +-5-years urban centre population) are kept. Four possible cases of 
relationships (+-5-years to ref year) are identified: (1) 'No overlaps', BIRTH (when comparing -5-
years layer) or DEATH (when comparing +5-years layer); (2) 'one to one' relationships, LINK (the ID 
of ref year is inherited in the +- 5-years layer), (3) 'many to 1', MERGE (all the 'many' boundaries in 
the +-5-years layer inherit the ref year ID); (4)0 'one or many to many', SPLIT (areas of the +-5-
years layer are split according to a maximum potential function computed in each pixel of the areas 
to be split from all the 'many' urban centres of the ref year; each split area inherit the ID of the ref 
year urban centre with the highest potential). The set of the new defined IDs it is used as input as 
ref year for the subsequent epoch analysis (e.g. completing ref year 2025 and -5-year 2020, at 
next iteration the newly defined 2020 IDs are used as ref year to link the 2015). ........................... 12 

Figure 5 Comparison of the 'fixed boundary' and the 'multi-temporal boundary' approaches. The 
'fixed boundary' (A, C) computes statistics of the GHS-UCDB across all epochs (1975-2030) based 
on the fixed 2025 boundaries; the 'multi-temporal boundary' approach assign a different boundary 
to each epoch allowing to follow the urban centre growth (B) and the urban centre shrinkage (D), 
and computing statistics of each epoch within the relevant boundary. .............................................. 13 
```

### [D6-p631]

[LIST/CONTENTS PAGE — transcribed verbatim; used as completeness checklist]

```text
List of Tables 

Table 1 Relationship between observed data gaps, data features, design principles and solutions 
adopted for the production of GHS-UCDB .............................................................................................. 5 

Table 2 GHS-UCDB Indicator fact sheet specimen with explanation of the fields .............................. 21 

Table 3 - Technical details of the datasets in GHS-UCDB_GLOBE_R2024A ..................................... 617 
```

### [D6-p632]

```text
Getting in touch with the EU 

In person 

All over the European Union there are hundreds of Europe Direct centres. You can find the 
address of the centre nearest you online (european-union.europa.eu/contact-eu/meet-us_en). 

On the phone or in writing 

Europe Direct is a service that answers your questions about the European Union. You can 
contact this service: 

— by freephone: 00 800 6 7 8 9 10 11 (certain operators may charge for these calls), 

— at the following standard number: +32 22999696, 

— via the following form: european-union.europa.eu/contact-eu/write-us_en. 

Finding information about the EU 

Online 

Information about the European Union in all the official languages of the EU is available on the 
Europa website (european-union.europa.eu). 

EU publications 

You can view or order EU publications at op.europa.eu/en/publications. Multiple copies of free 
publications can be obtained by contacting Europe Direct or your local documentation centre 
(european-union.europa.eu/contact-eu/meet-us_en). 

EU law and related documents 

For access to legal information from the EU, including all EU law since 1951 in all the official 
language versions, go to EUR-Lex (eur-lex.europa.eu). 
```

### [D6-p633]

```text
The Joint Research Centre (JRC) provides 
independent, evidence-based knowledge and 
science, supporting EU policies to positively 
impact society 

EU Science Hub 
Joint-research-centre.ec.europa.eu 
```


## A7 self-verification checklist

- Pages: 633 in range p1–p633; page anchors emitted in order: 633 (complete).
- Skipped pages (no text layer): none.
- Tables: document's own list names 3; captioned tables found in body: 3; uncaptioned ruled tables detected: 0; transcribed table IDs: 3. Listed but not transcribed as a table block: none.
- Figures/maps/graphs: document's own list names 5; figure IDs transcribed: 5 (0 continuation blocks). Listed but not found as a caption: none.
- Every table value sits inside an anchored table block (`[Dn-Tk]`, cell `rXcY`); all other printed text (including numbers in prose and in figure areas) sits inside a page-anchored block `[Dn-pN]` or figure block `[Dn-Fk]`.
- Values copied as extracted from the PDF text layer: no rounding, no unit conversion, no reformatting; precision kept as displayed.
- Contradictions: none resolved (none adjudicated in this module).
- Causal verbs: none in text added by this module (markup and flags only); source text is quoted verbatim and may itself contain such words.
- Hidden/undisplayed text excluded on pages: none (details in the JSON `extraction_gaps`).
- Scanned pages: none (every text page has a text layer); `[OCR-SOURCE]` not used.

## Extraction gaps declared by Module A

- GAP | [D6-p632] | 8 text spans lie outside the page or are clipped away by a clip path (not displayed); excluded by clip-aware extraction | OUT-OF-SCOPE