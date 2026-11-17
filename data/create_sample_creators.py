"""
Generate realistic sample dataset of 36 fictional Pakistani creators for InfluMatch prototype.
All profiles are strictly fictional demo data for academic FYP presentation.
"""
import pandas as pd
import json
from pathlib import Path

creators_data = [
    # 1. Beauty & Skincare - Karachi - Micro
    {
        "creator_id": "PK-001",
        "creator_name": "Aiman Glow Diaries",
        "handle": "@aiman.glowdiaries",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Micro",
        "follower_count": 48500,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Affordable Skincare & Acne Care",
        "content_description": "Karachi-based skincare enthusiast testing local Pakistani dermatological brands, serums, and sunscreen routines for humid weather.",
        "audience_persona": "Young Pakistani women (aged 18-28) in Karachi looking for budget-friendly acne routines and glowing skin tips.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & English",
        "average_views": 32000,
        "engagement_rate": 4.8,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Karachi ki garmi mein oily skin aur breakouts se bachne ke liye ye 3 drugstore serums must-have hain! Non-greasy aur budget friendly.",
            "Aaj kal mera daily AM skincare routine: gentle foaming wash + hyaluronic acid + matte sunscreen. Sunscreen skip hargiz mat karein!",
            "Honest review: Kiya ye viral Pakistani vitamin C serum waqai acne scars ko lighten karta hai? Watch full reel for before & after!"
        ]),
        "public_profile_link": "https://instagram.com/demo_aiman_glow"
    },
    # 2. Beauty & Skincare - Lahore - Mid
    {
        "creator_id": "PK-002",
        "creator_name": "Zainab Glam Studio",
        "handle": "@zainab.glamstudio",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Mid",
        "follower_count": 210000,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Bridal Makeup & Premium Cosmetics",
        "content_description": "Lahore certified makeup artist showcasing Pakistani bridal glam, waterproof wedding season cosmetics, and high-end makeup masterclasses.",
        "audience_persona": "Brides-to-be and fashion-conscious young women (20-35) in Lahore and Punjab seeking wedding season looks.",
        "content_tone": "Professional",
        "language": "Roman Urdu & English",
        "average_views": 115000,
        "engagement_rate": 3.9,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Shaadi season ke liye flawless HD base secret! Sweatproof formula jo 12 ghantay tak bilkul fresh rahe bina cakey hue.",
            "Desi Barat look with soft cut crease and bold Pakistani bridal lip shade. Sab details reel mein share kar di hain.",
            "Drugstore vs High-end foundations battle: Kaunsi foundation Pakistani skin tones pe best oxidize nahi hoti?"
        ]),
        "public_profile_link": "https://instagram.com/demo_zainab_glam"
    },
    # 3. Beauty & Skincare - Karachi - Nano
    {
        "creator_id": "PK-003",
        "creator_name": "Hira Pure Care",
        "handle": "@hirapurecare",
        "platform": "TikTok",
        "city": "Karachi",
        "follower_tier": "Nano",
        "follower_count": 8200,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Desi Totkay & Organic Skincare",
        "content_description": "Authentic organic remedies and natural skincare routines using kitchen ingredients and safe herbs for university students.",
        "audience_persona": "College & university girls in Karachi on strict pocket-money budgets looking for natural glow.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu & Urdu",
        "average_views": 14000,
        "engagement_rate": 6.5,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Besan aur haldi wala homemade face pack jo tanned skin ko 15 minute mein refresh karde. Try karein aur comments mein batayein!",
            "Agar Karachi ke pani ki wajah se baal gir rahe hain to ye neem aur methi dana water rinse zaroor try karein.",
            "500 rupees ke andar basic daily skincare pouch: face wash, aloe vera gel aur rose water toner."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_hirapurecare"
    },
    # 4. Beauty & Skincare - Islamabad - Macro
    {
        "creator_id": "PK-004",
        "creator_name": "Dr. Mahnoor Aesthetics",
        "handle": "@drmahnoor_skin",
        "platform": "Instagram",
        "city": "Islamabad",
        "follower_tier": "Macro",
        "follower_count": 680000,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Dermatology Science & Chemical Peels",
        "content_description": "Licensed aesthetic doctor breaking down chemical exfoliants, SPF truths, and debunking dangerous fairness creams in Pakistan.",
        "audience_persona": "Educated urban women & men across Pakistan looking for evidence-based clinical skincare advice.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 340000,
        "engagement_rate": 4.1,
        "commercial_tier_pricing": "High",
        "sample_post_captions": json.dumps([
            "Stop using steroid creams for rang gora! Ye aapki skin barrier ko permanently damage kar sakti hain. Scientific explanation here.",
            "Salicylic acid vs Niacinamide: Open pores aur blackheads ke liye kaunsa ingredient kab aur kaise lagana chahiye?",
            "Sunscreen myth busted: Indoor lights mein bhi SPF zaroori hai ya nahi? Dermatologist perspective."
        ]),
        "public_profile_link": "https://instagram.com/demo_drmahnoor"
    },
    # 5. Food & Dining - Karachi - Micro
    {
        "creator_id": "PK-005",
        "creator_name": "Karachi Food Hunt (Bilal)",
        "handle": "@karachifoodhunt",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Micro",
        "follower_count": 76000,
        "primary_niche": "Food & Dining",
        "sub_niche": "Street Food & Desi Khabbay",
        "content_description": "Late-night Burns Road biryani, hidden roll corners in Nazimabad, and honest local eatery reviews across Karachi.",
        "audience_persona": "Desi foodies, students, and weekend hangout lovers in Karachi who live for spicy biryani and chai.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu",
        "average_views": 52000,
        "engagement_rate": 5.2,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Burns Road ki ye 40 saal purani beef nihari! Nalli aur maghaz ke saath garam tandoori roti ka koi muqabla nahi.",
            "Tariq road ka secret cheese roll paratha: Crisp aisa ke dil khush ho jaye. Sirf 250 rupees mein full value!",
            "Sehri spot recommendation in Karachi: Garam doodh jalebi aur lassi jo roza rakhne ke liye perfect fuel hai."
        ]),
        "public_profile_link": "https://instagram.com/demo_karachifoodhunt"
    },
    # 6. Food & Dining - Lahore - Macro
    {
        "creator_id": "PK-006",
        "creator_name": "Chef Adeel Kitchen",
        "handle": "@chefadeelpk",
        "platform": "YouTube",
        "city": "Lahore",
        "follower_tier": "Macro",
        "follower_count": 890000,
        "primary_niche": "Food & Dining",
        "sub_niche": "Traditional Pakistani Recipes & Ramadan Treats",
        "content_description": "Master recipes for commercial Degi Biryani, Mutton Karahi, Ramadan Iftar platters, and bakery snacks explained step-by-step.",
        "audience_persona": "Homemakers, home cooks, and diaspora Pakistanis wanting authentic restaurant-quality desi taste at home.",
        "content_tone": "Informative",
        "language": "Roman Urdu & Urdu",
        "average_views": 420000,
        "engagement_rate": 3.7,
        "commercial_tier_pricing": "High",
        "sample_post_captions": json.dumps([
            "Bawarchi style Degi Chicken Biryani recipe! Masala banane ka asan tarika jo har daana khushbudar banaye.",
            "Ramadan special: 5 different quick samosa fillings jo aap freezer mein 1 month tak store kar sakte hain.",
            "Lahori Chargha restaurant secret recipe: Masala marination aur steaming technique bina deep fry ke bhi perfect crisp."
        ]),
        "public_profile_link": "https://youtube.com/demo_chefadeel"
    },
    # 7. Food & Dining - Rawalpindi - Nano
    {
        "creator_id": "PK-007",
        "creator_name": "Pindi Food Snaps (Hamza)",
        "handle": "@pindifoodsnaps",
        "platform": "TikTok",
        "city": "Rawalpindi",
        "follower_tier": "Nano",
        "follower_count": 9400,
        "primary_niche": "Food & Dining",
        "sub_niche": "Budget Student Cafes & Chai Dhabas",
        "content_description": "Raja Bazaar samosa chaat, Kartarpura breakfast spots, and Rawalpindi highway chai spots on student budgets.",
        "audience_persona": "Twin city university students, hostelites, and young boys seeking cheap, delicious daily meals.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu",
        "average_views": 18000,
        "engagement_rate": 7.1,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Kartarpura pindi ka nashta scene! Halwa puri aur channay with chatti ki lassi. Pindi boys ka real Sunday routine.",
            "Hostel walo ke liye 200 rupees ka lunch challenge! Saddar Pindi ki ye daal chawal plate unmatchable hai.",
            "Mid-night chai session at Saddar: Doodh patti aisi ke neend gayab ho jaye aur semester exams pass!"
        ]),
        "public_profile_link": "https://tiktok.com/@demo_pindifood"
    },
    # 8. Technology & Gadgets - Lahore - Mid
    {
        "creator_id": "PK-008",
        "creator_name": "TechTalk Bilal",
        "handle": "@techtalkbilal",
        "platform": "YouTube",
        "city": "Lahore",
        "follower_tier": "Mid",
        "follower_count": 340000,
        "primary_niche": "Technology & Gadgets",
        "sub_niche": "Smartphone Reviews & Budget Tech in PKR",
        "content_description": "Detailed mobile comparisons in Pakistani rupee budget brackets (30k to 80k), PTA tax guides, and camera shootouts.",
        "audience_persona": "Pakistani tech buyers, students, and professionals looking for honest value-for-money gadget recommendations.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 180000,
        "engagement_rate": 4.3,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Under 50,000 PKR Best 5G Phones in Pakistan right now! Battery, display aur gaming benchmark test detailed comparison.",
            "PTA Approved vs Non-PTA: Kiya 2026 mein iPhone JV lena chahye? Sab hidden cons aur network restrictions jaan lein.",
            "Redmi vs Realme 60fps gaming test in intense PUBG squad fights: Kaunsa phone heat up hota hai?"
        ]),
        "public_profile_link": "https://youtube.com/demo_techtalkbilal"
    },
    # 9. Technology & Gadgets - Karachi - Micro
    {
        "creator_id": "PK-009",
        "creator_name": "Gadget Girl Sarah",
        "handle": "@gadgetgirlsarah",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Micro",
        "follower_count": 62000,
        "primary_niche": "Technology & Gadgets",
        "sub_niche": "Smart Home, Accessories & Creator Setups",
        "content_description": "Aesthetic desk setups, wireless earbuds, smartwatches, and vlogging camera setups for female content creators.",
        "audience_persona": "Young working professionals, remote workers, and content creators looking for chic, reliable work tech.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & English",
        "average_views": 44000,
        "engagement_rate": 5.0,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "My minimalist WFH desk setup tour! Wireless keyboard, mechanical mouse aur budget RGB lighting Karachi mein kahan se milein?",
            "Best budget noise-cancelling earbuds under 6k PKR. Mic quality test for online Zoom meetings aur calls.",
            "Smartwatch review for daily health tracking: Step count accuracy aur heart rate sensor test."
        ]),
        "public_profile_link": "https://instagram.com/demo_gadgetgirl"
    },
    # 10. Technology & Gadgets - Islamabad - Mega
    {
        "creator_id": "PK-010",
        "creator_name": "Usman Tech Studio",
        "handle": "@usmantechpk",
        "platform": "YouTube",
        "city": "Islamabad",
        "follower_tier": "Mega",
        "follower_count": 1450000,
        "primary_niche": "Technology & Gadgets",
        "sub_niche": "Flagship Smartphone Unboxings & Electric Vehicles",
        "content_description": "Top-tier tech reviews, flagship smartphone teardowns, high-end PC builds, and modern automotive technology in Pakistan.",
        "audience_persona": "Broad Pakistani gadget lovers, gamers, and tech enthusiasts nationwide.",
        "content_tone": "Professional",
        "language": "Roman Urdu & English",
        "average_views": 750000,
        "engagement_rate": 3.4,
        "commercial_tier_pricing": "High",
        "sample_post_captions": json.dumps([
            "Samsung Galaxy Ultra vs iPhone Pro Max Camera Shootout in Islamabad Margalla Hills! Zoom and night photography test.",
            "Pakistan's first affordable EV car review: Real-world range test, charging costs aur road performance.",
            "Custom 4K Gaming PC build in 2026: Pakistani market hardware rates aur GPU availability reality check."
        ]),
        "public_profile_link": "https://youtube.com/demo_usmantech"
    },
    # 11. Fashion & Lifestyle - Karachi - Micro
    {
        "creator_id": "PK-011",
        "creator_name": "Sana Desi Chic",
        "handle": "@sanadesichic",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Micro",
        "follower_count": 55000,
        "primary_niche": "Fashion & Lifestyle",
        "sub_niche": "Lawn Styling, Kurti Trends & Street Hauls",
        "content_description": "Budget-friendly everyday lawn styling, Zainab Market thrift finds, and modest aesthetic Pakistani fashion hacks.",
        "audience_persona": "University girls and young working women looking for affordable, trendy everyday wardrobe ideas.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & English",
        "average_views": 38000,
        "engagement_rate": 5.4,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "1 plain white chikankari kurti ko 4 mukhtalif tareeqon se style karein: University to family dinner looks!",
            "Zainab Market Karachi thrift haul under 3000 PKR! Western tops aur oversized shirts ki hidden shops.",
            "Summer lawn trends: Simple laces aur organza borders laga kar plain kapray ko designer look dein."
        ]),
        "public_profile_link": "https://instagram.com/demo_sanadesichic"
    },
    # 12. Fashion & Lifestyle - Lahore - Mid
    {
        "creator_id": "PK-012",
        "creator_name": "Fatima Sohail Couture",
        "handle": "@fatimasohail_style",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Mid",
        "follower_count": 280000,
        "primary_niche": "Fashion & Lifestyle",
        "sub_niche": "Bridal Wear, Luxury Pret & Eid Collections",
        "content_description": "High-end Pakistani bridal inspirations, luxury designer pret unboxings, and grand Lahore society wedding aesthetics.",
        "audience_persona": "Affluent women, brides-to-be, and overseas Pakistani shoppers seeking premium festive wear.",
        "content_tone": "Inspirational / Aspirational",
        "language": "Roman Urdu & English",
        "average_views": 160000,
        "engagement_rate": 4.0,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Eid Festive Collection 2026: Raw silk ensembles with intricate hand embroidery. Royal tones for festive evenings.",
            "Lahori wedding guest look: Velvet shawl pairing with minimalist pastel peshwas for winter barat.",
            "Designer pret review: Kiya luxury brands ka lawn fabric price justify karta hai? In-depth fabric quality check."
        ]),
        "public_profile_link": "https://instagram.com/demo_fatimasohail"
    },
    # 13. Fashion & Lifestyle - Faisalabad - Nano
    {
        "creator_id": "PK-013",
        "creator_name": "Mariam Daily Fits",
        "handle": "@mariamdailyfits",
        "platform": "TikTok",
        "city": "Faisalabad",
        "follower_tier": "Nano",
        "follower_count": 9100,
        "primary_niche": "Fashion & Lifestyle",
        "sub_niche": "Local Textile Hauls & Budget Dupattas",
        "content_description": "Faisalabad wholesale textile market shopping guides, custom tailoring ideas, and casual everyday shalwar kameez.",
        "audience_persona": "Budget shoppers and housewives in Punjab looking for wholesale fabric rates and tailor design patterns.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu",
        "average_views": 15000,
        "engagement_rate": 6.8,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Faisalabad Clock Tower market se saste printed lawn suits! Wholesale rates pe retail shopping ka tarika.",
            "Gala aur daman ke latest design jo tailor ko dikha kar asani se banwaye ja sakte hain.",
            "Chiffon dupattay dye karwane aur matching laces choose karne ki easy guide."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_mariamfits"
    },
    # 14. Fitness & Health - Karachi - Micro
    {
        "creator_id": "PK-014",
        "creator_name": "Coach Hamza Fit",
        "handle": "@coachhamzafit",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Micro",
        "follower_count": 72000,
        "primary_niche": "Fitness & Health",
        "sub_niche": "Desi Diet Plans & Fat Loss Workouts",
        "content_description": "Practical weight loss and gym advice tailored to Pakistani cuisine (Roti, Daal, Salan calorie counting without starvation).",
        "audience_persona": "Pakistani men & women (20-40) fighting belly fat who want to stay fit while eating homemade desi food.",
        "content_tone": "Inspirational / Aspirational",
        "language": "Roman Urdu & English",
        "average_views": 48000,
        "engagement_rate": 5.1,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Bina roti chawwal choray wazan kam karein! Desi khanon mein portion control aur calorie counting ka asan tareeqa.",
            "Karachi gym sessions: Dumbbell home workout un logon ke liye jinke paas gym jane ka time nahi hai.",
            "Pakistani diet protein sources: Eggs, channay, daal aur chicken breast se daily protein target kaise pura karein?"
        ]),
        "public_profile_link": "https://instagram.com/demo_coachhamza"
    },
    # 15. Fitness & Health - Lahore - Mid
    {
        "creator_id": "PK-015",
        "creator_name": "Ayesha Fit Woman PK",
        "handle": "@ayeshafitwoman",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Mid",
        "follower_count": 185000,
        "primary_niche": "Fitness & Health",
        "sub_niche": "PCOS Management & Female Strength Training",
        "content_description": "Dedicated to Pakistani women overcoming PCOS, hormonal imbalances, postpartum fitness, and home pilates.",
        "audience_persona": "Pakistani females dealing with hormonal weight gain, sedentary lifestyles, and postpartum recovery.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 95000,
        "engagement_rate": 4.6,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "PCOS aur stubborn belly fat: Subah ka empty stomach drink aur gentle strength exercises jo hormones balance karein.",
            "Desi methi dana aur cinnamon tea benefits for insulin resistance and digestion improvement.",
            "15-minute home resistance band workout for moms and working women. No fancy equipment needed!"
        ]),
        "public_profile_link": "https://instagram.com/demo_ayeshafit"
    },
    # 16. Travel & Tourism - Islamabad - Mid
    {
        "creator_id": "PK-016",
        "creator_name": "Wanderlust Farhan",
        "handle": "@wanderlustfarhan",
        "platform": "YouTube",
        "city": "Islamabad",
        "follower_tier": "Mid",
        "follower_count": 310000,
        "primary_niche": "Travel & Tourism",
        "sub_niche": "Northern Areas & Adventure Road Trips",
        "content_description": "Cinematic road trips to Hunza, Skardu, Fairy Meadows, and hidden valleys of Khyber Pakhtunkhwa and Gilgit Baltistan.",
        "audience_persona": "Adventure travelers, youth travel groups, and families planning holidays in Northern Pakistan.",
        "content_tone": "Inspirational / Aspirational",
        "language": "Roman Urdu & English",
        "average_views": 220000,
        "engagement_rate": 4.9,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Islamabad to Skardu via Karakoram Highway complete 7-day budget itinerary, hotel rates aur road condition guide.",
            "Winter in Hunza: Frozen Attabad Lake aur snowy pass ki breathtaking cinematic shots. Pakistan is truly heaven!",
            "Solo backpacking tips in Northern Pakistan: Transport, safe guest houses aur packing checklist."
        ]),
        "public_profile_link": "https://youtube.com/demo_wanderfarhan"
    },
    # 17. Travel & Tourism - Karachi - Nano
    {
        "creator_id": "PK-017",
        "creator_name": "Beach & Balochistan Trips (Tariq)",
        "handle": "@tariqcoastalpk",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Nano",
        "follower_count": 7800,
        "primary_niche": "Travel & Tourism",
        "sub_niche": "Kund Malir, Astola Island & Coastal Highway",
        "content_description": "Weekend camping tours, stargazing at Kund Malir, scuba diving at Charna Island, and Makran Coastal highway drives.",
        "audience_persona": "Karachi thrill-seekers, college groups, and weekend road trip fans.",
        "content_tone": "Friendly",
        "language": "Roman Urdu",
        "average_views": 16000,
        "engagement_rate": 6.2,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Kund Malir aur Hingol National park weekend road trip guide from Karachi. Budget per person under 5000 PKR!",
            "Astola Island camping experience: Crystal clear blue water aur untouched beaches of Balochistan.",
            "Charna Island snorkeling season guide: Best time, safety boat tips aur underwater video clips."
        ]),
        "public_profile_link": "https://instagram.com/demo_tariqcoastal"
    },
    # 18. Gaming & Esports - Lahore - Micro
    {
        "creator_id": "PK-018",
        "creator_name": "Saad PUBG Gamer",
        "handle": "@saadgamerpk",
        "platform": "TikTok",
        "city": "Lahore",
        "follower_tier": "Micro",
        "follower_count": 92000,
        "primary_niche": "Gaming & Esports",
        "sub_niche": "PUBG Mobile, Free Fire & Gameplay Highlights",
        "content_description": "Competitive mobile gaming clutches, Pakistani tournament scrims, funny squad voice chat moments, and device gyro settings.",
        "audience_persona": "Young Pakistani boys and teenagers (14-25) addicted to mobile gaming and esports streaming.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu",
        "average_views": 85000,
        "engagement_rate": 7.4,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "1v4 clutch in Bootcamp! Jab random team mates mar jayein to akele kaise round save karein? Watch till end!",
            "PUBG Mobile 90fps best sensitivity settings for smooth recoil control. Gyroscope player guide.",
            "Desi squad voice chat fun: Jab Pakistani uncle mic on karke bachon pe chillayein gameplay ke doran."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_saadgamer"
    },
    # 19. Gaming & Esports - Karachi - Mid
    {
        "creator_id": "PK-019",
        "creator_name": "Alpha PK Gaming",
        "handle": "@alphagamingpk",
        "platform": "YouTube",
        "city": "Karachi",
        "follower_tier": "Mid",
        "follower_count": 420000,
        "primary_niche": "Gaming & Esports",
        "sub_niche": "PC Gaming, GTA RP & Live Streaming",
        "content_description": "Pakistani GTA 5 Roleplay servers, high-octane Valorant matches, funny stream reactions, and gaming rig benchmarks.",
        "audience_persona": "Hardcore Pakistani gamers, university tech students, and PC hardware fans.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu & English",
        "average_views": 210000,
        "engagement_rate": 5.3,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Karachi GTA RP Server: Police chase mein Pakistani rickshaw se escape karne ki failed koshish! Funniest stream moments.",
            "Valorant Diamond to Immortal ranked grind with Pakistani lobby: Insane clutch headshots with Vandal.",
            "RTX 4060 vs RTX 3060ti: Budget PC gaming builds in Pakistan ke liye kaunsa GPU best value hai?"
        ]),
        "public_profile_link": "https://youtube.com/demo_alphagaming"
    },
    # 20. Education & Career - Islamabad - Micro
    {
        "creator_id": "PK-020",
        "creator_name": "Taleem & Tech (Engr. Salman)",
        "handle": "@taleemtechpk",
        "platform": "YouTube",
        "city": "Islamabad",
        "follower_tier": "Micro",
        "follower_count": 88000,
        "primary_niche": "Education & Career",
        "sub_niche": "Freelancing, Upwork Skills & Remote Jobs",
        "content_description": "Practical guides on Upwork, Fiverr, Python coding, and AI tools for Pakistani youth looking to earn in USD.",
        "audience_persona": "Pakistani graduates, college students, and entry-level freelancers seeking remote online earning skills.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 56000,
        "engagement_rate": 5.8,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Pakistan se Upwork pe pehla project kaise lein? Winning proposal writing template aur portfolio guide.",
            "2026 mein freelance skills in demand: Web development, AI data entry, aur video editing jo achi income dein.",
            "Payoneer aur local Pakistani bank account linking process: Dollar payout receive karne ka legal tarika."
        ]),
        "public_profile_link": "https://youtube.com/demo_taleemtech"
    },
    # 21. Education & Career - Lahore - Nano
    {
        "creator_id": "PK-021",
        "creator_name": "CSS Aspirants Guide (Nimra)",
        "handle": "@cssguide.nimra",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Nano",
        "follower_count": 8700,
        "primary_niche": "Education & Career",
        "sub_niche": "CSS / PMS Exam Prep & English Essay",
        "content_description": "Study timetables, Dawn newspaper vocabulary breakdown, and optional subject selection strategies for civil service exams.",
        "audience_persona": "Serious CSS, PMS, and competitive exam aspirants across Punjab and Sindh universities.",
        "content_tone": "Professional",
        "language": "Roman Urdu & English",
        "average_views": 17000,
        "engagement_rate": 6.9,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Dawn editorial vocabulary notes for CSS aspirants: Daily 5 powerful words with contextual sentence examples.",
            "CSS English Essay structuring: Outline kaise banayein jo examiner ko instantly impress kare.",
            "10-hour daily study routine: Burnout se bachte hue focus sustain karne ke psychological tips."
        ]),
        "public_profile_link": "https://instagram.com/demo_cssnimra"
    },
    # 22. Entertainment & Comedy - Karachi - Macro
    {
        "creator_id": "PK-022",
        "creator_name": "Desi Vines Karachi (Faizan)",
        "handle": "@desivineskarachi",
        "platform": "TikTok",
        "city": "Karachi",
        "follower_tier": "Macro",
        "follower_count": 720000,
        "primary_niche": "Entertainment & Comedy",
        "sub_niche": "Family Relatable Sketches & Desi Rishta Parodies",
        "content_description": "Hilarious parodies of Pakistani wedding aunties, electricity load-shedding struggles, and desi parents typical conversations.",
        "audience_persona": "Mass Pakistani audience across demographics who love clean family humor and relatable daily desi tropes.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu",
        "average_views": 510000,
        "engagement_rate": 6.7,
        "commercial_tier_pricing": "High",
        "sample_post_captions": json.dumps([
            "Jab rishtay wale ghar aate hain: Pakistani Ammi ki non-stop acting aur chai ke sath biscuit etiquette!",
            "Bijli ka bill dekh kar Abba ka reaction: Pure ghar ke pankhay aur lights band karwane ka scene.",
            "Exam result wale din har Pakistani rishtedaar ka phone call: Number kitne aye beta?"
        ]),
        "public_profile_link": "https://tiktok.com/@demo_faizanvines"
    },
    # 23. Entertainment & Comedy - Rawalpindi - Mid
    {
        "creator_id": "PK-023",
        "creator_name": "Pindi Boyz Rants",
        "handle": "@pindiboyzrants",
        "platform": "Instagram",
        "city": "Rawalpindi",
        "follower_tier": "Mid",
        "follower_count": 230000,
        "primary_niche": "Entertainment & Comedy",
        "sub_niche": "Local Slang & Cricket Humor",
        "content_description": "Hilarious reactions to Pakistan Cricket Team matches, PSL match rants, and Twin City culture humor.",
        "audience_persona": "Young men, cricket fans, and teenagers who follow PSL and Pakistani sports memes.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu",
        "average_views": 160000,
        "engagement_rate": 5.9,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Pakistan team ka collapse dekh kar har fan ka dil: Kudrat ka nizaam abhi bhi umeed pe zinda hai!",
            "PSL season fever: Lahore Qalandars vs Karachi Kings match rivalry aur fan banter at Pindi Stadium.",
            "Rawalpindi ki barish aur metro bus ka rush: Pindi youth ka daily travel survival guide."
        ]),
        "public_profile_link": "https://instagram.com/demo_pindirants"
    },
    # 24. Parenting & Family - Lahore - Micro
    {
        "creator_id": "PK-024",
        "creator_name": "Dr. Nadia Mom Life",
        "handle": "@drnadiamomlife",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Micro",
        "follower_count": 67000,
        "primary_niche": "Parenting & Family",
        "sub_niche": "Toddler Nutrition & Positive Parenting",
        "content_description": "Pediatrician-mom sharing toddler food ideas, weaning recipes, screen-time solutions, and gentle parenting tips.",
        "audience_persona": "Pakistani mothers (aged 24-38) with young children seeking practical child healthcare and developmental advice.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & English",
        "average_views": 41000,
        "engagement_rate": 4.7,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Bachon ke liye 5 easy nutrient-rich snacks: Oats porridge, banana pancakes aur khajoor milkshake bina refined sugar ke.",
            "Tantrums handle karne ka gentle parenting approach: Cheekhnay ke bajaye bache ke emotions validate karein.",
            "Mausam badalnay pe bachon ki khansi aur nazla: Gharelu ehtiyat aur kab pediatrician ke paas jana zaroori hai."
        ]),
        "public_profile_link": "https://instagram.com/demo_drnadiamom"
    },
    # 25. Parenting & Family - Karachi - Mid
    {
        "creator_id": "PK-025",
        "creator_name": "Pakistani Mom Diaries (Sobia)",
        "handle": "@pakistanimomdiaries",
        "platform": "Facebook",
        "city": "Karachi",
        "follower_tier": "Mid",
        "follower_count": 195000,
        "primary_niche": "Parenting & Family",
        "sub_niche": "Family Meals, School Tiffins & Home Organization",
        "content_description": "Daily family grocery budgeting, school lunchbox prep routines, and Pakistani joint-family life hacks.",
        "audience_persona": "Housewives, working moms, and joint family homemakers across urban Pakistan.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu & Urdu",
        "average_views": 88000,
        "engagement_rate": 3.8,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Weekly school lunchbox meal prep: 5 easy healthy items jo subah 10 minute mein tiffin mein pack ho sakein.",
            "Joint family kitchen management: Grocery budget maintain karte hue monthly kitchen stock manage karein.",
            "Weekend family routine in Karachi: Bachon ke sath picnic at Sea View aur home cooked biryani."
        ]),
        "public_profile_link": "https://facebook.com/demo_pakistanimom"
    },
    # 26. Beauty & Skincare - Multan - Nano
    {
        "creator_id": "PK-026",
        "creator_name": "Multan Beauty Journal (Komal)",
        "handle": "@multanbeauty.komal",
        "platform": "Instagram",
        "city": "Multan",
        "follower_tier": "Nano",
        "follower_count": 7500,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Summer Sun Protection & Herbal Ubtan",
        "content_description": "Skincare suited for extreme Southern Punjab heat, Multani mitti body masks, and traditional fragrant bridal ubtan.",
        "audience_persona": "College girls and women in Multan, Bahawalpur, and South Punjab facing scorching heat and tanning.",
        "content_tone": "Friendly",
        "language": "Roman Urdu",
        "average_views": 13000,
        "engagement_rate": 6.1,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Multan ki shadeed garmi mein Multani mitti face pack: Sandalwood powder aur rose water ke sath cooling mask.",
            "Sun tan removal in 1 week: Natural tomato and curd remedy jo arms aur neck ki pigmentation kam kare.",
            "Budget sweatproof foundation routine for Southern Punjab summer weddings."
        ]),
        "public_profile_link": "https://instagram.com/demo_multanbeauty"
    },
    # 27. Fashion & Lifestyle - Peshawar - Micro
    {
        "creator_id": "PK-027",
        "creator_name": "Peshawar Style Hub (Asad)",
        "handle": "@peshawarstylehub",
        "platform": "TikTok",
        "city": "Peshawar",
        "follower_tier": "Micro",
        "follower_count": 49000,
        "primary_niche": "Fashion & Lifestyle",
        "sub_niche": "Traditional Peshawari Chappal & Kurta Waistcoat",
        "content_description": "Handmade leather Peshawari chappals, traditional Pashtun vests, waistcoats, and modern festive men's styling.",
        "audience_persona": "Young men in KP and Islamabad seeking traditional Pashtun & Pakistani festive menswear styling.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu & Pashto",
        "average_views": 39000,
        "engagement_rate": 5.6,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Authentic handmade Peshawari Chappal making process in Namak Mandi! Real leather durability check.",
            "Eid men styling: Black shalwar kameez with gold waistcoat and classic Kaptaan chappal look.",
            "Traditional shawl drape styles for cold winter nights in Peshawar and KP."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_peshawarstyle"
    },
    # 28. Food & Dining - Hyderabad - Nano
    {
        "creator_id": "PK-028",
        "creator_name": "Hyderabadi Zaika (Noman)",
        "handle": "@hyderabadizaika",
        "platform": "Facebook",
        "city": "Hyderabad",
        "follower_tier": "Nano",
        "follower_count": 8900,
        "primary_niche": "Food & Dining",
        "sub_niche": "Sindhi Biryani & Bombay Bakery Treats",
        "content_description": "Exploring iconic Bombay Bakery coffee cakes, Shahi bazaar Rabri, and fiery spicy Sindhi biryani hidden spots.",
        "audience_persona": "Food lovers in Hyderabad, Jamshoro university students, and Karachi day-trippers visiting Sindh.",
        "content_tone": "Casual & Desi",
        "language": "Roman Urdu & Sindhi",
        "average_views": 14000,
        "engagement_rate": 6.3,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Hyderabad ki famous Bombay Bakery Coffee Cake lene ke liye lambi line! Is it worth the hype? Honest review.",
            "Chhotki Gali ki authentic Sindhi Biryani: Aloo aur tez masalaydar boti with chilled mint raita.",
            "Shahi Bazaar ki Thandi Rabri: Matkay wali desi rabri with pistachios and khoya."
        ]),
        "public_profile_link": "https://facebook.com/demo_hydzaika"
    },
    # 29. Travel & Tourism - Lahore - Mid
    {
        "creator_id": "PK-029",
        "creator_name": "Heritage Trails PK (Zohair)",
        "handle": "@heritagetrailspk",
        "platform": "Instagram",
        "city": "Lahore",
        "follower_tier": "Mid",
        "follower_count": 175000,
        "primary_niche": "Travel & Tourism",
        "sub_niche": "Walled City Lahore, Mughal Architecture & Heritage",
        "content_description": "Walking tours inside the 12 Gates of Lahore, Badshahi Mosque sunset photography, and hidden architectural gems.",
        "audience_persona": "History enthusiasts, photography buffs, cultural tourists, and overseas Pakistanis visiting Lahore.",
        "content_tone": "Inspirational / Aspirational",
        "language": "Roman Urdu & English",
        "average_views": 98000,
        "engagement_rate": 4.4,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Sunset at Badshahi Mosque: Mughal architecture ke lajawab patterns aur peaceful spiritual atmosphere.",
            "Exploring the underground Turkish Hamam at Delhi Gate Lahore: 400 saal purani tareekh ki zinda tasveer.",
            "Night photography walk in Walled City: Haveli views, historic lanterns aur street food fragrance."
        ]),
        "public_profile_link": "https://instagram.com/demo_heritagetrails"
    },
    # 30. Fitness & Health - Islamabad - Nano
    {
        "creator_id": "PK-030",
        "creator_name": "Margalla Trail Runners (Saqib)",
        "handle": "@margallatrailrunners",
        "platform": "Instagram",
        "city": "Islamabad",
        "follower_tier": "Nano",
        "follower_count": 6900,
        "primary_niche": "Fitness & Health",
        "sub_niche": "Trail Running, Hiking & Outdoor Stamina",
        "content_description": "Trail 3 and Trail 5 weekend hiking groups, outdoor endurance cardio, hydration tips, and natural fitness.",
        "audience_persona": "Outdoor fitness fans, corporate employees in Islamabad looking for weekend hikes and cardio workouts.",
        "content_tone": "Inspirational / Aspirational",
        "language": "Roman Urdu & English",
        "average_views": 12000,
        "engagement_rate": 6.4,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Early morning Trail 3 hike in Margalla Hills: 5km uphill cardio hike that energizes your entire week!",
            "Proper hiking shoes vs ordinary sneakers: Rocky trails pe slip hone se kaise bachein?",
            "Electrolyte hydration recipe for summer outdoor workouts: Pink salt, lemon aur honey water mix."
        ]),
        "public_profile_link": "https://instagram.com/demo_margallatrails"
    },
    # 31. Beauty & Skincare - Lahore - Micro
    {
        "creator_id": "PK-031",
        "creator_name": "Rida Clean Beauty",
        "handle": "@ridacleanbeauty",
        "platform": "TikTok",
        "city": "Lahore",
        "follower_tier": "Micro",
        "follower_count": 58000,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Cruelty-free & Halal Skincare Brands",
        "content_description": "Promoting ethical, cruelty-free, alcohol-free halal certified beauty items, calming barrier serums, and gentle care.",
        "audience_persona": "Conscious Muslim female consumers seeking pure, halal-compliant, and gentle skin products in Pakistan.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 40000,
        "engagement_rate": 5.0,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Halal certified skincare brands in Pakistan: Kaunsi companies waqai safe aur non-toxic ingredients use karti hain?",
            "Centella Asiatica calming serum review: Redness aur sensitive skin ke liye soothing magic.",
            "Wudhu-friendly skincare routine: Light hydration jo pores clog kiye bina fresh glow de."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_ridabeauty"
    },
    # 32. Fashion & Lifestyle - Karachi - Mid
    {
        "creator_id": "PK-032",
        "creator_name": "Shahroz Modern Gent",
        "handle": "@shahrozmoderngent",
        "platform": "Instagram",
        "city": "Karachi",
        "follower_tier": "Mid",
        "follower_count": 160000,
        "primary_niche": "Fashion & Lifestyle",
        "sub_niche": "Men's Formal Suits, Grooming & Fragrances",
        "content_description": "Men's tailored suits, luxury Pakistani attars and perfumes, beard grooming, and wedding wardrobe for men.",
        "audience_persona": "Corporate men, grooms, and young Pakistani professionals interested in smart suiting and fine fragrances.",
        "content_tone": "Professional",
        "language": "Roman Urdu & English",
        "average_views": 85000,
        "engagement_rate": 4.2,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "Top 5 long-lasting summer perfumes for Pakistani weather! Jo garmi aur pasine mein bhi 8 ghantay chal sakein.",
            "Groom wedding guide: Bespoke sherwani vs modern tuxedo styling for your big day.",
            "Beard care essential oils: Patchy beard ko maintain aur groom karne ke practical steps."
        ]),
        "public_profile_link": "https://instagram.com/demo_shahrozgent"
    },
    # 33. Food & Dining - Multan - Micro
    {
        "creator_id": "PK-033",
        "creator_name": "Sohna Multan Foods (Waqas)",
        "handle": "@sohnamultanfoods",
        "platform": "TikTok",
        "city": "Multan",
        "follower_tier": "Micro",
        "follower_count": 65000,
        "primary_niche": "Food & Dining",
        "sub_niche": "Sohan Halwa, Multani Mangoes & Chaat",
        "content_description": "Original Hafiz Sohan Halwa tasting, Chaunsa mango seasonal varieties, and Multani spicy fish fries.",
        "audience_persona": "Desi food tourists, sweet lovers, and families seeking authentic traditional South Punjab flavors.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & Saraiki",
        "average_views": 46000,
        "engagement_rate": 5.3,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "Hussain Agahi Multan ka 70 saal purana Asli Desi Ghee Sohan Halwa! Banane ka live process dekhain.",
            "Multan mango harvest season: Anwar Ratol vs Chaunsa. Kaunsa aam sab se metha aur khushbudaar hai?",
            "Multani fried fish with special crushed red pepper chutney in cold winter evening."
        ]),
        "public_profile_link": "https://tiktok.com/@demo_multanfoods"
    },
    # 34. Education & Career - Karachi - Mid
    {
        "creator_id": "PK-034",
        "creator_name": "Career Compass PK (Kashif)",
        "handle": "@careercompasspk",
        "platform": "YouTube",
        "city": "Karachi",
        "follower_tier": "Mid",
        "follower_count": 240000,
        "primary_niche": "Education & Career",
        "sub_niche": "University Admissions & Scholarship Guides",
        "content_description": "IBA, FAST, NUST admission entry test prep, fully funded scholarships abroad (Erasmus, Fulbright), and career paths.",
        "audience_persona": "High school and undergraduate students, parents planning university admissions in Pakistan and abroad.",
        "content_tone": "Informative",
        "language": "Roman Urdu & English",
        "average_views": 130000,
        "engagement_rate": 4.5,
        "commercial_tier_pricing": "Medium",
        "sample_post_captions": json.dumps([
            "FAST vs NUST for Computer Science: Entry test syllabus, merit criteria aur job placement ground reality.",
            "Erasmus Mundus scholarship step-by-step application guide: Zero tuition fees and 1400 Euro monthly stipend for Pakistani students.",
            "How to prepare for IBA Karachi aptitude test: Math shortcuts and critical reading strategy."
        ]),
        "public_profile_link": "https://youtube.com/demo_careercompass"
    },
    # 35. Entertainment & Comedy - Lahore - Mega
    {
        "creator_id": "PK-035",
        "creator_name": "Lahori Haspatal (Junaid)",
        "handle": "@lahorihaspatal",
        "platform": "YouTube",
        "city": "Lahore",
        "follower_tier": "Mega",
        "follower_count": 1200000,
        "primary_niche": "Entertainment & Comedy",
        "sub_niche": "Street Pranks & Lahori Jugat Baazi",
        "content_description": "Good-natured public social experiments, witty Lahori street interviews, and viral situational comedy clips.",
        "audience_persona": "Youth, students, and general Pakistani households looking for pure entertainment and laughing sessions.",
        "content_tone": "Humorous / Entertaining",
        "language": "Roman Urdu & Punjabi",
        "average_views": 620000,
        "engagement_rate": 5.0,
        "commercial_tier_pricing": "High",
        "sample_post_captions": json.dumps([
            "Lahori Jugat Challenge at Anarkali Bazaar: Awam ka spontaneous hazir jawabi response sun kar hansi nahi rukegi!",
            "Fake foreign tourist speaking fluent Punjabi in Liberty Market: Shopkeepers ke shock expressions!",
            "When students face viva exam unprepared: Hilarious excuses to professors compilation."
        ]),
        "public_profile_link": "https://youtube.com/demo_lahorihaspatal"
    },
    # 36. Beauty & Skincare - Islamabad - Micro
    {
        "creator_id": "PK-036",
        "creator_name": "Alizeh Pure Glow",
        "handle": "@alizehpureglow",
        "platform": "Instagram",
        "city": "Islamabad",
        "follower_tier": "Micro",
        "follower_count": 42000,
        "primary_niche": "Beauty & Skincare",
        "sub_niche": "Korean Skincare for Pakistani Climate",
        "content_description": "Imported Korean glass skin routines adapted for Islamabad dry winters and humid monsoon seasons. Snail mucin and barrier repair.",
        "audience_persona": "Urban females in Islamabad and Rawalpindi interested in glass skin aesthetics and gentle Korean hydration.",
        "content_tone": "Friendly",
        "language": "Roman Urdu & English",
        "average_views": 31000,
        "engagement_rate": 5.5,
        "commercial_tier_pricing": "Low",
        "sample_post_captions": json.dumps([
            "K-Beauty glass skin routine: Snail mucin aur rice toner ko Pakistani dry weather mein layer karne ka sahi order.",
            "Affordable Korean dupes available in Islamabad pharmacies for barrier repair creams.",
            "Double cleansing 101: Oil cleanser followed by water-based foam wash se stubborn makeup aur SPF easily remove karein."
        ]),
        "public_profile_link": "https://instagram.com/demo_alizehglow"
    }
]

df = pd.DataFrame(creators_data)
output_path = Path("c:/Users/shahz/OneDrive/Desktop/frontend/data/creators.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Generated {len(df)} creators successfully at {output_path}")
