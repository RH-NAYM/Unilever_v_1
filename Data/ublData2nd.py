from ultralytics import YOLO

# Initialize YOLO models
daModel = YOLO('AI_Models/ublDA_v1.pt')
qpdsModel = YOLO('AI_Models/best.pt')
sosModel = YOLO('AI_Models/ublDA_v1.pt')


########################################################################################################################################################################
# Perfect Store : 
psSkinCare_cream_GL = [ 
                        "gl_foundation_crm", 
                        "gl_aryuvedic_crm", 
                        "gl_mltvit_crm"
                        ]

psSkinCare_cream_ponds = [
                            "ponds_white_beauty_crm"
                            ]

psSkinCare_face_wash_GL = [
                            "gl_insta_glow_fw"
                            ]

psSkinCare_face_wash_ponds = [
                                "ponds_white_beauty_fw", 
                                "ponds_pure_white_fw", 
                                "ponds_oil_control_fw", 
                                "ponds_pure_white_clay_fw", 
                                "ponds_white_beauty_clay_fw"
                                ]

psHairCare_shampoo_sunsilk = [
                                "sunsilk_black_large",
                                "sunsilk_black_small",
                                "sunsilk_tl_large",
                                "sunsilk_tl_small",
                                "sunsilk_hfs",
                                "sunsilk_hrr",
                                "sunsilk_volume",
                                "sunsilk_fresh"
                                ]

psHairCare_shampoo_clear = [
                            "clear_ahf",
                            "clear_cac",
                            "clear_csm_large",
                            "clear_csm_small"
                            ]

psHairCare_shampoo_tresemme = [
                                "tresemme_cr",
                                "tresemme_ks_large",
                                "tresemme_ks_small"
                                ]

psHairCare_shampoo_dove = [
                            "dove_hfr_large",
                            "dove_hfr_small",
                            "dove_irp_large",
                            "dove_irp_small",
                            "dove_hg",
                            "dove_no"
                            ]

psHairCare_conditioner_dove = [
                                "dove_cond"
                                ]
########################################################################################################################################################################

# Nutrition Store : 
nsBoost = ["boost_std"]

nsHorlicks = [
                "horlicks_diabetic",
                "horlicks_choco",
                "horlicks_junior",
                "horlicks_lite",
                "horlicks_mother",
                "horlicks_std",
                "horlicks_women"
                ]

nsMaltova = ["maltova_std"]
########################################################################################################################################################################

# Drug Store : 
dsPepsodent = ["pepsodent"]
########################################################################################################################################################################

# QPDS : 
qpdsSkinCare_vaseline = [
                            "vaseline_tm",
                            "vaseline_hw",
                            "vaseline_aloe"
                            ]
qpdsSkinCare_dove = ["dove_qpds"]
########################################################################################################################################################################

# sos : 
comSkinCleansing_soap = [
                            "lux",
                            "lifeboy",
                            "tibbet",
                            "sandalina",
                            "detol",
                            "meril",
                            "savlon",
                            "keya",
                            "bactrol"
                            ]

comSkinCare_faceWash = [
                                "himalaya_fw"
                                ]

comNutrition_milk = [
                        "dano_pusti",
                        "marks"
                        ]

comOralCare_paste = [
                        "closeup",
                        "colgate",
                        "mediplus"
                        ]

comHomeHyg_clean = [
                        "harpic"
                        ]
########################################################################################################################################################################





########################################################################################################################################################################

psFC = [
            "gl_foundation_crm", 
            "gl_aryuvedic_crm", 
            "gl_mltvit_crm",
            "ponds_white_beauty_crm",
            "da_skin_care_st"
        ]


psFW = [
            "gl_insta_glow_fw",
            "ponds_white_beauty_fw", 
            "ponds_pure_white_fw", 
            "ponds_oil_control_fw", 
            "ponds_pure_white_clay_fw", 
            "ponds_white_beauty_clay_fw",
            "da_skin_care_st"
        ]


psHC = [
            "sunsilk_black_large",
            "sunsilk_black_small",
            "sunsilk_tl_large",
            "sunsilk_tl_small",
            "sunsilk_hfs",
            "sunsilk_hrr",
            "sunsilk_volume",
            "sunsilk_fresh",
            "clear_ahf",
            "clear_cac",
            "clear_csm_large",
            "clear_csm_small",
            "tresemme_cr",
            "tresemme_ks_large",
            "tresemme_ks_small",
            "dove_hfr_large",
            "dove_hfr_small",
            "dove_irp_large",
            "dove_irp_small",
            "dove_hg",
            "dove_no",
            "dove_cond",
            "da_hair_care_st"
        ]

nsNT = [
            "boost_std",
            "horlicks_diabetic",
            "horlicks_choco",
            "horlicks_junior",
            "horlicks_lite",
            "horlicks_mother",
            "horlicks_std",
            "horlicks_women",
            "da_nutrition_st"
        ]

dsOC = [
            "pepsodent",
            "da_oral_care_st"
        ]


qpdsSC = [
            "vaseline_tm",
            "vaseline_hw",
            "vaseline_aloe",
            "dove_qpds",
            "qpds_st"
        ]

