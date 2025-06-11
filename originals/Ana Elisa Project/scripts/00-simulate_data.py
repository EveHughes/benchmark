#### Preamble ####
# Purpose: Simulates a dataset of hate crimes
# Author: Ana Elisa Lopez-Miranda
# Date: 22 May 2025
# Contact: a.lopez.miranda@mail.utoronto.ca
# License: MIT
# Pre-requisites:
# - Add `polars`: uv add polars
# - Add `numpy`: uv add numpy
# - Add `datetime`: uv add datetime



#### Workspace setup ####
import polars as pl
import numpy as np
from datetime import date, timedelta


rng_occurrence = np.random.default_rng(seed=853)
rng_reported = np.random.default_rng(seed=123)

Neighbourhood_158=[
  "Agincourt North (129)",
  "Agincourt South-Malvern West (128)",
  "Alderwood (20)",
  "Annex (95)",
  "Avondale (153)",
  "Banbury-Don Mills (42)",
  "Bathurst Manor (34)",
  "Bay–Cloverhill (169)",
  "Bayview Village (52)",
  "Bayview Woods-Steeles (49)",
  "Bedford Park-Nortown (39)",
  "Beechborough-Greenbrook (112)",
  "Bendale–Glen Andrew (156)",
  "Bendale South (157)",
  "Birchcliffe-Cliffside (122)",
  "Black Creek (24)",
  "Blake-Jones (69)",
  "Briar Hill-Belgravia (108)",
  "Bridle Path-Sunnybrook-York Mills (41)",
  "Broadview North (57)",
  "Brookhaven-Amesbury (30)",
  "Cabbagetown-South St. James Town (71)",
  "Caledonia-Fairbank (109)",
  "Casa Loma (96)",
  "Centennial Scarborough (133)",
  "Church–Wellesley (167)",
  "Clairlea-Birchmount (120)",
  "Clanton Park (33)",
  "Cliffcrest (123)",
  "Corso Italia-Davenport (92)",
  "Danforth - East York (59)",
  "Danforth (66)",
  "Don Valley Village (47)",
  "Dorset Park (126)",
  "Downtown Yonge East (168)",
  "Dovercourt Village (172)",
  "Downsview (155)",
  "Dufferin Grove (83)",
  "East End-Danforth (62)",
  "East L'Amoreaux (148)",
  "Edenbridge-Humber Valley (9)",
  "Eglinton East (138)",
  "Elms-Old Rexdale (5)",
  "Englemount-Lawrence (32)",
  "Eringate-Centennial-West Deane (11)",
  "Etobicoke City Centre (159)",
  "Etobicoke West Mall (13)",
  "Fenside-Parkwoods (150)",
  "Flemingdon Park (44)",
  "Forest Hill North (102)",
  "Forest Hill South (101)",
  "Fort York–Liberty Village (163)",
  "Glenfield-Jane Heights (25)",
  "Golfdale-Cedarbrae-Woburn (141)",
  "Greenwood-Coxwell (65)",
  "Guildwood (140)",
  "Harbourfront-CityPlace (165)",
  "Henry Farm (53)",
  "High Park North (88)",
  "High Park-Swansea (87)",
  "Highland Creek (134)",
  "Hillcrest Village (48)",
  "Humber Bay Shores (161)",
  "Humber Heights-Westmount (8)",
  "Humber Summit (21)",
  "Humbermede (22)",
  "Humewood-Cedarvale (106)",
  "Ionview (125)",
  "Islington (158)",
  "Junction Area (90)",
  "Junction–Wallace Emerson (171)",
  "Keelesdale-Eglinton West (110)",
  "Kennedy Park (124)",
  "Kensington-Chinatown (78)",
  "Kingsview Village-The Westway (6)",
  "Kingsway South (15)",
  "L'Amoreaux West (147)",
  "Lambton Baby Point (114)",
  "Lansing-Westgate (38)",
  "Lawrence Park North (105)",
  "Lawrence Park South (103)",
  "Leaside-Bennington (56)",
  "Little Portugal (84)",
  "Long Branch (19)",
  "Malvern East (146)",
  "Malvern West (145)",
  "Maple Leaf (29)",
  "Markland Wood (12)",
  "Milliken (130)",
  "Mimico-Queensway (160)",
  "Morningside (135)",
  "Morningside Heights (144)",
  "Moss Park (73)",
  "Mount Dennis (115)",
  "Mount Olive-Silverstone-Jamestown (2)",
  "Mount Pleasant East (99)",
  "New Toronto (18)",
  "Newtonbrook East (50)",
  "Newtonbrook West (36)",
  "North Riverdale (68)",
  "North St. James Town (74)",
  "North Toronto (173)",
  "O'Connor-Parkview (54)",
  "Oakdale–Beverly Heights (154)",
  "Oakridge (121)",
  "Oakwood Village (107)",
  "Old East York (58)",
  "Palmerston-Little Italy (80)",
  "Parkwoods-O'Connor Hills (149)",
  "Pelmo Park-Humberlea (23)",
  "Playter Estates-Danforth (67)",
  "Pleasant View (46)",
  "Princess-Rosethorn (10)",
  "Regent Park (72)",
  "Rexdale-Kipling (4)",
  "Rockcliffe-Smythe (111)",
  "Roncesvalles (86)",
  "Rosedale-Moore Park (98)",
  "Rouge (131)",
  "Runnymede-Bloor West Village (89)",
  "Rustic (28)",
  "Scarborough Village (139)",
  "South Eglinton–Davisville (174)",
  "South Parkdale (85)",
  "South Riverdale (70)",
  "St. Andrew-Windfields (40)",
  "St Lawrence-East Bayfront-The Islands (166)",
  "Steeles (116)",
  "Stonegate-Queensway (16)",
  "Tam O'Shanter-Sullivan (118)",
  "Taylor Massey (61)",
  "The Beaches (63)",
  "Thistletown-Beaumond Heights (3)",
  "Thorncliffe Park (55)",
  "Trinity-Bellwoods (81)",
  "University (79)",
  "Victoria Village (43)",
  "Wellington Place (164)",
  "West Hill (136)",
  "West Humber-Clairville (1)",
  "West Queen West (162)",
  "West Rouge (143)",
  "Westminster-Branson (35)",
  "Weston (113)",
  "Weston-Pelham Park (91)",
  "Wexford-Maryvale (119)",
  "Willowdale East (152)",
  "Willowdale West (37)",
  "Willowridge-Martingrove-Richview (7)",
  "Woburn North (142)",
  "Woodbine Corridor (64)",
  "Woodbine-Lumsden (60)",
  "Wychwood (94)",
  "Yonge–Bay Corridor (170)",
  "Yonge-Eglinton (100)",
  "Yonge–Doris (151)",
  "Yonge-St. Clair (97)",
  "York University Heights (27)",
  "Yorkdale-Glen Park (31)"
]

