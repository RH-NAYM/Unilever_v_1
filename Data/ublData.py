import torch
# psModel = torch.hub.load('yolov5', 'custom', path='AI_Models/ublV5.pt', source='local', device=0)
# nsModel = torch.hub.load('yolov5', 'custom', path='AI_Models/ublV5.pt', source='local', device=0)
# dsModel = torch.hub.load('yolov5', 'custom', path='AI_Models/ublV5.pt', source='local', device=0)
# qpdsModel = torch.hub.load('yolov5', 'custom', path='AI_Models/ublV5.pt', source='local', device=0)
# competitorModel = torch.hub.load('yolov5', 'custom', path='AI_Models/ublV5.pt', source='local', device=0)

from ultralytics import YOLO
model = YOLO('AI_Models/ublV8.pt')
# psModel = YOLO('AI_Models/ublV5.pt')
# nsModel = YOLO('AI_Models/ublV5.pt')
# dsModel = YOLO('AI_Models/ublV5.pt')
# qpdsModel = YOLO('AI_Models/ublV5.pt')
# competitorModel = YOLO('AI_Models/ublV5.pt')

########################################################################################################################################################################

class_names = {
                0:"Dove_Oxygen", 
                1:"Sunsilk_Green",
                2:"Sunsilk_Purple",
                3:"Tresemme_Green",
                4:"Tresemme_HD",
                5:"a",
                6:"b",
                7:"c", 
                8:"d",
                9:"e",
                10:"f",
                11:"g",
                12:"h",
                13:"i",
                14:"j", 
                15:"k",
                16:"l",
                17:"m",
                18:"n",
                19:"o",
                20:"p",
                21:"q", 
                22:"r",
                23:"s",
                24:"t",
                25:"u",
                26:"v",
                27:"w"
                }

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
########################################################################################################################################################################

# Competitor : 
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


allItems = {
                "psSkinCare_cream_GL" : [ 
                                        "gl_foundation_crm", 
                                        "gl_aryuvedic_crm", 
                                        "gl_mltvit_crm"
                                        ],
                "psSkinCare_cream_ponds" : [
                                            "ponds_white_beauty_crm"
                                            ],

                "psSkinCare_face_wash_GL" : [
                                            "gl_insta_glow_fw"
                                            ],
                "psSkinCare_face_wash_ponds" : [
                                                "ponds_white_beauty_fw", 
                                                "ponds_pure_white_fw", 
                                                "ponds_oil_control_fw", 
                                                "ponds_pure_white_clay_fw", 
                                                "ponds_white_beauty_clay_fw"
                                                ],
                "psHairCare_shampoo_sunsilk" : [
                                                "sunsilk_black_large",
                                                "sunsilk_black_small",
                                                "sunsilk_tl_large",
                                                "sunsilk_tl_small",
                                                "sunsilk_hfs",
                                                "sunsilk_hrr",
                                                "sunsilk_volume",
                                                "sunsilk_fresh"
                                                ],
                "psHairCare_shampoo_clear" : [
                                            "clear_ahf",
                                            "clear_cac",
                                            "clear_csm_large",
                                            "clear_csm_small"
                                            ],
                "psHairCare_shampoo_tresemme" : [
                                                "tresemme_cr",
                                                "tresemme_ks_large",
                                                "tresemme_ks_small"
                                                ],
                "psHairCare_shampoo_dove" : [
                                            "dove_hfr_large",
                                            "dove_hfr_small",
                                            "dove_irp_large",
                                            "dove_irp_small",
                                            "dove_hg",
                                            "dove_no"
                                            ],
                "psHairCare_conditioner_dove" : [
                                                "dove_cond"
                                                ]
                }