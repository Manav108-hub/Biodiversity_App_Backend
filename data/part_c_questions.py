import json

# Complete Human-Elephant Conflict Questionnaire
# Updated with softer language and comprehensive coverage of all sections
data = [
    # BASIC INFORMATION
    {
        "question_text": "Name of the village",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 1,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Date of Visit",
        "question_type": "date",
        "options": None,
        "is_required": True,
        "order_index": 2,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Post Office",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 3,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "District",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 4,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Name of respondent",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 5,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "GPS Location - Latitude",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 6,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"placeholder": "Enter latitude coordinates"}
    },
    {
        "question_text": "GPS Location - Longitude",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 7,
        "section": "Basic Information",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"placeholder": "Enter longitude coordinates"}
    },

    # DEMOGRAPHIC INFORMATION
    {
        "question_text": "Age",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 8,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 18, "max": 100}
    },
    {
        "question_text": "Gender",
        "question_type": "multiple_choice",
        "options": ["Male", "Female", "Other"],
        "is_required": True,
        "order_index": 9,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Education",
        "question_type": "multiple_choice",
        "options": ["No Education", "Lower Primary (LKG to Class 5)", "Upper Primary (Class 6 to Class 10)", "Matriculate (Class 10 passed)", "Higher Secondary (Class 12 passed)", "Graduate", "Post-Graduate", "Other"],
        "is_required": True,
        "order_index": 10,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Community/Tribe (If any)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 11,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Religion",
        "question_type": "multiple_choice",
        "options": ["Hinduism", "Buddhism", "Christianity", "Islam", "Other"],
        "is_required": True,
        "order_index": 12,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If religion is Other, please specify",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 13,
        "section": "Demographics",
        "depends_on": "Religion",
        "depends_on_value": "Other",
        "details": None
    },
    {
        "question_text": "Marital Status",
        "question_type": "multiple_choice",
        "options": ["Married", "Unmarried"],
        "is_required": True,
        "order_index": 14,
        "section": "Demographics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },

    # OCCUPATION AND ECONOMIC STATUS
    {
        "question_text": "Primary Occupation",
        "question_type": "multiple_choice",
        "options": ["Unemployed", "Daily Wages Laborer", "Farmer", "Shopkeeper", "Business", "Private Sector", "Government Employee", "Pensioner"],
        "is_required": True,
        "order_index": 15,
        "section": "Occupation",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "No. of members in your family",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 16,
        "section": "Household",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 1}
    },
    {
        "question_text": "Living since how long?",
        "question_type": "multiple_choice",
        "options": ["Many Generations", "Second Generation", "Recently Settled"],
        "is_required": True,
        "order_index": 17,
        "section": "Household",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If recently settled, since when?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 18,
        "section": "Household",
        "depends_on": "Living since how long?",
        "depends_on_value": "Recently Settled",
        "details": {"placeholder": "Please specify year or duration"}
    },

    # INFRASTRUCTURE ACCESS
    {
        "question_text": "Nearest Health Centre",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 19,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance to nearest Health Centre (km)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 20,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 0}
    },
    {
        "question_text": "Nearest Education Centre",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 21,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance to nearest Education Centre (km)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 22,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 0}
    },
    {
        "question_text": "Nearest Forest Department Office",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 23,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance to nearest Forest Department Office (km)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 24,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 0}
    },
    {
        "question_text": "Nearest Police Station or Outpost",
        "question_type": "text",
        "options": None,
        "is_required": True,
        "order_index": 25,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Distance to nearest Police Station or Outpost (km)",
        "question_type": "number",
        "options": None,
        "is_required": True,
        "order_index": 26,
        "section": "Infrastructure",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"min": 0}
    },

    # HOUSEHOLD INCOME AND UTILITIES
    {
        "question_text": "What is your monthly household income?",
        "question_type": "multiple_choice",
        "options": ["Less than ₹10,000", "₹10,000 - ₹20,000", "₹20,000 - ₹30,000", "₹30,000 - ₹40,000", "₹40,000 - ₹50,000", "More than ₹50,000"],
        "is_required": True,
        "order_index": 27,
        "section": "Household Economics",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do you have access to electricity in your household?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 28,
        "section": "Household Utilities",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "What is the primary source for water in your household?",
        "question_type": "multiple_choice",
        "options": ["Well", "Tube well", "River", "Stream", "Spring", "Piped Water", "Other"],
        "is_required": True,
        "order_index": 29,
        "section": "Household Utilities",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If water source is Other, please specify",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 30,
        "section": "Household Utilities",
        "depends_on": "What is the primary source for water in your household?",
        "depends_on_value": "Other",
        "details": None
    },
    {
        "question_text": "What is the primary cooking fuel used in your household?",
        "question_type": "multiple_choice",
        "options": ["Electricity", "Fire wood", "LPG (Liquefied Petroleum Gas)", "Other"],
        "is_required": True,
        "order_index": 31,
        "section": "Household Utilities",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If cooking fuel is Other, please specify",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 32,
        "section": "Household Utilities",
        "depends_on": "What is the primary cooking fuel used in your household?",
        "depends_on_value": "Other",
        "details": None
    },

    # FIREWOOD COLLECTION
    {
        "question_text": "Do you collect Firewood?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 33,
        "section": "Resource Collection",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "From where do you collect firewood?",
        "question_type": "multiple_choice",
        "options": ["Own Farm", "Clan Forest", "Community Forest", "Reserved Forest/Protected Areas (PAs)"],
        "is_required": False,
        "order_index": 34,
        "section": "Resource Collection",
        "depends_on": "Do you collect Firewood?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "How much distance you travel to collect firewood?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 35,
        "section": "Resource Collection",
        "depends_on": "Do you collect Firewood?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Distance in km or time taken"}
    },
    {
        "question_text": "What type of fire wood do you collect?",
        "question_type": "multiple_choice",
        "options": ["Naturally Fallen Branches and Trees", "Only Lopped Branches", "Cut Down Entire Tree"],
        "is_required": False,
        "order_index": 36,
        "section": "Resource Collection",
        "depends_on": "Do you collect Firewood?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "How often do you go for firewood collection?",
        "question_type": "multiple_choice",
        "options": ["Once in a DAY", "Twice in a DAY", "Thrice in a DAY", "More in a DAY", "Once in WEEK", "Twice in a WEEK", "Thrice in a WEEK", "More in a WEEK", "Once in a MONTH", "Twice in a MONTH", "Thrice in a MONTH", "More in a MONTH", "Once in a YEAR", "Twice in a YEAR", "Thrice in a YEAR", "More in a YEAR"],
        "is_required": False,
        "order_index": 37,
        "section": "Resource Collection",
        "depends_on": "Do you collect Firewood?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Any specific plants/trees that you collect as fire wood? (Please list up to 10)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 38,
        "section": "Resource Collection",
        "depends_on": "Do you collect Firewood?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List plant/tree names separated by commas", "max_items": 10}
    },

    # NON-TIMBER FOREST PRODUCTS (NTFPs)
    {
        "question_text": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 39,
        "section": "Resource Collection",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"examples": "Fodder/Vegetables/Honey/Mushroom/Firewood/Medicinal Plants/Fruits & Berries/Game Animal/Fishing/Broom Stick"}
    },
    {
        "question_text": "Which NTFPs do you collect? (Please list up to 10)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 40,
        "section": "Resource Collection",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List NTFP types separated by commas", "max_items": 10}
    },
    {
        "question_text": "In which season do you go for NTFP collection?",
        "question_type": "multiple_choice",
        "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "is_required": False,
        "order_index": 41,
        "section": "Resource Collection",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "How frequent do you go for NTFP collection?",
        "question_type": "multiple_choice",
        "options": ["Once in a DAY", "Twice in a DAY", "Thrice in a DAY", "More in a DAY", "Once in WEEK", "Twice in a WEEK", "Thrice in a WEEK", "More in a WEEK", "Once in a MONTH", "Twice in a MONTH", "Thrice in a MONTH", "More in a MONTH", "Once in a YEAR", "Twice in a YEAR", "Thrice in a YEAR", "More in a YEAR"],
        "is_required": False,
        "order_index": 42,
        "section": "Resource Collection",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "From where do you collect Non-Timber Forest Products (NTFPs)?",
        "question_type": "multiple_choice",
        "options": ["Own Farm", "Clan Forest", "Community Forest", "Reserved Forest/Protected Areas (PAs)"],
        "is_required": False,
        "order_index": 43,
        "section": "Resource Collection",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "How much distance do you travel to collect NTFPs? (km)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 44,
        "section": "Resource Collection",
        "depends_on": "Do you collect other Non-Timber Forest Products (NTFPs)?",
        "depends_on_value": "Yes",
        "details": {"min": 0}
    },

    # COMMUNITY FOREST AND PROTECTED AREAS
    {
        "question_text": "Is there any community reserved forest or Protected Area in your village?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 45,
        "section": "Forest Areas",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "If yes, please specify the name/type",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 46,
        "section": "Forest Areas",
        "depends_on": "Is there any community reserved forest or Protected Area in your village?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Are you allowed to collect NTFPs from community reserved forest or Protected Area (PAs)?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 47,
        "section": "Forest Areas",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },

    # WILDLIFE ENCOUNTERS
    {
        "question_text": "Any wild animal that you have encounter while going to forest?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 48,
        "section": "Wildlife Encounters",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"placeholder": "List animals encountered", "photo_upload": True}
    },

    # CULTIVATION
    {
        "question_text": "Do you cultivate?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 49,
        "section": "Agriculture",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "What is the total area of land you own (in acres/hectares/bigha)?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 50,
        "section": "Agriculture",
        "depends_on": "Do you cultivate?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify unit (acres/hectares/bigha)"}
    },
    {
        "question_text": "How much of this land do you currently cultivate (in acres/hectares/bigha)?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 51,
        "section": "Agriculture",
        "depends_on": "Do you cultivate?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify unit (acres/hectares/bigha)"}
    },
    {
        "question_text": "Is it jhum (shifting) cultivation?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 52,
        "section": "Agriculture",
        "depends_on": "Do you cultivate?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "After how many years do you shift your crop field?",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 53,
        "section": "Agriculture",
        "depends_on": "Is it jhum (shifting) cultivation?",
        "depends_on_value": "Yes",
        "details": {"min": 1}
    },
    {
        "question_text": "What are the crops you cultivate? (List up to 10 crops with details)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 54,
        "section": "Agriculture",
        "depends_on": "Do you cultivate?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List crops, cultivation seasons, and if you sell them", "max_items": 10}
    },

    # TRADITIONAL PRACTICES (HUNTING - using softer language)
    {
        "question_text": "Do you engage in traditional wildlife practices?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 55,
        "section": "Traditional Practices",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"note": "This refers to traditional community practices involving wildlife"}
    },
    {
        "question_text": "How frequent do you engage in these traditional practices?",
        "question_type": "multiple_choice",
        "options": ["Once in a DAY", "Twice in a DAY", "Thrice in a DAY", "More in a DAY", "Once in WEEK", "Twice in a WEEK", "Thrice in a WEEK", "More in a WEEK", "Once in a MONTH", "Twice in a MONTH", "Thrice in a MONTH", "More in a MONTH", "Once in a YEAR", "Twice in a YEAR", "Thrice in a YEAR", "More in a YEAR"],
        "is_required": False,
        "order_index": 56,
        "section": "Traditional Practices",
        "depends_on": "Do you engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "What animals are involved in these traditional practices? (List up to 5 species)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 57,
        "section": "Traditional Practices",
        "depends_on": "Do you engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List species names", "max_items": 5}
    },
    {
        "question_text": "In which season do you engage in these traditional practices?",
        "question_type": "multiple_choice",
        "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "is_required": False,
        "order_index": 58,
        "section": "Traditional Practices",
        "depends_on": "Do you engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "Did you previously engage in traditional wildlife practices?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 59,
        "section": "Traditional Practices",
        "depends_on": "Do you engage in traditional wildlife practices?",
        "depends_on_value": "No",
        "details": None
    },
    {
        "question_text": "How long has it been since you stopped these traditional practices?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 60,
        "section": "Traditional Practices",
        "depends_on": "Did you previously engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Years or time period"}
    },
    {
        "question_text": "How frequent did you previously engage in these traditional practices?",
        "question_type": "multiple_choice",
        "options": ["Once in a DAY", "Twice in a DAY", "Thrice in a DAY", "More in a DAY", "Once in WEEK", "Twice in a WEEK", "Thrice in a WEEK", "More in a WEEK", "Once in a MONTH", "Twice in a MONTH", "Thrice in a MONTH", "More in a MONTH", "Once in a YEAR", "Twice in a YEAR", "Thrice in a YEAR", "More in a YEAR"],
        "is_required": False,
        "order_index": 61,
        "section": "Traditional Practices",
        "depends_on": "Did you previously engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "What animals were previously involved in these traditional practices? (List up to 5 species)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 62,
        "section": "Traditional Practices",
        "depends_on": "Did you previously engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List species names", "max_items": 5}
    },
    {
        "question_text": "In which season did you previously engage in these traditional practices?",
        "question_type": "multiple_choice",
        "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "is_required": False,
        "order_index": 63,
        "section": "Traditional Practices",
        "depends_on": "Did you previously engage in traditional wildlife practices?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },

    # WILDLIFE ARTIFACTS/TROPHIES
    {
        "question_text": "Do you possess any animal trophies or wildlife articles?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 64,
        "section": "Wildlife Artifacts",
        "depends_on": None,
        "depends_on_value": None,
        "details": {"examples": "animal skins, bones, horns, antlers, feathers, ivory, etc."}
    },
    {
        "question_text": "Which species or wild animal artifacts do you possess?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 65,
        "section": "Wildlife Artifacts",
        "depends_on": "Do you possess any animal trophies or wildlife articles?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List species and artifact types", "photo_upload": True}
    },

    # PART B: HUMAN-ELEPHANT INTERACTION
    {
        "question_text": "Have you ever seen elephant?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 66,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Are there any wild elephants in your village?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 67,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do they visit your crop fields?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 68,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are there any wild elephants in your village?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Do they raid your crops?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 69,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they visit your crop fields?",
        "depends_on_value": "Yes",
        "details": None
    },

    # ELEPHANT CATEGORY DETAILS FOR SINGLE/LONE INDIVIDUAL
    {
        "question_text": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "question_type": "multiple_choice",
        "options": ["Single/Lone individual", "Group/Herd"],
        "is_required": False,
        "order_index": 70,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": None
    },

    # SINGLE ELEPHANT DETAILS
    {
        "question_text": "Single Elephant - Adult Male with Tusks (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 71,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Adult Male (without Tusks) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 72,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Adult Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 73,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Adult (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 74,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Sub-adult Male (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 75,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Sub-adult Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 76,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Sub-adult (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 77,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Juvenile Male (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 78,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Juvenile Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 79,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Juvenile (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 80,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },
    {
        "question_text": "Single Elephant - Calves (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 81,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Single/Lone individual",
        "details": {"min": 0}
    },

    # GROUP/HERD ELEPHANT DETAILS
    {
        "question_text": "How many elephants did you observe in the group/herd?",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 82,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 2}
    },
    {
        "question_text": "Group Elephants - Adult Male with Tusks (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 83,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Adult Male (without Tusks) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 84,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Adult Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 85,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Adult (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 86,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Sub-adult Male (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 87,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Sub-adult Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 88,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Sub-adult (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 89,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Juvenile Male (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 90,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Juvenile Female (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 91,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Juvenile (Unidentified) (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 92,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },
    {
        "question_text": "Group Elephants - Calves (Number)",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 93,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Was the elephant that raided your crops a single/lone individual or group/herd?",
        "depends_on_value": "Group/Herd",
        "details": {"min": 0}
    },

    # CROP DAMAGE DETAILS
    {
        "question_text": "Area of crop damaged (acres/bigha/hectare)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 94,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify area and unit"}
    },
    {
        "question_text": "How frequent do they visit your crop field?",
        "question_type": "multiple_choice",
        "options": ["Once in a DAY", "Twice in a DAY", "Thrice in a DAY", "More in a DAY", "Once in WEEK", "Twice in a WEEK", "Thrice in a WEEK", "More in a WEEK", "Once in a MONTH", "Twice in a MONTH", "Thrice in a MONTH", "More in a MONTH", "Once in a YEAR", "Twice in a YEAR", "Thrice in a YEAR", "More in a YEAR"],
        "is_required": False,
        "order_index": 95,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Time of visit",
        "question_type": "multiple_choice",
        "options": ["Morning", "Evening", "Afternoon", "Night"],
        "is_required": False,
        "order_index": 96,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "What are the crops they raid? (List up to 10 crops with raiding seasons)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 97,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "List crops and their raiding seasons", "max_items": 10}
    },

    # PROPERTY DAMAGE BY ELEPHANTS
    {
        "question_text": "Any other property (other than crops) damaged by wild elephants?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 98,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do they raid your crops?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - House(s)",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 99,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Fencing",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 100,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Boundary walls",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 101,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Roads/paths",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 102,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Electricity poles/wires",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 103,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Water pipelines/tanks",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 104,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Type of property damage - Storage units (granaries, sheds, etc.)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 105,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify type of storage units damaged"}
    },
    {
        "question_text": "Type of property damage - Other (please specify)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 106,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other property (other than crops) damaged by wild elephants?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify other property damage"}
    },

    # ELEPHANT PRESENCE TIMELINE
    {
        "question_text": "Since when the elephants have been here?",
        "question_type": "multiple_choice",
        "options": ["Recently", "5 years", "10 years", "15 years", "More than 20 years"],
        "is_required": True,
        "order_index": 107,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Do you think the elephants have come from somewhere outside Nagaland?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 108,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Where have they come from? (please specify, if any)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 109,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do you think the elephants have come from somewhere outside Nagaland?",
        "depends_on_value": "Yes",
        "details": None
    },

    # HUMAN-ELEPHANT CONFLICT TIMELINE AND CAUSES
    {
        "question_text": "Since when human-elephant conflict has been prevailing here?",
        "question_type": "multiple_choice",
        "options": ["Recently", "5 years", "10 years", "15 years", "More than 20 years"],
        "is_required": True,
        "order_index": 110,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Has human-elephant conflict increased in recent years?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 111,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Why do you think the human-elephant conflict has increased in your area?",
        "question_type": "multiple_choice",
        "options": ["Deforestation / habitat loss", "Easy access to crops", "Increase in elephant population", "Reduction in availability of natural food inside forests", "Fragmentation of elephant corridors", "Expansion of agriculture near forests", "Loss of traditional elephant movement routes", "Lack of mitigation measures", "Seasonal migration of elephants through village areas", "Others"],
        "is_required": False,
        "order_index": 112,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Has human-elephant conflict increased in recent years?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "If others, please specify the reasons",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 113,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Why do you think the human-elephant conflict has increased in your area?",
        "depends_on_value": "Others",
        "details": None
    },

    # ELEPHANT DETERRENT METHODS
    {
        "question_text": "Do you drive away the wild elephants while they raid your crops?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 114,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "How do you drive elephants away from your crop during crop raiding/damaging?",
        "question_type": "multiple_choice",
        "options": ["Burning Firecrackers", "Burning Fire", "Arrow/Sling Shot", "Air Fire with Rifles/Airguns", "Others"],
        "is_required": False,
        "order_index": 115,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do you drive away the wild elephants while they raid your crops?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    {
        "question_text": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 116,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Prevention measure - Trenches",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 117,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Prevention measure - Solar Fencing",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 118,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Prevention measure - Electric Fencing",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 119,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Prevention measure - Barb wire Fencing",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": False,
        "order_index": 120,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Prevention measure - Other (Please specify)",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 121,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Any other measures that you have adopted/practiced to prevent elephants from entering your crop field?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify other prevention measures"}
    },

    # NIGHT DUTY/VIGIL
    {
        "question_text": "Do you stay on night duty (vigil) to guard against elephants or other wildlife?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 122,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "During which month(s) do you usually do night duty?",
        "question_type": "multiple_choice",
        "options": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "is_required": False,
        "order_index": 123,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Do you stay on night duty (vigil) to guard against elephants or other wildlife?",
        "depends_on_value": "Yes",
        "details": {"allow_multiple": True}
    },
    
    # HUMAN CASUALTIES AND INJURIES
    {
        "question_text": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "question_type": "yes_no",
        "options": ["Yes", "No"],
        "is_required": True,
        "order_index": 124,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": None,
        "depends_on_value": None,
        "details": None
    },
    {
        "question_text": "Was it an injury or fatality?",
        "question_type": "multiple_choice",
        "options": ["Injury", "Fatality"],
        "is_required": False,
        "order_index": 125,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "With which species or wild animal did the incident occur?",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 126,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Location/Village of incident",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 127,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "Age of person involved in incident",
        "question_type": "number",
        "options": None,
        "is_required": False,
        "order_index": 128,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": {"min": 0}
    },
    {
        "question_text": "Gender of person involved in incident",
        "question_type": "multiple_choice",
        "options": ["Male", "Female"],
        "is_required": False,
        "order_index": 129,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": None
    },
    {
        "question_text": "How long ago did the incident occur? Please specify",
        "question_type": "text",
        "options": None,
        "is_required": False,
        "order_index": 130,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": {"placeholder": "Specify time period (days, months, years ago)"}
    },
    {
        "question_text": "When did the incident happen?",
        "question_type": "multiple_choice",
        "options": ["Morning", "Afternoon", "Evening", "Night", "Don't remember"],
        "is_required": False,
        "order_index": 131,
        "section": "Part B: Human-Elephant Interaction",
        "depends_on": "Are you aware of any incidents where a human was injured or harmed by elephants or other wild animals?",
        "depends_on_value": "Yes",
        "details": None
    }
]
