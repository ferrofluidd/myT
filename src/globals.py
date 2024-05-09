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
    SUIT_A_ANIMATION_DICT[os.path.basename(SUIT_A_ANIMATION_PATHS[i])[5:-4]] = SUIT_A_ANIMATION_PATHS[i]

for i in range(0, len(SUIT_B_ANIMATION_PATHS)):
    SUIT_B_ANIMATION_DICT[os.path.basename(SUIT_B_ANIMATION_PATHS[i])[5:-4]] = SUIT_B_ANIMATION_PATHS[i]

for i in range(0, len(SUIT_C_ANIMATION_PATHS)):
    SUIT_C_ANIMATION_DICT[os.path.basename(SUIT_C_ANIMATION_PATHS[i])[5:-4]] = SUIT_C_ANIMATION_PATHS[i]

SUIT_A_ANIMATIONS = list(SUIT_A_ANIMATION_DICT)
SUIT_B_ANIMATIONS = list(SUIT_B_ANIMATION_DICT)
SUIT_C_ANIMATIONS = list(SUIT_C_ANIMATION_DICT)
SUIT_A_ANIMATIONS.sort()
SUIT_B_ANIMATIONS.sort()
SUIT_C_ANIMATIONS.sort()

COG_DATA = {
"flunky": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_flunky.bam"),
           "hands": (0.949, 0.749, 0.749, 1.000),
           "name": "flunky",
           "scale": 0.96618,
           "dept": "c",
           "suit": "c",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"pencilpusher": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_pencilpusher.bam"),
           "name": "featherbedder",
           "hands": (0.580, 0.475, 0.455, 1.000),
           "scale": 0.63327,
           "dept": "c",
           "suit": "b",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"yesman": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_yesman.bam"),
           "hands": (0.823, 0.839, 0.835, 1.000),
           "name": "yesman",
           "scale": 0.68069,
           "dept": "c",
           "suit": "a",
           "emblem": "emblem_corp" },
"micromanager": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_micromanager.bam"),
           "hands": (0.949, 0.749, 0.749, 1.000),
           "name": "flunky",
           "scale": 0.24154,
           "dept": "c",
           "suit": "c",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"downsizer": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_downsizer.bam"),
           "name": "featherbedder",
           "hands": (0.644, 0.698, 0.659, 1.000),
           "scale": 0.85066,
           "dept": "c",
           "suit": "b",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"headhunter": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_headhunter.bam"),
           "hands": (0.949, 0.749, 0.749, 1.000),
           "name": "yesman",
           "scale": 1.07260,
           "dept": "c",
           "suit": "a",
           "emblem": "emblem_corp" },
"corporateraider": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_corporateraider.bam"),
           "name": "featherbedder",
           "hands": (0.792, 0.675, 0.623, 1.000),
           "scale": 1.63043,
           "dept": "c",
           "suit": "c",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"bigcheese": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_c.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_12","models","char", "suits", "ttcc_ene_bigcheese.bam"),
           "hands": (0.651, 0.804, 0.451, 1.000),
           "name": "yesman",
           "scale": 1.15511,
           "dept": "c",
           "suit": "a",
           "emblem": "emblem_corp" },
"shortchange": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_shortchange.bam"),
           "hands": (0.294, 0.651, 0.870, 1.000),
           "name": "flunky",
           "scale": 0.60386,
           "dept": "m",
           "suit": "c",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"pennypincher": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_pennypincher.bam"),
           "name": "featherbedder",
           "hands": (0.784, 0.329, 0.298, 1.000),
           "scale": 0.58580,
           "dept": "m",
           "suit": "a",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"tightwad": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_tightwad.bam"),
           "hands": (0.655, 0.945, 0.847, 1.000),
           "name": "yesman",
           "scale": 1.08695,
           "dept": "m",
           "suit": "c",
           "emblem": "emblem_corp" },
"beancounter": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_beancounter.bam"),
           "hands": (0.640, 0.690, 0.659, 1.000),
           "name": "flunky",
           "scale": 0.83175,
           "dept": "m",
           "suit": "b",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"numbercruncher": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_numbercruncher.bam"),
           "name": "featherbedder",
           "hands": (0.655, 0.945, 0.847, 1.000),
           "scale": 0.86633,
           "dept": "m",
           "suit": "a",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"moneybags": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_moneybags.bam"),
           "hands": (0.671, 0.761, 0.737, 1.000),
           "name": "yesman",
           "scale": 1.28019,
           "dept": "m",
           "suit": "c",
           "emblem": "emblem_corp" },
"loanshark": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_loanshark.bam"),
           "name": "featherbedder",
           "hands": (0.671, 0.761, 0.737, 1.000),
           "scale": 1.22873,
           "dept": "m",
           "suit": "b",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"robberbaron": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_m.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_10","models","char", "suits", "ttcc_ene_robberbaron.bam"),
           "hands": (0.737, 0.788, 0.769, 1.000),
           "name": "yesman",
           "scale": 1.15511,
           "dept": "m",
           "suit": "a",
           "emblem": "emblem_corp" },
    
"coldcaller": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_coldcaller.bam"),
           "hands": (0.082, 0.204, 0.745, 1.000),
           "name": "flunky",
           "scale": 0.84541,
           "dept": "s",
           "suit": "c",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"telemarketer": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_telemarketer.bam"),
           "name": "featherbedder",
           "hands": (0.918, 0.808, 0.761, 1.000),
           "scale": 0.70888,
           "dept": "s",
           "suit": "b",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"namedropper": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_namedropper.bam"),
           "hands": (0.714, 0.694, 0.819, 1.000),
           "name": "yesman",
           "scale": 0.71782,
           "dept": "m",
           "suit": "a",
           "emblem": "emblem_corp" },
"gladhander": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_gladhander.bam"),
           "hands": (0.835, 0.851, 0.847, 1.000),
           "name": "flunky",
           "scale": 1.14734,
           "dept": "s",
           "suit": "c",
           "isAnimated": 0,
           "emblem": "emblem_corp" },

"moverandshaker": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_moverandshaker.bam"),
           "name": "featherbedder",
           "hands": (0.918, 0.808, 0.761, 1.000),
           "scale": 0.89792,
           "dept": "s",
           "suit": "b",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"twoface": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_twoface.bam"),
           "hands": (0.918, 0.808, 0.761, 1.000),
           "name": "yesman",
           "scale": 0.86633,
           "dept": "s",
           "suit": "a",
           "emblem": "emblem_corp" },
"mingler": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_mingler.bam"),
           "name": "featherbedder",
           "hands": (0.949, 0.749, 0.949, 1.000),
           "scale": 0.94884,
           "dept": "s",
           "suit": "a",
           "isAnimated": 1,
           "emblem": "emblem_corp" },

"mrhollywood": {"suitTex": os.path.join(RESOURCES_DIR,"phase_3.5","maps","ttcc_ene_suittex_s.png"),
           "head": os.path.join(RESOURCES_DIR,"phase_9","models","char", "suits", "ttcc_ene_mrhollywood.bam"),
           "hands": (0.835, 0.851, 0.847, 1.000),
           "name": "yesman",
           "scale": 1.15511,
           "dept": "s",
           "suit": "a",
           "emblem": "emblem_corp" }
}
