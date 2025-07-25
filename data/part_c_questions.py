import json

# Complete survey questions from Parts A, B, and C formatted for database seeding
data = [
    # PART A: SOCIO-ECONOMY
    {
        "question_text": "Name of the village",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 1,
        "section": "Part A",
        "depends_on": None, # Ensure None, not empty string or 'null' for non-dependent fields
        "depends_on_value": None,
        "details": None # Ensure None, not 'null' string, for fields without details
    },
    {
        "question_text": "GPS Location - North (N)",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 2,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"format": "°        '                 \""} # This should be a dictionary
    },
    {
        "question_text": "GPS Location - East (E)",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 3,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"format": "°        '                 \""}
    },
    {
        "question_text": "Post Office",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 4,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "District",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 5,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Name of respondent",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 6,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Education",
        "question_type": "multiple_choice",
        "options": ["No Education", "Lower Primary", "Upper Primary", "Matriculate", "Higher Secondary", "Graduate", "Post Graduate"], # List
        "is_required": True,
        "order_index": 7,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Age",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 8,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Gender",
        "question_type": "multiple_choice",
        "options": ["Male", "Female", "Other"], # List
        "is_required": True,
        "order_index": 9,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Marital Status",
        "question_type": "multiple_choice",
        "options": ["Married", "Unmarried"], # List
        "is_required": True,
        "order_index": 10,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Primary Occupation",
        "question_type": "multiple_choice",
        "options": ["Farmer", "Daily Wages Labor", "Private Sector (Shopkeeper, Small Scale Industry, Mill Owner, etc.)", "Government Employee", "Contractor"], # List
        "is_required": True,
        "order_index": 11,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Secondary Occupation",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 12,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Date of visit",
        "question_type": "date",
        "options": None,
        "is_required": True,
        "order_index": 13,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Community",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 14,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Name of the FD/Range",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 15,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Religion",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 16,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Presence of Cell/Mobile Network",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 17,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Tribe (If Any)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 18,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Nearest Health Centre",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 19,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance (km) from Health Centre",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 20,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Nearest Education Centre",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 21,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance (km) from Education Centre",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 22,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Nearest Forest Department Office",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 23,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance (km) from Forest Department Office",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 24,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Nearest Police Station/Outpost",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 25,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance (km) from Police Station/Outpost",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 26,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "No. of members in Household (including the respondent)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 27,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Household Members Details",
        "question_type": "table",
        "options": None,
        "is_required": True,
        "order_index": 28,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": { # Dictionary
            "table_headers": ["Member", "Age", "Gender"],
            "max_rows": 6,
            "additional_field": "If More"
        }
    },
    {
        "question_text": "Living since how long?",
        "question_type": "multiple_choice",
        "options": ["Many Generations", "Second Generation", "Recently Settled (specify year)"], # List
        "is_required": True,
        "order_index": 29,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "What is your monthly household income?",
        "question_type": "multiple_choice",
        "options": ["Less than ₹10,000", "₹10,001 - ₹20,000", "₹30,001 - ₹40,000", "₹40,001 - ₹50,000", "More than ₹50,000"], # List
        "is_required": True,
        "order_index": 30,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do you have access to electricity in your household?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 31,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, since when? (Years)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 32,
        "section": "Part A",
        "depends_on": "Do you have access to electricity in your household?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Whether under any govt. scheme or privately owned? If so, which scheme",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 33,
        "section": "Part A",
        "depends_on": "Do you have access to electricity in your household?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "What is the primary source for water in your household?",
        "question_type": "multiple_choice",
        "options": ["Well", "Borehole", "River/Stream/Spring", "Piped Water (Purchased)", "Piped Water (Not Purchased)"], # List
        "is_required": True,
        "order_index": 34,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do source of water provided under any govt. scheme?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 35,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, under which scheme (Please specify)? Is it functional?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 36,
        "section": "Part A",
        "depends_on": "Do source of water provided under any govt. scheme?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Distance of water source from your house (km)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 37,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "What is the primary cooking fuel used in your household? (Ranking: *** Mostly, **Moderately, *Least)",
        "question_type": "table",
        "options": None,
        "is_required": True,
        "order_index": 38,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": { # Dictionary
            "table_headers": ["Fuel Type", "Ranking"],
            "fuel_types": ["Electricity", "Fire wood", "LPG (Liquefied Petroleum Gas)", "Other"]
        }
    },
    {
        "question_text": "If LPG, is it provided under any scheme of government?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": False,
        "order_index": 39,
        "section": "Part A",
        # This question doesn't directly depend on another "question_text"
        # It depends on the *answer* to the previous question's table row for 'LPG'
        # You might need custom logic in your frontend or a more complex depends_on structure
        "depends_on": "What is the primary cooking fuel used in your household? (Ranking: *** Mostly, **Moderately, *Least)", # String
        "depends_on_value": "LPG (Liquefied Petroleum Gas)", # String - This will match the 'Fuel Type'
        "details": None
    },
    {
        "question_text": "Do you collect Fire Wood?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 40,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, from where do you collect fire wood?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 41,
        "section": "Part A",
        "depends_on": "Do you collect Fire Wood?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Source", "Distance from House (km)"],
            "sources": ["Own Farm", "Reserved Forest/PAs"]
        }
    },
    {
        "question_text": "What type of fire wood do you collect? (You can select more than one option)",
        "question_type": "multiple_choice",
        "options": ["Naturally Fallen Branches/Trees", "Only Lopped Branches", "Cut Down Entire Tree/Plant"], # List
        "is_required": False,
        "order_index": 42,
        "section": "Part A",
        "depends_on": "Do you collect Fire Wood?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "How often do you go for fire wood collection?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 43,
        "section": "Part A",
        "depends_on": "Do you collect Fire Wood?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Time Period", "Frequency"],
            "periods": ["in a Day", "in a Week", "in a Month", "in a Year"],
            "frequency_options": ["Once", "Twice", "Thrice", "More"]
        }
    },
    {
        "question_text": "Any specific plants/trees that you collect as fire wood? (Ranking from High to Low)",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 44,
        "section": "Part A",
        "depends_on": "Do you collect Fire Wood?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Ranking", "Plant/Tree Species"],
            "max_rows": 5
        }
    },
    {
        "question_text": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 45,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "NTFPs Collection Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 46,
        "section": "Part A",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Ranking", "NTFPs (Fodder/Vegetables/Honey/Mushroom/Fire Woods/Medicinal Plants/Fruits & Berries/Game Animal/Fishing)", "Season of Collection", "Frequency"],
            "seasons": ["Spring (Mar-Apr)", "Summer (May-Jun)", "Monsoon (Jul-Aug)", "Autumn (Sep-Oct)", "Pre-Winter (Nov-Dec)", "Winter (Dec-Feb)"],
            "max_rows": 8
        }
    },
    {
        "question_text": "From where do you collect Non-Timber Forest Products (NTFPs)?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 47,
        "section": "Part A",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Source", "Distance from House (km)"],
            "sources": ["Own Farm", "Reserved Forest/PAs"]
        }
    },
    {
        "question_text": "Are you allowed to collect NTFPs from Reserved Forest/Protected Areas (PAs)?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 48,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Is there any community restriction to collection of NTFPs?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 49,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If so, why are there community restrictions?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 50,
        "section": "Part A",
        "depends_on": "Is there any community restriction to collection of NTFPs?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Any animal husbandry activities are you engaged in?",
        "question_type": "table",
        "options": None,
        "is_required": True,
        "order_index": 51,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": { # Dictionary
            "table_headers": ["Species", "Numbers", "Income/Earnings"],
            "species": ["Cattle", "Goats/Sheep", "Pig", "Chicken/Ducks"]
        }
    },
    {
        "question_text": "Any other wild animal you have encounter while going to forest – When? How long ago?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 52,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": { # Dictionary
            "table_headers": ["Animal", "When encountered"],
            "max_rows": 6
        }
    },
    {
        "question_text": "Do you cultivate crops?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 53,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do you practice Jhum cultivation?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 54,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Crops Cultivated Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 55,
        "section": "Part A",
        "depends_on": "Do you cultivate crops?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Ranking", "Crops Cultivated", "Total Area of Land Owned (Bigha)", "Area of land cultivated (Bigha)", "Season grown", "Income/Earnings", "Jhum frequency", "After How many Years"],
            "seasons": ["Spring (Mar-Apr)", "Summer (May-Jun)", "Monsoon (Jul-Aug)", "Autumn (Sep-Oct)", "Pre-Winter (Nov-Dec)", "Winter (Dec-Feb)"],
            "max_rows": 10
        }
    },
    {
        "question_text": "Do you previously go for hunting?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 56,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, how long it has been you left hunting?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 57,
        "section": "Part A",
        "depends_on": "Do you previously go for hunting?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "What are the species you generally hunt or used to hunt? (Ranking)",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 58,
        "section": "Part A",
        "depends_on": "Do you previously go for hunting?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Ranking", "Species"],
            "max_rows": 5
        }
    },
    {
        "question_text": "Hunting Frequency (if applicable)",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 59,
        "section": "Part A",
        "depends_on": "Do you previously go for hunting?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Time Period", "Frequency"],
            "periods": ["in a Day", "in a Week", "in a Month", "in a Year"],
            "frequency_options": ["Once", "Twice", "Thrice", "More"]
        }
    },
    {
        "question_text": "Do you have any animal trophy belonging?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 60,
        "section": "Part A",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, which species trophies do you have?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 61,
        "section": "Part A",
        "depends_on": "Do you have any animal trophy belonging?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Trophy Number", "Species"],
            "max_rows": 5
        }
    },

    # PART B: HUMAN-ELEPHANT CONFLICT
    {
        "question_text": "Do elephants visit your crops?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 62,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "How many individuals?",
        "question_type": "multiple_choice",
        "options": ["Single", "Lone Individual", "Group", "Herd"], # List
        "is_required": False,
        "order_index": 63,
        "section": "Part B",
        "depends_on": "Do elephants visit your crops?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Elephant Visit Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 64,
        "section": "Part B",
        "depends_on": "Do elephants visit your crops?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Age-Sex Class", "No. of Individual", "Do they raid/damage crops?", "Time spent raiding (Hours)", "Visit frequency", "Where they stay"],
            "age_sex_classes": [
                "Adult Male (AM) with Tusk",
                "Adult Male (AM) without Tusk",
                "Adult Female (AF)",
                "Adult Unidentified (AUN)",
                "Sub-adult Male (SAM)",
                "Sub-adult Female (SAF)",
                "Sub-adult Unidentified (SAUN)",
                "Juvenile Male (JUVM)",
                "Juvenile Female (JUVF)",
                "Juvenile Unidentified (JUNF)",
                "Calf Male (CLFM)",
                "Calf Female (CLFF)",
                "Calf Unidentified (CLFUN)",
                "Total"
            ]
        }
    },
    {
        "question_text": "Crop Raiding Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 65,
        "section": "Part B",
        "depends_on": "Do elephants visit your crops?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Name of Crop", "Area raided/damaged (Bigha)", "Season of raiding", "Time of visit"],
            "seasons": ["Spring (Mar-Apr)", "Summer (May-Jun)", "Monsoon (Jul-Aug)", "Autumn (Sep-Oct)", "Pre-Winter (Nov-Dec)", "Winter (Dec-Feb)"],
            "time_periods": ["Morning (4am-12pm)", "Afternoon (12pm-3pm)", "Evening (3pm-8pm)", "Night (8pm-4am)"],
            "max_rows": 8
        }
    },
    {
        "question_text": "House Destroyed/Damaged by Elephants",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 66,
        "section": "Part B",
        "depends_on": "Do elephants visit your crops?", # Adding this dependency based on typical questionnaire flow
        "depends_on_value": "Yes", # Assuming house damage relates to elephant visits
        "details": { # Dictionary
            "table_headers": ["Type of House", "Season damaged", "Time of visit", "Reason/Purpose"],
            "house_types": ["Hut", "Farm house", "Granary", "Wooden House", "RCC Pucca House"],
            "seasons": ["Spring (Mar-Apr)", "Summer (May-Jun)", "Monsoon (Jul-Aug)", "Autumn (Sep-Oct)", "Pre-Winter (Nov-Dec)", "Winter (Dec-Feb)"],
            "time_periods": ["Morning (4am-12pm)", "Afternoon (12pm-3pm)", "Evening (3pm-8pm)", "Night (8pm-4am)"]
        }
    },
    {
        "question_text": "Are you aware of any human being injured/killed by elephants?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 67,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Human Injury/Death Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 68,
        "section": "Part B",
        "depends_on": "Are you aware of any human being injured/killed by elephants?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Serial No.", "Death", "Injury", "Age (Years)", "Gender (M/F)", "How long ago?", "Time of incident", "Location/Village", "How was person killed/injured?"],
            "time_periods": ["Morning", "Afternoon", "Evening", "Night"],
            "max_rows": 5
        }
    },
    {
        "question_text": "Since when the elephants have been here?",
        "question_type": "multiple_choice",
        "options": ["Recently", "5 years", "10 years", "15 years", "More than 20 years"], # List
        "is_required": True,
        "order_index": 69,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do you think the elephants have come from somewhere outside Nagaland?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 70,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, from where they have come from?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 71,
        "section": "Part B",
        "depends_on": "Do you think the elephants have come from somewhere outside Nagaland?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "How do you drive elephants away from your crop during crop raiding/damaging?",
        "question_type": "multiple_choice",
        "options": ["Burning Fire Crackers", "Burning Fire", "Arrow/Sling Shot", "Air Fire with Rifles/Air Guns", "Make Hue & Cry", "Others"], # List
        "is_required": True,
        "order_index": 72,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 73,
        "section": "Part B",
        "depends_on": "Do elephants visit your crops?", # Adding a dependency here as it's about prevention.
        "depends_on_value": "Yes",
        "details": { # Dictionary
            "table_headers": ["Prevention Method", "Details"],
            "methods": [
                "Fencing (Trenches/Solar/Electric/Barb wire/Any Other)",
                "Traps (Snare/Pitfall/Others)",
                "Night Duty (When & How often?)"
            ]
        }
    },
    {
        "question_text": "Since when human-elephant conflict has been prevailing here?",
        "question_type": "multiple_choice",
        "options": ["Recently", "5 years", "10 years", "15 years", "More than 20 years"], # List
        "is_required": True,
        "order_index": 74,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Has human-elephant conflict increased in recent years?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 75,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Why do you think the human-elephant conflict has increased?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 76,
        "section": "Part B",
        "depends_on": "Has human-elephant conflict increased in recent years?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Are you aware of any elephant being killed?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 77,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Elephant Age/Sex Class (if killed)",
        "question_type": "multiple_choice",
        "options": ["Adult Male (AM)", "Adult Female (AF)", "Sub-adult Male (SAM)", "Sub-adult Female (SAF)", "Juvenile Male (JUVM)", "Juvenile Female (JUVF)", "Calf Male (CLFM)", "Calf Female (CLFF)"], # List
        "is_required": False,
        "order_index": 78,
        "section": "Part B",
        "depends_on": "Are you aware of any elephant being killed?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "If yes, when & where was the elephant killed?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 79,
        "section": "Part B",
        "depends_on": "Are you aware of any elephant being killed?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "How was the elephant killed?",
        "question_type": "multiple_choice",
        "options": ["Arrow/Rifles/Air Guns", "Electrocution", "Poisoning", "Traps (Snare/Pitfall/Other)"], # List
        "is_required": False,
        "order_index": 80,
        "section": "Part B",
        "depends_on": "Are you aware of any elephant being killed?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Should elephants be allowed to stay in your area?",
        "question_type": "multiple_choice",
        "options": ["Yes", "No", "Depends on government/forest department decision", "Other"], # List
        "is_required": True,
        "order_index": 81,
        "section": "Part B",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },

    # PART C: HUMAN-WILDLIFE CONFLICT (Other than elephant)
    {
        "question_text": "Any other wild animals that raid/damage crops?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 82,
        "section": "Part C",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Other Wild Animals Crop Raiding Details",
        "question_type": "table",
        "options": None,
        "is_required": False,
        "order_index": 83,
        "section": "Part C",
        "depends_on": "Any other wild animals that raid/damage crops?", # String
        "depends_on_value": "Yes", # String
        "details": { # Dictionary
            "table_headers": ["Wild Animal Species", "No. of Individuals", "Crops Affected", "Area Damaged (Bigha)", "Time of Raiding", "Visit Frequency", "Where they stay"],
            "time_periods": ["Morning", "Afternoon", "Evening", "Night"],
            "frequency_options": ["Once/day", "Twice/day", "Thrice/day", "More/day", "Once/week", "Twice/week", "More/week", "Once/month", "More/month", "Once/season", "More/season"],
            "stay_locations": ["Reserved Forest", "Protected Areas", "Farmland"],
            "max_rows": 5
        }
    },
    {
        "question_text": "Do you (a) drive them away or (b) kill other wild animals?",
        "question_type": "multiple_choice",
        "options": ["Drive Away", "Kill", "Both", "Neither"], # List
        "is_required": True,
        "order_index": 84,
        "section": "Part C",
        "depends_on": "Any other wild animals that raid/damage crops?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "If drive them away, how?",
        "question_type": "multiple_choice",
        "options": ["Burning Fire Crackers", "Burning Fire", "Arrow/Sling Shot", "Air Fire with Rifles/Air Guns", "Make Hue & Cry", "Others"], # List
        "is_required": False,
        "order_index": 85,
        "section": "Part C",
        "depends_on": "Do you (a) drive them away or (b) kill other wild animals?", # String
        "depends_on_value": "Drive Away", # String
        "details": None
    },
    {
        "question_text": "If killed, how?",
        "question_type": "multiple_choice",
        "options": ["Arrow/Slingshot/Rifles/Air Guns", "Poisoning", "Electrocution", "Traps(Snare/Pitfall/Other)"], # List
        "is_required": False,
        "order_index": 86,
        "section": "Part C",
        "depends_on": "Do you (a) drive them away or (b) kill other wild animals?", # String
        "depends_on_value": "Kill", # String
        "details": None
    },
    {
        "question_text": "Do you really think elephants or any other wild animals should be protected/conserved? If so, why?",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 87,
        "section": "Part C",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Are you aware of Asiatic elephant's globally endangered and nationally protected status?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 88,
        "section": "Part C",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Have you ever participated or observed any conservation program by forest department or any other organization?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 89,
        "section": "Part C",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "What have you learnt from conservation programs?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 90,
        "section": "Part C",
        "depends_on": "Have you ever participated or observed any conservation program by forest department or any other organization?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "Do you want to engage yourself and people of your area for the protection/conservation of elephants and other wildlife in your area?",
        "question_type": "yes_no",
        "options": ["Yes", "No"], # List
        "is_required": True,
        "order_index": 91,
        "section": "Part C",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "How will you engage yourself and people for the protection/conservation of elephants and other wildlife in your area?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 92,
        "section": "Part C",
        "depends_on": "Do you want to engage yourself and people of your area for the protection/conservation of elephants and other wildlife in your area?", # String
        "depends_on_value": "Yes", # String
        "details": None
    },
    {
        "question_text": "If no, why don't you want to engage in wildlife conservation?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 93,
        "section": "Part C",
        "depends_on": "Do you want to engage yourself and people of your area for the protection/conservation of elephants and other wildlife in your area?", # String
        "depends_on_value": "No", # String
        "details": None
    }
]