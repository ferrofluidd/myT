import os
import glob

DEFAULT_POS = (0,0,0)
DEFAULT_HPR = (180,0,0)

DEFAULT_CAMERA_POS = (0,-20,4.2)

SCREENSHOT_DIR = "../screenshots"
RESOURCES_DIR = "../resources"
CONFIG_DIR = "../VisorConfig.prc"

SUIT_A_MODEL = os.path.join(RESOURCES_DIR,"phase_3.5","models","char","suitA-mod.bam")
SUIT_B_MODEL = os.path.join(RESOURCES_DIR,"phase_3.5","models","char","suitB-mod.bam")
SUIT_C_MODEL = os.path.join(RESOURCES_DIR,"phase_3.5","models","char","suitC-mod.bam")

SHADOW_MODEL = os.path.join(RESOURCES_DIR,"phase_3","models","props","drop_shadow.bam")
SHADOW_SCALE = 0.45
SHADOW_COLOR = (0.0, 0.0, 0.0, 0.5)

COG_ICONS = os.path.join(RESOURCES_DIR,"phase_3.5","models","char","ttcc_ene_insignias.bam")
COG_ICONS_BASE = os.path.join(RESOURCES_DIR,"phase_3.5","models","char","ttcc_ene_insignias.bam")
COG_ICON_HPR = (0.00, 0.00, 0.00, 180.00, 0.00, 0.00, 1.00, 1.00, 1.00)

SHOE_TEXTURE = os.path.join(RESOURCES_DIR,"phase_3.5","maps","shoe.jpg")
HAND_TEXTURE = os.path.join(RESOURCES_DIR,"phase_3.5","maps","hand.jpg")
ARM_TEXTURE = os.path.join(RESOURCES_DIR,"phase_3.5","maps","s_arm.jpg")

SUIT_A_ANIMATION_PATHS = glob.glob(os.path.join(RESOURCES_DIR,"**","suitA-*.bam"), recursive=True)
SUIT_B_ANIMATION_PATHS = glob.glob(os.path.join(RESOURCES_DIR,"**","suitB-*.bam"), recursive=True)
SUIT_C_ANIMATION_PATHS = glob.glob(os.path.join(RESOURCES_DIR,"**","suitC-*.bam"), recursive=True)

SUIT_A_ANIMATION_DICT = {}
SUIT_B_ANIMATION_DICT = {}
SUIT_C_ANIMATION_DICT = {}

# split em up into dictionaries for the actor
for i in range(0, len(SUIT_A_ANIMATION_PATHS)):
    SUIT_A_ANIMATION_DICT[os.path.basename(SUIT_A_ANIMATION_PATHS[i])[13:-4]] = SUIT_A_ANIMATION_PATHS[i]

for i in range(0, len(SUIT_B_ANIMATION_PATHS)):
    SUIT_B_ANIMATION_DICT[os.path.basename(SUIT_B_ANIMATION_PATHS[i])[13:-4]] = SUIT_B_ANIMATION_PATHS[i]

for i in range(0, len(SUIT_C_ANIMATION_PATHS)):
    SUIT_C_ANIMATION_DICT[os.path.basename(SUIT_C_ANIMATION_PATHS[i])[13:-4]] = SUIT_C_ANIMATION_PATHS[i]

SUIT_A_ANIMATIONS = list(SUIT_A_ANIMATION_DICT)
SUIT_B_ANIMATIONS = list(SUIT_B_ANIMATION_DICT)
SUIT_C_ANIMATIONS = list(SUIT_C_ANIMATION_DICT)
SUIT_A_ANIMATIONS.sort()
SUIT_B_ANIMATIONS.sort()
SUIT_C_ANIMATIONS.sort()

COG_DATA = {
"foreman": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_4","models","char","ttr_m_ene_sellbotForeman.bam"),
           "hands": (0.886,0.737,0.784,1.0),
           "scale": 1.148,
           "dept": "s",
           "suit": "b",
           "emblem": "emblem_sales" },

"foreman_angry": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_4","models","char","ttr_m_ene_sellbotForemanAngry.bam"),
           "hands": (0.886,0.737,0.784,1.0),
           "scale": 1.148,
           "dept": "s",
           "suit": "b",
           "emblem": "emblem_sales" },

"auditor": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_4","models","char","ttr_m_ene_cashbotAuditor.bam"),
           "hands": (0.686,0.882,0.831,1.0),
           "scale": 1.378,
           "dept": "m",
           "suit": "c",
           "emblem": "emblem_money" },

"clerk": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_l.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_4","models","char","ttr_m_ene_lawbotClerk.bam"),
           "hands": (0.722,0.769,0.816,1.0),
           "scale": 1.323,
           "dept": "l",
           "suit": "b",
           "emblem": "emblem_legal" },

"club_president": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_4","models","char","ttr_m_ene_bossbotClubPresident.bam"),
           "hands": (0.950,0.750,0.750,1.0),
           "scale": 0.706,
           "dept": "c",
           "suit": "a",
           "emblem": "emblem_corp" },
"backstabber": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_l.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_11","models","char", "suits", "ttcc_ene_backstabber-zero.bam"),
           "hands": (0.950,0.750,0.750,1.0),
           "scale": 0.706,
           "dept": "l",
           "suit": "b",
           "emblem": "emblem_legal" },
}