Primary_Offence = ["Wilful Promotion of Hatred", "Assault With a Weapon", "Mischief Under $5000", "Indecent Communications", "Assault", "Uttering Threats - Bodily Harm", "Criminal Harassment", "Mischief Interfere With Property", "Mischief To Religious Property, Educational Institutions, Etc.", 
                   "Assault Causing Bodily Harm", "Uttering Threats - Property", "Public Incitement of Hatred ", "Arson",
                   "Theft","Robbery", "Disturbing Religious Worship Or Certain Meetings",
                   "Causing a Disturbance", "Advocating Genocide", "Firearms Related Offence",
                   "Harassing Communications", "Mischief Over $5000", "Mischief To Data",
                   "Assault Peace Officer","Other Criminal Code Offence Not Listed","Sexual Assault",
                   "Murder","Dangerous Operation Motor Vehicle", "Fail To Comply Probation", "Aggravated Assault"]     
Division =  ["D33", "D42", "D53", "D52", "D32", "D13", "D14", "D12", "D31", "D51",
"D43", "D22", "D55", "D11", "D41", "D23"]
Location_type = ["Religious Place of Worship/Cultural Centre","House (Townhouse, Retirement Home, Garage, Vehicle, Cottage)",
                 "Educational Institution (Universities, Colleges, Schools, etc.)",
                 "Streets/Roadways/Highway",
                 "Business/Retail",
                 "Other Commercial / Corporate Places ",
                 "Public Transportation",
                 "Government Building (Courthouse, Museums, Parliament Building, etc.)",
                 "Apartment Building (Condo, Retirement Buidling, etc.)",
                 "Open Area, Park or Parking Lot",
                 "Government Building",
                 "Medical Facility (Hospitals, Long-term Care, etc.)",
                 "Non-Commercial/Non for Profit"   ]
#### Simulate data ####
# Simulate 20 offences with occurence data, occurence time, reported date, division, location_type, bias, primary offence, neighbourhood, and arrest
bias_choice = ["AGE_BIAS", "MENTAL_OR_PHYSICAL_DISABILITY", "RACE_BIAS", "ETHNICITY_BIAS", "LANGUAGE_BIAS", "RELIGION_BIAS", "SEXUAL_ORIENTATION_BIAS", "GENDER_BIAS"]
bias = np.random.choice(bias_choice, size=20, replace=True)
arrest_choice = ["Yes", "No"]
arrest = np.random.choice(arrest_choice, size=20, replace=True)
division = np.random.choice(Division, size = 20, replace = True)
location_type = np.random.choice(Location_type, size=20, replace=True)
neighbourhood_158 = np.random.choice(Neighbourhood_158, size=20, replace = True)
primary_offence = np.random.choice(Primary_Offence, size=20, replace=True)
start_date = date(2018, 1,1)
end_date = date(2024, 12, 31)
range_date=(end_date-start_date).days
random_days_o = rng_occurrence.integers(0, range_date+1, size=20)
random_dates_o = [start_date +timedelta(days=int(d)) for d in random_days_o]
date_o = [d.isoformat() for d in random_dates_o]
random_days_r = rng_reported.integers(0, range_date+1, size=20)
random_dates_r = [start_date +timedelta(days=int(d)) for d in random_days_r]
date_r = [d.isoformat() for d in random_dates_r]
hate_crimes_df = pl.DataFrame(
    {
        "occurrence_date": date_o,
        "reported_date": date_r,
        "division": division,
        "location_type": location_type,
        "bias" :bias,
        "primary_offence": primary_offence,
        "neighbourhood": neighbourhood_158,
        "arrest": arrest
    }
)

hate_crimes_df.write_csv("simulated_data.csv")


