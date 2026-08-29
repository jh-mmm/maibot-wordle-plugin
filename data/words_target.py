"""Target words and definitions for Wordle."""

TARGET_WORDS: list[str] = ["aback", "abase", "abash", "abate", "abbey", "abbot", "abhor", "abide", "abled", "abode", "aboil", "abort", "about", "above", "abuse", "abuzz", "abyss", "ached", "achoo", "acing", "acorn", "acrid", "acted", "actor", "acute", "adage", "adapt", "added", "adder", "addle", "adept", "adieu", "adios", "admin", "admit", "adobe", "adobo", "adopt", "adore", "adorn", "adult", "aegis", "aerie", "affix", "afire", "afoot", "afore", "afoul", "after", "again", "agape", "agate", "agave", "agent", "agile", "aging", "agita", "aglow", "agony", "agora", "agree", "ahead", "ahold", "aided", "aider", "ailed", "aimed", "aioli", "aired", "airer", "aisle", "alarm", "album", "alder", "alert", "algae", "alias", "alibi", "alien", "align", "alike", "alive", "allay", "alley", "allot", "allow", "alloy", "aloft", "aloha", "alone", "along", "aloof", "aloud", "alpha", "altar", "alter", "amaro", "amass", "amaze", "amber", "ambit", "amble", "amend", "amigo", "amino", "amiss", "amity", "among", "amour", "amped", "ample", "amply", "amuck", "amuse", "ancho", "angel", "anger", "angle", "angry", "angst", "anime", "anise", "ankle", "annal", "annex", "annoy", "annul", "anode", "antic", "antsy", "anvil", "aorta", "apace", "apart", "aphid", "aping", "apnea", "apple", "apply", "apron", "aptly", "arbor", "arced", "ardor", "arena", "argon", "argot", "argue", "arise", "armed", "armor", "aroma", "arose", "array", "arrow", "arson", "artsy", "ascot", "ashed", "ashen", "aside", "asked", "asker", "askew", "aspen", "aspic", "assay", "asset", "aster", "astir", "atlas", "atoll", "atone", "atria", "attic", "audio", "audit", "auger", "augur", "aunty", "aural", "avail", "avast", "avert", "avian", "avoid", "await", "awake", "award", "aware", "awash", "awful", "awoke", "axial", "axiom", "axion", "azure", "babka", "bacon", "badge", "badly", "bagel", "baggy", "baked", "baker", "baldy", "baled", "baler", "balky", "balmy", "balsa", "banal", "bandy", "banjo", "bared", "barer", "barge", "baron", "basal", "based", "basic", "basil", "basin", "basis", "baste", "batch", "bated", "bathe", "batik", "baton", "batty", "bawdy", "bayed", "bayou", "beach", "beady", "beard", "beast", "beaut", "bebop", "beech", "beefy", "befit", "befog", "began", "begat", "beget", "begin", "begot", "begun", "beige", "being", "belch", "belie", "belle", "belly", "below", "bench", "bendy", "beret", "berry", "berth", "beset", "besot", "betel", "bevel", "bezel", "bible", "bicep", "biddy", "bided", "bidet", "bigot", "biked", "biker", "bilge", "bilgy", "billy", "binge", "bingo", "biome", "biped", "bipod", "birch", "birth", "bison", "biter", "bitsy", "bitty", "black", "blade", "blame", "bland", "blank", "blare", "blase", "blast", "blaze", "bleak", "bleat", "bleed", "bleep", "blend", "bless", "blimp", "blind", "bling", "blink", "bliss", "blitz", "bloat", "block", "bloke", "blond", "blood", "bloom", "blown", "bluer", "bluff", "blunt", "blurb", "blurt", "blush", "board", "boast", "bobby", "bocce", "boded", "boffo", "bogey", "boggy", "bogie", "bogus", "boing", "bolus", "boned", "boner", "boney", "bongo", "bonny", "bonus", "booby", "booed", "boost", "booth", "booty", "booze", "boozy", "borax", "bored", "borne", "boron", "bosom", "boson", "bossy", "botch", "bough", "boule", "bound", "bowed", "bowel", "bower", "boxed", "boxer", "brace", "braid", "brain", "brake", "brand", "brash", "brass", "brava", "brave", "bravo", "brawl", "brawn", "bread", "break", "breed", "briar", "bribe", "brick", "bride", "brief", "brier", "brine", "bring", "brink", "briny", "brisk", "broad", "broil", "broke", "bronc", "brood", "brook", "broom", "broth", "brown", "brunt", "brush", "brusk", "brute", "buddy", "budge", "buggy", "bugle", "build", "built", "bulge", "bulgy", "bulky", "bully", "bumpy", "bunch", "bunny", "burka", "burly", "burnt", "burro", "bursa", "burst", "bused", "bushy", "busty", "butch", "butte", "buxom", "buyer", "buzzy", "bylaw", "byway", "cabal", "cabby", "cabin", "cable", "cacao", "cache", "cacti", "caddy", "cadet", "cadge", "cadre", "caged", "cagey", "cairn", "caked", "calve", "camel", "cameo", "campy", "canal", "candy", "caned", "canny", "canoe", "canon", "caped", "caper", "capri", "caput", "carat", "cared", "caret", "cargo", "carny", "carol", "carom", "carry", "carte", "carve", "cased", "caste", "catch", "cater", "catty", "caulk", "cause", "caved", "cavil", "cawed", "cease", "cedar", "ceded", "celeb", "cello", "chaat", "chafe", "chaff", "chain", "chair", "chalk", "champ", "chant", "chaos", "chard", "charm", "chart", "chary", "chase", "chasm", "cheap", "cheat", "check", "cheek", "cheep", "cheer", "chemo", "chess", "chest", "chewy", "chick", "chide", "chief", "child", "chili", "chill", "chime", "chimp", "china", "chino", "chirp", "chive", "chock", "choir", "choke", "chomp", "chord", "chore", "chose", "chuck", "chump", "chunk", "churn", "chute", "cider", "cigar", "cinch", "circa", "cited", "civet", "civic", "civil", "clack", "clade", "claim", "clamp", "clang", "clank", "clash", "clasp", "class", "clean", "clear", "cleat", "cleft", "clerk", "click", "cliff", "climb", "clime", "cling", "clink", "cloak", "clock", "clomp", "clone", "close", "cloth", "cloud", "clout", "clove", "clown", "cluck", "clued", "clump", "clung", "clunk", "coach", "coast", "cobra", "cocky", "cocoa", "coded", "coder", "codex", "colic", "colon", "color", "combo", "comet", "comfy", "comic", "comma", "conch", "condo", "coned", "conga", "conic", "cooed", "copay", "coped", "copse", "coral", "cored", "corer", "corgi", "corky", "corny", "corps", "couch", "cough", "could", "count", "coupe", "court", "couth", "coven", "cover", "covet", "covey", "cowed", "cower", "coxed", "coyly", "crack", "craft", "cramp", "crane", "crank", "crash", "crass", "crate", "crave", "crawl", "craze", "crazy", "creak", "cream", "credo", "creed", "creek", "creep", "crema", "creme", "crepe", "crept", "cress", "crest", "crick", "cried", "crier", "crime", "crimp", "crisp", "croak", "crock", "crone", "crony", "crook", "croon", "cross", "croup", "crowd", "crown", "crude", "cruel", "crumb", "crump", "crush", "crust", "crypt", "cubby", "cubed", "cubic", "cubit", "cuing", "cumin", "cupid", "cured", "curer", "curio", "curly", "curry", "curse", "curve", "curvy", "cushy", "cuter", "cutie", "cutup", "cyber", "cycle", "cynic", "dacha", "daddy", "daffy", "daily", "dairy", "daisy", "dally", "dance", "dandy", "dared", "dated", "dater", "datum", "daunt", "dazed", "dealt", "death", "debar", "debit", "debug", "debut", "decaf", "decal", "decay", "decor", "decoy", "decry", "defer", "defog", "deify", "deign", "deist", "deity", "delay", "delta", "delve", "demon", "demur", "denim", "dense", "depot", "depth", "derby", "deter", "detox", "deuce", "devil", "diary", "diced", "dicer", "dicey", "digit", "diked", "dilly", "dimly", "dined", "diner", "dingo", "dingy", "dinky", "diode", "dippy", "dirge", "dirty", "disco", "ditch", "ditsy", "ditto", "ditty", "ditzy", "divan", "dived", "diver", "divot", "divvy", "dizzy", "dodge", "dodgy", "doggo", "doggy", "dogma", "doily", "doing", "doled", "dolly", "dolma", "domed", "donor", "donut", "doozy", "doped", "doper", "dopey", "dorky", "dosed", "doted", "dotty", "doubt", "dough", "doula", "douse", "dowdy", "dowel", "downy", "dowry", "dowse", "doxed", "dozed", "dozen", "dozer", "draft", "drain", "drake", "drama", "drank", "drape", "drawl", "drawn", "dread", "dream", "dress", "dried", "drier", "drift", "drill", "drink", "drive", "droid", "droit", "droll", "drone", "drool", "droop", "dross", "drove", "drown", "druid", "drunk", "dryer", "dryly", "ducat", "duchy", "ducky", "duked", "dully", "dummy", "dumpy", "dunce", "duped", "dusky", "dusty", "dutch", "duvet", "dwarf", "dweeb", "dwell", "dwelt", "dying", "eager", "eagle", "eared", "early", "earth", "eased", "easel", "eaten", "eater", "ebbed", "ebony", "ebook", "eclat", "edema", "edged", "edger", "edict", "edify", "educe", "eerie", "egged", "egret", "eider", "eight", "eject", "eking", "elate", "elbow", "elder", "elect", "elegy", "elfin", "elide", "elite", "elope", "elude", "email", "embed", "ember", "emcee", "emery", "emoji", "emote", "empty", "enact", "ended", "endow", "enema", "enemy", "enjoy", "ennui", "ensue", "enter", "entry", "envoy", "epoch", "epoxy", "equal", "equip", "erase", "erect", "erode", "erred", "error", "erupt", "essay", "ester", "ether", "ethic", "ethos", "ethyl", "etude", "evade", "event", "every", "evict", "evoke", "exact", "exalt", "excel", "exert", "exile", "exist", "expat", "expel", "extol", "extra", "exude", "exult", "exurb", "eying", "fable", "faced", "facet", "faded", "fader", "faint", "fairy", "faith", "faked", "faker", "fakir", "false", "famed", "fancy", "farce", "fared", "fatal", "fated", "fatty", "fatwa", "fault", "fauna", "favor", "faxed", "fazed", "feast", "fecal", "feces", "feign", "feint", "fella", "felon", "femme", "femur", "fence", "feral", "ferry", "fetal", "fetch", "feted", "fetid", "fetus", "fever", "fewer", "fiber", "ficus", "field", "fiend", "fiery", "fifth", "fifty", "fight", "filch", "filed", "filer", "filet", "filly", "filmy", "filth", "final", "finch", "fined", "finer", "fired", "first", "firth", "fishy", "fixed", "fixer", "fizzy", "fjord", "flack", "flail", "flair", "flake", "flaky", "flame", "flank", "flare", "flash", "flask", "fleck", "fleet", "flesh", "flick", "flied", "flier", "fling", "flint", "flirt", "float", "flock", "flood", "floor", "flora", "floss", "flour", "flout", "flown", "flowy", "fluff", "fluid", "fluke", "fluky", "flume", "flung", "flunk", "flush", "flute", "flyby", "flyer", "foamy", "focal", "focus", "fogey", "foggy", "fogie", "foist", "folic", "folio", "folky", "folly", "foray", "force", "forge", "forgo", "forte", "forth", "forty", "forum", "found", "fount", "foyer", "frack", "frail", "frame", "frank", "fraud", "freak", "freed", "freer", "fresh", "friar", "fried", "frill", "frise", "frisk", "fritz", "frizz", "frock", "frond", "front", "frosh", "frost", "froth", "frown", "froze", "fruit", "frump", "fryer", "fubar", "fudge", "fudgy", "fugue", "fully", "fumed", "fungi", "fungo", "funky", "funny", "furor", "furry", "fused", "fussy", "fusty", "futon", "fuzzy", "gabby", "gable", "gaffe", "gaily", "gamed", "gamer", "gamey", "gamma", "gamut", "gaped", "gassy", "gated", "gator", "gaudy", "gauge", "gaunt", "gauze", "gauzy", "gavel", "gawky", "gayer", "gayly", "gazed", "gazer", "gecko", "geeky", "geese", "genie", "genre", "geode", "getup", "ghost", "ghoul", "giant", "gibed", "giddy", "gimme", "girly", "girth", "given", "giver", "gizmo", "glade", "glamp", "gland", "glare", "glass", "glaze", "gleam", "glean", "glide", "glint", "glitz", "gloam", "gloat", "globe", "gloom", "gloop", "glory", "gloss", "glove", "glowy", "glued", "glute", "glyph", "gnarl", "gnash", "gnome", "godly", "gofer", "going", "golem", "golly", "gonad", "goner", "gonna", "gonzo", "goody", "gooey", "goofy", "goopy", "goose", "gored", "gorge", "gorse", "gotta", "gouge", "gourd", "grace", "grade", "graft", "grail", "grain", "grand", "grant", "grape", "graph", "grasp", "grass", "grate", "grave", "gravy", "graze", "great", "greed", "green", "greet", "grief", "grift", "grill", "grime", "grimy", "grind", "gripe", "grist", "groan", "groin", "groom", "grope", "gross", "group", "grout", "grove", "growl", "grown", "gruel", "gruff", "grump", "grunt", "guano", "guard", "guava", "guess", "guest", "guide", "guild", "guile", "guilt", "guise", "gulag", "gulch", "gully", "gumbo", "gummy", "gunky", "guppy", "gushy", "gussy", "gusto", "gusty", "gutsy", "gutty", "habit", "hacky", "haiku", "hairy", "halal", "halve", "handy", "hanky", "happy", "hardy", "harem", "harpy", "harry", "harsh", "haste", "hasty", "hatch", "hated", "hater", "haunt", "haute", "haven", "havoc", "hazed", "hazel", "heady", "heard", "heart", "heath", "heave", "heavy", "hedge", "hefty", "heist", "helix", "hello", "hence", "henna", "heron", "hertz", "hewed", "hexed", "hider", "hijab", "hiked", "hiker", "hilly", "hinge", "hinky", "hippo", "hippy", "hired", "hiree", "hirer", "hissy", "hitch", "hived", "hoagy", "hoard", "hoary", "hobby", "hocus", "hoist", "hokey", "hokum", "holed", "holly", "homed", "homer", "homey", "honed", "honey", "honor", "hooch", "hoody", "hooey", "hooky", "hoped", "hoppy", "horde", "horny", "horse", "hosed", "hotel", "hotly", "hound", "house", "hovel", "hover", "howdy", "hubby", "huffy", "hulky", "human", "humid", "humor", "humph", "humus", "hunch", "hunky", "hurry", "husky", "hussy", "hutch", "hydra", "hydro", "hyena", "hymen", "hyped", "hyper", "icier", "icily", "icing", "ideal", "idiom", "idiot", "idled", "idler", "idyll", "igloo", "iliac", "image", "imbed", "imbue", "impel", "imply", "inane", "inapt", "inbox", "incel", "incur", "index", "indie", "inept", "inert", "infer", "ingot", "inked", "inlay", "inlet", "inner", "input", "inset", "intel", "inter", "intro", "inure", "ionic", "irate", "irked", "irony", "islet", "issue", "itchy", "ivied", "ivory", "jaded", "janky", "japed", "jaunt", "jawed", "jazzy", "jelly", "jerky", "jerry", "jetty", "jewel", "jibed", "jiffy", "jihad", "jimmy", "joint", "joist", "joked", "joker", "jokey", "jolly", "joule", "joust", "jowly", "judge", "judgy", "juice", "juicy", "juked", "julep", "jumbo", "jumpy", "junky", "junta", "junto", "juror", "kabob", "kappa", "kaput", "karat", "karma", "kayak", "kazoo", "kebab", "kempt", "keyed", "khaki", "kiddo", "kinda", "kinky", "kiosk", "kissy", "kitty", "klutz", "knack", "knave", "knead", "kneed", "kneel", "knell", "knelt", "knife", "knish", "knock", "knoll", "known", "koala", "kooky", "koran", "krill", "kudos", "kudzu", "kugel", "kvell", "label", "labor", "laced", "lacey", "laden", "ladle", "lager", "laity", "lamed", "lamer", "lance", "lanky", "lapel", "lapse", "larch", "large", "larva", "laser", "lasso", "latch", "later", "latex", "lathe", "latke", "latte", "laugh", "laved", "layer", "layup", "lazed", "leach", "leafy", "leaky", "leant", "leapt", "learn", "lease", "leash", "least", "leave", "ledge", "leech", "leery", "lefty", "legal", "leggy", "legit", "lemma", "lemon", "lemur", "leper", "letup", "levee", "level", "lever", "lexis", "libel", "liege", "lifer", "light", "liked", "liken", "lilac", "limbo", "limey", "limit", "lined", "linen", "liner", "lingo", "lipid", "lippy", "liter", "lithe", "litre", "lived", "liven", "liver", "livid", "llama", "loamy", "loath", "lobby", "lobed", "local", "locus", "lodge", "loess", "lofty", "logic", "login", "logon", "lolly", "loner", "loony", "loopy", "loose", "loped", "lordy", "lorry", "loser", "lotto", "lotus", "louse", "lousy", "loved", "lover", "lower", "lowly", "loyal", "lubed", "lucid", "lucky", "lucre", "luger", "lumen", "lumpy", "lunar", "lunch", "lunge", "lupus", "lurch", "lured", "lurid", "lusty", "luted", "lying", "lymph", "lyric", "macaw", "macho", "macro", "madam", "madly", "mafia", "magic", "magma", "maize", "major", "maker", "malty", "mamba", "mambo", "mamma", "manga", "mange", "mango", "mangy", "mania", "manic", "manly", "manna", "manor", "manse", "maple", "march", "marry", "marsh", "mason", "masse", "match", "mated", "matey", "matte", "matzo", "mauve", "maven", "maxed", "maxim", "maybe", "mayor", "mealy", "meant", "meaty", "mecca", "medal", "media", "medic", "melee", "melon", "mensa", "mercy", "merge", "merit", "merry", "meshy", "messy", "metal", "meted", "meter", "metre", "metro", "mewed", "mezzo", "miasm", "micro", "midge", "midst", "might", "miked", "miler", "milky", "mimed", "mimic", "mince", "mined", "miner", "minim", "minor", "minty", "minus", "mired", "mirth", "miser", "missy", "misty", "mixed", "mixer", "mixup", "mocha", "mochi", "modal", "model", "modem", "modus", "mogul", "moist", "molar", "moldy", "molly", "momma", "mommy", "money", "month", "mooch", "moody", "mooed", "moose", "moped", "moper", "mopey", "moral", "moray", "moron", "morph", "mosey", "mossy", "motel", "motif", "motor", "motto", "mould", "moult", "mound", "mount", "mourn", "mouse", "mousy", "mouth", "moved", "mover", "movie", "mowed", "mower", "moxie", "mucky", "mucus", "muddy", "muggy", "mulch", "mummy", "munch", "mural", "murky", "mused", "mushy", "music", "musky", "mussy", "musty", "muted", "myrrh", "nabob", "nacho", "nadir", "naggy", "naive", "naked", "named", "nanny", "nappy", "nasal", "nasty", "natal", "naval", "navel", "needy", "neigh", "nerdy", "nerve", "nervy", "never", "newer", "newly", "newsy", "nexus", "nicer", "niche", "niece", "nifty", "night", "nimby", "ninja", "ninny", "ninth", "nippy", "nitro", "nixed", "noble", "nobly", "noise", "noisy", "nomad", "noose", "north", "nosed", "nosey", "notch", "noted", "novel", "nudge", "nuked", "nurse", "nutso", "nutty", "nylon", "nymph", "oaken", "oared", "oasis", "obese", "occur", "ocean", "ochre", "octal", "octet", "odder", "oddly", "odeum", "offal", "offed", "offer", "often", "ogled", "ogler", "oiled", "oiler", "okapi", "olden", "older", "oldie", "olive", "ombre", "omega", "onion", "onset", "oomph", "oozed", "opera", "opine", "opium", "opted", "optic", "orate", "orbed", "orbit", "order", "organ", "other", "otter", "ought", "ouija", "ounce", "outdo", "outed", "outer", "outgo", "outre", "ovary", "ovate", "overt", "ovine", "ovoid", "owing", "owned", "owner", "oxbow", "oxide", "ozone", "paced", "pacer", "paddy", "padre", "paean", "pagan", "paged", "pager", "paint", "paled", "paler", "palsy", "panda", "panel", "panic", "panty", "papal", "paper", "parch", "pared", "parer", "parka", "parry", "parse", "party", "passe", "pasta", "paste", "pasty", "patch", "patio", "patsy", "patty", "pause", "paved", "paver", "pawed", "payee", "payer", "peace", "peach", "pearl", "pecan", "pedal", "peeve", "penal", "pence", "penne", "penny", "peony", "peppy", "perch", "peril", "perky", "pesky", "pesto", "petal", "peter", "petit", "petri", "petty", "phase", "phish", "phone", "phony", "photo", "piano", "picky", "piece", "piety", "piggy", "piked", "piker", "pilaf", "piled", "pilot", "pinch", "pined", "piney", "pinky", "pinot", "pinto", "pinup", "pious", "piped", "piper", "pipet", "pique", "piste", "pitch", "pithy", "pivot", "pixel", "pixie", "pizza", "place", "plaid", "plain", "plait", "plane", "plank", "plant", "plasm", "plate", "plaza", "plead", "pleat", "plebe", "plied", "plier", "plink", "plonk", "pluck", "plumb", "plume", "plump", "plunk", "plush", "poach", "poesy", "point", "poise", "poked", "poker", "pokey", "polar", "poled", "polio", "polis", "polka", "polyp", "pooch", "poofy", "poppy", "popup", "porch", "pored", "porky", "posed", "poser", "posit", "posse", "potty", "pouch", "pound", "pouty", "power", "prank", "prawn", "preen", "press", "price", "prick", "pricy", "pride", "pried", "prima", "prime", "primo", "primp", "print", "prion", "prior", "prism", "priss", "privy", "prize", "probe", "prole", "promo", "prone", "prong", "proof", "prose", "proto", "proud", "prove", "prowl", "proxy", "prude", "prune", "psalm", "pshaw", "psych", "psyop", "pubic", "pubis", "pudge", "pudgy", "puffy", "puked", "pulpy", "pulse", "punch", "punky", "punny", "pupae", "pupil", "puppy", "puree", "purer", "purge", "purse", "pushy", "putty", "pwned", "pygmy", "pylon", "quack", "quaff", "quail", "quake", "qualm", "quant", "quark", "quart", "quash", "quasi", "queen", "queer", "quell", "query", "queso", "quest", "queue", "quick", "quiet", "quill", "quilt", "quirk", "quite", "quota", "quote", "quoth", "quran", "rabbi", "rabid", "raced", "racer", "radar", "radii", "radio", "radon", "raged", "rager", "rainy", "raise", "rajah", "raked", "rally", "ralph", "ramen", "ranch", "randy", "range", "rangy", "rapid", "rarer", "raspy", "rated", "rater", "ratio", "ratty", "raved", "raven", "raver", "rayon", "razed", "razor", "reach", "react", "ready", "realm", "rearm", "rebar", "rebel", "rebid", "rebus", "rebut", "rebuy", "recap", "recon", "recur", "recut", "redid", "redub", "redux", "reedy", "refer", "refit", "refry", "regal", "rehab", "reify", "reign", "reiki", "relax", "relay", "relic", "remap", "remit", "remix", "renal", "renew", "repay", "repel", "reply", "reran", "rerun", "resaw", "reset", "resin", "resod", "retag", "retch", "retie", "retro", "retry", "reuse", "revel", "revue", "rewax", "rewon", "rheum", "rhino", "rhyme", "ricin", "rider", "ridge", "rifle", "right", "rigid", "rigor", "riled", "rinse", "ripen", "riper", "risen", "riser", "risky", "ritzy", "rival", "riven", "river", "rivet", "roach", "roast", "robed", "robin", "robot", "rocky", "rodeo", "roger", "rogue", "roman", "roomy", "roost", "roped", "roper", "rosin", "rotor", "rouge", "rough", "round", "rouse", "route", "roved", "rover", "rowdy", "rowed", "rower", "royal", "ruble", "ruddy", "ruder", "rugby", "ruing", "ruled", "ruler", "rumba", "rummy", "rumor", "runny", "runup", "rupee", "rural", "rusty", "saber", "sable", "sabre", "sadly", "safer", "saggy", "saint", "salad", "sally", "salon", "salsa", "salty", "salve", "salvo", "samba", "samey", "sandy", "saner", "sappy", "sassy", "sated", "satin", "satyr", "sauce", "saucy", "sauna", "saute", "saved", "saver", "savor", "savoy", "savvy", "sawed", "scald", "scale", "scalp", "scaly", "scamp", "scant", "scape", "scare", "scarf", "scary", "scene", "scent", "schmo", "schwa", "scion", "scoff", "scold", "scone", "scoop", "scoot", "scope", "score", "scorn", "scour", "scout", "scowl", "scram", "scrap", "scree", "screw", "scrip", "scrod", "scrub", "scrum", "scuba", "scuff", "scull", "seamy", "sedan", "seder", "sedge", "seedy", "segue", "seize", "sense", "sepia", "serif", "serum", "serve", "setup", "seven", "sever", "sewed", "sewer", "shack", "shade", "shady", "shaft", "shake", "shaky", "shale", "shall", "shalt", "shame", "shank", "shape", "shard", "share", "shark", "sharp", "shave", "shawl", "sheaf", "shear", "sheen", "sheep", "sheer", "sheet", "sheik", "shelf", "shell", "shied", "shift", "shill", "shine", "shiny", "shire", "shirk", "shirt", "shiva", "shlep", "shlub", "shoal", "shock", "shoed", "shone", "shook", "shoot", "shore", "shorn", "short", "shout", "shove", "shown", "showy", "shred", "shrew", "shrub", "shrug", "shuck", "shunt", "shush", "shyly", "sided", "sidle", "siege", "sieve", "sight", "sigma", "silky", "silly", "silty", "since", "sinew", "singe", "sinus", "sired", "siren", "sissy", "sitar", "sited", "situp", "sixth", "sixty", "sized", "skate", "skeet", "skein", "skied", "skier", "skiff", "skill", "skimp", "skirt", "skulk", "skull", "skunk", "slack", "slain", "slake", "slang", "slant", "slash", "slate", "sleek", "sleep", "sleet", "slept", "slice", "slick", "slide", "slime", "slimy", "sling", "slink", "sloop", "slope", "slosh", "sloth", "slump", "slung", "slunk", "slurp", "slush", "slyly", "smack", "small", "smarm", "smart", "smash", "smear", "smell", "smelt", "smile", "smirk", "smite", "smith", "smock", "smoke", "smoky", "smote", "smush", "snack", "snafu", "snail", "snake", "snaky", "snare", "snarf", "snark", "snarl", "sneak", "sneer", "snide", "sniff", "snipe", "snoop", "snoot", "snore", "snort", "snout", "snowy", "snuck", "snuff", "soapy", "sober", "softy", "soggy", "solar", "soled", "solid", "solve", "sonar", "sonic", "sooth", "sooty", "soppy", "sorry", "sound", "soupy", "south", "sowed", "sower", "space", "spade", "spank", "spare", "spark", "spasm", "spate", "spawn", "speak", "spear", "speck", "speed", "spell", "spelt", "spend", "spent", "sperm", "spice", "spicy", "spied", "spiel", "spiff", "spike", "spiky", "spill", "spilt", "spine", "spiny", "spire", "spite", "splat", "splay", "split", "spoil", "spoke", "spoof", "spook", "spool", "spoon", "spore", "sport", "spout", "spray", "spree", "sprig", "spume", "spunk", "spurn", "spurt", "squab", "squad", "squat", "squib", "squid", "stack", "staff", "stage", "staid", "stain", "stair", "stake", "stale", "stalk", "stall", "stamp", "stand", "stank", "staph", "stare", "stark", "start", "stash", "state", "stave", "stead", "steak", "steal", "steam", "steed", "steel", "steep", "steer", "stein", "steno", "stent", "stern", "stick", "stiff", "still", "stilt", "sting", "stink", "stint", "stock", "stoic", "stoke", "stole", "stomp", "stone", "stony", "stood", "stool", "stoop", "store", "stork", "storm", "story", "stout", "stove", "strap", "straw", "stray", "strep", "strew", "strip", "strum", "strut", "stuck", "study", "stuff", "stump", "stung", "stunk", "stunt", "style", "suave", "sudsy", "suede", "sugar", "suing", "suite", "sulky", "sully", "sumac", "sunny", "sunup", "super", "surer", "surge", "surly", "sushi", "swain", "swale", "swami", "swamp", "swang", "swank", "swarm", "swash", "swath", "swear", "sweat", "sweep", "sweet", "swell", "swept", "swift", "swill", "swine", "swing", "swipe", "swirl", "swish", "swoon", "swoop", "sword", "swore", "sworn", "swung", "synch", "synod", "syrup", "tabby", "table", "taboo", "tacit", "tacky", "taffy", "taint", "taken", "taker", "talky", "tally", "talon", "talus", "tamed", "tamer", "tango", "tangy", "taped", "taper", "tapir", "tardy", "tarot", "tarry", "tased", "taser", "taste", "tasty", "tater", "tatty", "taunt", "taupe", "tawny", "taxed", "teach", "teary", "tease", "teddy", "teeny", "teeth", "telos", "tempo", "tempt", "tenet", "tenor", "tense", "tenth", "tepee", "tepid", "terra", "terry", "terse", "testy", "tetra", "thank", "theft", "their", "theme", "there", "these", "theta", "thick", "thief", "thigh", "thine", "thing", "think", "third", "thong", "thorn", "those", "three", "threw", "throb", "throw", "thrum", "thumb", "thump", "thyme", "tiara", "tibia", "tidal", "tided", "tiger", "tight", "tilde", "tiled", "timed", "timer", "timid", "tinge", "tinny", "tipsy", "tired", "titan", "titer", "tithe", "title", "tizzy", "toady", "toast", "today", "toddy", "token", "tonal", "toned", "toner", "toney", "tonga", "tonic", "tooth", "topaz", "topic", "torah", "torch", "torso", "torte", "torus", "total", "toted", "totem", "touch", "tough", "towed", "towel", "tower", "toxic", "toxin", "toyed", "trace", "track", "tract", "trade", "trail", "train", "trait", "tramp", "trans", "trash", "trawl", "tread", "treat", "treed", "trend", "tress", "triad", "trial", "tribe", "trice", "trick", "tried", "trike", "trill", "tripe", "trite", "troll", "tromp", "troop", "trope", "trout", "trove", "truce", "truck", "truer", "truly", "trump", "trunk", "truss", "trust", "truth", "tryst", "tubal", "tubby", "tubed", "tuber", "tufty", "tulip", "tulle", "tummy", "tumor", "tuned", "tuner", "tunic", "turbo", "tutor", "twain", "twang", "tweak", "tweed", "tween", "tweet", "twerk", "twerp", "twice", "twill", "twine", "twirl", "twist", "twixt", "tying", "typed", "udder", "ulcer", "ulnar", "ultra", "umber", "umbra", "unarm", "unbag", "unbox", "uncap", "uncle", "uncut", "under", "undid", "undue", "unfed", "unfit", "unhip", "unify", "union", "unite", "unity", "unjam", "unlit", "unmet", "unpin", "unsay", "unsee", "unset", "untag", "untie", "until", "unwed", "unzip", "upend", "upped", "upper", "upset", "urban", "urged", "urine", "usage", "usher", "using", "usual", "usurp", "usury", "utile", "utter", "uvula", "vague", "valet", "valid", "valor", "value", "valve", "vampy", "vaped", "vapid", "vapor", "vault", "vaunt", "vegan", "veiny", "veldt", "venal", "venom", "venue", "verge", "verse", "verso", "verve", "vexed", "vicar", "video", "vigil", "vigor", "villa", "vined", "vinyl", "viola", "viper", "viral", "virus", "visit", "visor", "vista", "vital", "vitro", "vivid", "vixen", "vocal", "vodka", "vogue", "voice", "voila", "vomit", "voted", "voter", "vouch", "vowed", "vowel", "vroom", "vying", "wacko", "wacky", "waded", "wader", "wafer", "waged", "wager", "wagon", "waist", "waive", "waked", "waken", "waltz", "waned", "wanly", "warty", "waste", "watch", "water", "waved", "waver", "waxed", "waxen", "weary", "weave", "wedge", "weedy", "weepy", "weigh", "weird", "whack", "whale", "wharf", "wheat", "wheel", "whelp", "where", "which", "whiff", "while", "whine", "whiny", "whirl", "whisk", "white", "whizz", "whole", "whomp", "whoop", "whorl", "whose", "widen", "wider", "widow", "width", "wield", "wight", "wiled", "willy", "wimpy", "wince", "winch", "windy", "wined", "wiped", "wiper", "wired", "wiser", "wispy", "witch", "witty", "woken", "woman", "women", "wonky", "woody", "wooed", "wooer", "wooly", "woozy", "wordy", "world", "wormy", "worry", "worse", "worst", "worth", "would", "wound", "woven", "wowed", "wrack", "wrath", "wreak", "wreck", "wrest", "wring", "wrist", "write", "wrong", "wrote", "wrung", "wryly", "wurst", "xenon", "xerox", "yacht", "yahoo", "yappy", "yearn", "yeast", "yeesh", "yield", "yodel", "yoked", "yokel", "young", "youth", "yucca", "yucky", "yummy", "zebra", "zesty", "zilch", "zippy", "zonal", "zoned", "zowie"]

WORD_DEFINITIONS: dict[str, dict[str, str]] = {
  "aback": {
    "phonetic": "ә'bæk",
    "meaning": "adv. 向后, 朝后, 突然, 船顶风地"
  },
  "abase": {
    "phonetic": "ә'beis",
    "meaning": "vt. 降低...的地位, 降低...的品格, 贬抑, 使谦卑"
  },
  "abash": {
    "phonetic": "ә'bæʃ",
    "meaning": "vt. 使不安, 使羞愧, 使困窘"
  },
  "abate": {
    "phonetic": "ә'beit",
    "meaning": "vt. 减少, 减轻, 减弱, 废除, 打折扣；vi. 减轻, 减弱, 减少, 失效, 被废除"
  },
  "abbey": {
    "phonetic": "'æbi",
    "meaning": "n. 大修道院"
  },
  "abbot": {
    "phonetic": "'æbәt",
    "meaning": "n. 男修道院院长, 大寺院男住持"
  },
  "abhor": {
    "phonetic": "әb'hɒ:",
    "meaning": "vt. 憎恶, 痛恨, 回避, 拒绝"
  },
  "abide": {
    "phonetic": "ә'baid",
    "meaning": "vi. 停留, 遵守, 居留, 继续下去；vt. 忍受, 经受, 屈从于"
  },
  "abled": {
    "phonetic": "'eibld",
    "meaning": "a. [前面往往带副词] (体格)强壮的, 身体(或体格)健全的；无残疾的"
  },
  "abode": {
    "phonetic": "ә'bәud",
    "meaning": "n. 住所, 住处；abide的过去式和过去分词"
  },
  "aboil": {
    "phonetic": "ә'bɒil",
    "meaning": "a. 沸腾的, 激烈的；adv. 沸腾地, 激烈地"
  },
  "abort": {
    "phonetic": "ә'bɒ:t",
    "meaning": "vi. 流产, 中途失败；vt. 使流产, 使失败, 使中止"
  },
  "about": {
    "phonetic": "ә'baut",
    "meaning": "prep. 在...周围, 大约, 有关, 关于；adv. 大约, 四处, 在附近, 周围"
  },
  "above": {
    "phonetic": "ә'bʌv",
    "meaning": "prep. 在上方, 超出；adv. 在上面；a. 上述的, 上面的"
  },
  "abuse": {
    "phonetic": "ә'bju:s.ә'bju:z",
    "meaning": "n. 滥用, 虐待, 恶习, 辱骂；vt. 滥用, 辱骂, 虐待"
  },
  "abuzz": {
    "phonetic": "ә'bʌz",
    "meaning": "a. 嗡嗡的, 嘈杂的"
  },
  "abyss": {
    "phonetic": "ә'bis",
    "meaning": "n. 深渊, 深邃, 地狱"
  },
  "ached": {
    "phonetic": "eɪkt",
    "meaning": "疼痛"
  },
  "achoo": {
    "phonetic": "ɑ:'tʃu:",
    "meaning": "n. 啊嚏"
  },
  "acing": {
    "phonetic": "",
    "meaning": "vt. 发球得分（ace的现在分词形式）"
  },
  "acorn": {
    "phonetic": "'eikɒ:n",
    "meaning": "n. 橡树果实；[机] 浆栎, 浆栎果"
  },
  "acrid": {
    "phonetic": "'ækrid",
    "meaning": "a. 苦味的, 辛辣的, 讥讽的, 刻薄的；[医] 辛辣的"
  },
  "acted": {
    "phonetic": "",
    "meaning": "v. 行动（act的过去分词）；行使…职能；扮演角色"
  },
  "actor": {
    "phonetic": "'æktә",
    "meaning": "n. 男演员, 行动者；[医] 作用物, 反应物"
  },
  "acute": {
    "phonetic": "ә'kju:t",
    "meaning": "a. 尖锐的, 敏锐的, 激烈的, 严重的, 急性的；[医] 急性的; 尖锐的"
  },
  "adage": {
    "phonetic": "'ædidʒ",
    "meaning": "n. 格言, 谚语"
  },
  "adapt": {
    "phonetic": "ә'dæpt",
    "meaning": "vt. 使适应, 改编；vi. 适应"
  },
  "added": {
    "phonetic": "'ædid",
    "meaning": "a. 额外的；更多的"
  },
  "adder": {
    "phonetic": "'ædә",
    "meaning": "n. 蝰蛇, 猪鼻蛇, 加法器；[计] 加法器"
  },
  "addle": {
    "phonetic": "'ædl",
    "meaning": "vt. 使昏乱, 使腐坏；vi. 变质；a. 昏乱的, 腐坏的"
  },
  "adept": {
    "phonetic": "ә'dept",
    "meaning": "a. 熟练的, 老练的, 巧妙的；n. 能手, 内行"
  },
  "adieu": {
    "phonetic": "ә'dju:",
    "meaning": "interj. 再见, 再会；n. 告别, 辞别"
  },
  "adios": {
    "phonetic": "ɑ:'djәus",
    "meaning": "[计] 模数输入输出系统, 自动诊断输入输出系统"
  },
  "admin": {
    "phonetic": "",
    "meaning": "[计] 行政管理程序"
  },
  "admit": {
    "phonetic": "әd'mit",
    "meaning": "vt. 承认, 接受, 允许进入, 容许；vi. 开向, 容许, 承认"
  },
  "adobe": {
    "phonetic": "ә'doubi",
    "meaning": "n. 风干土坯；[化] 风干砖; 土砖; 灰质粘土; 多孔粘土"
  },
  "adobo": {
    "phonetic": "ә'dәjbәj",
    "meaning": "n. 阿斗波(拉美、菲律宾等地的一种菜肴, 源自西班牙)"
  },
  "adopt": {
    "phonetic": "ә'dɒpt",
    "meaning": "vt. 采用, 正式通过, 收养, 接受；[医] 采取"
  },
  "adore": {
    "phonetic": "ә'dɒ:",
    "meaning": "vt. 崇拜, 爱慕, 喜爱；vi. 崇拜, 爱慕"
  },
  "adorn": {
    "phonetic": "ә'dɒ:n",
    "meaning": "vt. 装饰, 使生色"
  },
  "adult": {
    "phonetic": "'ædʌlt",
    "meaning": "n. 成人, 成虫；a. 成年的, 成熟的"
  },
  "aegis": {
    "phonetic": "'i:dʒis",
    "meaning": "n. 羊皮盾, 保护, 庇护, 赞助, 支持；[法] 庇护, 保护"
  },
  "aerie": {
    "phonetic": "'єәri",
    "meaning": "n. 猛禽的巢, 高处的房子, 高处的城堡"
  },
  "affix": {
    "phonetic": "ә'fiks",
    "meaning": "vt. 使附于, 署名, 粘贴, 盖印于；n. 附加物, 词缀"
  },
  "afire": {
    "phonetic": "ә'faiә",
    "meaning": "a. 燃烧的, 炽烈的；adv. 燃烧着"
  },
  "afoot": {
    "phonetic": "ә'fut",
    "meaning": "a. 徒步的, 在进行中的, 活动中的；adv. 徒步, 在进行中"
  },
  "afore": {
    "phonetic": "ә'fɒ:",
    "meaning": "adv. 在前；prep. 在...前"
  },
  "afoul": {
    "phonetic": "ә'faul",
    "meaning": "adv. 冲撞着；[法] 破撞, 缠住, 冲突"
  },
  "after": {
    "phonetic": "'ɑ:ftә",
    "meaning": "prep. 在...之后, 由于；conj. 在...之后；adv. 后来"
  },
  "again": {
    "phonetic": "ә'gein",
    "meaning": "adv. 再一次, 又, 到原处"
  },
  "agape": {
    "phonetic": "ә'geip",
    "meaning": "a. 张口发呆的, 目瞪口呆的；adv. 张口发呆地, 目瞪口呆地"
  },
  "agate": {
    "phonetic": "'ægәt",
    "meaning": "n. 玛瑙, 五又二分之一点铅字；[化] 玛瑙149"
  },
  "agave": {
    "phonetic": "ә'geivi",
    "meaning": "n. 龙舌兰；[机] 龙舌兰属"
  },
  "agent": {
    "phonetic": "'eidʒәnt",
    "meaning": "n. 代理商, 政府代表, 动原, 媒介；[计] 代理程序"
  },
  "agile": {
    "phonetic": "'ædʒail",
    "meaning": "a. 敏捷的, 灵活的, 机敏的"
  },
  "aging": {
    "phonetic": "'eidʒiŋ",
    "meaning": "n. 老化, 变陈；[计] 老化, 陈化"
  },
  "agita": {
    "phonetic": "æd'ʒi:tə",
    "meaning": "n. 胃酸消化不良"
  },
  "aglow": {
    "phonetic": "ә'glәu",
    "meaning": "a. 发光的, 通红的；adv. 发光地"
  },
  "agony": {
    "phonetic": "'ægәni",
    "meaning": "n. 极大的痛苦, 挣扎；[医] 濒死苦闷; 剧痛"
  },
  "agora": {
    "phonetic": "'ægәrә",
    "meaning": "n. 集会, 市场"
  },
  "agree": {
    "phonetic": "ә'gri:",
    "meaning": "vi. 同意, 赞成, 应允, 适合；vt. 承认, 认定, 同意"
  },
  "ahead": {
    "phonetic": "ә'hed",
    "meaning": "a. 领先的, 预先的, 向前的；adv. 领先, 预先, 向前, 胜于, 在前面, 在将来"
  },
  "ahold": {
    "phonetic": "ә'hәjld",
    "meaning": "n. 抓, 握；adv. 迎风航驶"
  },
  "aided": {
    "phonetic": "'eidid",
    "meaning": "a. 辅助的；半自动的"
  },
  "aider": {
    "phonetic": "",
    "meaning": "[法] 助手, 帮手, 辅助人"
  },
  "ailed": {
    "phonetic": "eɪl",
    "meaning": "vt. 使苦恼, 使烦恼；vi. 生病；n. 病痛, 苦恼"
  },
  "aimed": {
    "phonetic": "",
    "meaning": "目标；目的"
  },
  "aioli": {
    "phonetic": "ai'әjli",
    "meaning": "n. 蒜泥蛋黄酱(一种用蒜泥、蛋黄、橄榄油和柠檬汁配制的调味汁)"
  },
  "aired": {
    "phonetic": "",
    "meaning": "通风；夸耀；晾干（air的过去式和过去分词）"
  },
  "airer": {
    "phonetic": "'εәrә",
    "meaning": "n. 干燥器；晾衣架"
  },
  "aisle": {
    "phonetic": "ail",
    "meaning": "n. 走廊, 侧廊, 过道；[机] 走道"
  },
  "alarm": {
    "phonetic": "ә'lɑ:m",
    "meaning": "n. 惊恐, 警报, 警钟；vt. 使惊恐, 警告；[计] 报警信号"
  },
  "album": {
    "phonetic": "'ælbәm",
    "meaning": "n. 粘贴簿, 唱片套；[医] 白色物"
  },
  "alder": {
    "phonetic": "'ɒ:ldә",
    "meaning": "n. 桤木；[机] 赤杨木"
  },
  "alert": {
    "phonetic": "ә'lә:t",
    "meaning": "a. 警觉的, 灵敏的, 留心的；n. 警报；vt. 使警觉, 通知, 使意识到"
  },
  "algae": {
    "phonetic": "'ælgi:",
    "meaning": "pl. 藻类, 海藻；[化] 藻类"
  },
  "alias": {
    "phonetic": "'eiliæs",
    "meaning": "n. 别名, 化名；adv. 以化名为人所知；[计] 别名; 替换入口"
  },
  "alibi": {
    "phonetic": "'ælibai",
    "meaning": "n. 不在犯罪现场, 托辞；v. 为...辩解"
  },
  "alien": {
    "phonetic": "'eiljәn",
    "meaning": "n. 外国人, 外侨；a. 外国的, 相异的"
  },
  "align": {
    "phonetic": "ә'lain",
    "meaning": "vi. 排列, 排成一行, 结盟；vt. 使结盟, 使成一行, 校正"
  },
  "alike": {
    "phonetic": "ә'laik",
    "meaning": "a. 相似的, 同样的；adv. 一样, 以同样的方式"
  },
  "alive": {
    "phonetic": "ә'laiv",
    "meaning": "a. 活着的, 活泼的, 敏感的, 热闹的"
  },
  "allay": {
    "phonetic": "ә'lei",
    "meaning": "vt. 使平静, 使缓和"
  },
  "alley": {
    "phonetic": "'æli",
    "meaning": "n. 小路, 巷"
  },
  "allot": {
    "phonetic": "ә'lɒt",
    "meaning": "vt. 分配, 分摊指定；[经] (按股或按规定)分配, 配(拨)给, 规(派)定"
  },
  "allow": {
    "phonetic": "ә'lau",
    "meaning": "vt. 允许, 同意给予, 承认；vi. 容许, 猜想；[计] 允许命令"
  },
  "alloy": {
    "phonetic": "'ælɒi. ә'lɒi",
    "meaning": "n. 合金；vt. 将...铸成合金, 减低成色；vi. 合铸"
  },
  "aloft": {
    "phonetic": "ә'lɒft",
    "meaning": "adv. 在高处, 在上"
  },
  "aloha": {
    "phonetic": "ә'lәuhә",
    "meaning": "interj. 喂, 再见"
  },
  "alone": {
    "phonetic": "ә'lәun",
    "meaning": "a. 孤独的, 单独的, 独自的；adv. 独自地"
  },
  "along": {
    "phonetic": "ә'lɒŋ",
    "meaning": "adv. 平行地, 向前；prep. 沿着"
  },
  "aloof": {
    "phonetic": "ә'lu:f",
    "meaning": "a. 远离的, 冷淡的；adv. 远离, 冷漠超然地"
  },
  "aloud": {
    "phonetic": "ә'laud",
    "meaning": "adv. 出声地, 大声地"
  },
  "alpha": {
    "phonetic": "'ælfә",
    "meaning": "n. 希腊字母表的第一个字母, 最初, 开端；[医] α(希腊文的第一个字母), 甲种"
  },
  "altar": {
    "phonetic": "'ɒ:ltә",
    "meaning": "n. 圣坛, 祭坛"
  },
  "alter": {
    "phonetic": "'ɒ:ltә",
    "meaning": "v. 改变"
  },
  "amaro": {
    "phonetic": "",
    "meaning": "n. (Amaro)人名；(法、西、意、葡)阿马罗"
  },
  "amass": {
    "phonetic": "ә'mæs",
    "meaning": "vt. 积聚, 堆积"
  },
  "amaze": {
    "phonetic": "ә'meiz",
    "meaning": "vt. 使吃惊"
  },
  "amber": {
    "phonetic": "'æmbә",
    "meaning": "n. 琥珀, 琥珀色；a. 琥珀色的, 琥珀似的"
  },
  "ambit": {
    "phonetic": "'æmbit",
    "meaning": "n. 周围, 范围, 界限, 领域"
  },
  "amble": {
    "phonetic": "'æmbl",
    "meaning": "n. 马的缓行步态, 缓行漫步；vi. 马缓行, 从容漫步"
  },
  "amend": {
    "phonetic": "ә'mend",
    "meaning": "vt. 修改, 改善, 改良；vi. 改过自新"
  },
  "amigo": {
    "phonetic": "ә'mi:gәu",
    "meaning": "n. 朋友"
  },
  "amino": {
    "phonetic": "'æminәu",
    "meaning": "a. 氨基的；[医] 氨基"
  },
  "amiss": {
    "phonetic": "ә'mis",
    "meaning": "a. 有毛病的, 出差错的；adv. 错误地, 不顺当, 有缺陷地"
  },
  "amity": {
    "phonetic": "'æmiti",
    "meaning": "n. 友好, 亲善关系"
  },
  "among": {
    "phonetic": "ә'mʌŋ",
    "meaning": "prep. 在...之中"
  },
  "amour": {
    "phonetic": "ә'muә",
    "meaning": "n. 偷情, 性爱；[法] 奸情, 不正当的男女关系, 恋爱"
  },
  "amped": {
    "phonetic": "",
    "meaning": "a. 激动的; 兴奋的"
  },
  "ample": {
    "phonetic": "'æmpl",
    "meaning": "a. 大量的, 充足的, 丰富的"
  },
  "amply": {
    "phonetic": "'æmpli",
    "meaning": "adv. 充足地, 充裕地"
  },
  "amuck": {
    "phonetic": "ә'mʌk",
    "meaning": "adv. 狂乱地, 杀气腾腾地；a. 嗜杀的"
  },
  "amuse": {
    "phonetic": "ә'mju:z",
    "meaning": "vt. 消遣, 娱乐, 使发笑"
  },
  "ancho": {
    "phonetic": "'ænkəʊ",
    "meaning": "n. 安蔻椒, 干波布拉诺椒"
  },
  "angel": {
    "phonetic": "'eindʒәl",
    "meaning": "n. 天使, 守护神, 善人"
  },
  "anger": {
    "phonetic": "'æŋgә",
    "meaning": "n. 忿怒；vt. 激怒, 使发怒；vi. 发怒"
  },
  "angle": {
    "phonetic": "'æŋgl",
    "meaning": "n. 角, 角度, 角落；vi. 钓鱼, 谋取, 博取, 斜向移动, 转变角度；vt. 使转动角度, 在...钓鱼, 获取"
  },
  "angry": {
    "phonetic": "'æŋgri",
    "meaning": "a. 生气的, 愤怒的"
  },
  "angst": {
    "phonetic": "æŋst",
    "meaning": "n. 焦虑, 疑惧；[医] 恐怖"
  },
  "anime": {
    "phonetic": "'ænimei",
    "meaning": "[医] 硬树脂"
  },
  "anise": {
    "phonetic": "'ænis",
    "meaning": "n. 茴芹；[化] 茴香"
  },
  "ankle": {
    "phonetic": "'æŋkl",
    "meaning": "n. 踝；[医] 踝, 踝关节"
  },
  "annal": {
    "phonetic": "'ænәl",
    "meaning": "n. 记录；编年史"
  },
  "annex": {
    "phonetic": "ә'neks",
    "meaning": "n. 附加物, 附属建筑物；vt. 附加, 盖(印), 并吞"
  },
  "annoy": {
    "phonetic": "ә'nɒi",
    "meaning": "vt. 使恼怒, 骚扰"
  },
  "annul": {
    "phonetic": "ә'nʌl",
    "meaning": "vt. 废除, 宣告无效, 取消；[经] 撤销, 宣告无效"
  },
  "anode": {
    "phonetic": "'ænәud",
    "meaning": "n. 阳极；[化] 阳极; 正极"
  },
  "antic": {
    "phonetic": "'æntik",
    "meaning": "n. 滑稽动作；a. 古怪的"
  },
  "antsy": {
    "phonetic": "'æntsi",
    "meaning": "a. 热锅上的蚂蚁般的,坐立不安的"
  },
  "anvil": {
    "phonetic": "'ænvil",
    "meaning": "n. 铁砧；[医] 砧骨; 铁砧"
  },
  "aorta": {
    "phonetic": "ei'ɒ:tә",
    "meaning": "n. 主动脉；[医] 主动脉"
  },
  "apace": {
    "phonetic": "ә'peis",
    "meaning": "adv. 快速地, 急速地"
  },
  "apart": {
    "phonetic": "ә'pɑ:t",
    "meaning": "adv. 成零碎, 成距离, 分别地, 分离着；a. 分离的"
  },
  "aphid": {
    "phonetic": "'eifid",
    "meaning": "n. 蚜虫"
  },
  "aping": {
    "phonetic": "",
    "meaning": "模仿（ape的现在分词）"
  },
  "apnea": {
    "phonetic": "æp'ni:ә",
    "meaning": "n. 呼吸暂停, 窒息；[医] 呼吸暂停, 窒息"
  },
  "apple": {
    "phonetic": "'æpl",
    "meaning": "n. 苹果, 家伙；[医] 苹果"
  },
  "apply": {
    "phonetic": "ә'plai",
    "meaning": "vt. 涂, 应用；vi. 申请, 适用"
  },
  "apron": {
    "phonetic": "'eiprәn",
    "meaning": "n. 围裙；[医] 围裙"
  },
  "aptly": {
    "phonetic": "'æptli",
    "meaning": "adv. 适当地, 适宜地"
  },
  "arbor": {
    "phonetic": "'ɑ:bә",
    "meaning": "n. 藤架, 树, 心轴, 凉亭；[医] 树(树状结构)"
  },
  "arced": {
    "phonetic": "ɑ:kt",
    "meaning": "vi. 形成拱状物（arc的过去式与过去分词形式）"
  },
  "ardor": {
    "phonetic": "'ɑ:dә",
    "meaning": "n. 热忱, 热情, 情欲, 激情, 灼热；[医] 灼热; 热心"
  },
  "arena": {
    "phonetic": "ә'ri:nә",
    "meaning": "n. 角斗场, 舞台, 场地；[医] 尿沉渣, 尿沙; 脑沙"
  },
  "argon": {
    "phonetic": "'ɑ:gɒn",
    "meaning": "n. 氩；[化] 氩Ar"
  },
  "argot": {
    "phonetic": "'ɑ:gәu",
    "meaning": "n. 行话, 俚语, 黑话"
  },
  "argue": {
    "phonetic": "'ɑ:gju",
    "meaning": "vi. 提出理由, 争论, 辩论；vt. 主张, 辩论, 证明, 说服"
  },
  "arise": {
    "phonetic": "ә'raiz",
    "meaning": "vi. 站立, 出现, 起来"
  },
  "armed": {
    "phonetic": "ɑ:md",
    "meaning": "a. 有扶手的, 武装的, 有防卫器官的；[法] 武装的, 持械的, \"F带武器的"
  },
  "armor": {
    "phonetic": "'ɑ:mә",
    "meaning": "n. 盔甲, 潜水服, 装甲；vt. 为...装甲"
  },
  "aroma": {
    "phonetic": "ә'rәumә",
    "meaning": "n. 浓香, 香气；[医] 香气, 芳香气"
  },
  "arose": {
    "phonetic": "ә'rәuz",
    "meaning": "arise的过去式"
  },
  "array": {
    "phonetic": "ә'rei",
    "meaning": "n. 排列, 衣服, 大批, 军队；vt. 布署, 打扮, 排列；[计] 数组; 阵列"
  },
  "arrow": {
    "phonetic": "'ærәu",
    "meaning": "n. 箭, 箭状物, 箭头记号"
  },
  "arson": {
    "phonetic": "'ɑ:sәn",
    "meaning": "n. 纵火, 纵火罪；[法] 纵火, 放火"
  },
  "artsy": {
    "phonetic": "'ɑ:tsi",
    "meaning": "a. 装艺术的, 艺术家气派的"
  },
  "ascot": {
    "phonetic": "'æskәt",
    "meaning": "n. 领巾状领带；（大写）英国阿斯科特赛马会"
  },
  "ashed": {
    "phonetic": "",
    "meaning": "[机] 灰化了的, 成了灰的"
  },
  "ashen": {
    "phonetic": "'æʃәn",
    "meaning": "a. 由灰烬构成的, 灰色的, 苍白的；[机] 灰的, 似灰的"
  },
  "aside": {
    "phonetic": "ә'said",
    "meaning": "n. 小声说的话, 旁白；adv. 在一边, 离开, 另外"
  },
  "asked": {
    "phonetic": "",
    "meaning": "n. 卖方要价"
  },
  "asker": {
    "phonetic": "'ɑ:skә",
    "meaning": "n. 发问者, 请求者"
  },
  "askew": {
    "phonetic": "ә'skju:",
    "meaning": "a. 歪斜的；adv. 歪斜地"
  },
  "aspen": {
    "phonetic": "'æspәn",
    "meaning": "n. 山杨；a. 山杨的, 颤抖的"
  },
  "aspic": {
    "phonetic": "'æspik",
    "meaning": "n. 花色肉冻；[机] 薰衣草"
  },
  "assay": {
    "phonetic": "ә'sei",
    "meaning": "n. 试验, 化验, 分析；vt. 化验, 分析, 评价, 尝试；vi. 被验明内含成分"
  },
  "asset": {
    "phonetic": "'æset",
    "meaning": "n. 资产, 有益的东西"
  },
  "aster": {
    "phonetic": "'æstә",
    "meaning": "n. 紫苑属植物；[医] 星体"
  },
  "astir": {
    "phonetic": "ә'stә:",
    "meaning": "a. 活动的, 骚动的, 起床的"
  },
  "atlas": {
    "phonetic": "'ætlәs",
    "meaning": "n. 地图集, 图表集；[计] 自动测试和负载分析系统"
  },
  "atoll": {
    "phonetic": "'ætɒl",
    "meaning": "n. 环状珊瑚岛, 环礁"
  },
  "atone": {
    "phonetic": "ә'tәun",
    "meaning": "vi. 补偿, 弥补；[法] 赔偿, 补偿, 偿还"
  },
  "atria": {
    "phonetic": "'eitriә",
    "meaning": "pl. 门廊, 心房；[医] 房, 前房"
  },
  "attic": {
    "phonetic": "'ætik",
    "meaning": "n. 阁楼, 顶楼；[医] 鼓室上隐窝"
  },
  "audio": {
    "phonetic": "'ɒ:diou",
    "meaning": "a. 音频的, 声音的；[电] 声频"
  },
  "audit": {
    "phonetic": "'ɒ:dit",
    "meaning": "n. 审计, 查帐；vt. 查(帐), 旁听；vi. 查账；[计] 查帐; 审查; 检查"
  },
  "auger": {
    "phonetic": "'ɒ:gә",
    "meaning": "n. 螺旋钻, 木螺钻；[机] 木螺钻"
  },
  "augur": {
    "phonetic": "'ɒ:gә",
    "meaning": "n. 占卜官, 预言者；v. 预示, 预言"
  },
  "aunty": {
    "phonetic": "'ɑ:nti",
    "meaning": "n. 阿姨, 姨妈, 舅妈, 姑妈, 伯母"
  },
  "aural": {
    "phonetic": "'ɒ:rәl",
    "meaning": "a. 耳的, 听觉的, 气氛的, 气味的, 光环的；[医] 耳的; 先兆的"
  },
  "avail": {
    "phonetic": "ә'veil",
    "meaning": "vi. 有用, 有利；vt. 有利于；n. 效用, 利益"
  },
  "avast": {
    "phonetic": "ә'væst",
    "meaning": "int. 停!且慢!"
  },
  "avert": {
    "phonetic": "ә'vә:t",
    "meaning": "vt. 转开, 避免, 防止"
  },
  "avian": {
    "phonetic": "'eiviәn",
    "meaning": "a. 鸟类的；n. 鸟"
  },
  "avoid": {
    "phonetic": "ә'vɒid",
    "meaning": "vt. 避免, 防止, 撤消；[法] 避免, 回避, 躲开"
  },
  "await": {
    "phonetic": "ә'weit",
    "meaning": "vt. 等候；vi. 等待着"
  },
  "awake": {
    "phonetic": "ә'weik",
    "meaning": "a. 醒着的；vt. 唤醒, 唤起, 使意识到；vi. 醒来, 被唤起, 意识到"
  },
  "award": {
    "phonetic": "ә'wɒ:d",
    "meaning": "n. 奖品, 裁定, 判决；vt. 授予, 给予"
  },
  "aware": {
    "phonetic": "ә'wєә",
    "meaning": "a. 知道的, 有觉悟的"
  },
  "awash": {
    "phonetic": "ә'wɒʃ",
    "meaning": "a. 与水面齐平的, 被浪冲打的"
  },
  "awful": {
    "phonetic": "'ɒ:ful",
    "meaning": "a. 可怕的, 庄严的, 虔敬的"
  },
  "awoke": {
    "phonetic": "ә'wәuk",
    "meaning": "awake的过去式和过去分词"
  },
  "axial": {
    "phonetic": "'æksiәl",
    "meaning": "a. 轴的, 成轴的, 轴向的；[医] 轴的, 中轴的"
  },
  "axiom": {
    "phonetic": "'æksiәm",
    "meaning": "n. 自明之理, 公理, 原理, 格言；[法] 公理, 原理, 原则"
  },
  "axion": {
    "phonetic": "",
    "meaning": "[医] 脑脊髓, 脑脊髓轴"
  },
  "azure": {
    "phonetic": "'æʒә",
    "meaning": "n. 天蓝色, 碧空；a. 蔚蓝的"
  },
  "babka": {
    "phonetic": "'bɑ:bkә",
    "meaning": "n. 巴布卡蛋糕"
  },
  "bacon": {
    "phonetic": "'beikәn",
    "meaning": "n. 熏猪肉；[机] 腌肉"
  },
  "badge": {
    "phonetic": "bædʒ",
    "meaning": "n. 徽章, 标记；[计] 标记"
  },
  "badly": {
    "phonetic": "'bædli",
    "meaning": "adv. 严重地, 恶劣地, 极度地"
  },
  "bagel": {
    "phonetic": "'beiɡәl",
    "meaning": "n. 百吉饼（先蒸后烤的发面圈）；[俚]（体育比赛中）零蛋"
  },
  "baggy": {
    "phonetic": "'bægi",
    "meaning": "a. 袋状的, 松垂的"
  },
  "baked": {
    "phonetic": "'beikid",
    "meaning": "a. 烘焙的；烤的"
  },
  "baker": {
    "phonetic": "'beikә",
    "meaning": "n. 面包师；[医] 烤箱(骨科用)"
  },
  "baldy": {
    "phonetic": "'bɔ:ldi",
    "meaning": "n. 秃子；n. (Baldy)人名；(法)巴尔迪；a. 秃的；秃顶的"
  },
  "baled": {
    "phonetic": "beɪl",
    "meaning": "vt. 将某物打成包或包装成捆；n. 大包, 大捆；货物；n. (Bale)人名；(斐)姆巴莱；(塞)巴莱；(英)贝尔"
  },
  "baler": {
    "phonetic": "'beilә",
    "meaning": "[化] 打包机"
  },
  "balky": {
    "phonetic": "'bɒ:ki",
    "meaning": "a. 停蹄不前的"
  },
  "balmy": {
    "phonetic": "'bɑ:mi",
    "meaning": "a. 芳香的, 温和的, 止痛的；[化] 香脂气味的"
  },
  "balsa": {
    "phonetic": "'bɒlsә",
    "meaning": "n. 西印度轻木, 木筏"
  },
  "banal": {
    "phonetic": "bә'nɑ:l",
    "meaning": "a. 平凡的, 陈腐的"
  },
  "bandy": {
    "phonetic": "'bændi",
    "meaning": "a. 向外弯曲的；vt. 打来打去, 谈论, 往复投掷"
  },
  "banjo": {
    "phonetic": "'bændʒәu",
    "meaning": "n. 班卓琴"
  },
  "bared": {
    "phonetic": "",
    "meaning": "n. (Bared)人名；(阿拉伯)巴雷德"
  },
  "barer": {
    "phonetic": "bɛəə",
    "meaning": "a. 光秃秃的( bare的比较级 ); （房间、柜子等） 空的; 赤裸的; 刚好够的"
  },
  "barge": {
    "phonetic": "bɑ:dʒ",
    "meaning": "n. 驳船；vt. 用船运输；vi. 蹒跚, 闯入"
  },
  "baron": {
    "phonetic": "'bærәn",
    "meaning": "n. 男爵；[法] 男爵, 贵族, 大王"
  },
  "basal": {
    "phonetic": "'beisl",
    "meaning": "a. 基础的, 基本的；[医] 基底的, 基础的"
  },
  "based": {
    "phonetic": "beist",
    "meaning": "v. 立基于, 以…为基础（base的过去式和过去分词）"
  },
  "basic": {
    "phonetic": "'beisik",
    "meaning": "n. 基本原理, 要素, 基本规律；a. 基本的, 碱性的；(计算机)BASIC语言"
  },
  "basil": {
    "phonetic": "'bæzil",
    "meaning": "n. 罗勒属植物；[医] 罗勒, 矮糠"
  },
  "basin": {
    "phonetic": "'beisn",
    "meaning": "n. 盆, 盆地；[医] 第三脑室, 骨盆"
  },
  "basis": {
    "phonetic": "'beisis",
    "meaning": "n. 基础, 主要成分；[化] 基底"
  },
  "baste": {
    "phonetic": "beist",
    "meaning": "vt. 用长针脚粗缝, 润以油脂, 狠揍"
  },
  "batch": {
    "phonetic": "bætʃ",
    "meaning": "n. 一次所烘的面包, 一次所制之量, 一组, 批, 成批, 分批；v. 成批, 分批处理；[计] 一批"
  },
  "bated": {
    "phonetic": "",
    "meaning": "a. 减少, 减弱, 抑制, 压低, 降低, (英)(非正式)大怒"
  },
  "bathe": {
    "phonetic": "beið",
    "meaning": "vt. 沐浴, 用水洗；vi. 洗澡"
  },
  "batik": {
    "phonetic": "'bætik",
    "meaning": "n. 蜡防印花法, 蜡防印花布"
  },
  "baton": {
    "phonetic": "'bætәn",
    "meaning": "n. 指挥棒, 接力棒, 警棍"
  },
  "batty": {
    "phonetic": "'bæti",
    "meaning": "a. 疯癫的, 古怪的, 蝙蝠的"
  },
  "bawdy": {
    "phonetic": "'bɒ:di",
    "meaning": "a. 淫秽的, 言语猥亵的"
  },
  "bayed": {
    "phonetic": "",
    "meaning": "vi. （尤指猎犬等）吠, 叫, 咆哮（bay的过去式与过去分词形式）"
  },
  "bayou": {
    "phonetic": "'baiu:",
    "meaning": "n. 支流"
  },
  "beach": {
    "phonetic": "bi:tʃ",
    "meaning": "n. 海滩"
  },
  "beady": {
    "phonetic": "'bi:di",
    "meaning": "a. 晶亮如小珠的, 饰有珠子的, 起泡的"
  },
  "beard": {
    "phonetic": "biәd",
    "meaning": "n. 胡须；vt. 抓住胡须, 公开反对"
  },
  "beast": {
    "phonetic": "bi:st",
    "meaning": "n. 畜生, 动物, 野兽, 兽性"
  },
  "beaut": {
    "phonetic": "bju:t",
    "meaning": "n. 漂亮的东西(或人)"
  },
  "bebop": {
    "phonetic": "'bi:bɒp",
    "meaning": "n. 博普爵士乐"
  },
  "beech": {
    "phonetic": "bi:tʃ",
    "meaning": "n. 山毛榉；[机] 山毛榉"
  },
  "beefy": {
    "phonetic": "'bi:fi",
    "meaning": "a. (牛)多肉的, 象牛肉的, 粗壮的, 结实的"
  },
  "befit": {
    "phonetic": "bi'fit",
    "meaning": "vt. 适合于, 适宜于"
  },
  "befog": {
    "phonetic": "bi'fɒg",
    "meaning": "vt. 罩入雾中, 使困惑, 使模糊"
  },
  "began": {
    "phonetic": "bi'gæn",
    "meaning": "begin的过去式"
  },
  "begat": {
    "phonetic": "bi'^æt",
    "meaning": "v. <废> beget的过去式"
  },
  "beget": {
    "phonetic": "bi'get",
    "meaning": "vt. 为某人之生父, 招致, 产生, 引起"
  },
  "begin": {
    "phonetic": "bi'gin",
    "meaning": "v. 开始；[计] 开始"
  },
  "begot": {
    "phonetic": "bi'gɒt",
    "meaning": "beget的过去式和过去分词"
  },
  "begun": {
    "phonetic": "bi'gʌn",
    "meaning": "begin的过去分词"
  },
  "beige": {
    "phonetic": "beiʒ",
    "meaning": "a. 淡棕色的；n. 薄斜纹呢, 米色"
  },
  "being": {
    "phonetic": "'bi:iŋ",
    "meaning": "n. 存在, 性质, 生命, 人, 生物, be的现在分词"
  },
  "belch": {
    "phonetic": "beltʃ",
    "meaning": "vi. 打嗝, 喷吐；vt. 打嗝, 吼叫着发出(命令), 喷吐；n. 打嗝, 喷吐"
  },
  "belie": {
    "phonetic": "bi'lai",
    "meaning": "vt. 掩饰, 与...不符, 使失望"
  },
  "belle": {
    "phonetic": "bel",
    "meaning": "n. 美女"
  },
  "belly": {
    "phonetic": "'beli",
    "meaning": "n. 腹部, 食欲；vt. 使鼓起；vi. 鼓起, 匍匐前进"
  },
  "below": {
    "phonetic": "bi'lәu",
    "meaning": "prep. 在下面；adv. 在下面"
  },
  "bench": {
    "phonetic": "bentʃ",
    "meaning": "n. 长椅子；[机] 台"
  },
  "bendy": {
    "phonetic": "'bendi",
    "meaning": "a. 易弯曲的,柔韧的"
  },
  "beret": {
    "phonetic": "'berei",
    "meaning": "n. 贝雷帽"
  },
  "berry": {
    "phonetic": "'beri",
    "meaning": "n. 浆果；vi. 采集浆果"
  },
  "berth": {
    "phonetic": "bә:θ",
    "meaning": "n. 船岸之间的水区, 锚地, 卧铺；vi. 停泊；vt. 使停泊"
  },
  "beset": {
    "phonetic": "bi'set",
    "meaning": "vt. 围绕, 使苦恼, 镶嵌"
  },
  "besot": {
    "phonetic": "bi'sɒt",
    "meaning": "vt. 使糊涂, 使痴迷, 使沉醉"
  },
  "betel": {
    "phonetic": "'bi:tәl",
    "meaning": "[医] д叶(用д叶卷一些槟榔子碎片及石灰,作为咀嚼剂,有强壮、兴奋作用)"
  },
  "bevel": {
    "phonetic": "'bevәl",
    "meaning": "n. 斜面, 斜角, 斜角规；vi. 成斜角；vt. 使成斜角"
  },
  "bezel": {
    "phonetic": "'bezәl",
    "meaning": "[计] 窗口"
  },
  "bible": {
    "phonetic": "'baibl",
    "meaning": "n. 圣经"
  },
  "bicep": {
    "phonetic": "baɪ'sep",
    "meaning": "[体]二头肌训练机"
  },
  "biddy": {
    "phonetic": "'bidi",
    "meaning": "n. 小鸡, 母鸡, 下女, 女佣"
  },
  "bided": {
    "phonetic": "baɪdid",
    "meaning": "v. 等待, 停留( bide的过去式 ); 居住; 等待; 面临"
  },
  "bidet": {
    "phonetic": "bidet",
    "meaning": "n. 小浴盆, 坐浴盆；[医] 坐浴盆"
  },
  "bigot": {
    "phonetic": "'bigәt",
    "meaning": "n. 盲从者, 偏执的人"
  },
  "biked": {
    "phonetic": "baikt",
    "meaning": "v. 自行车( bike的过去式和过去分词 )"
  },
  "biker": {
    "phonetic": "'baikә(r)",
    "meaning": "n. 骑自行车/摩托车的人"
  },
  "bilge": {
    "phonetic": "bildʒ",
    "meaning": "n. 底舱, 舱底污水, 废话；vt. 使船底漏水；vi. 膨胀, 船底漏水"
  },
  "bilgy": {
    "phonetic": "'bildʒi",
    "meaning": "a. 舱底水般的, 舱底水般臭味的"
  },
  "billy": {
    "phonetic": "'bili",
    "meaning": "n. 警棍, 伙伴"
  },
  "binge": {
    "phonetic": "bindʒ",
    "meaning": "n. 狂闹, 狂欢"
  },
  "bingo": {
    "phonetic": "'biŋgәu",
    "meaning": "n. 宾戈(一种赌博游戏), 烈酒"
  },
  "biome": {
    "phonetic": "'baiәum",
    "meaning": "n. 生物群落区"
  },
  "biped": {
    "phonetic": "'baiped",
    "meaning": "n. 两足动物；a. 有两足的"
  },
  "bipod": {
    "phonetic": "'baipɒd",
    "meaning": "n. 两脚架"
  },
  "birch": {
    "phonetic": "bә:tʃ",
    "meaning": "n. 桦树, 桦木, 桦条；[医] 桦"
  },
  "birth": {
    "phonetic": "bә:θ",
    "meaning": "n. 出生, 起源；[医] 生产, 分娩"
  },
  "bison": {
    "phonetic": "'baisәn",
    "meaning": "n. 野牛"
  },
  "biter": {
    "phonetic": "'baitә",
    "meaning": "n. 咬人的人(或动物), 骗子"
  },
  "bitsy": {
    "phonetic": "'bitsi",
    "meaning": "a. <口>小的,极小的"
  },
  "bitty": {
    "phonetic": "'biti",
    "meaning": "a. 零零碎碎的"
  },
  "black": {
    "phonetic": "blæk",
    "meaning": "n. 黑色, 黑颜料；a. 黑色的"
  },
  "blade": {
    "phonetic": "bleid",
    "meaning": "n. 叶片, 刀锋, 刀口, 剑；[医] 页[片], 叶片, 刀片, 刀刃, 刀口"
  },
  "blame": {
    "phonetic": "bleim",
    "meaning": "n. 过失, 责备；vt. 责备, 归咎于"
  },
  "bland": {
    "phonetic": "blænd",
    "meaning": "a. 温和的, 乏味的, 冷漠的；[医] 温和的, 淡的"
  },
  "blank": {
    "phonetic": "blæŋk",
    "meaning": "n. 空格, 空白；a. 空白的, 空虚的, 完全的, 无色的；vi. 消失, 成为空白；vt. 使无效, 取消, 封锁；[计] 空白"
  },
  "blare": {
    "phonetic": "blєә",
    "meaning": "n. 巨响, 吼叫声, 光泽；vi. 高声鸣叫, 大叫；vt. 大声喊出"
  },
  "blase": {
    "phonetic": "'blɑ:zei",
    "meaning": "a. 厌倦享乐的, 玩腻了的"
  },
  "blast": {
    "phonetic": "blæst",
    "meaning": "n. 一阵风, 爆炸, 枯萎病；vt. 炸, 使枯萎；vi. 炸, 猛攻, 猛烈抨击, 枯萎"
  },
  "blaze": {
    "phonetic": "bleiz",
    "meaning": "n. 火焰, 烈火, 光辉；vi. 燃烧, 发光；vt. 使燃烧, 宣布, 在树皮上刻痕"
  },
  "bleak": {
    "phonetic": "bli:k",
    "meaning": "a. 萧瑟的, 荒凉的, 阴冷的"
  },
  "bleat": {
    "phonetic": "bli:t",
    "meaning": "n. 羊的叫声；vi. 咩咩叫；vt. 以颤抖的声音说"
  },
  "bleed": {
    "phonetic": "bli:d",
    "meaning": "vi. 流血, 悲痛, 渗出；vt. 使出血, 榨取"
  },
  "bleep": {
    "phonetic": "bli:p",
    "meaning": "n. 哔哔声；vi. 发出哔哔声"
  },
  "blend": {
    "phonetic": "blend",
    "meaning": "vt. 混合；n. 混合"
  },
  "bless": {
    "phonetic": "bles",
    "meaning": "vt. 祝福, 祈佑, 使神圣化"
  },
  "blimp": {
    "phonetic": "blimp",
    "meaning": "n. 软式小型飞船, 顽固的保守分子"
  },
  "blind": {
    "phonetic": "blaind",
    "meaning": "n. 蒙蔽物, 窗帘；a. 盲目的, 瞎的, 不加思考的；vt. 使失明, 蒙蔽, 遮暗；adv. 盲目地"
  },
  "bling": {
    "phonetic": "",
    "meaning": "n. 锦衣珠宝"
  },
  "blink": {
    "phonetic": "bliŋk",
    "meaning": "vi. 眨眼, 闪亮；vt. 眨眼, 使闪亮；n. 眨眼, 瞬间, 闪光, 闪烁；[计] 闪烁"
  },
  "bliss": {
    "phonetic": "blis",
    "meaning": "n. 福佑, 天赐的福；[计] 实现系统软件的基本语言"
  },
  "blitz": {
    "phonetic": "blits",
    "meaning": "n. 闪电战；vt. 以闪电战攻击"
  },
  "bloat": {
    "phonetic": "blәut",
    "meaning": "vt. 使膨胀, 腌制, 使自大；vi. 膨胀, 肿起；n. 肿胀病人"
  },
  "block": {
    "phonetic": "blɒk",
    "meaning": "n. 街区, 木块, 石块, 块；vt. 阻塞, 封锁, 使成块状；[计] 块, 数据块"
  },
  "bloke": {
    "phonetic": "blәuk",
    "meaning": "n. 小子, 家伙"
  },
  "blond": {
    "phonetic": "blɒnd",
    "meaning": "a. 金发的；n. 白肤碧眼金发的人"
  },
  "blood": {
    "phonetic": "blʌd",
    "meaning": "n. 血, 血统, 流血, 气质, 生命；vt. 使出血, 用血涂"
  },
  "bloom": {
    "phonetic": "blu:m",
    "meaning": "n. 花, 开花, 青春, 钢块；vi. 开花, 焕发青春, 茂盛；vt. 使茂盛, 把...轧成钢坯"
  },
  "blown": {
    "phonetic": "blәun",
    "meaning": "a. 吹制的, 喘气的, 开着花的；blow的过去分词"
  },
  "bluer": {
    "phonetic": "",
    "meaning": "染蓝检验工"
  },
  "bluff": {
    "phonetic": "blʌf",
    "meaning": "n. 断崖, 绝壁, 吓唬；a. 直率的；v. 吓唬, 欺骗"
  },
  "blunt": {
    "phonetic": "blʌnt",
    "meaning": "a. 钝的, 坦率的, 麻痹的"
  },
  "blurb": {
    "phonetic": "blә:b",
    "meaning": "n. 推荐广告；vt. 推荐吹捧"
  },
  "blurt": {
    "phonetic": "blә:t",
    "meaning": "vt. 冲口说出, 脱口说出"
  },
  "blush": {
    "phonetic": "blʌʃ",
    "meaning": "vi. 脸红, 羞愧；vt. 弄成红色；n. 脸红"
  },
  "board": {
    "phonetic": "bɒ:d",
    "meaning": "n. 木板, 甲板, 膳食, 会议桌；vt. 乘船, 供膳食, 用板覆盖；vi. 搭伙；[计] 板"
  },
  "boast": {
    "phonetic": "bәust",
    "meaning": "n. 吹牛；vi. 吹牛, 自夸；vt. 夸口说, 自恃有"
  },
  "bobby": {
    "phonetic": "'bɒbi",
    "meaning": "n. 警察"
  },
  "bocce": {
    "phonetic": "'bɑtʃi:",
    "meaning": "n. ( 意大利式) 室外地滚球戏"
  },
  "boded": {
    "phonetic": "bəʊdid",
    "meaning": "v. 预示, 预告, 预言( bode的过去式和过去分词 ); 等待, 停留( bide的过去分词 ); 居住; （过去式用bided）等待"
  },
  "boffo": {
    "phonetic": "'bɔfәu",
    "meaning": "a. 受欢迎的, 极成功的"
  },
  "bogey": {
    "phonetic": "'bәugi",
    "meaning": "n. 妖怪, 可怕的人(物)；[电] 标准"
  },
  "boggy": {
    "phonetic": "'bɒgi",
    "meaning": "a. 似沼泽的"
  },
  "bogie": {
    "phonetic": "'bәugi",
    "meaning": "n. 妖怪, 可怕的人(物)；[机] 转向架"
  },
  "bogus": {
    "phonetic": "'bәugәs",
    "meaning": "a. 假的, 伪造的；[经] 伪的, 伪造的"
  },
  "boing": {
    "phonetic": "'bәuiŋ",
    "meaning": "int. 啵嘤（弹簧突然弹开或振动时所发出的声音）"
  },
  "bolus": {
    "phonetic": "'bәulәs",
    "meaning": "n. 小而圆的物块, 大丸药"
  },
  "boned": {
    "phonetic": "bәund",
    "meaning": "a. 骨骼的；去掉骨头的；用骨架撑起的；施过骨粉料的；去骨的"
  },
  "boner": {
    "phonetic": "'bәunә",
    "meaning": "n. 可笑的错误"
  },
  "boney": {
    "phonetic": "'bәuni",
    "meaning": "a. 瘦骨嶙峋的；多骨的"
  },
  "bongo": {
    "phonetic": "'bɒŋgәu",
    "meaning": "n. 邦戈羚羊(产于非洲), 小手鼓"
  },
  "bonny": {
    "phonetic": "'bɒni",
    "meaning": "a. 漂亮的"
  },
  "bonus": {
    "phonetic": "'bәunәs",
    "meaning": "n. 奖金, 红利；[经] 奖金, 红利, 额外补贴"
  },
  "booby": {
    "phonetic": "'bu:bi",
    "meaning": "n. 呆子, 傻瓜"
  },
  "booed": {
    "phonetic": "bu:d",
    "meaning": "v. 发出嘘声( boo的过去式和过去分词 )"
  },
  "boost": {
    "phonetic": "bu:st",
    "meaning": "n. 推进, 吹捧；vt. 推进, 提高, 宣扬, 促进"
  },
  "booth": {
    "phonetic": "bu:θ",
    "meaning": "n. 亭, 摊棚；[经] 货摊, 电话间"
  },
  "booty": {
    "phonetic": "'bu:ti",
    "meaning": "n. 战利品, 获得之物；[法] 赃物, 掳获物, 战利品"
  },
  "booze": {
    "phonetic": "bu:z",
    "meaning": "vi. 豪饮；n. 酒, 酒宴"
  },
  "boozy": {
    "phonetic": "'bu:zi",
    "meaning": "a. 酩酊的, 嗜酒的"
  },
  "borax": {
    "phonetic": "'bɒ:ræks",
    "meaning": "n. 硼砂；[化] 硼砂"
  },
  "bored": {
    "phonetic": "",
    "meaning": "a. 无聊的；烦人的；无趣的"
  },
  "borne": {
    "phonetic": "bɔ:n",
    "meaning": "v. 忍受；负荷；结果实；生子女（bear的过去分词）"
  },
  "boron": {
    "phonetic": "'bɒ:rɒn",
    "meaning": "n. 硼；[化] 硼B"
  },
  "bosom": {
    "phonetic": "'buzәm",
    "meaning": "n. 胸部, 胸, 胸怀, 内部, 中间；vt. 怀抱"
  },
  "boson": {
    "phonetic": "'bәuzɒn",
    "meaning": "n. 玻色子；[化] 玻色子"
  },
  "bossy": {
    "phonetic": "'bɒsi",
    "meaning": "a. 专横的, 浮雕装饰的"
  },
  "botch": {
    "phonetic": "bɒtʃ",
    "meaning": "v. 拙笨地修补, 糟蹋；n. 拙笨的修补, 难看的补缀"
  },
  "bough": {
    "phonetic": "bau",
    "meaning": "n. 大树枝"
  },
  "boule": {
    "phonetic": "'bu:li",
    "meaning": "n. 议会, 下议院, 立法会议"
  },
  "bound": {
    "phonetic": "baund",
    "meaning": "n. 跃, 回跳, 范围, 边界；a. 受约束的, 装有封面的, 有义务的, 关联的, 被束缚的, 准备去...的, 便秘的；vi. 跳跃, 弹起；vt. 使跳, 限制, 形成...的疆界；bind过去式和过去分词；[计] 装订的"
  },
  "bowed": {
    "phonetic": "bәud",
    "meaning": "a. 弯如弓的, 低垂的"
  },
  "bowel": {
    "phonetic": "'bauәl",
    "meaning": "n. 肠, 内脏, 内部；vt. 挖...的内脏"
  },
  "bower": {
    "phonetic": "'bauә",
    "meaning": "n. 凉亭, 树阴处"
  },
  "boxed": {
    "phonetic": "bɔkst",
    "meaning": "a. 醉酒的"
  },
  "boxer": {
    "phonetic": "'bɒksә",
    "meaning": "n. 拳师"
  },
  "brace": {
    "phonetic": "breis",
    "meaning": "n. 支柱, 曲柄, 支撑, 一对；vt. 紧缚, 支撑, 激励；vi. 打起精神；[计] 花括号"
  },
  "braid": {
    "phonetic": "breid",
    "meaning": "n. 辫子, 穗带；vt. 编成辫, 镶边"
  },
  "brain": {
    "phonetic": "brein",
    "meaning": "n. 脑；vt. 打碎脑部"
  },
  "brake": {
    "phonetic": "breik",
    "meaning": "n. 刹车, 阻碍, 丛林；v. 刹车"
  },
  "brand": {
    "phonetic": "brænd",
    "meaning": "n. 商标, 牌子, 烙印；vt. 打烙印于"
  },
  "brash": {
    "phonetic": "bræʃ",
    "meaning": "a. 性急的, 仓促的, 无礼的, 傲慢的；n. 胃灼热, 骤雨, 碎石堆"
  },
  "brass": {
    "phonetic": "bræs.brɑ:s",
    "meaning": "n. 黄铜, 黄铜制品；a. 黄铜的, 铜管乐器的；v. 镀以黄铜, 支付"
  },
  "brava": {
    "phonetic": "'brɑ:vɑ:",
    "meaning": "int. [向女性喝彩时用]好啊!"
  },
  "brave": {
    "phonetic": "breiv",
    "meaning": "a. 勇敢的, 美好的, 华丽的；n. 勇敢者；vt. 勇敢地面对"
  },
  "bravo": {
    "phonetic": "'brɑ:vәu",
    "meaning": "n. 亡命徒, 喝彩；interj. 好啊；vt. 喝彩"
  },
  "brawl": {
    "phonetic": "brɒ:l",
    "meaning": "n. 争吵；vi. 争吵, 哗哗地流水"
  },
  "brawn": {
    "phonetic": "brɒ:n",
    "meaning": "n. 发达的肌肉, 膂力, 体力, 熟腌肉；[医] 肌质, 肌肉"
  },
  "bread": {
    "phonetic": "bred",
    "meaning": "n. 面包, 生计, 食物；vt. 裹以面包屑"
  },
  "break": {
    "phonetic": "breik",
    "meaning": "n. 休息, 中断, 破裂处, 绝交, 破晓, 突变；vt. 打破, 弄破, 弄坏, 破坏, 违反, 打断, 削弱, 放弃；vi. 破碎, 决裂, 破晓, 突变, 变弱, 暂停；n. 分隔符；[计] 分隔符; 中断; DOS内部命令:设定扫描中断按键的时机"
  },
  "breed": {
    "phonetic": "bri:d",
    "meaning": "n. 种类, 品种；v. 养育, 引起, 饲养, 繁殖"
  },
  "briar": {
    "phonetic": "'braiә",
    "meaning": "n. [植]石南；荆棘；用石南根制成之烟斗"
  },
  "bribe": {
    "phonetic": "braib",
    "meaning": "n. 贿赂；vt. 贿赂, 收买；vi. 行贿"
  },
  "brick": {
    "phonetic": "brik",
    "meaning": "n. 砖块, 积木；a. 用砖做的；vt. 用砖造, 用砖砌"
  },
  "bride": {
    "phonetic": "braid",
    "meaning": "n. 新娘"
  },
  "brief": {
    "phonetic": "bri:f",
    "meaning": "n. 摘要, 简报；a. 简短的, 短暂的；vt. 对...作简报, 摘要, 节录"
  },
  "brier": {
    "phonetic": "'braiә",
    "meaning": "n. 多刺木质茎植物；[医] 欧石南"
  },
  "brine": {
    "phonetic": "brain",
    "meaning": "n. 盐水, 海水, 海；vt. 用浓盐水处理"
  },
  "bring": {
    "phonetic": "briŋ",
    "meaning": "vt. 带来, 产生, 促使, 提出；vi. 生产"
  },
  "brink": {
    "phonetic": "briŋk",
    "meaning": "n. 边缘, 陡岸"
  },
  "briny": {
    "phonetic": "'braini",
    "meaning": "a. 盐水似的, 海水似的, 咸的；[机] 含盐度"
  },
  "brisk": {
    "phonetic": "brisk",
    "meaning": "a. 强烈的, 寒冷而干燥的, 活泼的；vt. 使活泼；vi. 活跃起来"
  },
  "broad": {
    "phonetic": "brɒ:d",
    "meaning": "a. 宽广的, 辽阔的, 广大的, 显著的；adv. 宽阔地；n. 宽阔部分"
  },
  "broil": {
    "phonetic": "brɒil",
    "meaning": "vi. 烤, 争吵, 激动；vt. 烤；n. 烤, 灼热, 争吵"
  },
  "broke": {
    "phonetic": "brәuk",
    "meaning": "a. 一文不名的；break的过去式"
  },
  "bronc": {
    "phonetic": "brɔŋk",
    "meaning": "n. 北美西部产的野马"
  },
  "brood": {
    "phonetic": "bru:d",
    "meaning": "n. 一窝, 一伙；vt. 孵, 沉思"
  },
  "brook": {
    "phonetic": "bruk",
    "meaning": "n. 小溪；vt. 容忍"
  },
  "broom": {
    "phonetic": "bru:m",
    "meaning": "n. 扫帚, 金雀花；vt. 扫除"
  },
  "broth": {
    "phonetic": "brɒθ",
    "meaning": "n. 原汁清汤, 肉汤；[医] 肉汤(培养基)"
  },
  "brown": {
    "phonetic": "braun",
    "meaning": "n. 褐色；a. 褐色的；v. (使)变褐色"
  },
  "brunt": {
    "phonetic": "brʌnt",
    "meaning": "n. 主要冲力, 冲击"
  },
  "brush": {
    "phonetic": "brʌʃ",
    "meaning": "n. 刷子, 毛笔, 争吵；vt. 刷；vi. 擦过, 掠过；[计] 电刷"
  },
  "brusk": {
    "phonetic": "brusk",
    "meaning": "a. (在态度或言词方面)粗暴的, 简慢的, 生硬无礼的, 鲁莽的, 粗率的, 唐突的"
  },
  "brute": {
    "phonetic": "bru:t",
    "meaning": "n. 畜生, 残忍或好色之人；a. 残忍的, 无理性的, 畜生的"
  },
  "buddy": {
    "phonetic": "'bʌdi",
    "meaning": "n. 好朋友, 伙伴"
  },
  "budge": {
    "phonetic": "bʌdʒ",
    "meaning": "vi. 微微移动；vt. 推动；n. 羔羊皮"
  },
  "buggy": {
    "phonetic": "'bʌgi",
    "meaning": "a. 多虫的；n. 双轮单座轻马车, 四轮单座马车"
  },
  "bugle": {
    "phonetic": "bju:gl",
    "meaning": "n. 喇叭, 号角；v. 吹号"
  },
  "build": {
    "phonetic": "bild",
    "meaning": "v. 建立, 建筑；n. 构造, 体格"
  },
  "built": {
    "phonetic": "bilt",
    "meaning": "build的过去式和过去分词"
  },
  "bulge": {
    "phonetic": "bʌldʒ",
    "meaning": "n. 胀, 膨胀；vi. 凸出；vt. 使膨胀"
  },
  "bulgy": {
    "phonetic": "'bʌldʒi",
    "meaning": "a. 膨胀的, 凸出的"
  },
  "bulky": {
    "phonetic": "'bʌlki",
    "meaning": "a. 庞大的；[机] 庞大, 笨重"
  },
  "bully": {
    "phonetic": "'buli",
    "meaning": "n. 欺凌弱小者, 土霸；vt. 威胁, 恐吓, 欺负；vi. 欺负；a. 特好的, 第一流的；adv. 十分"
  },
  "bumpy": {
    "phonetic": "'bʌmpi",
    "meaning": "a. 颠簸的, 崎岖不平的"
  },
  "bunch": {
    "phonetic": "bʌntʃ",
    "meaning": "n. 串, 束；[医] 骨肿块(马)"
  },
  "bunny": {
    "phonetic": "'bʌni",
    "meaning": "n. 兔子"
  },
  "burka": {
    "phonetic": "'bә:kә",
    "meaning": "n. (穆斯林女子在公众场合下穿的)蒙住全身(只留眼睛)的长袍"
  },
  "burly": {
    "phonetic": "'bә:li",
    "meaning": "a. 结实的, 粗壮的, 率直的"
  },
  "burnt": {
    "phonetic": "bә:nt",
    "meaning": "burn的过去式和过去分词"
  },
  "burro": {
    "phonetic": "'burәu",
    "meaning": "n. 小驴"
  },
  "bursa": {
    "phonetic": "'bә:sә",
    "meaning": "n. 囊, 黏液囊；[医] 囊, 粘液囊, 伞(昆虫)"
  },
  "burst": {
    "phonetic": "bә:st",
    "meaning": "n. 破裂, 突发, 爆发；v. 爆裂, 突发, 充满；[计] 二进制位组; 字符组; 脉冲串"
  },
  "bused": {
    "phonetic": "",
    "meaning": "[计] 多丛的"
  },
  "bushy": {
    "phonetic": "'buʃi",
    "meaning": "a. 灌木一样的, 灌木茂密的, 浓密的"
  },
  "busty": {
    "phonetic": "'bʌsti",
    "meaning": "a. 大胸脯的, 胸部丰满的"
  },
  "butch": {
    "phonetic": "butʃ",
    "meaning": "n. [俚]充当男性角色的女同性恋者；粗鲁的男人或男孩"
  },
  "butte": {
    "phonetic": "bju:t",
    "meaning": "n. 孤峰"
  },
  "buxom": {
    "phonetic": "'bʌksәm",
    "meaning": "a. (妇女)丰满的, 健美的"
  },
  "buyer": {
    "phonetic": "'baiә",
    "meaning": "n. 买主, 买方；[经] 买主, 买方, 买手"
  },
  "buzzy": {
    "phonetic": "'bʌzi",
    "meaning": "n. 伸缩式风钻"
  },
  "bylaw": {
    "phonetic": "'bailɔ:",
    "meaning": "n. 附则, 细则"
  },
  "byway": {
    "phonetic": "'baiwei",
    "meaning": "n. 旁道, 偏僻小路"
  },
  "cabal": {
    "phonetic": "kә'bæl",
    "meaning": "n. 秘密结社, (尤指政治上的)阴谋；vi. 策划阴谋"
  },
  "cabby": {
    "phonetic": "'kæbi",
    "meaning": "n. 出租车司机, 出租马车的车夫"
  },
  "cabin": {
    "phonetic": "'kæbin",
    "meaning": "n. 小屋, 客舱；vt. 关在小屋"
  },
  "cable": {
    "phonetic": "'keibl",
    "meaning": "n. 电缆, 海底电报, 缆, 索；vi. 打海底电报；vt. 发海底电报, 缚住；[计] 电缆"
  },
  "cacao": {
    "phonetic": "kә'kɑ:әu",
    "meaning": "n. 可可豆, 可可树；[医] 可可"
  },
  "cache": {
    "phonetic": "kæʃ",
    "meaning": "n. 隐藏所, 隐藏的粮食或物资, 贮藏物, 高速缓冲存储器；vt. 隐藏, 窖藏；[计] 高速缓冲存储器, 高速缓冲"
  },
  "cacti": {
    "phonetic": "'kæktai",
    "meaning": "pl. 仙人掌"
  },
  "caddy": {
    "phonetic": "'kædi",
    "meaning": "n. 小盒子, 小罐, 茶叶罐；[计] 光盘盒"
  },
  "cadet": {
    "phonetic": "kә'det",
    "meaning": "n. 军官学校学生；[法] 军校学生"
  },
  "cadge": {
    "phonetic": "kædʒ",
    "meaning": "v. 行乞, 乞讨, 贩卖"
  },
  "cadre": {
    "phonetic": "'kædri.'kɑ:dә",
    "meaning": "n. 框架, 干部；[经] 干部"
  },
  "caged": {
    "phonetic": "",
    "meaning": "a. 关在笼子里的"
  },
  "cagey": {
    "phonetic": "'keidʒi",
    "meaning": "a. 狡猾的, 机警的, 有戒心的, 不敢表态的, 小心谨慎的, 不甚友善的"
  },
  "cairn": {
    "phonetic": "kєәn",
    "meaning": "n. 石堆纪念碑, 石冢, 堆石界标"
  },
  "caked": {
    "phonetic": "keɪkt",
    "meaning": "a. 沾满（厚厚的）…的"
  },
  "calve": {
    "phonetic": "kɑ:v",
    "meaning": "v. 生小牛, 下仔, (使)崩解"
  },
  "camel": {
    "phonetic": "'kæml",
    "meaning": "n. 骆驼, 打捞浮筒"
  },
  "cameo": {
    "phonetic": "'kæmiәu",
    "meaning": "n. 刻有浮雕的宝石或贝壳"
  },
  "campy": {
    "phonetic": "'kæmpi",
    "meaning": "a. 一副下流相的, 忸怩作态的"
  },
  "canal": {
    "phonetic": "kә'næl",
    "meaning": "n. 运河, 水道, 管, 沟渠；vt. 开运河"
  },
  "candy": {
    "phonetic": "'kændi",
    "meaning": "n. 糖果, 冰糖；vt. 用糖煮, 使结晶为砂糖；vi. 结晶为砂糖"
  },
  "caned": {
    "phonetic": "",
    "meaning": "vt. 用苔杖打（cane的过去式与过去分词形式）"
  },
  "canny": {
    "phonetic": "'kæni",
    "meaning": "a. 精明的, 谨慎的, 节约的"
  },
  "canoe": {
    "phonetic": "kә'nu:",
    "meaning": "n. 独木舟, 轻舟；vi. 乘独木舟；vt. 用独木舟运"
  },
  "canon": {
    "phonetic": "'kænәn",
    "meaning": "n. 教会法规, 圣典, 准则, 标准, 教士；[医] 规范, [加农]炮"
  },
  "caped": {
    "phonetic": "",
    "meaning": "a. 披斗篷的"
  },
  "caper": {
    "phonetic": "'keipә",
    "meaning": "n. 跳跃；vi. 雀跃, 蹦跳"
  },
  "capri": {
    "phonetic": "'kɑ:pri:",
    "meaning": "n. 卡普里酒（产于卡普里岛）；（意大利南方的）卡普里岛"
  },
  "caput": {
    "phonetic": "'keipәt",
    "meaning": "n. 头, 首"
  },
  "carat": {
    "phonetic": "'kærәt",
    "meaning": "n. 克拉；[化] 开; 克拉(宝石、金刚石重量单位,等于0.2克)"
  },
  "cared": {
    "phonetic": "kɛəd",
    "meaning": "v. 关心( care的过去式和过去分词 ); 担心; 在乎; 介意"
  },
  "caret": {
    "phonetic": "'kærәt",
    "meaning": "n. 脱字符；[计] ^符号"
  },
  "cargo": {
    "phonetic": "'kɑ:gәu",
    "meaning": "n. 货物；[经] 货柜"
  },
  "carny": {
    "phonetic": "'kɑ:ni",
    "meaning": "vt. 哄骗；n. (流动)游艺场"
  },
  "carol": {
    "phonetic": "'kærәl",
    "meaning": "n. 颂歌, 欢乐的歌；v. 歌颂, 欢唱"
  },
  "carom": {
    "phonetic": "'kærәm",
    "meaning": "n. 连着双球的一击, 碰击而反跳；vi. 一击连撞二球, 碰击而反跳"
  },
  "carry": {
    "phonetic": "'kæri",
    "meaning": "n. 进位, 射程, 运载；vt. 携带, 运送, 支持, 传送, 包含；vi. 被携带, 能达到；[计] 进位; 进位数"
  },
  "carte": {
    "phonetic": "kɑ:t",
    "meaning": "n. (附有价目的)菜单"
  },
  "carve": {
    "phonetic": "kɑ:v",
    "meaning": "v. 雕刻, 切开"
  },
  "cased": {
    "phonetic": "keist",
    "meaning": "v. 包装；装入（case的过去式和过去分词形式）"
  },
  "caste": {
    "phonetic": "kæst. kɑ:st",
    "meaning": "n. 印度的种姓制度, (排他的)社会团体"
  },
  "catch": {
    "phonetic": "kætʃ",
    "meaning": "n. 捕捉, 陷阱, 捕捉之物, 抓, 拉手；vt. 捕捉, 赶上, 感染, 听清楚；vi. 抓住, 燃着"
  },
  "cater": {
    "phonetic": "'keitә",
    "meaning": "v. 提供饮食及服务, 投合, 迎合"
  },
  "catty": {
    "phonetic": "'kæti",
    "meaning": "a. 恶毒的, 如猫的；[经] 斤"
  },
  "caulk": {
    "phonetic": "kɒ:k",
    "meaning": "vt. 填...以防漏"
  },
  "cause": {
    "phonetic": "kɒ:z",
    "meaning": "n. 原因, 目标；vt. 引起, 使产生, 使遭受"
  },
  "caved": {
    "phonetic": "",
    "meaning": "vt.& vi. （使）塌陷, 倒塌（cave的过去式与过去分词形式）"
  },
  "cavil": {
    "phonetic": "'kævil",
    "meaning": "n. 无端的指责, 挑剔；v. 吹毛求疵"
  },
  "cawed": {
    "phonetic": "kɔ:d",
    "meaning": "v. Carbon-Arc Welding 碳弧焊( caw的过去式和过去分词 )"
  },
  "cease": {
    "phonetic": "si:s",
    "meaning": "n. 停止；v. 停止, 终了"
  },
  "cedar": {
    "phonetic": "'si:dә",
    "meaning": "n. 雪松, 香椿；[医] 香柏, 杉, 雪松"
  },
  "ceded": {
    "phonetic": "si:did",
    "meaning": "v. 让给, 割让, 放弃( cede的过去式 )"
  },
  "celeb": {
    "phonetic": "si'leb",
    "meaning": "n. 著明人士"
  },
  "cello": {
    "phonetic": "'tʃelәu",
    "meaning": "n. 大提琴"
  },
  "chaat": {
    "phonetic": "",
    "meaning": "南亚香料水果（或煮蔬菜）"
  },
  "chafe": {
    "phonetic": "tʃeif",
    "meaning": "n. 擦伤, 气恼；v. 摩擦, 擦痛, 激怒"
  },
  "chaff": {
    "phonetic": "tʃæf",
    "meaning": "n. 谷壳, 糠, 揶揄；v. 开玩笑, 戏弄"
  },
  "chain": {
    "phonetic": "tʃein",
    "meaning": "n. 链, 枷锁, 束缚；vt. 用铁练锁住, 束缚, 囚禁"
  },
  "chair": {
    "phonetic": "tʃєә",
    "meaning": "n. 椅子, 显要的席位, 主席；vt. 使入座, 使就任要职"
  },
  "chalk": {
    "phonetic": "tʃɒ:k",
    "meaning": "n. 粉笔, 白垩；vt. 用粉笔写, 记录"
  },
  "champ": {
    "phonetic": "tʃæmp",
    "meaning": "v. 大声地嚼, 格格地咬；n. 格格地嚼, 咀嚼声"
  },
  "chant": {
    "phonetic": "tʃænt. tʃɑ:nt",
    "meaning": "n. 圣歌, 赞美诗；v. 吟唱, 诵扬"
  },
  "chaos": {
    "phonetic": "'keiɒs",
    "meaning": "n. 大混乱, 混沌；[化] 混沌; 浑沌"
  },
  "chard": {
    "phonetic": "tʃɑ:d",
    "meaning": "n. 可供食用的甜菜"
  },
  "charm": {
    "phonetic": "tʃɑ:m",
    "meaning": "n. 吸引力, 魔力, 符咒；vt. 迷住, 使陶醉, 行魔法；vi. 用符咒, 有魅力"
  },
  "chart": {
    "phonetic": "tʃɑ:t",
    "meaning": "n. 图表, 海图；vt. 制成图表；[计] 图表"
  },
  "chary": {
    "phonetic": "'tʃєәri",
    "meaning": "a. 细心的, 吝啬的, 谨慎的"
  },
  "chase": {
    "phonetic": "tʃeis",
    "meaning": "n. 追求, 狩猎, 追逐；vt. 追捕, 追逐, 雕刻, 在...上镶嵌宝石；vi. 追赶, 奔跑"
  },
  "chasm": {
    "phonetic": "'kæzәm",
    "meaning": "n. 陷窟, 裂口"
  },
  "cheap": {
    "phonetic": "tʃi:p",
    "meaning": "a. 便宜的, 不值钱的, 可鄙的；adv. 便宜地"
  },
  "cheat": {
    "phonetic": "tʃi:t",
    "meaning": "n. 欺骗, 作弊, 骗子；v. 欺骗, 逃脱, 骗取"
  },
  "check": {
    "phonetic": "tʃek",
    "meaning": "n. 检查, 支票, 阻止物, 寄物牌, 象棋中将军；vt. 检查, 阻止, 核对, 寄存, 托运；vi. 逐项相符, 开支票；[计] 复选"
  },
  "cheek": {
    "phonetic": "tʃi:k",
    "meaning": "n. 颊, 厚颜, 脸蛋；[医] 颊"
  },
  "cheep": {
    "phonetic": "tʃi:p",
    "meaning": "n. 吱吱的叫声；v. 吱吱地叫"
  },
  "cheer": {
    "phonetic": "tʃiә",
    "meaning": "n. 愉快, 振奋, 欢呼；vi. 欢呼, 喝彩, 快活起来；vt. 使振奋, 欢呼"
  },
  "chemo": {
    "phonetic": "ˈki:məʊ",
    "meaning": "n. 化疗"
  },
  "chess": {
    "phonetic": "tʃes",
    "meaning": "n. 国际象棋；[建] 雀麦"
  },
  "chest": {
    "phonetic": "tʃest",
    "meaning": "n. 胸, 胸部, 衣柜, 箱子；[医] 胸, 胸廓"
  },
  "chewy": {
    "phonetic": "'tʃu:i",
    "meaning": "a. 需要多嚼的, 难嚼的"
  },
  "chick": {
    "phonetic": "tʃik",
    "meaning": "n. 小鸡, 小鸟, 竹帘"
  },
  "chide": {
    "phonetic": "tʃaid",
    "meaning": "v. 斥责, 责骂"
  },
  "chief": {
    "phonetic": "tʃi:f",
    "meaning": "n. 领袖, 酋长, 长官, 主要部分；a. 主要的, 首位的"
  },
  "child": {
    "phonetic": "tʃaild",
    "meaning": "n. 孩子, 产物, 追随者；[医] 儿童"
  },
  "chili": {
    "phonetic": "'tʃili",
    "meaning": "n. 干辣椒, 辣椒粉"
  },
  "chill": {
    "phonetic": "tʃil",
    "meaning": "n. 寒冷, 寒意, 失意；a. 寒冷的, 冷漠的；vt. 使寒心, 冷冻；vi. 变冷"
  },
  "chime": {
    "phonetic": "tʃaim",
    "meaning": "n. 钟声, 钟, 和谐；vi. 鸣, 奏出谐和的乐声, 和谐；vt. 敲出和谐的声音, 打钟报时, 重复说"
  },
  "chimp": {
    "phonetic": "tʃimp",
    "meaning": "n. 黑猩猩"
  },
  "china": {
    "phonetic": "'tʃainә",
    "meaning": "n. 中国, 瓷器；a. 中国的"
  },
  "chino": {
    "phonetic": "'tʃi:nәu",
    "meaning": "n. 斜纹棉布裤；丝光斜纹棉布"
  },
  "chirp": {
    "phonetic": "tʃә:p",
    "meaning": "n. 喳喳声, 唧唧声；v. 吱喳而鸣"
  },
  "chive": {
    "phonetic": "tʃaiv",
    "meaning": "n. 细香葱"
  },
  "chock": {
    "phonetic": "tʃɒk",
    "meaning": "n. 塞块, 木楔, 楔形木垫；vt. 用楔子垫阻, 收放定盘上；adv. 满满地"
  },
  "choir": {
    "phonetic": "'kwaiә",
    "meaning": "n. 唱诗班, 唱诗班的席位；v. 合唱"
  },
  "choke": {
    "phonetic": "tʃәuk",
    "meaning": "vt. 窒息, 阻塞, 噎, 抑制；vi. 窒息, 阻塞, 噎；n. 窒息, 噎, 阻气门"
  },
  "chomp": {
    "phonetic": "tʃɒmp",
    "meaning": "vi. 使劲地嚼, 格格地咬"
  },
  "chord": {
    "phonetic": "kɒ:d",
    "meaning": "n. 弦, 和音；[医] 索, 带"
  },
  "chore": {
    "phonetic": "tʃɒ:",
    "meaning": "n. 零工, 家务；[经] 零工"
  },
  "chose": {
    "phonetic": "tʃәuz",
    "meaning": "n. 动产；choose的过去式"
  },
  "chuck": {
    "phonetic": "tʃʌk",
    "meaning": "n. 抚弄, 赶走, 抛掷, 咯咯声, 颈肉, 卡盘；vt. 轻拍, 抛掷, 驱逐, 丢弃, 用卡盘夹住；vi. 咯咯叫"
  },
  "chump": {
    "phonetic": "tʃʌmp",
    "meaning": "n. 大木块, (羊)腰臀部的肉, 傻瓜"
  },
  "chunk": {
    "phonetic": "tʃʌŋk",
    "meaning": "n. 大块, 矮胖的人(或物)；[经] 定样"
  },
  "churn": {
    "phonetic": "tʃә:n",
    "meaning": "n. 搅乳器；v. 搅拌, 搅动"
  },
  "chute": {
    "phonetic": "ʃu:t",
    "meaning": "n. 瀑布, 斜槽；[化] 斜槽; 滑槽; 滑运道"
  },
  "cider": {
    "phonetic": "'saidә",
    "meaning": "n. 苹果汁, 苹果酒；[建] 苹果汁"
  },
  "cigar": {
    "phonetic": "si'gɑ:",
    "meaning": "n. 雪茄"
  },
  "cinch": {
    "phonetic": "sintʃ",
    "meaning": "n. 肚带, 紧握, 必然(发生)的事情；vt. 给...系肚带, 紧握住, 抓牢"
  },
  "circa": {
    "phonetic": "'sә:kә",
    "meaning": "prep. 大约在；[经] 大约"
  },
  "cited": {
    "phonetic": "",
    "meaning": "v. 引用（cite的过去分词）"
  },
  "civet": {
    "phonetic": "'sivit",
    "meaning": "n. 香猫, 香猫香, 麝猫香；[化] 灵猫香"
  },
  "civic": {
    "phonetic": "'sivik",
    "meaning": "a. 市的, 市民的, 公民的；[法] 公民的, 市民的, 公民资格的"
  },
  "civil": {
    "phonetic": "'sivәl",
    "meaning": "a. 市民的, 公民的, 有礼貌的；[法] 公民的, 国民的, 民用的"
  },
  "clack": {
    "phonetic": "klæk",
    "meaning": "v. 噼啪响；n. 噼啪响"
  },
  "clade": {
    "phonetic": "kleid",
    "meaning": "n. [生]进化枝,分化枝"
  },
  "claim": {
    "phonetic": "kleim",
    "meaning": "n. 要求, 要求权, 断言, 权利；vt. 要求, 认领, 主张；vi. 提出要求, 主张, 断言"
  },
  "clamp": {
    "phonetic": "klæmp",
    "meaning": "n. 夹钳；vt. 夹紧, 强加"
  },
  "clang": {
    "phonetic": "klæŋ",
    "meaning": "n. 当当声, 铿锵声；vi. 发出当当声, 发铿锵声；vt. 使发铿锵声"
  },
  "clank": {
    "phonetic": "klæŋk",
    "meaning": "n. 叮当声；vi. 发叮当声, 发铿锵声；vt. 使铿然作响"
  },
  "clash": {
    "phonetic": "klæʃ",
    "meaning": "n. 冲突, 撞击声, 抵触；vi. 冲突, 抵触；vt. 使发出撞击声；[计] 对撞"
  },
  "clasp": {
    "phonetic": "klɑ:sp",
    "meaning": "n. 扣子, 钩, 紧握；v. 扣紧, 紧握"
  },
  "class": {
    "phonetic": "klɑ:s",
    "meaning": "n. 班级, 阶级, 种类, 课；vt. 分类；[计] 类别; 类; 种类; 类程"
  },
  "clean": {
    "phonetic": "kli:n",
    "meaning": "a. 干净的, 清白的, 简洁的；adv. 清洁地, 完全地；vt. 清理, 使干净, 出空；vi. 被搞干净；n. 打扫"
  },
  "clear": {
    "phonetic": "kliә",
    "meaning": "a. 清楚的, 明确的, 澄清的；adv. 清晰地；vt. 澄清, 清除障碍；vi. 放晴, 变清澈；n. 空隙；[计] 清除"
  },
  "cleat": {
    "phonetic": "kli:t",
    "meaning": "n. 楔子, 栓, 系缆墩；vt. 装上栓, 把索系在栓上"
  },
  "cleft": {
    "phonetic": "kleft",
    "meaning": "n. 裂缝, 裂口；a. 劈开的；cleave的过去式和过去分词"
  },
  "clerk": {
    "phonetic": "klә:k",
    "meaning": "n. 办事员, 职员, 文书；vi. 当店员"
  },
  "click": {
    "phonetic": "klik",
    "meaning": "n. 咔哒声, 啪嗒声；vi. 作咔哒声；vt. 使发咔哒声；[计] 单击"
  },
  "cliff": {
    "phonetic": "klif",
    "meaning": "n. 悬崖, 绝壁"
  },
  "climb": {
    "phonetic": "klaim",
    "meaning": "v. 攀登, 上升, 爬；n. 攀登, 爬升"
  },
  "clime": {
    "phonetic": "klaim",
    "meaning": "n. 地方, 气候区"
  },
  "cling": {
    "phonetic": "kliŋ",
    "meaning": "vi. 粘紧, 附着, 紧贴, 坚持"
  },
  "clink": {
    "phonetic": "kliŋk",
    "meaning": "n. 叮当声；v. (使)发叮当声"
  },
  "cloak": {
    "phonetic": "klәuk",
    "meaning": "n. 斗蓬, 大氅, 掩护；vt. 遮掩, 隐匿, 使披斗蓬"
  },
  "clock": {
    "phonetic": "klɒk",
    "meaning": "n. 时钟, 计时器, (袜子上的)绣花边花；vt. 绣花样, 记时, 记录；vi. 记录时间；[计] 时钟"
  },
  "clomp": {
    "phonetic": "klɒmp",
    "meaning": "vi. 重踏着走"
  },
  "clone": {
    "phonetic": "klәun",
    "meaning": "n. 无性系；[计] 代用件"
  },
  "close": {
    "phonetic": "klәuz",
    "meaning": "n. 结束, 完结；a. 靠近的, 亲近的, 亲密的, 严密的, 关闭的, 狭窄的, 秘密的；vt. 关, 结束, 使靠近, 封闭, 使接近；vi. 关闭, 结束, 靠近；adv. 接近地, 紧密地；[计] 关闭"
  },
  "cloth": {
    "phonetic": "klɒ:θ. klɒθ",
    "meaning": "n. 布料, 织品, 布；[建] 布"
  },
  "cloud": {
    "phonetic": "klaud",
    "meaning": "n. 云, 阴暗, 烟雾, 疑团；vt. 以云遮敝, 笼罩, 使黯然；vi. 乌云密布, 阴沉"
  },
  "clout": {
    "phonetic": "klaut",
    "meaning": "n. 敲击, 破布；vt. 打补钉"
  },
  "clove": {
    "phonetic": "klәuv",
    "meaning": "n. 丁香；cleave的过去式"
  },
  "clown": {
    "phonetic": "klaun",
    "meaning": "n. 小丑, 乡下人"
  },
  "cluck": {
    "phonetic": "klʌk",
    "meaning": "n. 咯咯的叫声；v. 咯咯叫"
  },
  "clued": {
    "phonetic": "",
    "meaning": "(clue 的过去分词) n. 线索, 暗示；vt. 暗示, 提供线索"
  },
  "clump": {
    "phonetic": "klʌmp",
    "meaning": "n. 丛, 块, 笨重的脚步声；[计] 丛"
  },
  "clung": {
    "phonetic": "klʌŋ",
    "meaning": "cling的过去式和过去分词"
  },
  "clunk": {
    "phonetic": "klʌnk",
    "meaning": "n. 沉闷的金属声；v. 发出沉闷声"
  },
  "coach": {
    "phonetic": "kәutʃ",
    "meaning": "n. 四轮大马车, 教练；vt. 训练, 指导；vi. 坐马车旅行, 作指导"
  },
  "coast": {
    "phonetic": "kәust",
    "meaning": "n. 海岸, 滑坡；v. 沿海岸而行"
  },
  "cobra": {
    "phonetic": "'kәubrә",
    "meaning": "n. 眼镜蛇；[医] 眼镜蛇"
  },
  "cocky": {
    "phonetic": "'kɒki",
    "meaning": "a. 骄傲的, 自大的, 太过自信的"
  },
  "cocoa": {
    "phonetic": "'kәukәu",
    "meaning": "n. 可可粉, 可可茶, 可可色；[医] 可可, 可可豆"
  },
  "coded": {
    "phonetic": "'kәudid",
    "meaning": "a. 编码的；电码的；译成电码的"
  },
  "coder": {
    "phonetic": "'kәudә",
    "meaning": "n. 编码器；[计] 编码员"
  },
  "codex": {
    "phonetic": "'kәudeks",
    "meaning": "n. 手抄本, 法典, 药典；[计] 编译码器, 压缩/解压程序"
  },
  "colic": {
    "phonetic": "'kɒlik",
    "meaning": "n. 绞痛, 急腹痛；[医] 结肠的; 绞痛, 急腹痛"
  },
  "colon": {
    "phonetic": "'kәulәn",
    "meaning": "n. 冒号, 结肠；[医] 结肠"
  },
  "color": {
    "phonetic": "'kʌlә",
    "meaning": "n. 颜色, 面色, 颜料, 外貌；vt. 把...涂上颜色, 粉饰, 使脸红, 歪曲；vi. 变色"
  },
  "combo": {
    "phonetic": "'kɒmbәu",
    "meaning": "n. 小型爵士乐团"
  },
  "comet": {
    "phonetic": "'kɒmit",
    "meaning": "n. 彗星"
  },
  "comfy": {
    "phonetic": "'kʌmfi",
    "meaning": "a. 舒服的,轻松的"
  },
  "comic": {
    "phonetic": "'kɒmik",
    "meaning": "n. 连环漫画, 喜剧演员, 滑稽的人；a. 滑稽的, 有趣的, 喜剧的"
  },
  "comma": {
    "phonetic": "'kɒmә",
    "meaning": "n. 逗点, 逗号"
  },
  "conch": {
    "phonetic": "kɒŋk",
    "meaning": "n. 海螺壳"
  },
  "condo": {
    "phonetic": "kәn'dәu",
    "meaning": "n. 共同统治, 共管下的政府, 共管, 多层公寓大楼, 由个人占用的一套公寓房间"
  },
  "coned": {
    "phonetic": "kəʊnd",
    "meaning": "被探照灯光来照中的"
  },
  "conga": {
    "phonetic": "'kɒŋgә",
    "meaning": "n. 康茄舞, 康茄舞乐曲；vi. 跳康茄舞"
  },
  "conic": {
    "phonetic": "'kɒnik",
    "meaning": "a. 圆锥的, 圆锥形的；[医] 圆锥形的"
  },
  "cooed": {
    "phonetic": "ku:d",
    "meaning": "v. （鸽）咕咕地叫, 发出鸽叫般的声音( coo的过去式 ); 温柔可爱地说话"
  },
  "copay": {
    "phonetic": "'kəʊˌpeɪ",
    "meaning": "n. [美国英语]（指费用超过扣除款项由病人支付给保险公司的）共付医疗费[亦称作 copayment]"
  },
  "coped": {
    "phonetic": "kəupt",
    "meaning": "v. 成功地应付, 对付( cope的过去式和过去分词 )"
  },
  "copse": {
    "phonetic": "kɒps",
    "meaning": "n. 矮林, 小灌木林, 萌生林"
  },
  "coral": {
    "phonetic": "'kɒrәl",
    "meaning": "n. 珊瑚, 珊瑚色；[化] 珊瑚"
  },
  "cored": {
    "phonetic": "",
    "meaning": "a. 有心的；装芯的"
  },
  "corer": {
    "phonetic": "'kɒ:rә",
    "meaning": "n. (果实的)去心器"
  },
  "corgi": {
    "phonetic": "'kɔ:^i",
    "meaning": "n. 小狗"
  },
  "corky": {
    "phonetic": "'kɒ:ki",
    "meaning": "a. 软木的, 活泼的"
  },
  "corny": {
    "phonetic": "'kɒ:ni",
    "meaning": "a. 谷类的, 乡巴佬似的, 粗野的；[建] 角制的, 角(质)的"
  },
  "corps": {
    "phonetic": "kɒ:",
    "meaning": "n. 军, 队, 部队, 兵种；[医] 对, 团; 体, 物体"
  },
  "couch": {
    "phonetic": "kautʃ",
    "meaning": "n. 长沙发, 睡椅, 卧榻；vt. 横躺, 表达；vi. 躺下, 蹲伏"
  },
  "cough": {
    "phonetic": "kɒf",
    "meaning": "n. 咳嗽；vi. 咳嗽；vt. 咳出"
  },
  "could": {
    "phonetic": "kud",
    "meaning": "aux. 可以, 能"
  },
  "count": {
    "phonetic": "kaunt",
    "meaning": "vt. 计算, 视为；vi. 计数；n. 计算, 合计, 计数, 伯爵；[计] 计数"
  },
  "coupe": {
    "phonetic": "'ku:pei",
    "meaning": "n. 双座四轮轿式马车, 小轿车, 双门轿式小汽车, (英)铁路客车尾部的分隔车厢"
  },
  "court": {
    "phonetic": "kɒ:t",
    "meaning": "n. 法院, 庭院, 奉承；vt. 献殷勤, 追求, 招致；vi. 求爱"
  },
  "couth": {
    "phonetic": "ku:θ",
    "meaning": "a. 文雅的, 有礼貌的"
  },
  "coven": {
    "phonetic": "'kʌvәn, 'kәu-",
    "meaning": "n. 女巫大聚会"
  },
  "cover": {
    "phonetic": "'kʌvә",
    "meaning": "n. 盖子, 封面, 藉口；vt. 覆盖, 掩饰, 保护, 掩护, 包括；vi. 覆盖"
  },
  "covet": {
    "phonetic": "'kʌvit",
    "meaning": "v. 妄想, 垂涎"
  },
  "covey": {
    "phonetic": "'kʌvi",
    "meaning": "n. (一)群, 一队"
  },
  "cowed": {
    "phonetic": "kaʊd",
    "meaning": "vt. 恐吓（cow的过去式与过去分词形式）"
  },
  "cower": {
    "phonetic": "'kauә",
    "meaning": "vi. 畏缩, 退缩, 抖缩"
  },
  "coxed": {
    "phonetic": "kɔkst",
    "meaning": "a. (赛艇)有舵手的"
  },
  "coyly": {
    "phonetic": "kɔɪlɪ",
    "meaning": "adv. 害羞地, 羞怯地"
  },
  "crack": {
    "phonetic": "kræk",
    "meaning": "n. 裂缝, 爆裂声；v. (使)爆裂, (使)裂开, (使)发出爆裂声；a. 第一流的；adv. 啪地一声"
  },
  "craft": {
    "phonetic": "kræft",
    "meaning": "n. 技艺, 手艺, 诡计；vt. 精心制作"
  },
  "cramp": {
    "phonetic": "kræmp",
    "meaning": "n. 痉挛, 腹部绞痛, 铁夹钳；a. 狭窄的, 难认的；vt. 使抽筋, 以铁箍扣紧, 束缚"
  },
  "crane": {
    "phonetic": "krein",
    "meaning": "n. 鹤, 起重机；vt. 伸颈, 起重机起吊；vi. 伸颈看, 迟疑"
  },
  "crank": {
    "phonetic": "kræŋk",
    "meaning": "a. 不稳的, 脾气暴燥的, 易怒的；n. 曲柄, 奇想；vt. 装曲柄；vi. 转动曲柄"
  },
  "crash": {
    "phonetic": "kræʃ",
    "meaning": "n. 哗啦声, 猛撞, 崩溃, 粗布；v. 撞碎, 破碎, (使)...坠毁；a. 速成的；[计] 崩溃"
  },
  "crass": {
    "phonetic": "kræs",
    "meaning": "a. 粗俗的, 愚钝的, 粗糙的, 非常的"
  },
  "crate": {
    "phonetic": "kreit",
    "meaning": "n. 板条箱, 装货箱；[建] 篓, 筐"
  },
  "crave": {
    "phonetic": "kreiv",
    "meaning": "v. 渴望, 热望, 恳求"
  },
  "crawl": {
    "phonetic": "krɒ:l",
    "meaning": "n. 爬行, 匍匐而行, 养鱼池；v. 爬行"
  },
  "craze": {
    "phonetic": "kreiz",
    "meaning": "n. 狂热, 大流行；v. (使)发狂, (使)开裂"
  },
  "crazy": {
    "phonetic": "'kreizi",
    "meaning": "a. 发狂的, 狂热的"
  },
  "creak": {
    "phonetic": "kri:k",
    "meaning": "n. 辗轧声, 嘎吱嘎吱声；vi. 作辗轧声, 发出辗轧声"
  },
  "cream": {
    "phonetic": "kri:m",
    "meaning": "n. 乳酪, 奶油, 面霜；[医] 乳油, 乳皮; 乳膏, 霜"
  },
  "credo": {
    "phonetic": "'kri:dәu",
    "meaning": "n. 信条"
  },
  "creed": {
    "phonetic": "kri:d",
    "meaning": "n. 宗教信条, 教义, 纲领"
  },
  "creek": {
    "phonetic": "kri:k",
    "meaning": "n. 小溪, 小河, 小湾"
  },
  "creep": {
    "phonetic": "kri:p",
    "meaning": "n. 爬, 徐行, 蠕动；vi. 爬, 蔓延, 潜行"
  },
  "crema": {
    "phonetic": "'kreɪmə",
    "meaning": "[地名] [意大利] 克雷马"
  },
  "creme": {
    "phonetic": "",
    "meaning": "n. 奶油调味液, 乳剂, 香甜的酒"
  },
  "crepe": {
    "phonetic": "kreip",
    "meaning": "n. 绉丝, 绉呢, 绉绸, 绉布, 绉线, 绉橡胶, 皱胶, 绉纸, 黑绉纱, 小而极薄的烤饼；[化] 皱片"
  },
  "crept": {
    "phonetic": "krept",
    "meaning": "creep的过去式"
  },
  "cress": {
    "phonetic": "kres",
    "meaning": "n. 水芹"
  },
  "crest": {
    "phonetic": "krest",
    "meaning": "n. 冠, 饰毛, 头盔的顶部；vi. 到达绝顶；vt. 加以顶饰"
  },
  "crick": {
    "phonetic": "krik",
    "meaning": "n. 肌肉抽筋, 急性硬直；vt. 引起痉挛"
  },
  "cried": {
    "phonetic": "kraid",
    "meaning": "v. 哭泣；喊叫（cry的过去分词）"
  },
  "crier": {
    "phonetic": "'kraiә",
    "meaning": "n. 喊叫者, 哭泣者, 传呼员；[法] 传呼员, 法警"
  },
  "crime": {
    "phonetic": "kraim",
    "meaning": "n. 犯罪, 罪行, 罪恶；[法] 犯罪, 罪, 罪恶"
  },
  "crimp": {
    "phonetic": "krimp",
    "meaning": "n. 诱人当兵的人, 拳曲, 鬈发；vt. 诱...去当兵, 使拳曲, 使有褶"
  },
  "crisp": {
    "phonetic": "krisp",
    "meaning": "a. 脆的, 新鲜的, 活泼的；v. (使)烘脆, (使)拳曲, (使)起皱；n. 松脆物"
  },
  "croak": {
    "phonetic": "krәuk",
    "meaning": "n. 呱呱叫声, 哇哇声；vi. 呱呱地叫, 发牢骚；vt. 用嘶哑的声音说"
  },
  "crock": {
    "phonetic": "krɒk",
    "meaning": "n. 壶, 罐, 碎瓦片；vt. 使受伤, 弄衰弱；vi. 摩擦脱色, 衰竭"
  },
  "crone": {
    "phonetic": "krәun",
    "meaning": "n. 干瘪老太婆, 老母羊"
  },
  "crony": {
    "phonetic": "'krәuni",
    "meaning": "n. 密友, 亲密伙伴, 好朋友"
  },
  "crook": {
    "phonetic": "kruk",
    "meaning": "n. 钩, 弯曲部分, 坏蛋；vt. 使弯曲, 诈骗；vi. 弯曲"
  },
  "croon": {
    "phonetic": "kru:n",
    "meaning": "v. 低声歌唱, 低唱, 低吟；n. 低唱, 低吟, 轻哼"
  },
  "cross": {
    "phonetic": "krɒs",
    "meaning": "n. 十字架, 十字架形物件, 交叉, 十字标, 交叉路, 磨难, 杂交；a. 生气的, 交叉的, 相反的；v. 交叉, 横过, 越过；[计] 交叉, 十字标"
  },
  "croup": {
    "phonetic": "kru:p",
    "meaning": "n. 哮吼, 四脚动物的臀部；[医] 格鲁布, 哮吼"
  },
  "crowd": {
    "phonetic": "kraud",
    "meaning": "n. 群众, 一伙人；vt. 拥挤, 挤满, 挤进"
  },
  "crown": {
    "phonetic": "kraun",
    "meaning": "n. 王冠, 王权, 顶点；vt. 使成王, 加冕, 居...之顶"
  },
  "crude": {
    "phonetic": "kru:d",
    "meaning": "a. 天然的, 未成熟的, 粗糙的, 粗鲁的；n. 天然的物质"
  },
  "cruel": {
    "phonetic": "'kru:әl",
    "meaning": "a. 残酷的, 令人极痛苦的；[法] 残忍的, 残酷的"
  },
  "crumb": {
    "phonetic": "krʌm",
    "meaning": "n. 碎屑, 面包屑, 少许；vt. 捏碎, 弄碎"
  },
  "crump": {
    "phonetic": "krʌmp",
    "meaning": "vi. 轰地一声爆炸；n. 炸弹, 嘎吱声"
  },
  "crush": {
    "phonetic": "krʌʃ",
    "meaning": "n. 压碎, 粉碎, 群众, 迷恋；vt. 压破, 征服, 塞, 弄皱, 榨出；vi. 被压碎, 起皱, 挤"
  },
  "crust": {
    "phonetic": "krʌst",
    "meaning": "n. 外壳, 坚硬外皮, 面包皮；vt. 盖以硬皮；vi. 结硬皮"
  },
  "crypt": {
    "phonetic": "kript",
    "meaning": "n. 土窖, 地穴, 地下室；[医] 隐窝; 滤泡, 腺管"
  },
  "cubby": {
    "phonetic": "'kʌbi",
    "meaning": "n. 小房间"
  },
  "cubed": {
    "phonetic": "kju:bd",
    "meaning": "[医]荜澄茄"
  },
  "cubic": {
    "phonetic": "'kju:bik",
    "meaning": "a. 立方体的, 立方的；[机] 立方的, 立方体的"
  },
  "cubit": {
    "phonetic": "'kju:bit",
    "meaning": "n. 肘尺"
  },
  "cuing": {
    "phonetic": "",
    "meaning": "n. 提示, 线索；vt. 给...暗示(或提示)；[计] 尾接指令"
  },
  "cumin": {
    "phonetic": "'kʌmin",
    "meaning": "n. 莳萝, 土茴香子；[化] 枯茗; 欧莳萝; 异丙苯"
  },
  "cupid": {
    "phonetic": "'kju:pid",
    "meaning": "n. 丘比特, 丘比特画像, 美男孩"
  },
  "cured": {
    "phonetic": "'kjuәd",
    "meaning": "a. 治愈的；熟化的；熏制的"
  },
  "curer": {
    "phonetic": "'kjuәrә",
    "meaning": "治疗者, 治疗器"
  },
  "curio": {
    "phonetic": "'kjuәriәu",
    "meaning": "n. 古董"
  },
  "curly": {
    "phonetic": "'kә:li",
    "meaning": "a. 拳曲的, 卷毛的, 弯曲的"
  },
  "curry": {
    "phonetic": "'kʌri. 'kә:ri",
    "meaning": "n. 咖哩粉, 咖哩饭菜；vt. 用咖哩粉调味, 用马梳梳, 制革"
  },
  "curse": {
    "phonetic": "kә:s",
    "meaning": "n. 咒骂, 诅咒；vt. 诅咒, 咒骂"
  },
  "curve": {
    "phonetic": "kә:v",
    "meaning": "n. 曲线, 弯曲, 曲线球；vt. 弯, 使弯曲；vi. 成曲形"
  },
  "curvy": {
    "phonetic": "'kә:vi",
    "meaning": "a. 弯曲的；曲线美的（等于curvaceous）"
  },
  "cushy": {
    "phonetic": "'kuʃi",
    "meaning": "a. 舒适的, 安逸的"
  },
  "cuter": {
    "phonetic": "",
    "meaning": "a. 可爱的；聪明的（cute的比较级）"
  },
  "cutie": {
    "phonetic": "'kju:ti",
    "meaning": "n. 漂亮女孩"
  },
  "cutup": {
    "phonetic": "'kʌtʌp",
    "meaning": "n. 插科打诨的人, 胡闹的人"
  },
  "cyber": {
    "phonetic": "'saibә",
    "meaning": "a. 网络的, 计算机的"
  },
  "cycle": {
    "phonetic": "'saikl",
    "meaning": "n. 周期, 循环, 自行车, 一段时间, 整套；vi. 循环, 轮转, 骑自行车；vt. 使循环, 使轮转；[计] 环路; 周期; 循环"
  },
  "cynic": {
    "phonetic": "'sinik",
    "meaning": "n. 犬儒学派的人, 玩世不恭的人, 愤世嫉俗者, 好挖苦人的人；a. 犬儒学派的"
  },
  "dacha": {
    "phonetic": "'dætʃә",
    "meaning": "n. <俄>俄国郊外的别墅"
  },
  "daddy": {
    "phonetic": "'dædi",
    "meaning": "n. 爸爸"
  },
  "daffy": {
    "phonetic": "'dæfi",
    "meaning": "a. 愚笨的, 疯狂的"
  },
  "daily": {
    "phonetic": "'deili",
    "meaning": "a. 每日的, 日常的；adv. 每日地, 日常地；n. 日报"
  },
  "dairy": {
    "phonetic": "'dєәri",
    "meaning": "n. 牛奶公司, 乳品店, 乳牛场"
  },
  "daisy": {
    "phonetic": "'deizi",
    "meaning": "n. 雏菊, 一流人物；a. 第一流的"
  },
  "dally": {
    "phonetic": "'dæli",
    "meaning": "vi. 戏耍, 玩弄, 闲混；vt. 浪费"
  },
  "dance": {
    "phonetic": "dæns. dɑ:ns",
    "meaning": "n. 跳舞, 舞蹈, 舞会；v. 跳舞"
  },
  "dandy": {
    "phonetic": "'dændi",
    "meaning": "n. 花花公子；a. 服装浮华的, 极好的"
  },
  "dared": {
    "phonetic": "",
    "meaning": "v. 敢于（竟敢）"
  },
  "dated": {
    "phonetic": "'deitid",
    "meaning": "a. 有日期的, 陈旧的"
  },
  "dater": {
    "phonetic": "'deitә",
    "meaning": "n. 日期戳子；[经] 日期戳"
  },
  "datum": {
    "phonetic": "'deitәm",
    "meaning": "n. 论据, 材料, 资料, 已知数；[医] 材料, 资料, 论据"
  },
  "daunt": {
    "phonetic": "dɒ:nt",
    "meaning": "vt. 威吓, 难倒, 使气馁"
  },
  "dazed": {
    "phonetic": "'deizd",
    "meaning": "a. 头昏的, 眼花的；[医] 茫然的, 迷乱的"
  },
  "dealt": {
    "phonetic": "delt",
    "meaning": "deal的过去式和过去分词"
  },
  "death": {
    "phonetic": "deθ",
    "meaning": "n. 死亡；[医] 死亡"
  },
  "debar": {
    "phonetic": "di'bɑ:",
    "meaning": "vt. 排除, 防止, 禁止；[法] 阻止, 阻挡, 排除"
  },
  "debit": {
    "phonetic": "'debit",
    "meaning": "n. 借方, 借；vt. 记入借方"
  },
  "debug": {
    "phonetic": "di:'bʌg",
    "meaning": "vt. 除错, 改正有毛病部分, 除去窃听器, 调试；[计] 调试; DOS外部命令:其功能是对命令文件或执行文件进行调试或测试；也可用于编写小的命令文件"
  },
  "debut": {
    "phonetic": "'deibju:",
    "meaning": "n. 初次登台, 开张；v. 初次登台"
  },
  "decaf": {
    "phonetic": "'di:kæf",
    "meaning": "n. 脱咖啡因咖啡, 无咖啡因咖啡"
  },
  "decal": {
    "phonetic": "'di:kæl. di'kæl",
    "meaning": "n. 贴花纸；贴花釉法"
  },
  "decay": {
    "phonetic": "di'kei",
    "meaning": "n. 衰退, 腐败；v. (使)衰退, (使)腐败"
  },
  "decor": {
    "phonetic": "'deikɔ:(r); (?@) dei'kɔ:r",
    "meaning": "n. 装饰, 布置"
  },
  "decoy": {
    "phonetic": "di'kɒi",
    "meaning": "n. 圈套, 诱骗；vt. 诱骗"
  },
  "decry": {
    "phonetic": "di'krai",
    "meaning": "vt. 反对, 责难, 诽谤, 诋毁"
  },
  "defer": {
    "phonetic": "di'fә:",
    "meaning": "vi. 推迟, 延期, 听从；vt. 使推迟, 使延期"
  },
  "defog": {
    "phonetic": "di:'fɒg",
    "meaning": "vt. 从...除雾"
  },
  "deify": {
    "phonetic": "'di:ifai",
    "meaning": "vt. 奉为神, 奉若神明, 崇拜"
  },
  "deign": {
    "phonetic": "dein",
    "meaning": "vi. 屈尊；vt. 赐予"
  },
  "deist": {
    "phonetic": "'di:ist",
    "meaning": "n. 自然神论信仰者"
  },
  "deity": {
    "phonetic": "'di:iti",
    "meaning": "n. 神, 神性"
  },
  "delay": {
    "phonetic": "di'lei",
    "meaning": "n. 耽搁, 迟滞；v. 耽搁, 延迟；[计] 延迟, 延时"
  },
  "delta": {
    "phonetic": "'deltә",
    "meaning": "n. 三角洲, 希腊字母的第四个字；[医] δ(希腊文的第四个字母), 丁种, 三角, 三角形区"
  },
  "delve": {
    "phonetic": "delv",
    "meaning": "v. 探究, 查考；n. 坑, 穴"
  },
  "demon": {
    "phonetic": "'di:mәn",
    "meaning": "n. 魔鬼"
  },
  "demur": {
    "phonetic": "di'mә:",
    "meaning": "vi. 提出异议, 反对, 抗辩；n. 异议, 反对"
  },
  "denim": {
    "phonetic": "'denim",
    "meaning": "n. 斜纹粗棉布, 牛仔布, 劳动布, (非正式)工作服, 工装裤"
  },
  "dense": {
    "phonetic": "dens",
    "meaning": "a. 密集的, 浓厚的"
  },
  "depot": {
    "phonetic": "'depәu",
    "meaning": "n. 停车场, 车站, 贮藏所, 仓库；[医] 仓库, 贮存, 积存"
  },
  "depth": {
    "phonetic": "depθ",
    "meaning": "n. 深度, 深处, 深奥；[计] 深度"
  },
  "derby": {
    "phonetic": "'dɑ:bi",
    "meaning": "n. 德比(英国中部都市), 德比赛马, 大赛马"
  },
  "deter": {
    "phonetic": "di'tә:",
    "meaning": "vt. 制止, 吓住, 威慑"
  },
  "detox": {
    "phonetic": "di:'tɔks",
    "meaning": "n. 戒瘾病房；戒瘾诊所"
  },
  "deuce": {
    "phonetic": "dju:s",
    "meaning": "n. 两点, 平手, 平分；[经] 二元钞票"
  },
  "devil": {
    "phonetic": "'devәl",
    "meaning": "n. 魔鬼；vt. 折磨, 戏弄"
  },
  "diary": {
    "phonetic": "'daiәri",
    "meaning": "n. 日记；[经] 日记簿"
  },
  "diced": {
    "phonetic": "'daɪst",
    "meaning": "v. 将…切成小方块, 切成丁( dice的过去式和过去分词 )"
  },
  "dicer": {
    "phonetic": "'daisә",
    "meaning": "n. 玩掷骰子游戏的人, 帽子, 头盔"
  },
  "dicey": {
    "phonetic": "'daisi",
    "meaning": "a. 不确定的, 危险的, 冒险性的"
  },
  "digit": {
    "phonetic": "'didʒit",
    "meaning": "n. 数字, 位数, 指头；[计] 数位; 位"
  },
  "diked": {
    "phonetic": "daɪk",
    "meaning": "n. 堤防, 堤坝；障碍物；（英）壕沟；vt. 筑堤防护；开沟排水（等于dyke）；n. (Dike)人名；(英、西)戴克；(塞)迪凯"
  },
  "dilly": {
    "phonetic": "'dili",
    "meaning": "n. 好东西, 杰出人物"
  },
  "dimly": {
    "phonetic": "'dimli",
    "meaning": "adv. 微暗, 朦胧"
  },
  "dined": {
    "phonetic": "daind",
    "meaning": "v. 吃饭, 进餐( dine的过去式和过去分词 ); 设宴款待, 请客"
  },
  "diner": {
    "phonetic": "'dainә",
    "meaning": "n. 用餐者"
  },
  "dingo": {
    "phonetic": "'diŋgәu",
    "meaning": "n. 澳洲野犬"
  },
  "dingy": {
    "phonetic": "'diŋdʒi",
    "meaning": "a. 暗淡的, 昏暗的, 邋遢的"
  },
  "dinky": {
    "phonetic": "'diŋki",
    "meaning": "a. 极小的, 不足道的, 整洁的"
  },
  "diode": {
    "phonetic": "'daiәud",
    "meaning": "n. 二极管；[化] 二极管"
  },
  "dippy": {
    "phonetic": "'dipi",
    "meaning": "a. 脑筋不正常的, 昏头昏脑的"
  },
  "dirge": {
    "phonetic": "dә:dʒ",
    "meaning": "n. 挽歌, 哀乐"
  },
  "dirty": {
    "phonetic": "'dә:ti",
    "meaning": "a. 肮脏的, 卑鄙的；vt. 弄脏；vi. 变脏"
  },
  "disco": {
    "phonetic": "'diskәu",
    "meaning": "n. 夜总会, 迪斯科, 的士高"
  },
  "ditch": {
    "phonetic": "ditʃ",
    "meaning": "n. 沟渠；vt. 在...开沟；vi. 开沟"
  },
  "ditsy": {
    "phonetic": "ˈditsi",
    "meaning": "a. <美><俚>没有头脑的, 愚蠢的"
  },
  "ditto": {
    "phonetic": "'ditәu",
    "meaning": "n. 同上, 同上符号, 很相似的人(或物)；vt. 重复；adv. 如前地"
  },
  "ditty": {
    "phonetic": "'diti",
    "meaning": "n. 小调, 小曲"
  },
  "ditzy": {
    "phonetic": "ˈdɪtsi",
    "meaning": "a. <美><俚>没有头脑的, 愚蠢的"
  },
  "divan": {
    "phonetic": "di'væn",
    "meaning": "n. 长沙发, 咖啡馆"
  },
  "dived": {
    "phonetic": "",
    "meaning": "跳水, 潜水, 俯冲, 猛冲, 突然下降, 把手伸入, 钻研, 插进, 伸入, 投入, 探究"
  },
  "diver": {
    "phonetic": "'daivә",
    "meaning": "n. 潜水者"
  },
  "divot": {
    "phonetic": "'divәt",
    "meaning": "n. 草皮, 草皮断片"
  },
  "divvy": {
    "phonetic": "'divi",
    "meaning": "v. 分摊；n. 分摊, 分配, 瓜分"
  },
  "dizzy": {
    "phonetic": "'dizi",
    "meaning": "a. 晕眩的, 眼花缭乱的；vt. 使晕眩"
  },
  "dodge": {
    "phonetic": "dɒdʒ",
    "meaning": "v. 避开, 躲避；n. 诡计, 躲藏"
  },
  "dodgy": {
    "phonetic": "'dɒdʒi",
    "meaning": "a. 狡猾的, 逃避的, 难弄的"
  },
  "doggo": {
    "phonetic": "'dɔɡәu",
    "meaning": "adv. 隐秘地；躲藏地；一动也不动地"
  },
  "doggy": {
    "phonetic": "'dɔ^i",
    "meaning": "n. 小狗儿；a. 时髦的, 装阔气的"
  },
  "dogma": {
    "phonetic": "'dɒgmә",
    "meaning": "n. 教条"
  },
  "doily": {
    "phonetic": "'dɒili",
    "meaning": "n. 小型装饰桌巾"
  },
  "doing": {
    "phonetic": "'du:iŋ",
    "meaning": "n. 行为, 活动"
  },
  "doled": {
    "phonetic": "dəuld",
    "meaning": "v. 救济物( dole的过去式和过去分词 ); 失业救济金"
  },
  "dolly": {
    "phonetic": "'dɒli",
    "meaning": "n. 洋娃娃, (洗衣用)捣棒；vi. 移动车；vt. 用移动车移动"
  },
  "dolma": {
    "phonetic": "'dɒlmə",
    "meaning": "包心卷"
  },
  "domed": {
    "phonetic": "",
    "meaning": "a. 圆屋顶的, 圆盖状的, 圆顶的, 半球形的"
  },
  "donor": {
    "phonetic": "'dәunә",
    "meaning": "n. 捐赠人；[化] 给体; 供体"
  },
  "donut": {
    "phonetic": "'dәu,nʌt",
    "meaning": "[医] 电子回旋加速器环状真空室, 同步加速器环状真空室"
  },
  "doozy": {
    "phonetic": "ˈdu:zi",
    "meaning": "a. <美俚>非常出色的人（物）的, 非常显眼的"
  },
  "doped": {
    "phonetic": "dәupt",
    "meaning": "a. 掺杂过的；掺杂的"
  },
  "doper": {
    "phonetic": "'dәupә",
    "meaning": "加油者, 滑脂枪, 滑润油注射剂"
  },
  "dopey": {
    "phonetic": "'dәupi",
    "meaning": "a. 被麻醉的, 呆笨的, 迟钝的"
  },
  "dorky": {
    "phonetic": "'dɔ:ki",
    "meaning": "a. 愚蠢的; 无能的; 不称职的; 笨的"
  },
  "dosed": {
    "phonetic": "dɑs; dɔs",
    "meaning": "abbr. 磁盘操作系统（Disk Operating System）"
  },
  "doted": {
    "phonetic": "dəʊtid",
    "meaning": "v. 溺爱, 宠爱, 过分地喜爱( dote的过去式和过去分词 )"
  },
  "dotty": {
    "phonetic": "'dɒti",
    "meaning": "a. 多点的, 愚蠢的, 薄弱的"
  },
  "doubt": {
    "phonetic": "daut",
    "meaning": "n. 怀疑, 疑惑；v. 怀疑, 不信"
  },
  "dough": {
    "phonetic": "dәu",
    "meaning": "n. 生面团；[化] 捏塑体; 生面团"
  },
  "doula": {
    "phonetic": "",
    "meaning": "产妇陪护（给产妇以心理支持）"
  },
  "douse": {
    "phonetic": "daus",
    "meaning": "vt. 插入水中, 浇(或洒、泼)水在...上, 熄(灯、火等), 平息；vi. 浸泡；n. 泼洒"
  },
  "dowdy": {
    "phonetic": "'daudi",
    "meaning": "a. 过时的, 懒散的；n. 懒散女人, 邋遢女人"
  },
  "dowel": {
    "phonetic": "'dauәl",
    "meaning": "n. 销子, 木钉；vt. 用暗销接合"
  },
  "downy": {
    "phonetic": "'dauni",
    "meaning": "a. 绒毛的, 柔和的, 有草丘陵地的"
  },
  "dowry": {
    "phonetic": "'dauәri",
    "meaning": "n. 嫁妆；[法] 陪嫁物, 嫁妆"
  },
  "dowse": {
    "phonetic": "dauz",
    "meaning": "v. 探寻水源"
  },
  "dozed": {
    "phonetic": "dəuzd",
    "meaning": "v. 打盹儿, 打瞌睡( doze的过去式和过去分词 )"
  },
  "dozen": {
    "phonetic": "'dʌzn",
    "meaning": "n. 打, 十二个；a. 一打的"
  },
  "dozer": {
    "phonetic": "'dәuzә",
    "meaning": "n. 打瞌睡的人, 推土机"
  },
  "draft": {
    "phonetic": "dræft. drɑ:ft",
    "meaning": "n. 气流, 草稿, 汇票, 草案；vt. 起草, 征兵；[计] 草稿"
  },
  "drain": {
    "phonetic": "drein",
    "meaning": "n. 排水沟, 消耗, 排水；vt. 排出, 喝光, 耗尽；vi. 排水, 流干"
  },
  "drake": {
    "phonetic": "dreik",
    "meaning": "n. 公鸭, 蜉蝣类"
  },
  "drama": {
    "phonetic": "'drɑ:mә",
    "meaning": "n. 戏剧, 戏剧艺术"
  },
  "drank": {
    "phonetic": "dræŋk",
    "meaning": "drink的过去式"
  },
  "drape": {
    "phonetic": "dreip",
    "meaning": "n. 布帘, 褶皱；vt. 用布帘覆盖, 披上；vi. 成褶皱状"
  },
  "drawl": {
    "phonetic": "drɒ:l",
    "meaning": "v. 慢吞吞地说, 故意拉长调子讲话；n. 慢吞吞拉长调子的说话方式"
  },
  "drawn": {
    "phonetic": "drɒ:n",
    "meaning": "a. 拔出的；draw的过去分词"
  },
  "dread": {
    "phonetic": "dred",
    "meaning": "n. 恐惧, 可怕的人(或事)；a. 可怕的, 可怖的；v. 恐惧, 害怕"
  },
  "dream": {
    "phonetic": "dri:m",
    "meaning": "n. 梦, 空想, 愿望；v. 做梦, 想象, 梦想"
  },
  "dress": {
    "phonetic": "dres",
    "meaning": "n. 服装, 覆盖物；vi. 穿着；vt. 给...穿衣, 整理"
  },
  "dried": {
    "phonetic": "draid",
    "meaning": "a. 弄干了的"
  },
  "drier": {
    "phonetic": "'draiә",
    "meaning": "n. 干燥机, 干燥剂；[化] 干燥剂; 催干剂; 干燥设备; 干燥器; 烘缸"
  },
  "drift": {
    "phonetic": "drift",
    "meaning": "n. 漂流物, 漂流, 动向；v. (使)漂流"
  },
  "drill": {
    "phonetic": "dril",
    "meaning": "n. 钻孔机, 钻子, 播种机, 粗斜纹布；v. 训练, 钻孔"
  },
  "drink": {
    "phonetic": "driŋk",
    "meaning": "n. 饮料, 酒；v. 喝, 喝酒"
  },
  "drive": {
    "phonetic": "draiv",
    "meaning": "n. 驾车, 快车道, 推进力, 驱动, 动力, 击球, 驱动器；vt. 开车, 驱使, 推动, 驾驶；vi. 开车, 猛击, 飞跑；[计] 驱动器"
  },
  "droid": {
    "phonetic": "drɔid",
    "meaning": "n. 机器人"
  },
  "droit": {
    "phonetic": "drɒit",
    "meaning": "n. 权利, 所有权"
  },
  "droll": {
    "phonetic": "drɒl",
    "meaning": "a. 好笑的, 滑稽的, 逗趣的"
  },
  "drone": {
    "phonetic": "drәun",
    "meaning": "n. 雄蜂, 懒惰者, 嗡嗡的声音, 无人驾驶飞机(或船)；vi. 嗡嗡作声, 混日子；vt. 低沉地说"
  },
  "drool": {
    "phonetic": "dru:l",
    "meaning": "vi. 流口水, 淌, 胡说八道；vt. 从嘴淌下, 过分动感情地表示；n. 口水, 胡说"
  },
  "droop": {
    "phonetic": "dru:p",
    "meaning": "vi. 下垂, 消沉；vt. 使下垂；n. 低垂, 消沉"
  },
  "dross": {
    "phonetic": "drɒs",
    "meaning": "n. 浮渣, 碎屑, 渣滓；[化] 浮渣"
  },
  "drove": {
    "phonetic": "drәuv",
    "meaning": "n. 畜群；drive的过去式"
  },
  "drown": {
    "phonetic": "draun",
    "meaning": "vi. 淹死；vt. 把...淹死, 淹没"
  },
  "druid": {
    "phonetic": "'dru:id",
    "meaning": "n. 巫师, 占卜者, 祭师"
  },
  "drunk": {
    "phonetic": "drʌŋk",
    "meaning": "a. 喝醉了的；drink的过去式"
  },
  "dryer": {
    "phonetic": "'draiә",
    "meaning": "n. 干衣机, 干燥剂；[化] 干燥剂; 催干剂; 干燥器; 干燥设备; 烘箱"
  },
  "dryly": {
    "phonetic": "'draili",
    "meaning": "adv. 冷淡地, 枯躁无味地"
  },
  "ducat": {
    "phonetic": "'dʌkәt",
    "meaning": "入场券, 门票"
  },
  "duchy": {
    "phonetic": "'dʌtʃi",
    "meaning": "n. 公爵领地, 公国, 直辖领地"
  },
  "ducky": {
    "phonetic": "'dʌki",
    "meaning": "a. 极好的, 可爱的, 令人愉快的"
  },
  "duked": {
    "phonetic": "",
    "meaning": "vi. 战斗（duke的过去式与过去分词形式）"
  },
  "dully": {
    "phonetic": "'dʌli",
    "meaning": "adv. 钝地, 迟钝地, 不清楚地"
  },
  "dummy": {
    "phonetic": "'dʌmi",
    "meaning": "n. 傀儡, 假人, 仿制品；a. 虚设的, 假的, 名义上的"
  },
  "dumpy": {
    "phonetic": "'dʌmpi",
    "meaning": "a. 矮胖的, 粗短的"
  },
  "dunce": {
    "phonetic": "dʌns",
    "meaning": "n. 智力迟钝的学生, 傻瓜"
  },
  "duped": {
    "phonetic": "du:pt",
    "meaning": "v. 欺骗或哄骗某人（做某事）( dupe的过去式和过去分词 )"
  },
  "dusky": {
    "phonetic": "'dʌski",
    "meaning": "a. 微暗的, 暗淡的, 暗黑色的, 多黑影的, 黑黝黝的, 微黑色的, 忧郁的"
  },
  "dusty": {
    "phonetic": "'dʌsti",
    "meaning": "a. 灰尘多的, 无聊的, 含糊的, 粉末状的"
  },
  "dutch": {
    "phonetic": "dʌtʃ",
    "meaning": "n. 荷兰人, 荷兰语；a. 荷兰的"
  },
  "duvet": {
    "phonetic": "du:'vei",
    "meaning": "n. 羽绒被"
  },
  "dwarf": {
    "phonetic": "dwɒ:f",
    "meaning": "n. 矮子, 侏儒；v. (使)变矮小"
  },
  "dweeb": {
    "phonetic": "dwi:b",
    "meaning": "n. <俚>呆子, 怪人"
  },
  "dwell": {
    "phonetic": "dwel",
    "meaning": "vi. 居住, 居住(于), 存在(于)"
  },
  "dwelt": {
    "phonetic": "dwelt",
    "meaning": "dwell的过去式和过去分词"
  },
  "dying": {
    "phonetic": "'daiiŋ",
    "meaning": "a. 垂死的；[法] 快要死的, 垂死的, 临终的"
  },
  "eager": {
    "phonetic": "'i:gә",
    "meaning": "a. 热心的, 渴望的, 热望的"
  },
  "eagle": {
    "phonetic": "'i:gl",
    "meaning": "n. 鹰, 鹰状标饰"
  },
  "eared": {
    "phonetic": "iәd",
    "meaning": "a. 有...耳的, 有把的, 有穗的"
  },
  "early": {
    "phonetic": "'ә:li",
    "meaning": "a. 早的, 早熟的；adv. 很早, 初"
  },
  "earth": {
    "phonetic": "ә:θ",
    "meaning": "n. 地球, 泥土, 世界, 尘世；vt. 埋入土中, 赶入洞内；vi. 躲入洞内"
  },
  "eased": {
    "phonetic": "",
    "meaning": "a. 放松的"
  },
  "easel": {
    "phonetic": "'i:zәl",
    "meaning": "n. 画架, 黑板架"
  },
  "eaten": {
    "phonetic": "'i:tәn",
    "meaning": "eat的过去分词"
  },
  "eater": {
    "phonetic": "'i:tә",
    "meaning": "n. 吃...的人, 生吃的水果, 美味的水果"
  },
  "ebbed": {
    "phonetic": "ebd",
    "meaning": "v. （指潮水）退( ebb的过去式和过去分词 ); 落; 减少; 衰落"
  },
  "ebony": {
    "phonetic": "'ebәni",
    "meaning": "n. 乌木；a. 乌木制的"
  },
  "ebook": {
    "phonetic": "",
    "meaning": "n. 电子书"
  },
  "eclat": {
    "phonetic": "",
    "meaning": "n. 大成功, 喝采"
  },
  "edema": {
    "phonetic": "i(:)'di:mә",
    "meaning": "n. 水肿, 浮肿；[医] 水肿"
  },
  "edged": {
    "phonetic": "edʒd",
    "meaning": "a. 有某种或几种刃的"
  },
  "edger": {
    "phonetic": "'edʒә",
    "meaning": "n. 磨边机；轧边机；刨边机"
  },
  "edict": {
    "phonetic": "'i:dikt",
    "meaning": "n. 布告, 法令；[经] 布告, 法令"
  },
  "edify": {
    "phonetic": "'edifai",
    "meaning": "vt. 启迪, 熏陶, 教诲"
  },
  "educe": {
    "phonetic": "i'dju:s",
    "meaning": "vt. 引出, 推断出, 使显出"
  },
  "eerie": {
    "phonetic": "'iәri",
    "meaning": "a. 怪诞的, 可怕的, 奇异的, 令人迷惑不解的"
  },
  "egged": {
    "phonetic": "",
    "meaning": "v. 煽动, 挑唆；用蛋黄蛋白调拌（egg的过去分词形式）"
  },
  "egret": {
    "phonetic": "'i:gret",
    "meaning": "n. 白鹭"
  },
  "eider": {
    "phonetic": "'aidә",
    "meaning": "n. 绒鸭, 绒鸭绒"
  },
  "eight": {
    "phonetic": "eit",
    "meaning": "num. 八, 八个"
  },
  "eject": {
    "phonetic": "i'dʒekt",
    "meaning": "vt. 逐放, 放逐, 喷射；[化] 排出"
  },
  "eking": {
    "phonetic": "",
    "meaning": "v. 增加；延长（eke的ing 形式）"
  },
  "elate": {
    "phonetic": "i'leit",
    "meaning": "vt. 使兴高采烈, 使得意"
  },
  "elbow": {
    "phonetic": "'elbәu",
    "meaning": "n. 手肘, 弯头, 扶手；v. 用手肘推开, 推挤"
  },
  "elder": {
    "phonetic": "'eldә",
    "meaning": "n. 年长者, 老人, 前辈；a. 年长的, 资深的"
  },
  "elect": {
    "phonetic": "i'lekt",
    "meaning": "n. 当选人, 被选的人；a. 被选的, 选出的；vt. 选举, 选择；vi. 作选择"
  },
  "elegy": {
    "phonetic": "'elidʒi",
    "meaning": "n. 悲歌, 哀歌, 挽歌"
  },
  "elfin": {
    "phonetic": "'elfin",
    "meaning": "a. 小妖精的, 象小妖精的；n. 小精灵, 矮人, 淘气鬼"
  },
  "elide": {
    "phonetic": "i'laid",
    "meaning": "vt. 省略(元音、辅音), 删去(字、句等), 取消"
  },
  "elite": {
    "phonetic": "ei'li:t",
    "meaning": "n. 精华, 精锐, 中坚分子"
  },
  "elope": {
    "phonetic": "i'lәup",
    "meaning": "vi. 私奔, 潜逃；[法] 私奔, 弃职, 逃亡"
  },
  "elude": {
    "phonetic": "i'lu:d",
    "meaning": "vt. 逃避, 规避, 把...难倒"
  },
  "email": {
    "phonetic": "'i:'meil",
    "meaning": "n. 电子信函"
  },
  "embed": {
    "phonetic": "im'bed",
    "meaning": "vt. 使插入, 使嵌入, 使深留脑中；[计] 嵌入"
  },
  "ember": {
    "phonetic": "'embә",
    "meaning": "n. 灰烬, 余烬"
  },
  "emcee": {
    "phonetic": "'em'si:",
    "meaning": "n. 司仪, 主持人；vt. 担任...主持人, 主持"
  },
  "emery": {
    "phonetic": "'emәri",
    "meaning": "n. 金刚砂；[化] 金刚砂"
  },
  "emoji": {
    "phonetic": "",
    "meaning": "n. 表情符号"
  },
  "emote": {
    "phonetic": "i'mәut",
    "meaning": "vi. 装模作样, 表现感情"
  },
  "empty": {
    "phonetic": "'empti",
    "meaning": "a. 空的, 空虚的, 空腹的, 空洞的；n. 空的东西, 空车；vt. 倒空, 使变空, 使排出；vi. 流空；[计] 空"
  },
  "enact": {
    "phonetic": "i'nækt",
    "meaning": "vt. 制定法律, 扮演, 颁布；[法] 法令, 法规, 条例"
  },
  "ended": {
    "phonetic": "",
    "meaning": "a. 结束的（end的过去分词）"
  },
  "endow": {
    "phonetic": "in'dau",
    "meaning": "vt. 捐赠, 捐助, 赋予；[法] 赠送财产给, 分给寡妇一份遗产, 授与"
  },
  "enema": {
    "phonetic": "'enimә",
    "meaning": "n. 灌肠剂；[医] 灌肠法, 灌肠剂"
  },
  "enemy": {
    "phonetic": "'enimi",
    "meaning": "n. 敌人, 仇敌, 敌军；a. 敌人的"
  },
  "enjoy": {
    "phonetic": "in'dʒɒi",
    "meaning": "vt. 享受, 喜欢, 欣赏；[法] 享受, 享有, 获得某种利益"
  },
  "ennui": {
    "phonetic": "'ɒnwi:",
    "meaning": "n. 倦怠, 厌倦；[医] 厌倦"
  },
  "ensue": {
    "phonetic": "en'su:",
    "meaning": "vi. 跟着发生, 继起；vt. 追求"
  },
  "enter": {
    "phonetic": "'entә",
    "meaning": "vt. 进入, 参加, 开始, 输入, 回车；vi. 进去, 参加；[计] 输入, 回车"
  },
  "entry": {
    "phonetic": "'entri",
    "meaning": "n. 登录, 条目, 进入, 入口, 报关；[计] 登录项, 输入项, 条目"
  },
  "envoy": {
    "phonetic": "'envɒi",
    "meaning": "n. 外交使节, 特使；[法] 使者, 代表, 使节"
  },
  "epoch": {
    "phonetic": "'i:pɒk",
    "meaning": "n. 新纪元, 时代, 时期"
  },
  "epoxy": {
    "phonetic": "e'pɒksi",
    "meaning": "a. 环氧的；[化] 环氧; 表氧; 桥氧"
  },
  "equal": {
    "phonetic": "'i:kwәl",
    "meaning": "n. 对手, 匹敌, 同辈；a. 相等的, 平等的, 胜任的, 合适的, 平静的, 不相上下的；vt. 等于, 比得上；[计] 等长度编码"
  },
  "equip": {
    "phonetic": "i'kwip",
    "meaning": "vt. 装备, 配备；[机] 设备, 装置"
  },
  "erase": {
    "phonetic": "i'reis",
    "meaning": "vt. 抹去, 擦掉；[计] 清洗; 擦除; 抹除; DOS内部命令:从磁盘上删除一个或多个文件"
  },
  "erect": {
    "phonetic": "i'rekt",
    "meaning": "a. 直立的, 竖立的, 笔直的；vt. 使竖立, 使直立, 树立, 建立；vi. 勃起"
  },
  "erode": {
    "phonetic": "i'rәud",
    "meaning": "vt. 腐蚀, 侵蚀；vi. 受腐蚀"
  },
  "erred": {
    "phonetic": "ə:d",
    "meaning": "v. 犯错误, 做错事( err的过去式和过去分词 )"
  },
  "error": {
    "phonetic": "'erә",
    "meaning": "n. 错误, 过失, 失误, 误差；[计] 错误"
  },
  "erupt": {
    "phonetic": "i'rʌpt",
    "meaning": "vi. 爆发；vt. 喷出"
  },
  "essay": {
    "phonetic": "'esei. e'sei",
    "meaning": "n. 随笔, 短文, 评论, 企图；vt. 试图"
  },
  "ester": {
    "phonetic": "'estә",
    "meaning": "n. 酯；[化] 酯"
  },
  "ether": {
    "phonetic": "'i:θә",
    "meaning": "n. 醚, 苍天, 以太；[化] 醚; 以太"
  },
  "ethic": {
    "phonetic": "'eθik",
    "meaning": "n. 道德规范, 伦理"
  },
  "ethos": {
    "phonetic": "'i:θɔs",
    "meaning": "n. 气质；民族精神；社会思潮"
  },
  "ethyl": {
    "phonetic": "'eθil, 'i:θail",
    "meaning": "[化] 乙基；[医] 乙基"
  },
  "etude": {
    "phonetic": "ei'tju:d",
    "meaning": "n. 练习曲"
  },
  "evade": {
    "phonetic": "i'veid",
    "meaning": "v. (巧妙地)逃脱, 规避, 逃避"
  },
  "event": {
    "phonetic": "i'vent",
    "meaning": "n. 事件, 结果, 事情的进程, 竞赛项目；[计] 事件"
  },
  "every": {
    "phonetic": "'evri",
    "meaning": "a. 每一, 所有的"
  },
  "evict": {
    "phonetic": "i'vikt",
    "meaning": "vt. 逐出, 赶出, 驱逐；[法] 逐出, 驱逐, 没收"
  },
  "evoke": {
    "phonetic": "i'vәuk",
    "meaning": "vt. 唤起, 引起, 召(魂)；[法] 提审, 移送"
  },
  "exact": {
    "phonetic": "ig'zækt",
    "meaning": "a. 精确的, 准确的, 精密的；vt. 强求, 急需"
  },
  "exalt": {
    "phonetic": "ig'zɒ:lt",
    "meaning": "vt. 提升, 提高, 赞扬, 使得意；vi. 使人兴奋, 使人得意"
  },
  "excel": {
    "phonetic": "ik'sel",
    "meaning": "vt. 胜过, 优于, 擅长；vi. 胜过其他"
  },
  "exert": {
    "phonetic": "ig'zә:t",
    "meaning": "vt. 发挥, 运用, 施以影响；[法] 施加, 产生, 行使"
  },
  "exile": {
    "phonetic": "'eksail",
    "meaning": "n. 放逐, 流放, 被放逐者；vt. 放逐, 流放, 使背井离乡"
  },
  "exist": {
    "phonetic": "ig'zist",
    "meaning": "vi. 存在, 生存, 发生"
  },
  "expat": {
    "phonetic": "ˈeksˈpeɪt",
    "meaning": "v. 逐出国外; 脱离国籍; 放逐; 移居国外；n. 亡命国外者"
  },
  "expel": {
    "phonetic": "ik'spel",
    "meaning": "vt. 驱逐, 逐出, 排出, 开除；[医] 排除, 迫出"
  },
  "extol": {
    "phonetic": "ik'stәul",
    "meaning": "vt. 颂扬, 称赞, 吹捧"
  },
  "extra": {
    "phonetic": "'ekstrә",
    "meaning": "n. 额外的事物, 另外的收费；a. 额外的, 特别的；adv. 额外地, 特别地, 非常地"
  },
  "exude": {
    "phonetic": "ig'zju:d",
    "meaning": "v. (使)流出, (使)渗出"
  },
  "exult": {
    "phonetic": "ig'zʌlt",
    "meaning": "vi. 非常高兴, 欢欣"
  },
  "exurb": {
    "phonetic": "'ekzә:b",
    "meaning": "n. 远郊地区"
  },
  "eying": {
    "phonetic": "",
    "meaning": "vt. 定睛地看（eye的现在分词形式）"
  },
  "fable": {
    "phonetic": "'feibl",
    "meaning": "n. 寓言, 神话, 谎言；vi. 虚构, 作寓言"
  },
  "faced": {
    "phonetic": "feist",
    "meaning": "a. 有某种面孔或表情的"
  },
  "facet": {
    "phonetic": "'fæsit",
    "meaning": "n. (多面体的)面, 方面, 琢面；[医] 小平面, 小面"
  },
  "faded": {
    "phonetic": "'feidid",
    "meaning": "a. 已褪色的, 已凋谢的"
  },
  "fader": {
    "phonetic": "'feidә",
    "meaning": "n. 音量控制器, 增益调节器, 混频电位器；[电] 化音器"
  },
  "faint": {
    "phonetic": "feint",
    "meaning": "n. 昏厥, 昏倒；a. 模糊的, 微弱的, 无力的；vi. 昏倒, 变得微弱"
  },
  "fairy": {
    "phonetic": "'fєәri",
    "meaning": "n. 仙女, 精灵；a. 仙女的"
  },
  "faith": {
    "phonetic": "feiθ",
    "meaning": "n. 信心, 信任, 忠实, 保证；[法] 信任, 信仰, 信念"
  },
  "faked": {
    "phonetic": "",
    "meaning": "捏造；假装…的样子（fake的过去式、过去分词）"
  },
  "faker": {
    "phonetic": "'feikә",
    "meaning": "n. 骗子, (卖滑头货的)摊贩；[经] 伪造者, 骗子"
  },
  "fakir": {
    "phonetic": "'fei.kiә",
    "meaning": "n. 托钵僧, 苦行者"
  },
  "false": {
    "phonetic": "fɒ:ls",
    "meaning": "a. 错误的, 虚伪的, 假的, 不老实的；adv. 不准确地, 欺诈地"
  },
  "famed": {
    "phonetic": "feimd",
    "meaning": "a. 著名的, 闻名的"
  },
  "fancy": {
    "phonetic": "'fænsi",
    "meaning": "n. 想象力, 幻想, 喜好；a. 想象的, 精美的, 新奇的, 奇特的, 高价的, 特级的；vt. 想象, 设想, 相信, 喜爱；vi. 想象, 幻想"
  },
  "farce": {
    "phonetic": "fɑ:s",
    "meaning": "n. 闹剧, 滑稽剧, 胡闹"
  },
  "fared": {
    "phonetic": "",
    "meaning": "n. 法依笛（服装品牌）"
  },
  "fatal": {
    "phonetic": "'feitәl",
    "meaning": "a. 致命的, 重大的, 命运注定的, 粗心的, 不幸的；[医] 致命的, 致死的"
  },
  "fated": {
    "phonetic": "'feitid",
    "meaning": "a. 宿命的, 命中注定的, 受命运支配的"
  },
  "fatty": {
    "phonetic": "'fæti",
    "meaning": "a. 肥胖的, 脂肪的, 含脂肪的；[医] 脂肪的"
  },
  "fatwa": {
    "phonetic": "'fætwɑ:",
    "meaning": "n. (伊斯兰教)法学家的裁决"
  },
  "fault": {
    "phonetic": "fɒ:lt",
    "meaning": "n. 过错, 故障, 毛病；vt. 挑剔；vi. 产生断层, 弄错；[计] 故障"
  },
  "fauna": {
    "phonetic": "'fɒ:nә",
    "meaning": "n. 动物群；[医] 动物区系"
  },
  "favor": {
    "phonetic": "'feivә",
    "meaning": "n. 好意, 喜爱；vt. 赐予, 支持, 喜欢, 证实"
  },
  "faxed": {
    "phonetic": "fækst",
    "meaning": "v. 传真传输( fax的过去式和过去分词 ); 传真（文档、信件等）"
  },
  "fazed": {
    "phonetic": "feizd",
    "meaning": "v. 打扰, 使担忧, 烦扰( faze的过去式和过去分词 )"
  },
  "feast": {
    "phonetic": "fi:st",
    "meaning": "n. 宴会, 酒席, 享受, 节日；vt. 款待, 享乐, 请客；vi. 参加宴会, 尽情地吃, 享受"
  },
  "fecal": {
    "phonetic": "'fi:kәl",
    "meaning": "a. 排泄物的, 渣滓的；[医] 粪便的"
  },
  "feces": {
    "phonetic": "'fi:'si:z",
    "meaning": "pl. 粪, 屎；[医] 粪便"
  },
  "feign": {
    "phonetic": "fein",
    "meaning": "vt. 假装, 装作；vi. 作假"
  },
  "feint": {
    "phonetic": "feint",
    "meaning": "n. 伪装, 假装, 假托, 佯攻；vi. 装作, 假装, 佯攻；a. 假的, 虚饰的"
  },
  "fella": {
    "phonetic": "felә",
    "meaning": "n. 小伙子；[俚]伙伴, 伙计"
  },
  "felon": {
    "phonetic": "'felәn",
    "meaning": "n. 重罪犯, 恶棍, 瘭疽；[医] 瘭疽, 指头脓炎"
  },
  "femme": {
    "phonetic": "fem",
    "meaning": "n. 妻子, (美)(非正式)女子；[法] 妻子, 妇女"
  },
  "femur": {
    "phonetic": "'fi:mә",
    "meaning": "n. 大腿骨, (昆虫的)腿节；[医] 股骨, 股"
  },
  "fence": {
    "phonetic": "fens",
    "meaning": "n. 围墙, 栅栏, 买卖赃物的人, 剑术；vt. 用篱笆围住, 练习剑术, 防护；vi. 击剑, 搪塞"
  },
  "feral": {
    "phonetic": "'fiәrәl",
    "meaning": "a. 野生的, 凶猛的, 野兽的；[医] 凶猛的, 野生的"
  },
  "ferry": {
    "phonetic": "'feri",
    "meaning": "n. 渡船, 渡口；[法] 摆渡营业权, 轮渡"
  },
  "fetal": {
    "phonetic": "'fi:tәl",
    "meaning": "a. 胎儿的, 胎的；[医] 胎的, 胎儿的"
  },
  "fetch": {
    "phonetic": "fetʃ",
    "meaning": "n. 取得, 拿, 诡计, 魂；vt. 接来, 取来, 售得, 带来, 推出, 引出, 杀死, 吸引, 到达；vi. 取物, 前进；[计] 取"
  },
  "feted": {
    "phonetic": "feɪtid",
    "meaning": "v. 宴请（某人）, 向…致敬( fete的过去式和过去分词 )"
  },
  "fetid": {
    "phonetic": "'fetid",
    "meaning": "a. 恶臭的；[医] 恶臭的"
  },
  "fetus": {
    "phonetic": "'fi:tәs",
    "meaning": "n. 胎儿；[医] 胎, 胎儿"
  },
  "fever": {
    "phonetic": "'fi:vә",
    "meaning": "n. 发烧, 发热, 热病；[医] 发热, 热"
  },
  "fewer": {
    "phonetic": "'fju:ә",
    "meaning": "a. 较少的"
  },
  "fiber": {
    "phonetic": "'faibә",
    "meaning": "n. 纤维, 构造, 纤维制品；[化] 纤维"
  },
  "ficus": {
    "phonetic": "",
    "meaning": "[医] 无花果属"
  },
  "field": {
    "phonetic": "fi:ld",
    "meaning": "n. 领域, 田地, 场地, 战场, 场, 域；vt. 使...晒在场上, 使上场；a. 田间的, 野生的, 野外的, 田赛的；[计] 域, 字段"
  },
  "fiend": {
    "phonetic": "fi:nd",
    "meaning": "n. 魔鬼, 邪神, 能手, 成癖者"
  },
  "fiery": {
    "phonetic": "'faiәri",
    "meaning": "a. 炽热的, 热烈的, 暴躁的"
  },
  "fifth": {
    "phonetic": "fifθ",
    "meaning": "num. 第五, 五分之一"
  },
  "fifty": {
    "phonetic": "'fifti",
    "meaning": "num. 五十, 五十个"
  },
  "fight": {
    "phonetic": "fait",
    "meaning": "n. 打架, 争吵, 斗志；v. 对抗, 打架"
  },
  "filch": {
    "phonetic": "filtʃ",
    "meaning": "vt. 偷窃, 窃取"
  },
  "filed": {
    "phonetic": "",
    "meaning": "v. [专利]申请；存档（file的过去分词形式）"
  },
  "filer": {
    "phonetic": "'failә",
    "meaning": "n. 文件编档员, 文件装钉员, 锉磨工人；[计] 文件管理程序"
  },
  "filet": {
    "phonetic": "fi'lei, 'fi:lei",
    "meaning": "n. 头带, 轮廓线, 带状物, 带子, 束发带, 肉片, 鱼片, 襻, 嵌条, 丘带, (内)圆角；vt. 用带缚, 把(肉/鱼)切成片, 用饰带装饰"
  },
  "filly": {
    "phonetic": "'fili",
    "meaning": "n. 小雌马, 小姑娘"
  },
  "filmy": {
    "phonetic": "'filmi",
    "meaning": "a. 薄膜的, 薄的, 朦胧的"
  },
  "filth": {
    "phonetic": "filθ",
    "meaning": "n. 污秽, 不洁, 猥亵；[法] 污秽, 污物, 淫猥"
  },
  "final": {
    "phonetic": "'fainl",
    "meaning": "n. 期末考试, 结局, 决赛；a. 最后的, 终极的, 决定性的"
  },
  "finch": {
    "phonetic": "fintʃ",
    "meaning": "n. 雀科鸣鸟"
  },
  "fined": {
    "phonetic": "",
    "meaning": "v. 罚钱（fine的过去式）"
  },
  "finer": {
    "phonetic": "'fainә",
    "meaning": "a. 出色的, 好的"
  },
  "fired": {
    "phonetic": "",
    "meaning": "n. 因祸得福（电影名）"
  },
  "first": {
    "phonetic": "fә:st",
    "meaning": "adv. 首先, 第一, 优先；a. 第一的；num. 第一；n. 开始, 第一"
  },
  "firth": {
    "phonetic": "fә:θ",
    "meaning": "n. 峡湾, 河口"
  },
  "fishy": {
    "phonetic": "'fiʃi",
    "meaning": "a. 鱼似的, 多鱼的, 腥臭的, 呆滞的"
  },
  "fixed": {
    "phonetic": "fikst",
    "meaning": "a. 固定的, 不变的；[法] 固定的, 确定的, 不变的"
  },
  "fixer": {
    "phonetic": "'fiksә",
    "meaning": "n. 定色剂, 定影剂, 毒贩子；[化] 定影剂; 定香剂; 固色剂; 固着剂; 固定剂"
  },
  "fizzy": {
    "phonetic": "'fizi",
    "meaning": "a. 嘶嘶作响的, 起泡沫的"
  },
  "fjord": {
    "phonetic": "fjɔ:d",
    "meaning": "n. 峡湾"
  },
  "flack": {
    "phonetic": "flæk",
    "meaning": "n. 高射炮, 对空炮火, 广告, 宣传"
  },
  "flail": {
    "phonetic": "fleil",
    "meaning": "n. 连枷；v. 用连枷打, 打"
  },
  "flair": {
    "phonetic": "fleә",
    "meaning": "n. 鉴别力, 才能, 天资, 资质, 眼光"
  },
  "flake": {
    "phonetic": "fleik",
    "meaning": "n. 小薄片, 扁薄的一层, 火星, 晒鱼架子；vt. 使成薄片；vi. 剥落"
  },
  "flaky": {
    "phonetic": "'fleiki",
    "meaning": "a. 薄片的, 成片的, 薄而易剥落的"
  },
  "flame": {
    "phonetic": "fleim",
    "meaning": "n. 火焰, 火舌, 热情, 光辉；vt. 焚烧, 用火焰给...灭菌, 用火焰传送(信号), 点燃, 激动；vi. 燃烧, 爆发, 闪耀；[计] 无聊邮件, 无益邮件"
  },
  "flank": {
    "phonetic": "flæŋk",
    "meaning": "n. 侧面, 侧腹, 胁, 腰窝肉；vt. 攻击侧面, 守侧面；vi. 侧面与...相接"
  },
  "flare": {
    "phonetic": "'flєә",
    "meaning": "n. 闪光, 闪耀；vi. 闪光, 闪耀；vt. 用发光信号发出, 使闪耀, 使张开"
  },
  "flash": {
    "phonetic": "flæʃ",
    "meaning": "n. 闪光, 闪现, 一瞬间；vi. 闪光, 闪现, 反射；vt. 使闪光, 反射"
  },
  "flask": {
    "phonetic": "flæsk",
    "meaning": "n. 细颈瓶, 烧瓶, 小水瓶；[化] 瓶; 烧瓶"
  },
  "fleck": {
    "phonetic": "flek",
    "meaning": "n. 斑点, 雀斑, 斑纹；vt. 使起斑点, 使有斑纹, 使有斑驳"
  },
  "fleet": {
    "phonetic": "fli:t",
    "meaning": "n. 舰队, 港湾, 小河；a. 快速的, 敏捷的, 浅的, 短暂的；adv. 浅；vi. 疾驰, 飞逝, 掠过；vt. 消磨, 变换船(或船员)的位置"
  },
  "flesh": {
    "phonetic": "'fleʃ",
    "meaning": "n. 肉, 肉体, 肉欲, 人性, 亲属, 人类, 众生, 人体；vt. 以肉喂, 激起...的杀戳情绪, 使肥, 赋以血肉；vi. 长胖"
  },
  "flick": {
    "phonetic": "flik",
    "meaning": "n. 快速的轻打, 轻打声, 弹开；v. 轻弹, 轻轻拂去, 忽然摇动"
  },
  "flied": {
    "phonetic": "flaid",
    "meaning": "v. 为fly的过去式及过去分词, (棒球)打出高飞球"
  },
  "flier": {
    "phonetic": "'flaiә",
    "meaning": "n. 飞行者, 快船, 快车；[经] 投机买卖, 孤注一掷, 传单"
  },
  "fling": {
    "phonetic": "fliŋ",
    "meaning": "n. 投掷, 急冲, 嘲弄；vt. 投, 丢下, 抛弃, 使陷入, 挥动, 嘲笑, 扫视；vi. 猛冲"
  },
  "flint": {
    "phonetic": "flint",
    "meaning": "n. 打火石, 燧石, 极硬的东西；[化] 燧石"
  },
  "flirt": {
    "phonetic": "flә:t",
    "meaning": "n. 卖弄风骚的人, 急动, 急扔；vt. 忽然弹出, 轻快摆动, 挥动；vi. 调情, 玩弄, 摆动, 轻率地对待"
  },
  "float": {
    "phonetic": "flәut",
    "meaning": "n. 漂流物, 浮舟, 漂浮, 浮萍, 彩车；vi. 浮动, 飘动, 散播, 摇摆, 动摇, 浮动；vt. 使漂浮, 容纳, 淹没, 发行, 实行；[计] 浮动"
  },
  "flock": {
    "phonetic": "flɒk",
    "meaning": "n. 兽群, 鸟群, 一群人, 大量, 棉束；vi. 成群而行, 聚集；vt. 用棉束填满"
  },
  "flood": {
    "phonetic": "flʌd",
    "meaning": "n. 洪水, 大量之水, 涨潮；vt. 淹没, 使泛滥, 注满；vi. 被淹, 溢出, 涌进"
  },
  "floor": {
    "phonetic": "flɒ:",
    "meaning": "n. 地板, 楼层, 底部, 底价；vt. 铺地板, 打倒；n. 地面, 地板, 基底；[计] 基底"
  },
  "flora": {
    "phonetic": "'flɒ:rә",
    "meaning": "n. 植物群；[医] 植物区系, 植物丛, 植物群, 菌丛"
  },
  "floss": {
    "phonetic": "flɒs",
    "meaning": "n. 丝棉, 乱丝"
  },
  "flour": {
    "phonetic": "'flauә",
    "meaning": "n. 面粉, 粉沫, 碎粉；[医] 面粉, 麦粉"
  },
  "flout": {
    "phonetic": "flaut",
    "meaning": "vt. 嘲笑, 愚弄；vi. 表示轻蔑；n. 嘲笑, 愚弄, 轻视"
  },
  "flown": {
    "phonetic": "flәun",
    "meaning": "fly的过去分词"
  },
  "flowy": {
    "phonetic": "",
    "meaning": "[网络] 流动"
  },
  "fluff": {
    "phonetic": "flʌf",
    "meaning": "n. 软毛, 柔毛, 绒毛, 错误, 无价值的东西；vi. 起毛, 变松, 出错；vt. 使起毛, 抖松, 念错"
  },
  "fluid": {
    "phonetic": "'flu:id",
    "meaning": "n. 液体, 分泌液, 流体；a. 流动的, 可改变的"
  },
  "fluke": {
    "phonetic": "flu:k",
    "meaning": "v. 侥幸成功；n. 锚爪, 侥幸, 偶然事故"
  },
  "fluky": {
    "phonetic": "'flu:ki",
    "meaning": "a. 侥幸的, 幸中的, 不可靠的"
  },
  "flume": {
    "phonetic": "flu:m",
    "meaning": "n. 峡沟, 引水槽, 水道；vt. 顺流搬运, 用槽引水；vi. 造水槽, 使用引水槽"
  },
  "flung": {
    "phonetic": "fl ʌŋ",
    "meaning": "扔, 丢, 掷, 抛, 急伸, 挥动, 扫视, (猛)推, 急派(军队), 猛冲, 急行, 直冲, 乱踢"
  },
  "flunk": {
    "phonetic": "flʌŋk",
    "meaning": "n. 失败, 不及格；vi. 失败, 考试不及格, 放弃；vt. 使不及格"
  },
  "flush": {
    "phonetic": "flʌʃ",
    "meaning": "n. 流溢, 面红, 旺盛, 发烧, 惊飞的鸟, 同花牌；a. 丰足的, 齐平的, 满盈的, 泛滥的；adv. 齐平地, 直接地；vi. 脸发红, 奔涌, 旺盛, 惊飞；vt. 淹没, 冲洗, 使脸红, 使激动, 使齐平, 使惊飞"
  },
  "flute": {
    "phonetic": "flu:t",
    "meaning": "n. 笛, 横笛, 凹槽；vi. 吹笛子；vt. 用长笛奏, 刻凹槽于"
  },
  "flyby": {
    "phonetic": "'flaibai",
    "meaning": "n. 在低空飞过指定地点, 飞越"
  },
  "flyer": {
    "phonetic": "'flaiә",
    "meaning": "n. 飞鸟, 飞行物, 飞行员, 快车, 传单, 飞跳；[经] 投机买卖, 孤注一掷, (广告)传单"
  },
  "foamy": {
    "phonetic": "'fәumi",
    "meaning": "a. 全是泡沫的, 起泡沫的, 泡沫的"
  },
  "focal": {
    "phonetic": "'fәukl",
    "meaning": "a. 焦点的, 在焦点上的；[医] 病灶的, 灶的"
  },
  "focus": {
    "phonetic": "'fәukәs",
    "meaning": "n. 焦点, 焦距；vi. 聚焦, 注视；vt. 使聚焦, 调焦, 集中；[计] 焦点"
  },
  "fogey": {
    "phonetic": "'fәu^i",
    "meaning": "n. (思想)守旧者, 抱残守缺的人"
  },
  "foggy": {
    "phonetic": "'fɒgi",
    "meaning": "a. 雾深的, 模糊的"
  },
  "foist": {
    "phonetic": "fɒist",
    "meaning": "vt. 硬卖给, 偷偷插入, 使混入"
  },
  "folic": {
    "phonetic": "",
    "meaning": "[医]叶酸"
  },
  "folio": {
    "phonetic": "'fәuliәu",
    "meaning": "n. 对开纸, 页码, (原稿的)一页；a. 对折的, 对开的；vt. 编页码"
  },
  "folky": {
    "phonetic": "'fəuki",
    "meaning": "a. 普通的; 常见的"
  },
  "folly": {
    "phonetic": "'fɒli",
    "meaning": "n. 愚蠢, 荒唐事, 讽刺剧"
  },
  "foray": {
    "phonetic": "'fɒrei",
    "meaning": "vi. 侵略, 劫掠, 袭击；n. 侵掠, 侵略, 攻击"
  },
  "force": {
    "phonetic": "fɒ:s",
    "meaning": "n. 力量, 武力, 势力, 影响力, 军队, 力, 效力；vt. 强迫, 强夺, 推动, 提高；[计] 人工转移; 强制"
  },
  "forge": {
    "phonetic": "fɒ:dʒ",
    "meaning": "n. 熔炉, 铁工厂；vt. 打制, 锻造, 伪造；vi. 锻造, 伪造"
  },
  "forgo": {
    "phonetic": "fɒ:'gәu",
    "meaning": "vt. 摒绝, 放弃"
  },
  "forte": {
    "phonetic": "fɔ:t",
    "meaning": "n. 长处, 特长, 拿手, 优点"
  },
  "forth": {
    "phonetic": "fɒ:θ",
    "meaning": "adv. 往前, 以后, 向外"
  },
  "forty": {
    "phonetic": "'fɒ:ti",
    "meaning": "num. 四十, 四十个"
  },
  "forum": {
    "phonetic": "'fɒ:rәm",
    "meaning": "n. 论坛, 公开讨论的广场, 法庭, 讨论会；[法] 讨论会, 专题讨论, 公共论坛"
  },
  "found": {
    "phonetic": "faund",
    "meaning": "vt. 建立, 创立, 铸造；find的过去式和过去分词"
  },
  "fount": {
    "phonetic": "faunt",
    "meaning": "n. 泉, 源泉, 墨水缸, 一副铅字"
  },
  "foyer": {
    "phonetic": "'fɔiei",
    "meaning": "n. 门厅, 入门大堂"
  },
  "frail": {
    "phonetic": "freil",
    "meaning": "a. 脆弱的, 虚弱的, 意志薄弱的；n. 少女, 少妇, 灯心草篓"
  },
  "frame": {
    "phonetic": "freim",
    "meaning": "n. 框, 结构, 体格；vt. 构成, 设计, 制定, 使适合, 陷害；[计] 框架, 图文框, 帧"
  },
  "frank": {
    "phonetic": "fræŋk",
    "meaning": "a. 坦白的, 率直的, 老实的；vt. 免费邮寄；n. 免费邮寄特权"
  },
  "fraud": {
    "phonetic": "frɒ:d",
    "meaning": "n. 欺骗, 欺诈, 诡计, 骗子；[经] 欺诈, 舞弊, 骗子"
  },
  "freak": {
    "phonetic": "fri:k",
    "meaning": "n. 畸形人, 畸形物, 不正常的事物, 反复无常；a. 奇异的, 反常的"
  },
  "freed": {
    "phonetic": "",
    "meaning": "a. 释放的"
  },
  "freer": {
    "phonetic": "'fri:ә(r)",
    "meaning": "n. 给予自由的人或事物"
  },
  "fresh": {
    "phonetic": "freʃ",
    "meaning": "a. 新鲜的, 新奇的, 另外的, 淡的, 精神饱满的, 冒失的；adv. 最新地, 刚刚；n. 开始, 泛滥"
  },
  "friar": {
    "phonetic": "'fraiә",
    "meaning": "n. 修道士"
  },
  "fried": {
    "phonetic": "fraid",
    "meaning": "a. 油炸的"
  },
  "frill": {
    "phonetic": "fril",
    "meaning": "n. (衣饰上的)皱边, 皱边纸饰；vi. 起边皱；vt. 折成皱边"
  },
  "frise": {
    "phonetic": "fri:z",
    "meaning": "aileron[空]弗利兹副翼阻力副翼"
  },
  "frisk": {
    "phonetic": "frisk",
    "meaning": "n. 乱跳, 欢闹, 活跃；vi. 欢跃, 蹦跳；vt. 轻摇"
  },
  "fritz": {
    "phonetic": "frits",
    "meaning": "n. 德国兵, 德国人"
  },
  "frizz": {
    "phonetic": "friz",
    "meaning": "n. 拳发, 拳曲；v. (使)拳曲"
  },
  "frock": {
    "phonetic": "frɒk",
    "meaning": "n. 女礼服, 连衣裙, 工装, 罩袍, 僧衣"
  },
  "frond": {
    "phonetic": "'frɒnd",
    "meaning": "n. 叶, 植物体；[医] 叶(指蕨类、棕榈类、苏铁类)"
  },
  "front": {
    "phonetic": "frʌnt",
    "meaning": "n. 前面, 开头, 前线, 阵线, 态度；vt. 面对, 朝向, 对抗；vi. 朝向"
  },
  "frosh": {
    "phonetic": "frɒʃ",
    "meaning": "n. 大学(或中学)一年级生"
  },
  "frost": {
    "phonetic": "frɒst",
    "meaning": "n. 霜, 冰冻, 冷漠；vt. 覆着霜, 冻结, 结霜；vi. 受冻, 起霜"
  },
  "froth": {
    "phonetic": "frɒθ",
    "meaning": "n. 泡, 泡沫, 琐物；vt. 使生泡沫；vi. 发泡, 吹泡"
  },
  "frown": {
    "phonetic": "fraun",
    "meaning": "n. 皱眉；vi. 皱眉头；vt. 皱眉表示"
  },
  "froze": {
    "phonetic": "frәuz",
    "meaning": "freeze的过去式"
  },
  "fruit": {
    "phonetic": "fru:t",
    "meaning": "n. 水果, 果类, 结果；[医] 果实, 种实"
  },
  "frump": {
    "phonetic": "frʌmp",
    "meaning": "n. 邋遢女人, 守旧者"
  },
  "fryer": {
    "phonetic": "fraiә",
    "meaning": "n. 做油煎食物的人, 可供油炸的食品, 油炸锅"
  },
  "fubar": {
    "phonetic": "fju:bɑ:",
    "meaning": "n. 信息条；信息面板；a. 无法处置的；无法插手整理的"
  },
  "fudge": {
    "phonetic": "fʌdʒ",
    "meaning": "n. 虚构的故事, 谎言, 胡说；interj. 胡说八道；vi. 蒙混, 做傻事；vt. 粗制滥造, 捏造, 逃避职责"
  },
  "fugue": {
    "phonetic": "fju:g",
    "meaning": "n. 赋格曲, 神游；v. 谱赋格曲"
  },
  "fully": {
    "phonetic": "'fuli",
    "meaning": "adv. 十分地, 完全地, 充分地"
  },
  "fumed": {
    "phonetic": "fju:md",
    "meaning": "v. 愤怒( fume的过去式和过去分词 ); 大怒; 发怒; 冒烟"
  },
  "fungi": {
    "phonetic": "'fʌndʒai, 'fʌŋ^ai",
    "meaning": "pl. 真菌, 突然发生而迅速生长的东西；[医] 真菌, 霉菌, 蕈, 海绵肿"
  },
  "fungo": {
    "phonetic": "'fʌŋgәu",
    "meaning": "n. 为练习守备所击的飞球"
  },
  "funky": {
    "phonetic": "'fʌŋki",
    "meaning": "a. 畏缩的, 怯懦的, 恶臭的"
  },
  "funny": {
    "phonetic": "'fʌni",
    "meaning": "a. 好笑的, 有趣的, 滑稽的；n. 滑稽人物"
  },
  "furor": {
    "phonetic": "'fjuәrɒ:",
    "meaning": "n. 喧闹, 激怒, 感动, 狂热；[医] 狂乱, 狂暴, 狂怒"
  },
  "furry": {
    "phonetic": "'fә:ri",
    "meaning": "a. 毛皮的, 盖着毛皮的, 似毛皮的"
  },
  "fused": {
    "phonetic": "fju:zd",
    "meaning": "a. 熔化的, 熔凝的"
  },
  "fussy": {
    "phonetic": "'fʌsi",
    "meaning": "a. 易怒的, 爱挑剔的, 难取悦的, 易烦恼的"
  },
  "fusty": {
    "phonetic": "'fʌsti",
    "meaning": "a. 发霉的, 守旧的, 陈腐的"
  },
  "futon": {
    "phonetic": "ˈfu:tɒn",
    "meaning": "n. 日本床垫, 蒲团; （有支架可折叠成长榻的）蒲团"
  },
  "fuzzy": {
    "phonetic": "'fʌzi",
    "meaning": "a. 有微毛的, 模糊的；[电] 微毛"
  },
  "gabby": {
    "phonetic": "'^æbi",
    "meaning": "a. 饶舌的"
  },
  "gable": {
    "phonetic": "'geibl",
    "meaning": "n. 山形墙, 人字板"
  },
  "gaffe": {
    "phonetic": "gæf",
    "meaning": "n. 过失, 失态, 出丑"
  },
  "gaily": {
    "phonetic": "'geili",
    "meaning": "adv. 华丽地, 欢乐地"
  },
  "gamed": {
    "phonetic": "",
    "meaning": "v. 打赌, 赌输赢（game的过去式与过去分词形式）"
  },
  "gamer": {
    "phonetic": "'ɡeimә",
    "meaning": "n. 玩家, 博弈者"
  },
  "gamey": {
    "phonetic": "'^eimi",
    "meaning": "a. 多猎物的, 味道强的, 勇敢的"
  },
  "gamma": {
    "phonetic": "'^æmә",
    "meaning": "n. 希腊语的第三个字母(Γ,γ)；[医] γ(希腊文第三个字母), 丙种, 微克(千分之一毫克)"
  },
  "gamut": {
    "phonetic": "'gæmәt",
    "meaning": "n. 音阶, 整个范围, 全部, 音域"
  },
  "gaped": {
    "phonetic": "geɪpt",
    "meaning": "v. 目瞪口呆地凝视( gape的过去式和过去分词 ); 张开, 张大"
  },
  "gassy": {
    "phonetic": "'gæsi",
    "meaning": "a. 气体的, 气状的, 含气的"
  },
  "gated": {
    "phonetic": "'ɡeitid",
    "meaning": "a. 有关卡的；带栅门的"
  },
  "gator": {
    "phonetic": "'ɡeitә",
    "meaning": "n. 短吻鳄"
  },
  "gaudy": {
    "phonetic": "'gɒ:di",
    "meaning": "a. 俗丽的, 华而不实的；n. 盛大宴会"
  },
  "gauge": {
    "phonetic": "geidʒ",
    "meaning": "n. 标准度量, 计量器；vt. 精确计量, 估计；[计] 线规"
  },
  "gaunt": {
    "phonetic": "gɒ:nt",
    "meaning": "a. 瘦削的, 憔悴的, 荒凉的"
  },
  "gauze": {
    "phonetic": "gɒ:z",
    "meaning": "n. 薄纱, 纱布, 金属网；[医] 纱布"
  },
  "gauzy": {
    "phonetic": "'gɒ:zi",
    "meaning": "a. 纱似的, 薄的"
  },
  "gavel": {
    "phonetic": "'gævәl",
    "meaning": "n. 槌；[法] 赋税或租金, 议事槌, 小木槌"
  },
  "gawky": {
    "phonetic": "'^ɔ:ki",
    "meaning": "a. 愚笨的, 腼腆的, 粗笨的, 笨拙的"
  },
  "gayer": {
    "phonetic": "",
    "meaning": "a. 华美的, 快乐的"
  },
  "gayly": {
    "phonetic": "'ɡeili",
    "meaning": "adv. 快乐地；华美地"
  },
  "gazed": {
    "phonetic": "ɡeizd",
    "meaning": "v. 凝视, 注视( gaze的过去式和过去分词 )"
  },
  "gazer": {
    "phonetic": "",
    "meaning": "n. 凝视者"
  },
  "gecko": {
    "phonetic": "'gekәu",
    "meaning": "n. 壁虎；[医] 蛤蚧"
  },
  "geeky": {
    "phonetic": "'ɡiːkɪ",
    "meaning": "a. <俚>令人讨厌的"
  },
  "geese": {
    "phonetic": "^i:s",
    "meaning": "n. 鹅, 鹅肉, 呆头鹅, 傻瓜"
  },
  "genie": {
    "phonetic": "'dʒi:ni",
    "meaning": "n. 妖怪, 鬼"
  },
  "genre": {
    "phonetic": "'ʒɒŋrә",
    "meaning": "n. 类型, 流派"
  },
  "geode": {
    "phonetic": "'dʒi:әud",
    "meaning": "n. 空心石核, 晶洞, 晶洞状物；[医] 淋巴腔"
  },
  "getup": {
    "phonetic": "",
    "meaning": "n. 式样, 打扮"
  },
  "ghost": {
    "phonetic": "gәust",
    "meaning": "n. 鬼, 灵魂, 幻影, 一丝, 一点；v. 鬼似地游荡"
  },
  "ghoul": {
    "phonetic": "gu:l",
    "meaning": "n. 食尸鬼, 饿鬼, 盗墓者"
  },
  "giant": {
    "phonetic": "'dʒaiәnt",
    "meaning": "n. 巨人, 大力士, 巨大怪物；a. 庞大的, 巨大的"
  },
  "gibed": {
    "phonetic": "dʒaɪbd",
    "meaning": "v. 嘲笑, 嘲弄( gibe的过去式和过去分词 )"
  },
  "giddy": {
    "phonetic": "'gidi",
    "meaning": "a. 眼花的, 头晕的；v. (使)眼花, (使)眩晕"
  },
  "gimme": {
    "phonetic": "'^imi",
    "meaning": "<口>=give me(或give it to me)"
  },
  "girly": {
    "phonetic": "'ɡә:li",
    "meaning": "a. 像少女的"
  },
  "girth": {
    "phonetic": "gә:θ",
    "meaning": "n. (树的)干围, 周长, 肚带；vt. 围绕, 包围；vi. 围长为"
  },
  "given": {
    "phonetic": "'givәn",
    "meaning": "a. 赠予的, 沉溺的, 约定的；give的过去分词"
  },
  "giver": {
    "phonetic": "'givә",
    "meaning": "n. 给予者, 赠予人"
  },
  "gizmo": {
    "phonetic": "'gizmәu",
    "meaning": "n. 小发明, 小玩意儿"
  },
  "glade": {
    "phonetic": "gleid",
    "meaning": "n. 林间空地, 沼泽地"
  },
  "glamp": {
    "phonetic": "",
    "meaning": ""
  },
  "gland": {
    "phonetic": "glænd",
    "meaning": "n. 腺, 密封套；[化] 衬片; 密封垫"
  },
  "glare": {
    "phonetic": "glєә",
    "meaning": "n. 闪耀光, 刺眼；vi. 发眩光, 瞪视；vt. 瞪眼表示"
  },
  "glass": {
    "phonetic": "glɑ:s",
    "meaning": "n. 玻璃, 玻璃杯, 透镜；vt. 装玻璃于, 反射, 反映；vi. 成玻璃状"
  },
  "glaze": {
    "phonetic": "'gleiz",
    "meaning": "n. 釉, 上光, 光滑面；vt. 装以玻璃, 上釉于；vi. 变得光滑, (目光)变呆滞"
  },
  "gleam": {
    "phonetic": "gli:m",
    "meaning": "n. 光束, 微光, 反光；vi. 闪烁, 隐约地闪现；vt. 使发微光, 使闪烁"
  },
  "glean": {
    "phonetic": "gli:n",
    "meaning": "v. 拾落穗, 收集"
  },
  "glide": {
    "phonetic": "glaid",
    "meaning": "n. 滑动, 滑过, 流水；vi. 滑动, 滑翔, 溜走, 流逝；vt. 使滑动"
  },
  "glint": {
    "phonetic": "glint",
    "meaning": "n. 闪光, 一闪；vi. 闪耀, 闪闪发光, 反射, 迅速移动；vt. 使发光, 使闪光"
  },
  "glitz": {
    "phonetic": "glɪts",
    "meaning": "n. 闪光, 炫目, 浮华"
  },
  "gloam": {
    "phonetic": "^lәum",
    "meaning": "n. <古>黄昏, 薄暮；v. 变朦胧"
  },
  "gloat": {
    "phonetic": "glәut",
    "meaning": "vi. 满足地看, 幸灾乐祸, 贪婪地盯视；n. 贪婪的盯视, 满足的注视, 幸灾乐祸"
  },
  "globe": {
    "phonetic": "glәub",
    "meaning": "n. 球, 球状物, 地球仪, 天体；v. (使)成球状"
  },
  "gloom": {
    "phonetic": "glu:m",
    "meaning": "n. 忧郁, 暗处, 幽暗；vi. 变忧沉, 变黑暗；vt. 使忧郁, 使黑暗"
  },
  "gloop": {
    "phonetic": "",
    "meaning": "难看（或味道差、感觉不舒服）的半流体物质；黏稠物"
  },
  "glory": {
    "phonetic": "'glɒ:ri",
    "meaning": "n. 光荣, 荣耀, 荣誉, 壮丽, 繁荣；vi. 自豪"
  },
  "gloss": {
    "phonetic": "glɒs",
    "meaning": "n. 光彩, 假象, 注释；vt. 使光彩, 掩盖, 上光于, 注释, 曲解；vi. 发光, 作注释"
  },
  "glove": {
    "phonetic": "glʌv",
    "meaning": "n. 手套；vt. 给...戴手套"
  },
  "glued": {
    "phonetic": "ɡluːd",
    "meaning": "v. 用胶水将物体粘合( glue的过去式和过去分词 )"
  },
  "glute": {
    "phonetic": "",
    "meaning": "[网络] 臀部训练器；臀部伸张；胯部"
  },
  "glyph": {
    "phonetic": "glif",
    "meaning": "[计] 符号, 点符"
  },
  "gnarl": {
    "phonetic": "nɑ:l",
    "meaning": "n. 木节, 木瘤；vi. 形成木节, 咆哮；vt. 扭曲"
  },
  "gnash": {
    "phonetic": "næʃ",
    "meaning": "v. 咬牙切齿；n. 咬"
  },
  "gnome": {
    "phonetic": "nәum",
    "meaning": "n. 格言, 箴言, 侏儒, 土地神"
  },
  "godly": {
    "phonetic": "'gɒdli",
    "meaning": "a. 敬神的, 虔诚的, 神的"
  },
  "gofer": {
    "phonetic": "'^әjfә(r)",
    "meaning": "vt. 使起皱褶/皱纹；n. 皱褶, (烫皱褶用的)熨斗, 襞"
  },
  "going": {
    "phonetic": "'gәuiŋ",
    "meaning": "n. 去, 离去, 工作情况, 地面状况, 行为；a. 进行中的, 流行的, 成功的, 现存的"
  },
  "golem": {
    "phonetic": "'^әulem",
    "meaning": "n. 机器人"
  },
  "golly": {
    "phonetic": "'gɒli",
    "meaning": "n. 神；interj. 呀, 天哪, 发誓"
  },
  "gonad": {
    "phonetic": "'gәunæd",
    "meaning": "n. 性腺, 生殖腺"
  },
  "goner": {
    "phonetic": "'gɒnә",
    "meaning": "n. 已死者, 无法挽救的人"
  },
  "gonna": {
    "phonetic": "'ɡɔnә",
    "meaning": "abbr. （美）将要（等于going to）"
  },
  "gonzo": {
    "phonetic": "'ɡɔnzәu",
    "meaning": "a. 疯狂的；愚蠢的；偏激主观的；怪论连篇的"
  },
  "goody": {
    "phonetic": "'gudi:",
    "meaning": "n. 身分低微之老妇, 糖果, 姥姥；a. 感伤的, 伪善的；interj. 太好了"
  },
  "gooey": {
    "phonetic": "'gu:i",
    "meaning": "a. 胶粘的, 自作多情的；n. 胶粘物, 性格软弱的人"
  },
  "goofy": {
    "phonetic": "'gu:fi",
    "meaning": "a. 愚笨的, 傻瓜的"
  },
  "goopy": {
    "phonetic": "ˈɡu:pi",
    "meaning": "a. <俚>傻的, 痴呆的； <美><俚>粘稠的, 滑腻的"
  },
  "goose": {
    "phonetic": "gu:s",
    "meaning": "n. 鹅, 雌鹅, 鹅肉, 弯把熨斗；vt. 与...性交, 突然加大油门, 使生色, 喝倒彩"
  },
  "gored": {
    "phonetic": "gɔ:d",
    "meaning": "v. （动物）用角撞伤, 用牙刺破( gore的过去式和过去分词 )"
  },
  "gorge": {
    "phonetic": "gɒ:dʒ",
    "meaning": "n. 峡谷, 凹槽, 塞饱, 咽喉；vi. 狼吞虎咽；vt. 塞饱, 狼吞虎咽地吃"
  },
  "gorse": {
    "phonetic": "gɒ:s",
    "meaning": "n. 荆豆, 桧"
  },
  "gotta": {
    "phonetic": "'^ɔtә",
    "meaning": "必须, 有, 拥有"
  },
  "gouge": {
    "phonetic": "gaudʒ",
    "meaning": "n. 圆凿, 用圆凿凿成的槽, 挖, 掘；vt. 用圆凿削, 挖出, 欺骗"
  },
  "gourd": {
    "phonetic": "guәd",
    "meaning": "n. 葫芦"
  },
  "grace": {
    "phonetic": "greis",
    "meaning": "n. 优雅, 风度, 慈悲, 恩惠, 体面, 赦免, 恩典, 谢恩祷告；vt. 使优美"
  },
  "grade": {
    "phonetic": "greid",
    "meaning": "n. 等级, 年级, 阶段, 成绩, 程度, 坡度, 斜坡；vt. 分等, 分级, 评分；vi. 属于某等级, 逐渐变化"
  },
  "graft": {
    "phonetic": "grɑ:ft",
    "meaning": "n. 嫁接, 贪污；v. 嫁接, 移植, 贪污"
  },
  "grail": {
    "phonetic": "^reil",
    "meaning": "n. 长期以来梦寐以求的东西"
  },
  "grain": {
    "phonetic": "grein",
    "meaning": "n. 谷粒, 颗粒, 谷类, 纹理, 本质；v. (使)成谷粒"
  },
  "grand": {
    "phonetic": "grænd",
    "meaning": "a. 庄重的, 壮观的, 显赫的, 重大的, 最高的, 雄伟的, 宏大的, 豪华的, 傲慢的；[法] 重大的, 主要的, 伟大的"
  },
  "grant": {
    "phonetic": "grænt",
    "meaning": "n. 授予, 授予物, 允许；vt. 允许, 承认, 授与；[计] 授权命令"
  },
  "grape": {
    "phonetic": "greip",
    "meaning": "n. 葡萄, 葡萄树；[医] 葡萄"
  },
  "graph": {
    "phonetic": "græf",
    "meaning": "n. 曲线图, 图表, 图形；[计] 图形"
  },
  "grasp": {
    "phonetic": "græsp",
    "meaning": "n. 把握, 抓紧, 理解, 抓, 柄, 控制；vt. 抓住, 紧握, 领会；vi. 抓"
  },
  "grass": {
    "phonetic": "græs",
    "meaning": "n. 草, 草原, 牧场；[医] 草, 禾本"
  },
  "grate": {
    "phonetic": "^reit",
    "meaning": "n. 炉格, 炉篦, 炉栅, 火炉, 壁炉, 格栅；vt. 装格栅于, 磨擦, 轧碎, 磨碎, 使焦急, 触怒, 使人烦躁, 刺激, 激怒；vt.vi. 擦响, 发出刺耳的尖厉声"
  },
  "grave": {
    "phonetic": "greiv",
    "meaning": "n. 墓穴, 坟墓, 终结, 死亡；a. 庄重的, 严肃的, 重大的, 低沉的；vt. 雕刻"
  },
  "gravy": {
    "phonetic": "'greivi",
    "meaning": "n. 肉汁, 外快"
  },
  "graze": {
    "phonetic": "greiz",
    "meaning": "n. 吃草, 放牧, 擦伤, 轻擦；v. (使)吃草, 放牧, 轻擦, 擦伤"
  },
  "great": {
    "phonetic": "greit",
    "meaning": "a. 大的, 非常的, 主要的, 重大的, 崇高的, 伟大的；adv. 顺利地, 得意地；n. 全部, 大人物, 大师"
  },
  "greed": {
    "phonetic": "gri:d",
    "meaning": "n. 贪欲, 贪婪"
  },
  "green": {
    "phonetic": "gri:n",
    "meaning": "n. 绿色, 绿色颜料；a. 绿色的, 未成熟的, 新鲜的, 青春的, 无经验的, 脸色发青的"
  },
  "greet": {
    "phonetic": "gri:t",
    "meaning": "vt. 问候, 致敬, 欢迎, 映入眼帘"
  },
  "grief": {
    "phonetic": "gri:f",
    "meaning": "n. 伤心, 忧愁, 悲痛, 不幸, 灾难"
  },
  "grift": {
    "phonetic": "grift",
    "meaning": "n. 诈骗；vt. 诈骗"
  },
  "grill": {
    "phonetic": "gril",
    "meaning": "n. 烤架, 铁格子, 烤肉；v. 烧, 烤, 严加盘问, 给...装栅栏"
  },
  "grime": {
    "phonetic": "graim",
    "meaning": "n. 尘垢, 煤尘, 污点；vt. 使污秽, 使...弄脏"
  },
  "grimy": {
    "phonetic": "'graimi",
    "meaning": "a. 污秽的, 肮脏的"
  },
  "grind": {
    "phonetic": "graind",
    "meaning": "n. 磨, 碾, 苦差, 摩擦声, 用功的学生；vt. 磨擦, 磨碎, 磨光, 折磨, 压榨；vi. 磨, 磨碎, 苦干"
  },
  "gripe": {
    "phonetic": "graip",
    "meaning": "n. 紧握, 柄, 把手, 控制；vt. 抓紧, 抱住, 使肠痛, 激怒；vi. 肠绞痛, 抱怨"
  },
  "grist": {
    "phonetic": "grist",
    "meaning": "n. 谷物, 面粉, 碎麦芽, 大量"
  },
  "groan": {
    "phonetic": "grәun",
    "meaning": "n. 呻吟, 叹息；vi. 呻吟, 抱怨, 受压迫；vt. 呻吟地说"
  },
  "groin": {
    "phonetic": "^rɔin",
    "meaning": "n. 腹股沟, 交叉拱；[医] 腹股沟"
  },
  "groom": {
    "phonetic": "gru:m",
    "meaning": "n. 马夫, 新郎, 男仆；vt. 喂马, 使...整洁, 推荐；vi. 打扮, 穿戴"
  },
  "grope": {
    "phonetic": "grәup",
    "meaning": "v. 摸索；n. 摸索"
  },
  "gross": {
    "phonetic": "grәus",
    "meaning": "n. 总数, 总量；a. 总共的, 未打折扣的, 恶劣的, 粗野的；vt. 总共收入"
  },
  "group": {
    "phonetic": "gru:p",
    "meaning": "n. 团体, 组, 团, 群；v. 聚合, 成群；[计] 创建组; 组, 用户组"
  },
  "grout": {
    "phonetic": "graut",
    "meaning": "n. 薄泥浆, 水泥浆；vt. 用薄泥浆填塞, (猪)用鼻子拱"
  },
  "grove": {
    "phonetic": "grәuv",
    "meaning": "n. 小树林"
  },
  "growl": {
    "phonetic": "graul",
    "meaning": "n. 吠声, 咆哮声；v. 怒吠, 咆哮, 吼"
  },
  "grown": {
    "phonetic": "grәun",
    "meaning": "a. 长大的, 成年的, 长满某物的；grow的过去分词"
  },
  "gruel": {
    "phonetic": "'gru:әl",
    "meaning": "n. 稀粥；vt. 使极度疲劳, 惩罚"
  },
  "gruff": {
    "phonetic": "grʌf",
    "meaning": "a. 粗哑的, 粗鲁的, 粗率的, 板着脸孔的"
  },
  "grump": {
    "phonetic": "^rʌmp",
    "meaning": "n. 一阵坏脾气, 发火, 脾气坏的人；vi. 闹情绪, 发牢骚"
  },
  "grunt": {
    "phonetic": "grʌnt",
    "meaning": "vi. 作呼噜声；vt. 咕哝；n. 呼噜声, 咕哝"
  },
  "guano": {
    "phonetic": "'gwɑ:nәu",
    "meaning": "n. 海鸟粪, 鸟粪石, 鱼肥料；vt. 施海鸟肥料"
  },
  "guard": {
    "phonetic": "gɑ:d",
    "meaning": "n. 守卫者, 警戒, 护卫队, 防护装置；vt. 保卫, 看守, 当心；vi. 防止, 警惕, 警卫, 看守"
  },
  "guava": {
    "phonetic": "'^wɑ:vә",
    "meaning": "n. 番石榴"
  },
  "guess": {
    "phonetic": "ges",
    "meaning": "n. 猜测, 臆测；v. 猜测, 臆测"
  },
  "guest": {
    "phonetic": "gest",
    "meaning": "n. 客人, 来宾, 旅客；[化] 客体"
  },
  "guide": {
    "phonetic": "gaid",
    "meaning": "n. 引导者, 导游, 指南, 路标；vt. 指导, 支配, 管理, 带领, 操纵；vi. 任向导；[计] 辅助线"
  },
  "guild": {
    "phonetic": "gild",
    "meaning": "n. 团体, 协会, 行业协会；[经] 同业公会"
  },
  "guile": {
    "phonetic": "gail",
    "meaning": "n. 狡猾, 狡计"
  },
  "guilt": {
    "phonetic": "gilt",
    "meaning": "n. 罪行, 内疚；[法] 罪, 犯罪, 罪行"
  },
  "guise": {
    "phonetic": "gaiz",
    "meaning": "n. 相似, 外观, 伪装；v. 穿戴, 伪装"
  },
  "gulag": {
    "phonetic": "^u:'lɑ:^",
    "meaning": "[俄]古拉格(集中营)"
  },
  "gulch": {
    "phonetic": "gʌlʃ",
    "meaning": "n. 地沟, 冲沟"
  },
  "gully": {
    "phonetic": "'gʌli",
    "meaning": "n. 小峡谷, 排水沟"
  },
  "gumbo": {
    "phonetic": "'^ʌmbәu",
    "meaning": "n. 大杂烩"
  },
  "gummy": {
    "phonetic": "'gʌmi",
    "meaning": "a. 树胶的, 粘的；[医] 树胶状的, 梅毒瘤状的"
  },
  "gunky": {
    "phonetic": "",
    "meaning": "油腻的；黏性的"
  },
  "guppy": {
    "phonetic": "'^ʌpi",
    "meaning": "n. 古比"
  },
  "gushy": {
    "phonetic": "'^ʌʃi",
    "meaning": "a. 过分多情的"
  },
  "gussy": {
    "phonetic": "'^ʌsi",
    "meaning": "vt.vi. (把...)打扮/装饰得花枝招展"
  },
  "gusto": {
    "phonetic": "'gʌstәu",
    "meaning": "n. 爱好, 嗜好, 由衷的高兴"
  },
  "gusty": {
    "phonetic": "'gʌsti",
    "meaning": "a. 刮风的, 阵阵猛急的, 突发的, 津津有味的"
  },
  "gutsy": {
    "phonetic": "'^ʌtsi",
    "meaning": "a. 有勇气的, 有力量的"
  },
  "gutty": {
    "phonetic": "'gʌti",
    "meaning": "a. 有种的, 胆大的, 有勇气的"
  },
  "habit": {
    "phonetic": "'hæbit",
    "meaning": "n. 习惯, 嗜好, 习性；vt. 使穿衣"
  },
  "hacky": {
    "phonetic": "'hæki",
    "meaning": "n. 出租汽车司机"
  },
  "haiku": {
    "phonetic": "'haiku:",
    "meaning": "n. haiku (Jap) 俳句"
  },
  "hairy": {
    "phonetic": "'hєәri",
    "meaning": "a. 多毛的, 毛状的, 长毛的"
  },
  "halal": {
    "phonetic": "hә'lɑ:l",
    "meaning": "n. 伊斯兰教律法的合法食物；v. 按伊斯兰教律法屠宰牲畜"
  },
  "halve": {
    "phonetic": "hɑ:v",
    "meaning": "vt. 二等分, 对半分享, 把...减半"
  },
  "handy": {
    "phonetic": "'hændi",
    "meaning": "a. 便利的, 敏捷的, 容易取得的；[化] 便于使用的; 易操作的"
  },
  "hanky": {
    "phonetic": "'hæŋki",
    "meaning": "n. 手帕"
  },
  "happy": {
    "phonetic": "'hæpi",
    "meaning": "a. 快乐的, 幸福的, 愉快的, 恰当的"
  },
  "hardy": {
    "phonetic": "'hɑ:di",
    "meaning": "a. 难的, 艰苦的, 坚硬的, 勇敢的；adv. 努力地, 辛苦地, 坚硬地"
  },
  "harem": {
    "phonetic": "'herәm",
    "meaning": "n. 闺房, (闺房里的)妻妾"
  },
  "harpy": {
    "phonetic": "'hɑ:pi",
    "meaning": "n. 哈比(希腊神话中残酷贪婪者)"
  },
  "harry": {
    "phonetic": "'hæri",
    "meaning": "vt. 掠夺, 使苦恼, 强使前行, 折磨, 骚扰"
  },
  "harsh": {
    "phonetic": "hɑ:ʃ",
    "meaning": "a. 粗糙的, 刺耳的, 严厉的；[法] 粗糙的, 严厉的, 苛刻的"
  },
  "haste": {
    "phonetic": "heist",
    "meaning": "n. 匆忙, 急忙"
  },
  "hasty": {
    "phonetic": "'heisti",
    "meaning": "a. 匆匆的, 轻率的, 性怠的"
  },
  "hatch": {
    "phonetic": "hætʃ",
    "meaning": "n. 孵化, 舱口；vt. 孵, 孵出, 策划；vi. 孵化"
  },
  "hated": {
    "phonetic": "heitid",
    "meaning": "v. 憎恨( hate的过去式和过去分词 ); 讨厌; 不愿; 为…感到抱歉"
  },
  "hater": {
    "phonetic": "'heitә(r)",
    "meaning": "n. 怀恨者"
  },
  "haunt": {
    "phonetic": "hɒ:nt",
    "meaning": "n. 常到的地方, 生息地；vt. 常到, 出没于, 萦绕于；vi. 出没, 作祟"
  },
  "haute": {
    "phonetic": "",
    "meaning": "n. (Haute)人名；(德)豪特；(法)奥特"
  },
  "haven": {
    "phonetic": "'heivn",
    "meaning": "n. 港, 避难所, 安息所；vt. 安置...于港中, 庇护, 入港"
  },
  "havoc": {
    "phonetic": "'hævәk",
    "meaning": "n. 大破坏, 蹂躏；vt. 严重破坏"
  },
  "hazed": {
    "phonetic": "heizd",
    "meaning": "v. （使）笼罩在薄雾中( haze的过去式和过去分词 ); 戏弄, 欺凌（新生等, 有时作为加入美国大学生联谊会的条件）"
  },
  "hazel": {
    "phonetic": "'heizl",
    "meaning": "n. 榛子, 榛树, 淡褐色；a. 榛树的, 淡褐色的"
  },
  "heady": {
    "phonetic": "'hedi",
    "meaning": "a. 顽固的, 任性的, 性急的, 猛烈的"
  },
  "heard": {
    "phonetic": "hә:d",
    "meaning": "hear的过去式和过去分词"
  },
  "heart": {
    "phonetic": "hɑ:t",
    "meaning": "n. 心, 心脏, 中心, 内心, 感情, 精神, 心情, 宝贝儿；vt. 鼓励"
  },
  "heath": {
    "phonetic": "hi:θ",
    "meaning": "n. 石南荒原, 低矮灌木"
  },
  "heave": {
    "phonetic": "hi:v",
    "meaning": "n. 举, 抛, 起伏, 鼓起；vt. 用力举起, 使举起, 使鼓起；vi. 抛出, 起伏, 喘息, 凸起"
  },
  "heavy": {
    "phonetic": "'hevi",
    "meaning": "a. 重的, 巨大的, 沉重的, 笨重的, 过度的；adv. 沉重地；n. 重物, 严肃角色"
  },
  "hedge": {
    "phonetic": "hedʒ",
    "meaning": "n. 树篱, 障碍, 套头交易；vt. 用树篱围, 套期保值, 妨碍, 两面下注以防...的损失；vi. 筑树篱, 躲闪, 两面下注以防损失；a. 树篱的, 偷偷摸摸的"
  },
  "hefty": {
    "phonetic": "'hefti",
    "meaning": "a. 重的, 肌肉发达的"
  },
  "heist": {
    "phonetic": "haist",
    "meaning": "n. 强夺, 拦劫, 抢劫；vt. 强夺, 拦劫, 抢劫"
  },
  "helix": {
    "phonetic": "'hi:liks",
    "meaning": "n. 螺旋, 螺旋状物, 耳轮；[化] 螺旋"
  },
  "hello": {
    "phonetic": "hә'lәu",
    "meaning": "interj. 喂, 嘿"
  },
  "hence": {
    "phonetic": "hens",
    "meaning": "adv. 因此, 从此"
  },
  "henna": {
    "phonetic": "'henә",
    "meaning": "n. 指甲花, 指甲花染料, 红褐色；[化] 散沫花叶粉; 指甲花叶粉"
  },
  "heron": {
    "phonetic": "'herәn",
    "meaning": "n. 鹭"
  },
  "hertz": {
    "phonetic": "'hә:ts",
    "meaning": "n. 赫, 赫兹；[计] 赫兹"
  },
  "hewed": {
    "phonetic": "hju:d",
    "meaning": "v. （用斧、刀等）砍、劈( hew的过去式和过去分词 ); 砍成; 劈出; 开辟"
  },
  "hexed": {
    "phonetic": "",
    "meaning": "[电影]激情杀人狂"
  },
  "hider": {
    "phonetic": "",
    "meaning": "[计] 封闭多边形"
  },
  "hijab": {
    "phonetic": "hɪˈdʒɑ:b",
    "meaning": "n. 穆斯林妇女戴的面纱或头巾"
  },
  "hiked": {
    "phonetic": "haikt",
    "meaning": "v. 徒步旅行( hike的过去式和过去分词 ); <口>提高（价格等）"
  },
  "hiker": {
    "phonetic": "'haikә",
    "meaning": "n. 徒步旅行者"
  },
  "hilly": {
    "phonetic": "'hili",
    "meaning": "a. 多丘陵的, 多山岗的, 险峻的"
  },
  "hinge": {
    "phonetic": "hindʒ",
    "meaning": "n. 铰链, 关键, 枢纽；vt. 装铰链；vi. 靠铰链移动, 依...而转移"
  },
  "hippo": {
    "phonetic": "'hipәu",
    "meaning": "n. 河马；[化] 吐根(的别名)"
  },
  "hippy": {
    "phonetic": "'hipi",
    "meaning": "n. 嬉皮士"
  },
  "hired": {
    "phonetic": "",
    "meaning": "v. 租用；雇用（hire的过去式及过去分词形式）"
  },
  "hiree": {
    "phonetic": "",
    "meaning": "[经] 被雇者"
  },
  "hirer": {
    "phonetic": "'haiәrә",
    "meaning": "n. 租借者, 雇主；[经] 雇主, 租借者"
  },
  "hitch": {
    "phonetic": "hitʃ",
    "meaning": "n. 猛拉, 急推, 蹒跚, 故障；vt. 猛拉, 系住；vi. 蹒跚, 被钩住"
  },
  "hived": {
    "phonetic": "haɪvd",
    "meaning": "v. 使（蜂）入蜂箱( hive的过去式和过去分词 ); （蜂）进入蜂箱; 把一部份分离出来, 卖掉公司的一部分"
  },
  "hoagy": {
    "phonetic": "hə'ʊædʒɪ",
    "meaning": "n. 大型三明治"
  },
  "hoard": {
    "phonetic": "hɒ:d",
    "meaning": "n. 贮藏物, 密藏的金钱；v. 囤积, 贮藏"
  },
  "hoary": {
    "phonetic": "'hɒ:ri",
    "meaning": "a. 灰白的, 陈旧的；[医] 灰发的, 白发的"
  },
  "hobby": {
    "phonetic": "'hɒbi",
    "meaning": "n. 嗜好, 癖好, 爱好"
  },
  "hocus": {
    "phonetic": "'hәukәs",
    "meaning": "vt. 欺骗, 麻醉"
  },
  "hoist": {
    "phonetic": "hɒist",
    "meaning": "n. 升高, 起重机, 推动；v. 升起, 升高, 举起"
  },
  "hokey": {
    "phonetic": "'hәjki",
    "meaning": "a. 虚情假意的, 做作的"
  },
  "hokum": {
    "phonetic": "'houkәm",
    "meaning": "n. 低级噱头, 废话"
  },
  "holed": {
    "phonetic": "",
    "meaning": "a. 进洞的"
  },
  "holly": {
    "phonetic": "'hɒli",
    "meaning": "n. 冬青树"
  },
  "homed": {
    "phonetic": "",
    "meaning": "vi. 回家（home的过去式与过去分词形式）"
  },
  "homer": {
    "phonetic": "'hәumә",
    "meaning": "n. 本垒打, 传信鸽"
  },
  "homey": {
    "phonetic": "'hәumi",
    "meaning": "a. 家庭似的, 自在的, 舒适的"
  },
  "honed": {
    "phonetic": "həʊnd",
    "meaning": "v. 把（刀、剑等）磨光( hone的过去式和过去分词 )"
  },
  "honey": {
    "phonetic": "'hʌni",
    "meaning": "n. 蜂蜜, 甜蜜, 爱人；a. 蜂蜜似的, 甜蜜的, 甘美的；vt. 加蜜使甜, 对...说甜言蜜语；vi. 说甜言蜜语, 奉承"
  },
  "honor": {
    "phonetic": "'ɒnә",
    "meaning": "n. 荣誉, 头衔, 信用, 尊敬, 名誉, 阁下, 勋章；vt. 尊敬, 授予荣誉, 承兑, 实践"
  },
  "hooch": {
    "phonetic": "hu:tʃ",
    "meaning": "n. 私酒, 烈酒"
  },
  "hoody": {
    "phonetic": "ˈhʊdi",
    "meaning": "n. 年轻小混混"
  },
  "hooey": {
    "phonetic": "'hu:i",
    "meaning": "n. 胡言乱语, 傻事；interj. 真傻, 骗人"
  },
  "hooky": {
    "phonetic": "'huki",
    "meaning": "n. 逃学者；vt. 偷；a. 多钩的"
  },
  "hoped": {
    "phonetic": "",
    "meaning": "v. 希望（hope的过去分词）"
  },
  "hoppy": {
    "phonetic": "'hɔpi",
    "meaning": "n. 吸毒成瘾者；a. 蛇麻草的；啤酒花的；跳动的"
  },
  "horde": {
    "phonetic": "hɒ:d",
    "meaning": "n. (一)群, 游牧部落, 移动群；vi. 成群结队"
  },
  "horny": {
    "phonetic": "'hɒ:ni",
    "meaning": "a. 角的, 似角一样坚硬的, 角质的, 老茧的；[医] 角性的, 角的"
  },
  "horse": {
    "phonetic": "hɒ:s",
    "meaning": "n. 马, 骑兵, 脚架；vi. 骑马, 取笑；vt. 使骑马, 系马于"
  },
  "hosed": {
    "phonetic": "",
    "meaning": "vt. 用软管浇（hose的过去式与过去分词形式）"
  },
  "hotel": {
    "phonetic": "hәu'tel",
    "meaning": "n. 旅馆, 客栈"
  },
  "hotly": {
    "phonetic": "'hɒtli",
    "meaning": "adv. 暑热地, 激烈地, 热心地"
  },
  "hound": {
    "phonetic": "haund",
    "meaning": "n. 猎犬；vt. 带猎犬狩猎, 追捕, 激励, 使追逐"
  },
  "house": {
    "phonetic": "haus",
    "meaning": "n. 房子, 住宅, 机构, 议院, 家族, 家庭；vt. 给...房子住, 收藏；vi. 住, 躲藏"
  },
  "hovel": {
    "phonetic": "'hʌvәl",
    "meaning": "n. 简陋小屋, 杂物间, 家畜小屋"
  },
  "hover": {
    "phonetic": "'hʌvә",
    "meaning": "vi. 盘旋, 翱翔, 徘徊；vt. 孵；n. 翱翔"
  },
  "howdy": {
    "phonetic": "'haudi",
    "meaning": "int. 您好(招呼用语)"
  },
  "hubby": {
    "phonetic": "'hʌbi",
    "meaning": "n. 丈夫"
  },
  "huffy": {
    "phonetic": "'hʌfi",
    "meaning": "a. 怒冲冲的"
  },
  "hulky": {
    "phonetic": "'hʌlkɪ",
    "meaning": "笨重的"
  },
  "human": {
    "phonetic": "'hju:mәn",
    "meaning": "n. 人, 人类；a. 人类的, 似人类的, 人性的, 有同情心的"
  },
  "humid": {
    "phonetic": "'hju:mid",
    "meaning": "a. 潮湿的, 湿润的, 多湿气的"
  },
  "humor": {
    "phonetic": "'hju:mә",
    "meaning": "n. 幽默, 诙谐, 心情；vt. 迎合, 牵就, 顺应"
  },
  "humph": {
    "phonetic": "'hʌmf",
    "meaning": "interj. 哼；vi. 发哼声"
  },
  "humus": {
    "phonetic": "'hju:mәs",
    "meaning": "n. 腐殖质；[化] 腐殖质"
  },
  "hunch": {
    "phonetic": "hʌntʃ",
    "meaning": "n. 肉峰, 预感, 大块；vt. 弯腰驼背, 预感到, 耸肩；vi. 向前移动, 隆起"
  },
  "hunky": {
    "phonetic": "'hʌŋki",
    "meaning": "n. 来自中欧(或东欧)的移民"
  },
  "hurry": {
    "phonetic": "'hʌri",
    "meaning": "n. 匆忙, 急忙, 急促；vt. 急派, 催促；vi. 匆忙, 赶快"
  },
  "husky": {
    "phonetic": "'hʌski",
    "meaning": "n. 强壮结实之人, 爱斯基摩人；a. 有壳的, 声音沙哑的, 强壮的"
  },
  "hussy": {
    "phonetic": "'hʌsi",
    "meaning": "n. 粗野女子, 轻佻女子"
  },
  "hutch": {
    "phonetic": "hʌtʃ",
    "meaning": "n. 箱, 厨, 笼, 小屋；vt. 把...装箱"
  },
  "hydra": {
    "phonetic": "'haidrә",
    "meaning": "n. 水螅, 九头蛇, 难以根除之祸害"
  },
  "hydro": {
    "phonetic": "'haidrәu",
    "meaning": "n. 水疗医院"
  },
  "hyena": {
    "phonetic": "hai'i:nә",
    "meaning": "n. 袋狼, 残酷的人, 贪婪的人"
  },
  "hymen": {
    "phonetic": "'haimen",
    "meaning": "n. 结婚, 处女膜, 许门(婚姻之神)；[医] 处女膜"
  },
  "hyped": {
    "phonetic": "",
    "meaning": "a. 兴奋的；v. 炒作（hype的过去分词）"
  },
  "hyper": {
    "phonetic": "'haipә",
    "meaning": "a. 亢奋的；高度紧张的"
  },
  "icier": {
    "phonetic": "ˈaɪsi:ə",
    "meaning": "a. 冰冷的( icy的比较级 ); 结冰的; （嗓音、态度等）冷冰冰的; 冷峻的"
  },
  "icily": {
    "phonetic": "'aisili",
    "meaning": "adv. 冷冰冰地"
  },
  "icing": {
    "phonetic": "'aisiŋ",
    "meaning": "n. 糖衣, 结冰"
  },
  "ideal": {
    "phonetic": "ai'diәl",
    "meaning": "n. 理想, 典范, 观念, 思想, 最后目标；a. 理想的, 完美的, 空想的, 观念的, 唯心论的"
  },
  "idiom": {
    "phonetic": "'idiәm",
    "meaning": "n. 习语, 成语, 惯用语法, 方言"
  },
  "idiot": {
    "phonetic": "'idiәt",
    "meaning": "n. 白痴, 极蠢之人；[医] 白痴者, 痴子"
  },
  "idled": {
    "phonetic": "ˈaidld",
    "meaning": "v. 虚度( idle的过去式和过去分词 ); 空转; 挂空挡; 未熄火"
  },
  "idler": {
    "phonetic": "'aidlә",
    "meaning": "n. 懒惰者, 游手好闲的人, 惰轮；[化] 惰轮"
  },
  "idyll": {
    "phonetic": "'idil, 'aidil",
    "meaning": "n. 叙事诗, 田园景色, 田园诗, 田园乐曲, 牧歌"
  },
  "igloo": {
    "phonetic": "'iglu:",
    "meaning": "n. 圆顶建筑"
  },
  "iliac": {
    "phonetic": "'iliæk",
    "meaning": "a. 髂骨的, 回肠的；[医] 髂的, 髂骨的"
  },
  "image": {
    "phonetic": "'imidʒ",
    "meaning": "n. 影像, 肖像, 想象, 图像, 形象, 翻版；vt. 作...的像, 反映, 想象, 象征；n. 图像；[计] 图象"
  },
  "imbed": {
    "phonetic": "im'bed",
    "meaning": "[计] 嵌入；[医] 包埋, 植入"
  },
  "imbue": {
    "phonetic": "im'bju:",
    "meaning": "vt. 使感染, 灌输, 使浸透"
  },
  "impel": {
    "phonetic": "im'pel",
    "meaning": "vt. 推动, 激励, 驱使, 迫使"
  },
  "imply": {
    "phonetic": "im'plai",
    "meaning": "vt. 暗示, 意味；[计] 隐含"
  },
  "inane": {
    "phonetic": "i'nein",
    "meaning": "a. 空虚的, 愚蠢的, 空洞的；n. 空洞乏物"
  },
  "inapt": {
    "phonetic": "in'æpt",
    "meaning": "a. 不适当的, 不熟练的"
  },
  "inbox": {
    "phonetic": "",
    "meaning": "[计] 入站"
  },
  "incur": {
    "phonetic": "in'kә:",
    "meaning": "vt. 招致, 蒙受, 遭遇；[经] 招致, 蒙受, 担负"
  },
  "index": {
    "phonetic": "'indeks",
    "meaning": "n. 索引, 指针, 指数, 指标；vt. 编入索引中, 指出；vi. 做索引；[计] 下标; 附标; 变址; 索引; 编索引"
  },
  "indie": {
    "phonetic": "'indi",
    "meaning": "n. 独立制片人, 独立制作的影(唱)片"
  },
  "inept": {
    "phonetic": "in'ept",
    "meaning": "a. 不适当的, 不理智的, 笨拙的；[法] 不称职者, 无能的, 不符要求的"
  },
  "inert": {
    "phonetic": "i'nә:t",
    "meaning": "a. 惰性的, 迟钝的, 无活力的, 呆滞的；[医] 惰性的, 无作用的, 无效的"
  },
  "infer": {
    "phonetic": "in'fә:",
    "meaning": "vt. 推论出, 推断；vi. 作推论"
  },
  "ingot": {
    "phonetic": "'iŋgәt",
    "meaning": "n. 锭, 铸块；[化] 坯料"
  },
  "inked": {
    "phonetic": "",
    "meaning": "vt. 墨水涂染（ink的过去式）"
  },
  "inlay": {
    "phonetic": "'inlei",
    "meaning": "vt. 嵌入, 镶嵌, 装帧；n. 镶嵌物, 镶嵌工艺, 镶补"
  },
  "inlet": {
    "phonetic": "'inlet",
    "meaning": "n. 进口, 插入物；[化] 入口; 进口; 投料口; 供料口"
  },
  "inner": {
    "phonetic": "'inә",
    "meaning": "a. 内部的, 内心的；n. 内部"
  },
  "input": {
    "phonetic": "'input",
    "meaning": "n. 输入, 输入电路；vt. 输入；[计] 输入"
  },
  "inset": {
    "phonetic": "'inset",
    "meaning": "vt. 嵌入；n. 插入物, 插页, 插图"
  },
  "intel": {
    "phonetic": "",
    "meaning": "n. 美国英特尔公司（财富500强公司之一, 以生产CPU芯片著称）"
  },
  "inter": {
    "phonetic": "in'tә:",
    "meaning": "vt. 埋葬；prep. 在中间"
  },
  "intro": {
    "phonetic": "'intrәu",
    "meaning": "n. 介绍；[计] 简介"
  },
  "inure": {
    "phonetic": "i'njuә",
    "meaning": "vt. 使习惯于；vi. 生效"
  },
  "ionic": {
    "phonetic": "ai'ɒnik",
    "meaning": "a. 离子的, 爱奥尼亚的, 爱奥尼亚韵律的, 爱奥尼亚式的；n. 爱奥尼亚方言"
  },
  "irate": {
    "phonetic": "'aireit",
    "meaning": "a. 发怒的, 生气的"
  },
  "irked": {
    "phonetic": "ɜ:kt",
    "meaning": "v. <正, 文>使烦恼, 激怒( irk的过去式和过去分词 )"
  },
  "irony": {
    "phonetic": "'aiәrәni",
    "meaning": "n. 反语, 讽刺, 具有讽刺意味的事"
  },
  "islet": {
    "phonetic": "'ailit",
    "meaning": "n. 小岛；[医] 岛, 小岛"
  },
  "issue": {
    "phonetic": "'isju",
    "meaning": "n. 发行, 问题, 后果, 流出, 出口, 争端；vi. 发行, 流出, 造成...结果, 传下；vt. 使流出, 放出, 发行, 发布, 发给"
  },
  "itchy": {
    "phonetic": "'itʃi",
    "meaning": "a. 渴望的, 痒的, 生疥疮的"
  },
  "ivied": {
    "phonetic": "'aivid",
    "meaning": "a. 常春藤遮盖着的"
  },
  "ivory": {
    "phonetic": "'aivәri",
    "meaning": "n. 象牙, 乳白色；a. 象牙制的, 乳白色的"
  },
  "jaded": {
    "phonetic": "'dʒeidid",
    "meaning": "a. 疲倦不堪的, 厌倦的"
  },
  "janky": {
    "phonetic": "",
    "meaning": ""
  },
  "jaunt": {
    "phonetic": "dʒɒ:nt",
    "meaning": "n. 远足, 徒步旅游；vi. 远足, 徒步旅游"
  },
  "jawed": {
    "phonetic": "dʒɔ:d",
    "meaning": "a. 有颌的, 有颚的"
  },
  "jazzy": {
    "phonetic": "'dʒæzi",
    "meaning": "a. 爵士的, 奔放的, 激烈的"
  },
  "jelly": {
    "phonetic": "'dʒeli",
    "meaning": "n. 果冻, 果冻甜食, 胶状物；v. (使)结冻, (使)成胶状"
  },
  "jerky": {
    "phonetic": "'dʒә:ki",
    "meaning": "a. 急动的, 抽筋的, 不平稳的；n. 牛肉干"
  },
  "jerry": {
    "phonetic": "'dʒeri",
    "meaning": "a. 草率的, 偷工减料的；[经] 偷工减料的, 工程粗略的"
  },
  "jetty": {
    "phonetic": "'dʒeti",
    "meaning": "n. 突堤, 防波堤, 码头；a. 黑玉般的, 乌黑发亮的；vi. 伸出"
  },
  "jewel": {
    "phonetic": "'dʒu:әl",
    "meaning": "n. 珠宝, 贵重物, 镶珠宝的饰物；vt. 饰以珠宝, 镶以宝石"
  },
  "jibed": {
    "phonetic": "dʒaɪbd",
    "meaning": "v. 与…一致( jibe的过去式和过去分词 ); （与…）相符; 相匹配"
  },
  "jiffy": {
    "phonetic": "'dʒifi",
    "meaning": "n. 瞬间"
  },
  "jihad": {
    "phonetic": "dʒi'hɑ:d",
    "meaning": "n. 讨伐异教徒, 拥护运动"
  },
  "jimmy": {
    "phonetic": "'dʒimi",
    "meaning": "n. 铁撬；vt. 撬"
  },
  "joint": {
    "phonetic": "dʒɒint",
    "meaning": "n. 连接处, 接合, 关节；a. 共同的, 联合的, 连接的, 合办的；vt. 连接, 接合, 使有接头；vi. 贴合, 长节"
  },
  "joist": {
    "phonetic": "dʒɒist",
    "meaning": "n. 托梁, 桁"
  },
  "joked": {
    "phonetic": "dʒəukt",
    "meaning": "v. 开玩笑( joke的过去式和过去分词 ); 戏弄; 闹着玩; 说着玩"
  },
  "joker": {
    "phonetic": "'dʒәukә",
    "meaning": "n. 诙谐者, 家伙, 巧计；[法] 曲笔"
  },
  "jokey": {
    "phonetic": "'dʒәjki",
    "meaning": "a. 好开玩笑的, 滑稽的"
  },
  "jolly": {
    "phonetic": "'dʒɒli",
    "meaning": "a. 愉快的, 高兴的, 宜人的；vt. 恭维, 使高兴, 取笑；vi. 开玩笑；adv. 非常, 极为"
  },
  "joule": {
    "phonetic": "dʒaul",
    "meaning": "n. 焦耳；[化] 焦耳"
  },
  "joust": {
    "phonetic": "dʒaust",
    "meaning": "n. 马背长矛打斗, 格斗；vi. 进行马上长矛比武"
  },
  "jowly": {
    "phonetic": "'dʒajli",
    "meaning": "a. 下颚宽厚的, 有双下巴的"
  },
  "judge": {
    "phonetic": "dʒʌdʒ",
    "meaning": "n. 法官, 裁判员, 审判官, 鉴定人；vt. 审理, 鉴定, 判断, 判决, 裁定；vi. 下判断, 作评价"
  },
  "juice": {
    "phonetic": "dʒu:s",
    "meaning": "n. 汁, 活力, 体液；vt. 挤出汁来, 加汁"
  },
  "juicy": {
    "phonetic": "'dʒusi",
    "meaning": "a. 多汁液的, 生动的, 多水分的"
  },
  "julep": {
    "phonetic": "'dʒu:lep",
    "meaning": "[医] 甜酒, 甜香酒"
  },
  "jumbo": {
    "phonetic": "'dʒʌmbәu",
    "meaning": "n. 庞然大物；a. 巨大的"
  },
  "jumpy": {
    "phonetic": "'dʒʌmpi",
    "meaning": "a. 跳跃的, 跳动的, 神经质的"
  },
  "junky": {
    "phonetic": "'dʒʌŋki",
    "meaning": "n. 吸海洛因成瘾者, 吸毒的人, 毒品贩子, 废旧品商人"
  },
  "junta": {
    "phonetic": "'dʒʌntә",
    "meaning": "n. 以武力政变上台的(军)政府, 私党, 阴谋小集团, 政务会"
  },
  "junto": {
    "phonetic": "'dʒʌntәu",
    "meaning": "n. 私党, 秘密结社, 阴谋团体"
  },
  "juror": {
    "phonetic": "'dʒuәrә",
    "meaning": "n. 陪审员, 审查委员；[法] 陪审员, 陪审官, 宣誓者"
  },
  "kabob": {
    "phonetic": "kә'bɒb",
    "meaning": "n. 烤肉串"
  },
  "kappa": {
    "phonetic": "'kæpә",
    "meaning": "n. 希腊文第十个字母(K)"
  },
  "kaput": {
    "phonetic": "kә'pu:t",
    "meaning": "a. 完蛋了的, 彻底失败了的, 坏了的, 过时了的"
  },
  "karat": {
    "phonetic": "'kærәt",
    "meaning": "n. 开(金等贵金属单位)"
  },
  "karma": {
    "phonetic": "'kɑ:mә",
    "meaning": "n. 因果报应, 命运"
  },
  "kayak": {
    "phonetic": "'kaiæk",
    "meaning": "n. 爱斯基摩人划子"
  },
  "kazoo": {
    "phonetic": "kә'zu:",
    "meaning": "n. 卡祖笛"
  },
  "kebab": {
    "phonetic": "kә'bɑ:b",
    "meaning": "n. 烤肉串配蔬菜"
  },
  "kempt": {
    "phonetic": "kempt",
    "meaning": "a. 收拾得很整洁的"
  },
  "keyed": {
    "phonetic": "ki:d",
    "meaning": "a. 锁着的, 用拱顶石连住的, 乐器有键的, 已调节音调的, 已被定于某调的；[计] 键的"
  },
  "khaki": {
    "phonetic": "'kɑ:ki",
    "meaning": "a. 卡其色的, 土黄色的；n. 卡其色, 卡其色军服"
  },
  "kiddo": {
    "phonetic": "'kidәu",
    "meaning": "n. 老兄, 老姐"
  },
  "kinda": {
    "phonetic": "'kaindә",
    "meaning": "adv. 有几分；有一点"
  },
  "kinky": {
    "phonetic": "'kiŋki",
    "meaning": "a. 弯曲的, 古怪的"
  },
  "kiosk": {
    "phonetic": "ki'ɒsk",
    "meaning": "n. 亭, 凉亭, 报摊"
  },
  "kissy": {
    "phonetic": "'kisi",
    "meaning": "a. 想要接吻的"
  },
  "kitty": {
    "phonetic": "'kiti",
    "meaning": "n. 小猫, 全部赌注"
  },
  "klutz": {
    "phonetic": "klʌts",
    "meaning": "n. 笨手笨脚的人, 笨蛋"
  },
  "knack": {
    "phonetic": "næk",
    "meaning": "n. 熟练技术, 巧妙手法, 诀窍；[化] 窍门"
  },
  "knave": {
    "phonetic": "neiv",
    "meaning": "n. 恶棍, 骗徒, (纸牌的)杰克；[法] 流氓行为, 无赖, 恶棍"
  },
  "knead": {
    "phonetic": "ni:d",
    "meaning": "vt. 揉, 按摩, 捏；[机] 揉合"
  },
  "kneed": {
    "phonetic": "ni:d",
    "meaning": "a. 有膝一般的关节的, 有节的"
  },
  "kneel": {
    "phonetic": "ni:l",
    "meaning": "vi. 跪下"
  },
  "knell": {
    "phonetic": "nel",
    "meaning": "n. 丧钟声, 哀伤的声音, 凶兆；v. 鸣丧钟"
  },
  "knelt": {
    "phonetic": "nelt",
    "meaning": "v. 跪下（kneel的过去式）"
  },
  "knife": {
    "phonetic": "naif",
    "meaning": "n. 小刀, 匕首；vt. 切割, 伤害, 切, 戳；vi. 劈开, 穿过"
  },
  "knish": {
    "phonetic": "kniʃ",
    "meaning": "n. 以肉、乳酪、水果馅炸饼"
  },
  "knock": {
    "phonetic": "nɒk",
    "meaning": "n. 敲, 敲打, 敲门；v. 敲击, 互撞, 攻击"
  },
  "knoll": {
    "phonetic": "nәul",
    "meaning": "n. 小山, 圆丘；vt. 敲钟；vi. 敲响"
  },
  "known": {
    "phonetic": "nәun",
    "meaning": "a. 已知的, 有名的；know的过去分词"
  },
  "koala": {
    "phonetic": "kә'ɑ:lә",
    "meaning": "n. 袋熊"
  },
  "kooky": {
    "phonetic": "'ku:ki",
    "meaning": "a. 古怪的, 乖僻的, 疯狂的, 讨厌的"
  },
  "koran": {
    "phonetic": "kɒ'rɑ:n",
    "meaning": "n. <<可兰经>>"
  },
  "krill": {
    "phonetic": "kril",
    "meaning": "n. [动]磷虾"
  },
  "kudos": {
    "phonetic": "'kju:dɒs",
    "meaning": "n. 称赞, 光荣, 荣誉"
  },
  "kudzu": {
    "phonetic": "'kædzu:",
    "meaning": "n. 野葛"
  },
  "kugel": {
    "phonetic": "",
    "meaning": "n. 一种烤制的布丁; 形状类似面条; 由土豆、鸡蛋和调味类做成的传统食品; （姓氏）库高"
  },
  "kvell": {
    "phonetic": "kvel",
    "meaning": "vi.<美俚>吹牛, 扬扬得意"
  },
  "label": {
    "phonetic": "'leibl",
    "meaning": "n. 标签, 称号, 商标, 标志；vt. 贴标签于, 标注；[计] 标志; 标注; DOS外部命令:用于建立改变或删除磁盘卷标号"
  },
  "labor": {
    "phonetic": "'leibә",
    "meaning": "n. 劳动, 努力, 工作, 劳工, 分娩；vi. 劳动, 努力, 苦干；vt. 详细分析, 使厌烦"
  },
  "laced": {
    "phonetic": "leist",
    "meaning": "a. 用带子束紧了的, 饰有花边的"
  },
  "lacey": {
    "phonetic": "'leisi",
    "meaning": "a. 花边的"
  },
  "laden": {
    "phonetic": "'leidn",
    "meaning": "a. 装满的, 负载的, 苦恼的；lade的过去分词"
  },
  "ladle": {
    "phonetic": "'leidl",
    "meaning": "n. 勺子, 长柄勺；vt. 以勺舀取, 以勺掬, 不分对象予以赠送"
  },
  "lager": {
    "phonetic": "'lɑ:gә",
    "meaning": "n. 贮陈啤酒"
  },
  "laity": {
    "phonetic": "'leiәti",
    "meaning": "n. 俗人, 外行；[医] 外行[人]"
  },
  "lamed": {
    "phonetic": "'lɑ:med",
    "meaning": "n. 希伯莱语中的第十二个字母"
  },
  "lamer": {
    "phonetic": "leimə",
    "meaning": "a. 瘸的( lame的比较级 ); 站不住脚的; 差劲的; 蹩脚的"
  },
  "lance": {
    "phonetic": "lɑ:ns",
    "meaning": "n. 长矛, 柳叶刀, 执矛战士；vt. 以长矛攻击, 冲进；vi. 急进"
  },
  "lanky": {
    "phonetic": "'læŋki",
    "meaning": "a. 瘦长的"
  },
  "lapel": {
    "phonetic": "lә'pel",
    "meaning": "n. 翻领"
  },
  "lapse": {
    "phonetic": "læps",
    "meaning": "n. 过失, 流逝, 失效；vi. 犯错, 堕落, 减退, 消失, 流逝；vt. 使失效"
  },
  "larch": {
    "phonetic": "lɑ:tʃ",
    "meaning": "n. 落叶松属植物；[医] 落叶松"
  },
  "large": {
    "phonetic": "lɑ:dʒ",
    "meaning": "a. 大的, 大量的, 宽大的, 广博的；adv. 大大地, 夸大地"
  },
  "larva": {
    "phonetic": "'lɑ:vә",
    "meaning": "n. 幼虫；[医] 幼虫(昆虫), 蚴(蠕虫)"
  },
  "laser": {
    "phonetic": "'leizә",
    "meaning": "n. 激光；[计] 激光器"
  },
  "lasso": {
    "phonetic": "'læsәu",
    "meaning": "n. 套索, 以套索捕；vt. 以套索捕"
  },
  "latch": {
    "phonetic": "lætʃ",
    "meaning": "n. 门闩；vi. 上闩, 抓住, 占有；vt. 闩上；[计] 门闩线路; 锁存器"
  },
  "later": {
    "phonetic": "'leitә",
    "meaning": "adv. 以后, 随后"
  },
  "latex": {
    "phonetic": "'leiteks",
    "meaning": "n. 乳液, 胶乳；[化] 胶乳"
  },
  "lathe": {
    "phonetic": "leið",
    "meaning": "n. 车床；vt. 用车床加工"
  },
  "latke": {
    "phonetic": "'lɑ:tki",
    "meaning": "n. 马铃薯饼,土豆烙饼"
  },
  "latte": {
    "phonetic": "ˈlɑ:teɪ",
    "meaning": "n. 拿铁咖啡; （意大利语）牛奶"
  },
  "laugh": {
    "phonetic": "lɑ:f",
    "meaning": "n. 笑, 笑声；vi. 笑, 大笑；vt. 以笑表示"
  },
  "laved": {
    "phonetic": "leɪvd",
    "meaning": "v. <文> 洗涤( lave的过去式和过去分词 ); 给…沐浴; （水）冲刷; 沿…流淌"
  },
  "layer": {
    "phonetic": "'leiә",
    "meaning": "n. 层, 产卵鸡, 放置者；vt. 分层堆积, 压植；[计] 层"
  },
  "layup": {
    "phonetic": "'leiʌp",
    "meaning": "接头[合]处"
  },
  "lazed": {
    "phonetic": "leɪzd",
    "meaning": "v. 混日子( laze的过去式和过去分词 ); 懒散; 闲散; 闲散地打发时间"
  },
  "leach": {
    "phonetic": "li:tʃ",
    "meaning": "vt. 过滤, 萃取；vi. 滤掉；n. 过滤, 过滤器, 沥出物"
  },
  "leafy": {
    "phonetic": "'li:fi",
    "meaning": "a. 叶茂盛的, 多叶的, 叶状的"
  },
  "leaky": {
    "phonetic": "'li:ki",
    "meaning": "a. 有漏洞的, 易泄漏秘密的, 爱哭的；[电] 漏的"
  },
  "leant": {
    "phonetic": "lent",
    "meaning": "lean的过去式和过去分词"
  },
  "leapt": {
    "phonetic": "lept",
    "meaning": "leap的过去式和过去分词"
  },
  "learn": {
    "phonetic": "lә:n",
    "meaning": "vt. 学习；认识到；得知"
  },
  "lease": {
    "phonetic": "li:s",
    "meaning": "n. 租约, 租期, 租；vt. 出租, 租出, 租得"
  },
  "leash": {
    "phonetic": "li:ʃ",
    "meaning": "n. (拴狗颈的)皮带；vt. 以皮带束缚, 束缚"
  },
  "least": {
    "phonetic": "li:st",
    "meaning": "n. 最少, 最小, 最小限度；a. 最少的, 最小的；adv. 最小, 最少"
  },
  "leave": {
    "phonetic": "li:v",
    "meaning": "n. 许可, 告别, 请假, 休假；vt. 离开, 剩下, 遗忘, 委托, 丢弃；vi. 出发, 离开, 生叶"
  },
  "ledge": {
    "phonetic": "ledʒ",
    "meaning": "n. 突出部分, 暗礁, 矿层"
  },
  "leech": {
    "phonetic": "li:tʃ",
    "meaning": "n. 水蛭, 吸血鬼, 榨取他人利益的人；vt. 以水蛭吸血；vi. 依附并榨取别人"
  },
  "leery": {
    "phonetic": "'liәri",
    "meaning": "a. 机敏的, 猜疑的, 狡猾的"
  },
  "lefty": {
    "phonetic": "'lefti",
    "meaning": "n. 左撇子, 左翼分子"
  },
  "legal": {
    "phonetic": "'li:gәl",
    "meaning": "a. 法律的, 法定的, 合法的；[经] 法定权利; 法律(上)的, 合法的"
  },
  "leggy": {
    "phonetic": "'legi",
    "meaning": "a. 长腿的, 腿细长的, 茎长的"
  },
  "legit": {
    "phonetic": "l ә'dʒit",
    "meaning": "a. 合法的, 正统的, 守法的"
  },
  "lemma": {
    "phonetic": "'lemә",
    "meaning": "n. 辅助定理, 论点, 引理；[医] 膜, 衣"
  },
  "lemon": {
    "phonetic": "'lemәn",
    "meaning": "n. 柠檬, 柠檬树, 柠檬色；[医] 柠檬"
  },
  "lemur": {
    "phonetic": "'li:mә",
    "meaning": "n. 狐猴"
  },
  "leper": {
    "phonetic": "'lepә",
    "meaning": "n. 麻疯病患者, 受蔑视的人；[医] 麻风病人"
  },
  "letup": {
    "phonetic": "'letʌp",
    "meaning": "n. 停止, 中止, 放松"
  },
  "levee": {
    "phonetic": "'levi",
    "meaning": "n. 早朝, 大堤；vt. 为...筑堤"
  },
  "level": {
    "phonetic": "'levl",
    "meaning": "n. 水平, 水准, 平地；a. 同高的, 平坦的, 齐平的, 水平的；vt. 弄平, 夷平, 使同等, 瞄准, 对准；vi. 变平, 拉平；[计] 级别"
  },
  "lever": {
    "phonetic": "'levә",
    "meaning": "n. 杠杆, 似杠杆之工具；vt. 撬开；vi. 使用杠杆"
  },
  "lexis": {
    "phonetic": "'leksәs",
    "meaning": "n. 词, 词汇"
  },
  "libel": {
    "phonetic": "'laibәl",
    "meaning": "n. 以文字损害名誉, 诽谤罪, 侮辱；v. 诽谤, 中伤, 损害名誉"
  },
  "liege": {
    "phonetic": "li:dʒ",
    "meaning": "n. 君主, 王侯, 臣下；a. 君主的, 臣下的, 君臣关系的"
  },
  "lifer": {
    "phonetic": "'laifә",
    "meaning": "n. 无期徒刑者, 职业军人；[法] 无期徒刑犯"
  },
  "light": {
    "phonetic": "lait",
    "meaning": "n. 光, 光亮, 灯, 日光, 发光体, 光源, 杰出人物, 火花, 眼光；a. 轻的, 少量的, 轻微的, 轻快的, 轻浮的, 明亮的, 淡色的, 容易的；vt. 点燃, 照亮；vi. 点着, 变亮, 突降, 偶然碰到；adv. 轻地"
  },
  "liked": {
    "phonetic": "",
    "meaning": "v. 喜欢（like的过去式）"
  },
  "liken": {
    "phonetic": "'laikәn",
    "meaning": "vt. 比喻, 比拟"
  },
  "lilac": {
    "phonetic": "'lailәk",
    "meaning": "n. 丁香, 丁香花, 淡紫色；a. 淡紫色的"
  },
  "limbo": {
    "phonetic": "'limbәu",
    "meaning": "n. 地狱边缘, 监狱, 忘却；[法] 监狱, 拘禁, 忘却"
  },
  "limey": {
    "phonetic": "'laimi",
    "meaning": "n. 英国海军, 英国人"
  },
  "limit": {
    "phonetic": "'limit",
    "meaning": "n. 界限, 边界, 限度, 极限, 限制；vt. 限制, 限定"
  },
  "lined": {
    "phonetic": "laind",
    "meaning": "a. 有内衬的；具线纹的"
  },
  "linen": {
    "phonetic": "'linin",
    "meaning": "n. 亚麻布, 亚麻线, 亚麻制品；a. 亚麻布制的, 亚麻的"
  },
  "liner": {
    "phonetic": "'lainә",
    "meaning": "n. 班机, 划线者, 定期船, 衬里；[化] 衬垫; 垫带; 套管"
  },
  "lingo": {
    "phonetic": "'liŋgәu",
    "meaning": "n. 外国话, 隐语；[经] 行话, 航业暗语"
  },
  "lipid": {
    "phonetic": "'lipid, 'laipid",
    "meaning": "n. 脂类, 类脂物, 脂质；[化] 类脂; 脂质; 脂类"
  },
  "lippy": {
    "phonetic": "'lipi",
    "meaning": "a. 爱顶嘴的, 无礼的"
  },
  "liter": {
    "phonetic": "'li:tә",
    "meaning": "n. 公升；[化] 升"
  },
  "lithe": {
    "phonetic": "laið",
    "meaning": "a. 柔软的"
  },
  "litre": {
    "phonetic": "li:tә(r)",
    "meaning": "n. 升, 公升；[计] 升"
  },
  "lived": {
    "phonetic": "livd. 'laivd",
    "meaning": "a. 有生命的"
  },
  "liven": {
    "phonetic": "'laivәn",
    "meaning": "vt. 使高兴, 使快活；vi. 快活起来"
  },
  "liver": {
    "phonetic": "'livә",
    "meaning": "n. 肝脏, 生活者, 居民；[医] 肝"
  },
  "livid": {
    "phonetic": "'livid",
    "meaning": "a. 铁青的；[医] 青紫的"
  },
  "llama": {
    "phonetic": "'lɑ:mә",
    "meaning": "n. 美洲驼"
  },
  "loamy": {
    "phonetic": "'lәumi",
    "meaning": "a. 壤土(似)的"
  },
  "loath": {
    "phonetic": "lәuθ",
    "meaning": "a. 不情愿的, 厌恶的"
  },
  "lobby": {
    "phonetic": "'lɒbi",
    "meaning": "n. 大厅, 休息室, 游说议员者；vi. 游说议员, 游说；vt. 游说"
  },
  "lobed": {
    "phonetic": "lәubd",
    "meaning": "a. 分裂的, 有叶的"
  },
  "local": {
    "phonetic": "'lәukәl",
    "meaning": "a. 地方性的, 当地的, 局部的, 乡土的, 本地的；n. 当地居民, 本地新闻, 局部；[计] 本地的; 局部"
  },
  "locus": {
    "phonetic": "'lәukәs",
    "meaning": "n. 轨迹；地点, 所在地"
  },
  "lodge": {
    "phonetic": "lɒdʒ",
    "meaning": "n. 小屋, 门房, 支部, 旅舍, 分会；vi. 临时住宿, 倒伏, 寄宿, 投宿；vt. 安顿, 容纳, 提出, 把...射入, 存放"
  },
  "loess": {
    "phonetic": "'lәuis",
    "meaning": "n. 黄土"
  },
  "lofty": {
    "phonetic": "'lɒfti",
    "meaning": "a. 高的, 傲慢的, 崇高的, 高级的, 玄虚的"
  },
  "logic": {
    "phonetic": "'lɒdʒik",
    "meaning": "n. 逻辑, 逻辑学, 推理的方法, 推理, 逻辑性；[计] 逻辑"
  },
  "login": {
    "phonetic": "",
    "meaning": "[计] 注册(程序), 登记, 用户注册程序"
  },
  "logon": {
    "phonetic": "'lәugәn",
    "meaning": "n. [电脑]注册, 进入系统"
  },
  "lolly": {
    "phonetic": "'lɔli",
    "meaning": "n. 棒糖, 硬糖, 类似棒糖的东西, 冰棍"
  },
  "loner": {
    "phonetic": "'lәunә",
    "meaning": "n. 喜孤独的人, 不合群的动物"
  },
  "loony": {
    "phonetic": "'lu:ni",
    "meaning": "a. 发狂的, 极蠢的；n. 疯子"
  },
  "loopy": {
    "phonetic": "'lu:pi",
    "meaning": "a. 多圈的, 呆头呆脑的, 糊涂的"
  },
  "loose": {
    "phonetic": "lu:s",
    "meaning": "n. 发射, 放任, 放纵；a. 宽松的, 松的, 宽的, 不牢固的, 散漫的, 自由的, 不精确的；vt. 释放, 放枪, 开船；vi. 变松, 开火；adv. 松散地"
  },
  "loped": {
    "phonetic": "ləʊpt",
    "meaning": "v. （尤指动物）轻跳着奔跑( lope的过去式和过去分词 )"
  },
  "lordy": {
    "phonetic": "'lɔ:di",
    "meaning": "int. （表示惊讶等）老天爷"
  },
  "lorry": {
    "phonetic": "'lɒri",
    "meaning": "n. 卡车, 货车；[化] 载重汽车"
  },
  "loser": {
    "phonetic": "'lu:zә",
    "meaning": "n. 失败者, 遗失者；[法] 失败者, 失物者, 遗失者"
  },
  "lotto": {
    "phonetic": "'lɒtәu",
    "meaning": "n. 抽数码游戏"
  },
  "lotus": {
    "phonetic": "'lәjtәs",
    "meaning": "n. 莲, 莲花, 荷花, 荷；[电] LOTUS, 莲花公司"
  },
  "louse": {
    "phonetic": "laus",
    "meaning": "n. 虱子, 寄生虫；[医] 虱"
  },
  "lousy": {
    "phonetic": "'lauzi",
    "meaning": "a. 污秽的, 恶心的, 生虱的"
  },
  "loved": {
    "phonetic": "lʌvd",
    "meaning": "v. 热爱（love的过去分词）"
  },
  "lover": {
    "phonetic": "'lʌvә",
    "meaning": "n. 爱人, 爱好者"
  },
  "lower": {
    "phonetic": "'lәuә",
    "meaning": "a. 低的, 下级的, 下层的；vi. 降低, 跌落, 减弱；vt. 放下, 降下, 减弱, 贬低"
  },
  "lowly": {
    "phonetic": "'lәuli",
    "meaning": "a. 地位低的, 卑下的, 谦卑的；adv. 位置低下的, 低声地, 谦逊地"
  },
  "loyal": {
    "phonetic": "'lɒiәl",
    "meaning": "a. 忠诚的, 忠实的, 忠贞的"
  },
  "lubed": {
    "phonetic": "",
    "meaning": "abbr. lubricated 喝醉了的"
  },
  "lucid": {
    "phonetic": "'lu:sid",
    "meaning": "a. 明晰的, 清澈的, 透明的, 透彻的；[医] 清明的, 透明的, 清醒的"
  },
  "lucky": {
    "phonetic": "'lʌki",
    "meaning": "a. 幸运的, 吉祥的, 好运的, 侥幸的"
  },
  "lucre": {
    "phonetic": "'lu:kә",
    "meaning": "n. 收益, 钱财"
  },
  "luger": {
    "phonetic": "'lu:^ә",
    "meaning": "[德]鲁格尔(德国造半自动手枪的商标名), [luger ]鲁格尔手枪"
  },
  "lumen": {
    "phonetic": "'lu:min",
    "meaning": "n. 流明, 腔；[医] 腔, 流明(光通单位)"
  },
  "lumpy": {
    "phonetic": "'lʌmpi",
    "meaning": "a. 多瘤的, 波浪起伏的, 粗笨的"
  },
  "lunar": {
    "phonetic": "'lu:nә",
    "meaning": "a. 阴历的, 月的, 微亮的(指光)；[医] 月的, 银的"
  },
  "lunch": {
    "phonetic": "lʌntʃ",
    "meaning": "n. 午餐"
  },
  "lunge": {
    "phonetic": "lʌndʒ",
    "meaning": "n. 刺, 刺进, 跃进, 套马索；v. 突进, 刺"
  },
  "lupus": {
    "phonetic": "'lu:pәs",
    "meaning": "n. 狼疮, 豺狼座；[医] 狼疮"
  },
  "lurch": {
    "phonetic": "lә:tʃ",
    "meaning": "n. 惨败, 倾斜, 挫折, 举步蹒跚, 徘徊；vi. 惨败, 倾斜, 徘徊；vt. 击败"
  },
  "lured": {
    "phonetic": "",
    "meaning": "vt. 吸引, 引诱（lure的过去式与过去分词形式）"
  },
  "lurid": {
    "phonetic": "'luәrid",
    "meaning": "a. 火烧似的, 苍白的, 华丽的, 可怕的"
  },
  "lusty": {
    "phonetic": "'lʌsti",
    "meaning": "a. 健壮的, 精力充沛的"
  },
  "luted": {
    "phonetic": "luːt; ljuːt",
    "meaning": "n. 琵琶；vi. 弹诗琴；vt. 弹诗琴表达；用封泥封；n. (Lute)人名；(塞)卢特"
  },
  "lying": {
    "phonetic": "'laiiŋ",
    "meaning": "n. 说谎；a. 横躺的, 说谎的"
  },
  "lymph": {
    "phonetic": "limf",
    "meaning": "n. 淋巴；[医] 淋巴, 浆, 苗"
  },
  "lyric": {
    "phonetic": "'lirik",
    "meaning": "n. 抒情诗, 歌词；a. 抒情的"
  },
  "macaw": {
    "phonetic": "mә'kɒ:",
    "meaning": "n. 金刚鹦鹉, 芳香核果棕榈"
  },
  "macho": {
    "phonetic": "'mɑ:tʃәu",
    "meaning": "[医] 结节型皮肤利什曼病"
  },
  "macro": {
    "phonetic": "'mækrәu",
    "meaning": "pref. 宏；a. 巨大的, 大量的；[计] 宏"
  },
  "madam": {
    "phonetic": "'mædәm",
    "meaning": "n. 女士, 夫人"
  },
  "madly": {
    "phonetic": "'mædli",
    "meaning": "adv. 发狂地, 精神失常地, 愚蠢地"
  },
  "mafia": {
    "phonetic": "'mæfiә",
    "meaning": "n. 黑手党, 秘密政党"
  },
  "magic": {
    "phonetic": "'mædʒik",
    "meaning": "n. 魔术, 魔法；a. 魔术的, 有魔力的, 不可思议的"
  },
  "magma": {
    "phonetic": "'mægmә",
    "meaning": "n. 岩浆, 糊剂, 乳浆剂；[化] 晶浆"
  },
  "maize": {
    "phonetic": "meiz",
    "meaning": "n. 玉蜀黍, 黄色；a. 玉蜀黍色的, 黄色的"
  },
  "major": {
    "phonetic": "'meidʒә",
    "meaning": "n. 主修课, 成年人, 陆军少校；a. 主要的, 较多的, 大部分的, 成年的, 严重的；vi. 主修；[计] 主要, 主要刻度"
  },
  "maker": {
    "phonetic": "'meikә",
    "meaning": "n. 制造者, 上帝；[经] 制造者, 出票人"
  },
  "malty": {
    "phonetic": "'mɒ:lti",
    "meaning": "a. 麦芽的, 有麦芽的, 喝醉的"
  },
  "mamba": {
    "phonetic": "'mɑ:mbә",
    "meaning": "n. 树眼镜蛇；[医] 窄头眼镜蛇(南非产)"
  },
  "mambo": {
    "phonetic": "'mɑ:mbәu",
    "meaning": "n. 曼博舞, 曼博音乐；vi. 跳曼博舞"
  },
  "mamma": {
    "phonetic": "'mɑ:mә",
    "meaning": "n. 妈妈, 乳房；[医] 乳房"
  },
  "manga": {
    "phonetic": "'mæŋɡә",
    "meaning": "n. 日本漫画"
  },
  "mange": {
    "phonetic": "'meindʒ",
    "meaning": "n. 兽疥癣；[医] 兽疥癣"
  },
  "mango": {
    "phonetic": "'mæŋgәu",
    "meaning": "n. 芒果；[化] 芒果Mangifera indica"
  },
  "mangy": {
    "phonetic": "'meindʒi",
    "meaning": "a. 疥癣的, 污秽的"
  },
  "mania": {
    "phonetic": "'meiniә",
    "meaning": "n. 狂躁, 热衷, 狂热；[医] 躁狂, 狂"
  },
  "manic": {
    "phonetic": "'meinik",
    "meaning": "a. 躁狂的；n. 躁狂者"
  },
  "manly": {
    "phonetic": "'mænli",
    "meaning": "a. 象男人的, 强壮的, 适于男人的"
  },
  "manna": {
    "phonetic": "'mænә",
    "meaning": "n. 吗哪天赐食物, 精神食粮, 甘露；[医] 甘露, 木蜜"
  },
  "manor": {
    "phonetic": "'mænә",
    "meaning": "n. 庄园；[法] 采邑, 庄园, 采地"
  },
  "manse": {
    "phonetic": "mæns",
    "meaning": "n. 牧师住宅"
  },
  "maple": {
    "phonetic": "'meipl",
    "meaning": "n. 枫, 枫木, 淡棕色；[机] 枫木"
  },
  "march": {
    "phonetic": "mɑ:tʃ",
    "meaning": "n. 三月, 进行, 行军, 步伐, 长途跋涉, 进行曲, 边界；vi. 进军, 前进, 交界；vt. 使行军, 使行进"
  },
  "marry": {
    "phonetic": "'mæri",
    "meaning": "vt. 与...结婚, 娶, 嫁；vi. 结婚"
  },
  "marsh": {
    "phonetic": "mɑ:ʃ",
    "meaning": "n. 沼泽, 湿地；a. 沼泽的"
  },
  "mason": {
    "phonetic": "meisn",
    "meaning": "n. 泥瓦匠, 共济会会员；vt. 用砖瓦砌成"
  },
  "masse": {
    "phonetic": "mæ'sei",
    "meaning": "[体]竖直挫球"
  },
  "match": {
    "phonetic": "mætʃ",
    "meaning": "n. 比赛, 火柴, 对手；vt. 使相配, 使比赛, 与...竞争；vi. 结婚, 相配；[计] 比较"
  },
  "mated": {
    "phonetic": "",
    "meaning": "成双的；成对的"
  },
  "matey": {
    "phonetic": "'meiti",
    "meaning": "a. 易为人亲近的, 融洽的；n. 伙伴, 朋友"
  },
  "matte": {
    "phonetic": "mæt",
    "meaning": "a. 表面粗糙的；n. 无光粗糙层, 冰铜"
  },
  "matzo": {
    "phonetic": "'mɑ:tsәu",
    "meaning": "(pl. matzot, matzoth, matzos)(=matsah)犹太逾越节薄饼(逾越节期间犹太人所吃的一种不发酵的硬面饼)"
  },
  "mauve": {
    "phonetic": "mәuv",
    "meaning": "n. 苯胺紫, 淡紫色；a. 淡紫色的"
  },
  "maven": {
    "phonetic": "'meivin",
    "meaning": "n. 内行, 专家"
  },
  "maxim": {
    "phonetic": "'mæksim",
    "meaning": "n. 格言, 座右铭；[法] 格言, 准则, 原则"
  },
  "maybe": {
    "phonetic": "'meibi:",
    "meaning": "adv. 也许, 大概；n. 可能性"
  },
  "mayor": {
    "phonetic": "'mєә",
    "meaning": "n. 市长；[法] 市长"
  },
  "mealy": {
    "phonetic": "'mi:li",
    "meaning": "a. 粉状的"
  },
  "meant": {
    "phonetic": "ment",
    "meaning": "mean的过去式和过去分词"
  },
  "meaty": {
    "phonetic": "'mi:ti",
    "meaning": "a. 肉的, 似肉的, 多肉的"
  },
  "mecca": {
    "phonetic": "'mekә",
    "meaning": "n. 麦加"
  },
  "medal": {
    "phonetic": "'medl",
    "meaning": "n. 奖牌, 勋章；vt. 授勋予"
  },
  "media": {
    "phonetic": "'mi:diә",
    "meaning": "n. 媒体；[计] 媒质"
  },
  "medic": {
    "phonetic": "'medik",
    "meaning": "n. 苜蓿属植物, 医师, 医科学生"
  },
  "melee": {
    "phonetic": "me'lei",
    "meaning": "n. 互殴, 激烈的论战, 混战"
  },
  "melon": {
    "phonetic": "'melәn",
    "meaning": "n. 瓜, 甜瓜, 红利, 赃物；[化] 三聚二氰亚胺"
  },
  "mensa": {
    "phonetic": "'mensә",
    "meaning": "[医] Ж面"
  },
  "mercy": {
    "phonetic": "'mә:si",
    "meaning": "n. 仁慈, 宽恕, 慈悲, 怜悯, 幸运；[法] 权宜处置权, 决定权, 宽恕"
  },
  "merge": {
    "phonetic": "mә:dʒ",
    "meaning": "vt. 使合并, 使消失, 吞没；vi. 合并, 渐渐消失；[计] 合并"
  },
  "merit": {
    "phonetic": "'merit",
    "meaning": "n. 优点, 功绩, 价值, 功过, 真相；vt. 值得；vi. 应受"
  },
  "merry": {
    "phonetic": "'meri",
    "meaning": "a. 快乐的, 愉快的, 嬉戏作乐的"
  },
  "meshy": {
    "phonetic": "'meʃi",
    "meaning": "a. 网状的, 象网的"
  },
  "messy": {
    "phonetic": "'mesi",
    "meaning": "a. 散乱的, 污秽的, 麻烦的"
  },
  "metal": {
    "phonetic": "'metәl",
    "meaning": "n. 金属, 金属制品, 合金, 本质, 质料；a. 金属制的；vt. 以金属覆盖"
  },
  "meted": {
    "phonetic": "mi:tid",
    "meaning": "v. <正, 文>（对某人）施以, 给予（处罚等）( mete的过去式和过去分词 )"
  },
  "meter": {
    "phonetic": "'mi:tә",
    "meaning": "n. 米, 公尺, 仪表, 计量器；vt. 以仪表计量"
  },
  "metre": {
    "phonetic": "'mi:tә",
    "meaning": "n. 公尺, 格律, 韵律；[医] 米, 公尺"
  },
  "metro": {
    "phonetic": "'metrәu",
    "meaning": "n. 地铁"
  },
  "mewed": {
    "phonetic": "mju:d",
    "meaning": "v. 作猫或海鸟叫, 咪咪叫( mew的过去式和过去分词 )"
  },
  "mezzo": {
    "phonetic": "'metsәu. 'meddzɔ:",
    "meaning": "a. （意）一半的；中央的"
  },
  "miasm": {
    "phonetic": "",
    "meaning": "[医] 瘴毒, 瘴气"
  },
  "micro": {
    "phonetic": "",
    "meaning": "[计] 表示\"小\",\"微\",\"微量\",\"百分之一\""
  },
  "midge": {
    "phonetic": "midʒ",
    "meaning": "n. 蠓, 侏儒；[医] 蠓, 蚋"
  },
  "midst": {
    "phonetic": "midst",
    "meaning": "n. 中间；prep. 在...中间"
  },
  "might": {
    "phonetic": "mait",
    "meaning": "n. 力量, 权力；aux. 可能, 也许"
  },
  "miked": {
    "phonetic": "",
    "meaning": "vt. 通过话筒传送（mike的过去式与过去分词形式）"
  },
  "miler": {
    "phonetic": "'mailә",
    "meaning": "n. 一英里跑运动员"
  },
  "milky": {
    "phonetic": "'milki",
    "meaning": "a. 乳状的, 乳白色的, 柔和的"
  },
  "mimed": {
    "phonetic": "'maɪmd",
    "meaning": "v. 指手画脚地表演, 用哑剧的形式表演( mime的过去式和过去分词 )"
  },
  "mimic": {
    "phonetic": "'mimik",
    "meaning": "a. 模仿的, 摹拟的；n. 效颦者, 模仿者, 小丑, 仿制品；vt. 模仿, 摹拟"
  },
  "mince": {
    "phonetic": "mins",
    "meaning": "n. 切碎物；vt. 切碎, 矫揉做作地说；vi. 碎步走, 装腔作势"
  },
  "mined": {
    "phonetic": "",
    "meaning": "n. 开采"
  },
  "miner": {
    "phonetic": "'mainә",
    "meaning": "n. 矿工, 开矿机, 坑道工兵；[经] 矿工"
  },
  "minim": {
    "phonetic": "'minim",
    "meaning": "n. 量滴(液量单位), 一滴, 微量；[医] 量滴"
  },
  "minor": {
    "phonetic": "'mainә",
    "meaning": "n. 未成年人, 副修科目；a. 较小的, 二流的, 未成年的；vi. 副修；[计] 次要"
  },
  "minty": {
    "phonetic": "'minti",
    "meaning": "a. 有薄荷香的, 有薄荷味的"
  },
  "minus": {
    "phonetic": "'mainәs",
    "meaning": "n. 负号, 不足；a. 减的, 负的, 阴性的；prep. 减, 缺；[计] 负差"
  },
  "mired": {
    "phonetic": "'maired",
    "meaning": "n. 微倒度；迈尔德（男子名）；微度"
  },
  "mirth": {
    "phonetic": "mә:θ",
    "meaning": "n. 欢笑, 欢乐, 愉快"
  },
  "miser": {
    "phonetic": "'maizә",
    "meaning": "n. 守财奴, 吝啬鬼, (石油工程上用的)锥钻头"
  },
  "missy": {
    "phonetic": "'misi",
    "meaning": "n. 少女, 姑娘, 小姐"
  },
  "misty": {
    "phonetic": "'misti",
    "meaning": "a. 有雾的, 模糊的, 笼罩着雾的"
  },
  "mixed": {
    "phonetic": "mikst",
    "meaning": "a. 混合的, 形形色色的, 弄糊涂的；[计] 混合的"
  },
  "mixer": {
    "phonetic": "'miksә",
    "meaning": "n. 混合者, 混合器, 搅拌机, 搅拌器, 混频器, (非正式)交际家, 与人相处的人；[计] 混频器, 音装置"
  },
  "mixup": {
    "phonetic": "",
    "meaning": "n. 混合；混合物"
  },
  "mocha": {
    "phonetic": "'mәukә",
    "meaning": "n. 穆哈上等咖啡；a. 用咖啡调味的"
  },
  "mochi": {
    "phonetic": "'mɔtʃi",
    "meaning": "<日>n.糯米团(用糯米粉做的糕团)[日文汉字：饼]"
  },
  "modal": {
    "phonetic": "'mәudl",
    "meaning": "a. 形式的, 样式的, 形态上的, 模态的；[计] 模态的"
  },
  "model": {
    "phonetic": "'mɒdәl",
    "meaning": "n. 模型, 模范, 模特儿；a. 模范的, 作模型用的；vi. 做模型, 做模特儿；vt. 使模仿, 塑造；[计] 模型"
  },
  "modem": {
    "phonetic": "'mәudem",
    "meaning": "n. 调制解调器；[计] 调制解调器"
  },
  "modus": {
    "phonetic": "'mәudәs",
    "meaning": "[计] 假言的；[医] 方式, 方法"
  },
  "mogul": {
    "phonetic": "mәu'^ʌl, 'mәu^ʌl",
    "meaning": "n. 大人物, 有权势的人"
  },
  "moist": {
    "phonetic": "mɒist",
    "meaning": "a. 潮湿的, 多雨的, 感伤的, 含泪的；[医] 湿的"
  },
  "molar": {
    "phonetic": "'mәulә",
    "meaning": "a. 磨碎的, 臼齿的, 摩尔的, 克分子的；n. 臼齿, 磨牙"
  },
  "moldy": {
    "phonetic": "'mәuldi",
    "meaning": "a. 发霉的, 腐臭的"
  },
  "molly": {
    "phonetic": "'mɔli",
    "meaning": "n. [俚]懦夫；娘娘腔的男人"
  },
  "momma": {
    "phonetic": "",
    "meaning": "n. 妈咪"
  },
  "mommy": {
    "phonetic": "'mɒmi",
    "meaning": "n. 妈咪"
  },
  "money": {
    "phonetic": "'mʌni",
    "meaning": "n. 金钱, 一笔款, 财富, 货币, 金额；[经] 货币, 金钱, 财产"
  },
  "month": {
    "phonetic": "mʌnθ",
    "meaning": "n. 月；[经] 月"
  },
  "mooch": {
    "phonetic": "mu:tʃ",
    "meaning": "vi. 彷徨, 漫步；vt. 偷, 央求, 讨"
  },
  "moody": {
    "phonetic": "'mu:di",
    "meaning": "a. 心情不稳的, 郁郁寡欢的, 喜怒无常的"
  },
  "mooed": {
    "phonetic": "mu:d",
    "meaning": "v. （牛叫声）哞( moo的过去式和过去分词 )"
  },
  "moose": {
    "phonetic": "mu:s",
    "meaning": "n. 麋, 驼鹿"
  },
  "moped": {
    "phonetic": "'mәuped",
    "meaning": "n. 助动车"
  },
  "moper": {
    "phonetic": "",
    "meaning": "闲荡的人"
  },
  "mopey": {
    "phonetic": "'mәjpi",
    "meaning": "a. 没精打采的,闷闷不乐的,消沉的"
  },
  "moral": {
    "phonetic": "'mɒrәl",
    "meaning": "n. 道德, 品行, 寓意；a. 道德的, 品性端正的, 精神上的"
  },
  "moray": {
    "phonetic": "'mɒ:rei",
    "meaning": "n. 海鳝"
  },
  "moron": {
    "phonetic": "'mɒ:rɒn",
    "meaning": "n. 低能者, 笨人；[医] 痴愚者"
  },
  "morph": {
    "phonetic": "mɔf",
    "meaning": "[计] 形态, 词态"
  },
  "mosey": {
    "phonetic": "'mәuzi",
    "meaning": "vi. 漫步, 徘徊, 离去"
  },
  "mossy": {
    "phonetic": "'mɒsi",
    "meaning": "a. 生苔的, 似苔的, 陈腐的"
  },
  "motel": {
    "phonetic": "mәu'tel",
    "meaning": "n. 汽车旅馆"
  },
  "motif": {
    "phonetic": "mәu'ti:f",
    "meaning": "n. 主题, 基调, 动机, 基本图案；[法] 主旨, 主题, 动机"
  },
  "motor": {
    "phonetic": "'mәutә",
    "meaning": "n. 马达, 发动机, 原动力, 汽车；a. 马达的, 发动机的, 汽车的, 发动的；vt. 推动, 以汽车载运；vi. 乘汽车, 驾车"
  },
  "motto": {
    "phonetic": "'mɒtәu",
    "meaning": "n. 箴言, 座右铭, 警句"
  },
  "mould": {
    "phonetic": "mәuld",
    "meaning": "n. 模子, 模制品, 松软沃土, 霉；vt. 形成, 浇铸, 用泥土覆盖；vi. 发霉"
  },
  "moult": {
    "phonetic": "mәult",
    "meaning": "n. 换毛, 脱毛；v. 脱毛, 换毛"
  },
  "mound": {
    "phonetic": "maund",
    "meaning": "n. 土墩, 堤, 小山；vt. 筑堤, 用土堆防卫；vi. 积成堆"
  },
  "mount": {
    "phonetic": "maunt",
    "meaning": "n. 乘骑用马, 框, 衬纸, 山；vi. 乘马, 爬上, 增长；vt. 爬上, 使上马, 装上, 装裱, 安放, 制作...的标本, 设置, 上演；[计] 安装"
  },
  "mourn": {
    "phonetic": "mɒ:n",
    "meaning": "v. 哀悼, 忧伤, 服丧"
  },
  "mouse": {
    "phonetic": "maus",
    "meaning": "n. 老鼠, 胆小羞怯的人, 鼠标；vi. 捕鼠, 窥探；vt. 探出；[计] 鼠标"
  },
  "mousy": {
    "phonetic": "'mausi",
    "meaning": "a. 象老鼠的, 多老鼠的, 胆小的"
  },
  "mouth": {
    "phonetic": "mauθ",
    "meaning": "n. 嘴, 口, 口腔, 口状物；vi. 装腔作势说话, 做鬼脸；vt. 说出, 做作地说"
  },
  "moved": {
    "phonetic": "",
    "meaning": "v. 移动, 移动到；感动（move的过去式, 过去分词）"
  },
  "mover": {
    "phonetic": "'mu:vә",
    "meaning": "n. 移动的人, 原动力, 鼓动者"
  },
  "movie": {
    "phonetic": "'mu:vi",
    "meaning": "n. 电影"
  },
  "mowed": {
    "phonetic": "",
    "meaning": "mow的过去式和过去分词"
  },
  "mower": {
    "phonetic": "'mәuә",
    "meaning": "n. 刈草的人, 刈草机"
  },
  "moxie": {
    "phonetic": "'mɒksi",
    "meaning": "n. 精力, 活力, 大胆"
  },
  "mucky": {
    "phonetic": "'mʌki",
    "meaning": "a. 粪的, 脏的"
  },
  "mucus": {
    "phonetic": "'mju:kәs",
    "meaning": "n. 粘液；[化] 粘液"
  },
  "muddy": {
    "phonetic": "'mʌdi",
    "meaning": "a. 泥泞的, 浑浊的, 模糊的；vt. 使污浊, 使沾上泥污"
  },
  "muggy": {
    "phonetic": "'mʌgi",
    "meaning": "a. 闷热的"
  },
  "mulch": {
    "phonetic": "mʌltʃ",
    "meaning": "n. 覆盖物, 护根, 根篱；vt. 铺护盖物, 做护根"
  },
  "mummy": {
    "phonetic": "'mʌmi",
    "meaning": "n. 木乃伊, 瘦而干瘪之人, 妈咪；[医] 干尸, 木乃伊; 普鲁士红"
  },
  "munch": {
    "phonetic": "mʌntʃ",
    "meaning": "v. 用力咀嚼, 大声咀嚼"
  },
  "mural": {
    "phonetic": "'mjuәrәl",
    "meaning": "a. 壁的, 壁上的, 壁似的；n. 壁画"
  },
  "murky": {
    "phonetic": "'mә:ki",
    "meaning": "a. 黝暗的, 阴沉的, 朦胧的"
  },
  "mused": {
    "phonetic": "m'ju:zd",
    "meaning": "v. 沉思, 冥想( muse的过去式和过去分词 ); 沉思自语说（某事）"
  },
  "mushy": {
    "phonetic": "'mʌʃi",
    "meaning": "a. 浓粥状的, 含糊不清, 感伤的"
  },
  "music": {
    "phonetic": "'mju:zik",
    "meaning": "n. 音乐, 乐曲"
  },
  "musky": {
    "phonetic": "'mʌski",
    "meaning": "a. 麝香的, 产生麝香的, 麝香似的"
  },
  "mussy": {
    "phonetic": "'mʌsi",
    "meaning": "a. 杂乱的, 紊乱的, 肮脏的"
  },
  "musty": {
    "phonetic": "'mʌsti",
    "meaning": "a. 发霉的, 霉臭的, 落伍的"
  },
  "muted": {
    "phonetic": "",
    "meaning": "a. 变弱了的, 变柔和了的"
  },
  "myrrh": {
    "phonetic": "mә:",
    "meaning": "n. 没药树；[化] 没药"
  },
  "nabob": {
    "phonetic": "'neibɔb",
    "meaning": "n. 印度莫卧儿帝国的地方长官, 在印度发财的欧洲人, 富豪"
  },
  "nacho": {
    "phonetic": "'nɑ:tʃәj",
    "meaning": "n. (墨西哥人食用的)烤干酪辣味玉米片"
  },
  "nadir": {
    "phonetic": "'nei.diә",
    "meaning": "n. 天底, 最低点"
  },
  "naggy": {
    "phonetic": "'næɡɪ",
    "meaning": "小马"
  },
  "naive": {
    "phonetic": "nɑ:'i:v",
    "meaning": "a. 天真的, 纯真的, 幼稚的"
  },
  "naked": {
    "phonetic": "'neikid",
    "meaning": "a. 裸体的, 无装饰的, 无保护的, 赤贫的；[医] 裸露的"
  },
  "named": {
    "phonetic": "neimd",
    "meaning": "a. 被指名的, 指定的；[计] 命名的, 指定的, 有名的"
  },
  "nanny": {
    "phonetic": "'næni",
    "meaning": "n. 保姆；母山羊"
  },
  "nappy": {
    "phonetic": "'næpi",
    "meaning": "n. 尿布, 菜盆；a. 起毛的, 多毛的, 酒精含量高的"
  },
  "nasal": {
    "phonetic": "'neizl",
    "meaning": "a. 鼻的, 鼻声的, 尖锐的；n. 鼻音, 鼻音字"
  },
  "nasty": {
    "phonetic": "'nɑ:sti",
    "meaning": "a. 污秽的, 下流的, 险恶的"
  },
  "natal": {
    "phonetic": "'neitl",
    "meaning": "a. 出生的, 诞生的；[医] 分娩的, 生产的; 臀的"
  },
  "naval": {
    "phonetic": "'neivl",
    "meaning": "a. 海军的, 军舰的, 有舰队的；[法] 海军的, 军舰的, 船的"
  },
  "navel": {
    "phonetic": "'neivl",
    "meaning": "n. 脐, 肚脐, 中央, 中心；[医] 脐"
  },
  "needy": {
    "phonetic": "'ni:di",
    "meaning": "a. 贫穷的, 贫困的, 生活艰苦的"
  },
  "neigh": {
    "phonetic": "nei",
    "meaning": "n. 马嘶声；vi. 马嘶"
  },
  "nerdy": {
    "phonetic": "'nɜːdi",
    "meaning": "a. 傻瓜似的；蠢的"
  },
  "nerve": {
    "phonetic": "nә:v",
    "meaning": "n. 精神, 勇气, 叶脉, 神经；vt. 鼓起勇气"
  },
  "nervy": {
    "phonetic": "'nә:vi",
    "meaning": "a. 有勇气的, 易激动的"
  },
  "never": {
    "phonetic": "'nevә",
    "meaning": "adv. 从不, 决不, 不曾；[法] 永不, 决不, 从来没有"
  },
  "newer": {
    "phonetic": "",
    "meaning": "a. 更新的, 更新"
  },
  "newly": {
    "phonetic": "'nju:li",
    "meaning": "adv. 重新, 最近"
  },
  "newsy": {
    "phonetic": "'nju:si",
    "meaning": "a. 多新闻的, 有报道价值的, 爱闲话的；n. 报童"
  },
  "nexus": {
    "phonetic": "'neksәs",
    "meaning": "n. 连结, 关系；[化] 融合膜"
  },
  "nicer": {
    "phonetic": "",
    "meaning": "a. 良好的"
  },
  "niche": {
    "phonetic": "nitʃ",
    "meaning": "n. 壁龛；vt. 放入壁龛, 安顿"
  },
  "niece": {
    "phonetic": "ni:s",
    "meaning": "n. 侄女, 甥女"
  },
  "nifty": {
    "phonetic": "'nifti",
    "meaning": "a. 俏皮的, 时髦的；n. 俏皮话, 漂亮话"
  },
  "night": {
    "phonetic": "nait",
    "meaning": "n. 夜, 夜晚, 晚上, 黑暗, 夜晚的工作；[法] 夜, 黑夜, 黑暗"
  },
  "nimby": {
    "phonetic": "ˈnɪmbi",
    "meaning": "n. <美口>宁比"
  },
  "ninja": {
    "phonetic": "'nindʒә",
    "meaning": "n. （受过偷窃技术专门训练被雇作间谍或刺客的）日本武士"
  },
  "ninny": {
    "phonetic": "'nini",
    "meaning": "n. 笨人, 傻子"
  },
  "ninth": {
    "phonetic": "nainθ",
    "meaning": "num. 第九, 九分之一"
  },
  "nippy": {
    "phonetic": "'nipi",
    "meaning": "a. 刺骨的, 凛冽的, 锐利的"
  },
  "nitro": {
    "phonetic": "'naitrәu",
    "meaning": "n. 硝基"
  },
  "nixed": {
    "phonetic": "nikst",
    "meaning": "[美俚]被禁止 的"
  },
  "noble": {
    "phonetic": "'nәubl",
    "meaning": "n. 贵族；a. 高贵的, 高尚的, 贵族的, 辉煌的"
  },
  "nobly": {
    "phonetic": "'nәubli",
    "meaning": "adv. 华丽地, 高尚地, 豪爽地"
  },
  "noise": {
    "phonetic": "nɒiz",
    "meaning": "n. 噪音, 杂音, 响声, 喧闹；vt. 谣传；vi. 喧闹；[计] 噪声"
  },
  "noisy": {
    "phonetic": "'nɒizi",
    "meaning": "a. 嘈杂的, 喧闹的；[机] 噪声的, 嘈杂的"
  },
  "nomad": {
    "phonetic": "'nәumәd",
    "meaning": "n. 游牧部落一员, 流浪者；a. 游牧的, 流浪的"
  },
  "noose": {
    "phonetic": "nu:s",
    "meaning": "n. 套索, 束缚, 陷阱；vt. 用套索捉"
  },
  "north": {
    "phonetic": "nɒ:θ",
    "meaning": "n. 北方, 北；a. 北的, 北方的；adv. 向北方, 在北方"
  },
  "nosed": {
    "phonetic": "'nәuzd",
    "meaning": "a. 有...鼻子的"
  },
  "nosey": {
    "phonetic": "'nәuzi",
    "meaning": "a. 大鼻子的, (非正式)(贬)爱管闲事的, 爱探听的, 好打听的"
  },
  "notch": {
    "phonetic": "nɒtʃ",
    "meaning": "n. 刻痕, 等级, 峡谷；vt. 刻凹痕, 用刻痕计算, 赢得"
  },
  "noted": {
    "phonetic": "'nәutid",
    "meaning": "a. 著名的, 显著的, 扬名的"
  },
  "novel": {
    "phonetic": "'nɒvl",
    "meaning": "n. 小说, 长篇故事；a. 新奇的, 异常的"
  },
  "nudge": {
    "phonetic": "nʌdʒ",
    "meaning": "n. 用肘轻推, 推动, 讨厌家伙"
  },
  "nuked": {
    "phonetic": "nju:kt",
    "meaning": "v. 以核武器攻击, , 以核武器摧毁( nuke的过去式和过去分词 )"
  },
  "nurse": {
    "phonetic": "nә:s",
    "meaning": "n. 护士, 保姆, 奶妈；vt. 看护, 照顾, 培养；vi. 喂奶, 看护病人"
  },
  "nutso": {
    "phonetic": "'nʌtsәj",
    "meaning": "a. <口>痴狂的,发疯的,发狂的"
  },
  "nutty": {
    "phonetic": "'nʌti",
    "meaning": "a. 产坚果的"
  },
  "nylon": {
    "phonetic": "'nailɒn",
    "meaning": "n. 尼龙；[化] 尼龙; 聚酰胺纤维"
  },
  "nymph": {
    "phonetic": "nimf",
    "meaning": "n. 居于山林水泽的仙女, 蛹, 美丽的少女；[医] 稚虫, 若虫, 蝻"
  },
  "oaken": {
    "phonetic": "'әukәn",
    "meaning": "a. 橡木制的"
  },
  "oared": {
    "phonetic": "'ɔ:d",
    "meaning": "有桨的"
  },
  "oasis": {
    "phonetic": "әu'eisis",
    "meaning": "n. 绿洲, 舒适的地方；[医] 绿洲(沙漠中), 健岛(病变区中的健康组织)"
  },
  "obese": {
    "phonetic": "әu'bi:s",
    "meaning": "a. 肥胖的；[医] 肥胖的"
  },
  "occur": {
    "phonetic": "ә'kә:",
    "meaning": "vi. 发生, 被想到, 存在"
  },
  "ocean": {
    "phonetic": "'әuʃәn",
    "meaning": "n. 海洋, 广阔, 许多, 一大片；[法] 海洋, 海"
  },
  "ochre": {
    "phonetic": "'әukә",
    "meaning": "n. 赭石, 赭色；vt. 涂赭色于"
  },
  "octal": {
    "phonetic": "'ɒktәl",
    "meaning": "a. 八进制的；[电] 八进"
  },
  "octet": {
    "phonetic": "ɔk'tet",
    "meaning": "[计] 八位二进制数的位组; 八位字节；[化] 八隅体; 八角; 八角体; 八重态; 八重线; 八重峰"
  },
  "odder": {
    "phonetic": "ɔdə",
    "meaning": "a. 奇怪的( odd的比较级 ); 临时的; 奇数的; 不固定的"
  },
  "oddly": {
    "phonetic": "'ɒdli",
    "meaning": "adv. 奇怪地"
  },
  "odeum": {
    "phonetic": "әu'di:әm",
    "meaning": "n. 表演场, 音乐厅, 剧场"
  },
  "offal": {
    "phonetic": "'ɒfәl",
    "meaning": "n. 碎屑, 残渣, 下水, 不能吃的部份, 垃圾, 被鄙弃的人；[化] 废料; 下角料"
  },
  "offed": {
    "phonetic": "",
    "meaning": "vi. [用于祈使句]走开, 滚开, 站开（off的过去式与过去分词形式）"
  },
  "offer": {
    "phonetic": "'ɒfә",
    "meaning": "n. 给予(物), 出价, 提议, 意图, 报价；vt. 提供, 出价, 奉献, 试图, 使出现, 演出；vi. 出现, 献祭, 提议, 求婚"
  },
  "often": {
    "phonetic": "'ɒ:fn",
    "meaning": "adv. 时常, 常常"
  },
  "ogled": {
    "phonetic": "ˈəʊgəld",
    "meaning": "v. （向…）抛媚眼, 送秋波( ogle的过去式和过去分词 )"
  },
  "ogler": {
    "phonetic": "",
    "meaning": "n. ogle的变形"
  },
  "oiled": {
    "phonetic": "ɒild",
    "meaning": "a. 涂油的, 用油防水的, 浸油的；[机] 涂油的, 擦油"
  },
  "oiler": {
    "phonetic": "'ɒilә",
    "meaning": "n. 油商, 加油工, 涂油者, 注油壶；[化] 加油器; 加油者"
  },
  "okapi": {
    "phonetic": "әu'kɑ:pi",
    "meaning": "n. [动]霍加皮(产于非洲东部)"
  },
  "olden": {
    "phonetic": "әuldn",
    "meaning": "a. 古时的, 从前的；vt. 使衰老；vi. 变老"
  },
  "older": {
    "phonetic": "'әuldә",
    "meaning": "a. 年长的；较旧的"
  },
  "oldie": {
    "phonetic": "'әjldi",
    "meaning": "n. 老人, 陈旧之物"
  },
  "olive": {
    "phonetic": "'ɒliv",
    "meaning": "n. 橄榄, 橄榄树, 橄榄色, 橄榄枝；a. 黄绿色的, 黄褐色的, 橄榄色的"
  },
  "ombre": {
    "phonetic": "'ɔmbrei",
    "meaning": "(=omber) n.三人玩的奥伯尔牌戏"
  },
  "omega": {
    "phonetic": "'әumigә",
    "meaning": "n. 希腊字母的最后一个字, 终了, 最后；[医] ω(希腊文第二十四个字母)"
  },
  "onion": {
    "phonetic": "'ʌnjәn",
    "meaning": "n. 洋葱；vt. 因洋葱使掉泪"
  },
  "onset": {
    "phonetic": "'ɒnset",
    "meaning": "n. 开始, 攻击, 进攻；[医] 起始, 开始"
  },
  "oomph": {
    "phonetic": "umf",
    "meaning": "n. 性感, 热情, 精力, 吸引力"
  },
  "oozed": {
    "phonetic": "u:zd",
    "meaning": "v. （浓液等）慢慢地冒出, 渗出( ooze的过去式和过去分词 ); 使（液体）缓缓流出; （浓液）渗出, 慢慢流出"
  },
  "opera": {
    "phonetic": "'ɒpәrә",
    "meaning": "n. 歌剧"
  },
  "opine": {
    "phonetic": "әu'pain",
    "meaning": "v. 想, 以为"
  },
  "opium": {
    "phonetic": "'әupjәm",
    "meaning": "n. 鸦片；[化] 阿片; 鸦片"
  },
  "opted": {
    "phonetic": "ɔptid",
    "meaning": "v. 选择, 挑选( opt的过去式和过去分词 )"
  },
  "optic": {
    "phonetic": "'ɒptik",
    "meaning": "a. 眼睛的, 视觉的, 光学的；n. 镜片"
  },
  "orate": {
    "phonetic": "'ɒ:reit",
    "meaning": "vi. 演说, 演讲, 高谈阔论"
  },
  "orbed": {
    "phonetic": "ɔ:bd",
    "meaning": "a. 球状的, 圆形的"
  },
  "orbit": {
    "phonetic": "'ɒ:bit",
    "meaning": "n. 轨道, 常轨, 眼眶；vt. 绕...轨道而行；vi. 进入轨道, 盘旋"
  },
  "order": {
    "phonetic": "'ɒ:dә",
    "meaning": "n. 次序, 规则, 命令；vi. 命令, 定货；vt. 整理, 命令, 定购；n. 顺序, 阶数；[计] 顺序, 阶数"
  },
  "organ": {
    "phonetic": "'ɒ:gәn",
    "meaning": "n. 风琴, 器官, 元件, 机构, 机关；[电] 风琴"
  },
  "other": {
    "phonetic": "'ʌðә",
    "meaning": "a. 其他的, 另外的, 从前的；pron. 其他的, 他人, 另外一个"
  },
  "otter": {
    "phonetic": "'ɒtә",
    "meaning": "n. 水獭, 水獭皮"
  },
  "ought": {
    "phonetic": "ɒ:t",
    "meaning": "aux. 应该, 大概；n. 责任"
  },
  "ouija": {
    "phonetic": "'wi:dʒɑ:",
    "meaning": "n. 占卜板"
  },
  "ounce": {
    "phonetic": "auns",
    "meaning": "n. 盎司, 少量, 雪豹；[医] 英两, Г"
  },
  "outdo": {
    "phonetic": ".aut'du:",
    "meaning": "vt. 超越, 胜过, 战胜"
  },
  "outed": {
    "phonetic": "autid",
    "meaning": "v. 伸出( out的过去式和过去分词 ); 揭露; 驱逐; 使熄灭"
  },
  "outer": {
    "phonetic": "'autә",
    "meaning": "a. 外部的, 外面的, 在外的, 远离中心的；[机] 外部的, 外面的, 外侧的"
  },
  "outgo": {
    "phonetic": ".aut'gәu",
    "meaning": "n. 外出, 支出, 出口；vt. 胜过, 优于"
  },
  "outre": {
    "phonetic": "",
    "meaning": "a. 越出常轨的；过度的；荒诞的"
  },
  "ovary": {
    "phonetic": "'әuvәri",
    "meaning": "n. 卵巢, 子房, 果核；[医] 卵巢, 子房"
  },
  "ovate": {
    "phonetic": "'әuveit",
    "meaning": "a. 卵形的；[医] 卵圆形的(叶)"
  },
  "overt": {
    "phonetic": "'әuvә:t",
    "meaning": "a. 明显的, 公然的, 蓄意的；[法] 明显的, 公开的"
  },
  "ovine": {
    "phonetic": "'әuvain",
    "meaning": "a. 绵羊的；[医] 羊的"
  },
  "ovoid": {
    "phonetic": "'әuvɒid",
    "meaning": "a. 卵形的, 梨形的；n. 卵形体"
  },
  "owing": {
    "phonetic": "'әuiŋ",
    "meaning": "a. 未付的, 亏欠的, 受惠的, 归因于...的；[经] 应付的, 欠着的, 未付的"
  },
  "owned": {
    "phonetic": "",
    "meaning": "v. 拥有；承认（own的过去分词）"
  },
  "owner": {
    "phonetic": "'әunә",
    "meaning": "n. 拥有者, 物主, 所有人；[经] 所有者, 物主, 业主"
  },
  "oxbow": {
    "phonetic": "ˈɒksbəʊ",
    "meaning": "n. 牛轭U字形部分, U字形弯曲；a. 呈U字形弯曲的"
  },
  "oxide": {
    "phonetic": "'ɒksaid",
    "meaning": "n. 氧化物；[医] 氧化物"
  },
  "ozone": {
    "phonetic": "'әuzәun",
    "meaning": "n. 新鲜的空气, 臭氧, 使人愉快的影响；[化] 臭氧"
  },
  "paced": {
    "phonetic": "peist",
    "meaning": "a. 节奏均匀的"
  },
  "pacer": {
    "phonetic": "'peisә",
    "meaning": "[电] 步测器"
  },
  "paddy": {
    "phonetic": "'pædi",
    "meaning": "n. 稻, 谷, 爱尔兰人, 警察；[法] 警察"
  },
  "padre": {
    "phonetic": "'pɑ:dri",
    "meaning": "n. 神父, 随军牧师"
  },
  "paean": {
    "phonetic": "'pi:әn",
    "meaning": "n. 凯歌, 欢乐歌, 赞美歌"
  },
  "pagan": {
    "phonetic": "'peigәn",
    "meaning": "n. 异教徒, 无宗教信仰者；a. 异教的, 异教徒的"
  },
  "paged": {
    "phonetic": "",
    "meaning": "分页的"
  },
  "pager": {
    "phonetic": "'peidʒә(r)",
    "meaning": "[计] 页调度程序"
  },
  "paint": {
    "phonetic": "peint",
    "meaning": "n. 油漆, 颜料, 绘画作品, 涂漆；vt. 油漆, 绘, 画, 描绘, 装饰, 点缀；vi. 绘画, 涂漆"
  },
  "paled": {
    "phonetic": "peild",
    "meaning": "围栅的"
  },
  "paler": {
    "phonetic": "",
    "meaning": "n. (Paler)人名；(罗)帕勒尔；灰白的；暗淡的；无力的（ pale的比较级 ）；苍白的"
  },
  "palsy": {
    "phonetic": "'pɒ:lzi",
    "meaning": "n. 中风, 麻痹, (不由自主的)颤动, 麻痹状态；vt. 麻痹, 使瘫痪"
  },
  "panda": {
    "phonetic": "'pændә",
    "meaning": "n. 大熊猫, 小熊猫"
  },
  "panel": {
    "phonetic": "'pænl",
    "meaning": "n. 嵌板, 仪表板, 专题讨论小组, 全体陪审员；vt. 嵌镶板"
  },
  "panic": {
    "phonetic": "'pænik",
    "meaning": "n. 恐慌, 惊慌；a. 惊慌的, 没有理由的, 恐慌的；vt. 使惊慌, 使狂热；vi. 惊慌"
  },
  "panty": {
    "phonetic": "'pænti",
    "meaning": "n. 女裤；童裤（等于panties）"
  },
  "papal": {
    "phonetic": "'peipl",
    "meaning": "a. 罗马教皇的, 教皇制度的"
  },
  "paper": {
    "phonetic": "'peipә",
    "meaning": "n. 纸, 文件, 文章, 报纸, 证券, 证件；vt. 用纸糊, 贴壁纸于, 用纸包装；vi. 贴壁纸；a. 纸做的, 纸上的"
  },
  "parch": {
    "phonetic": "pɑ:tʃ",
    "meaning": "vt. 烤, 烘, 使干透；vi. 烤干, 焦干"
  },
  "pared": {
    "phonetic": "peəd",
    "meaning": "v. 削皮( pare的过去式和过去分词 ); 削掉; 修剪（指甲等）; 逐步减小（数量或体积）"
  },
  "parer": {
    "phonetic": "",
    "meaning": "n. 削皮的人, 削皮刀, 削皮器"
  },
  "parka": {
    "phonetic": "'pɑ:kә",
    "meaning": "n. 皮制连帽大衣, 派克大衣"
  },
  "parry": {
    "phonetic": "'pæri",
    "meaning": "vt. 挡开, 回避, 闪避的回答；n. 挡开, 回避, 闪避的回答"
  },
  "parse": {
    "phonetic": "pɑ:s",
    "meaning": "vt. 从语法上分析；[计] 分列"
  },
  "party": {
    "phonetic": "'pɑ:ti",
    "meaning": "n. 宴会, 党, 政党, 团体, 当事人, 聚会；v. 举办聚会"
  },
  "passe": {
    "phonetic": "",
    "meaning": "a. 已过盛年的, 雕落的, 已过青春妙龄的, 过时的, 老式的, 陈旧的, 落伍的"
  },
  "pasta": {
    "phonetic": "'pæstә",
    "meaning": "n. 意大利面食；[医] 糊剂, 泥膏剂"
  },
  "paste": {
    "phonetic": "peist",
    "meaning": "n. 面团, 面食, 浆糊, 糊状物, 粘贴, 用拳重击；vt. 用浆糊粘, 张贴, 狠狠地打；[计] 粘贴"
  },
  "pasty": {
    "phonetic": "'peisti. 'pæsti",
    "meaning": "a. 面糊似的, (脸色)苍白的, 软弱的；n. 肉馅饼"
  },
  "patch": {
    "phonetic": "pætʃ",
    "meaning": "n. 片, 补缀, 碎片, 斑, 傻瓜；vt. 补缀, 掩饰, 拼凑, 平息；[计] 修补; 拼凑"
  },
  "patio": {
    "phonetic": "'pɑ:tiәu",
    "meaning": "n. 屋子与花园之间的一片供晴天休息用的石砌空地"
  },
  "patsy": {
    "phonetic": "'pætsi",
    "meaning": "n. 容易受骗的人, 懦夫, 替罪羊"
  },
  "patty": {
    "phonetic": "'pæti",
    "meaning": "n. 小馅饼"
  },
  "pause": {
    "phonetic": "pɒ:z",
    "meaning": "n. 暂停, 中止, 停顿, 间歇, 踌躇, 休止符；vi. 暂停, 中止, 停顿, 踌躇；[计] DOS内部命令:暂时停止批处理文件的执行"
  },
  "paved": {
    "phonetic": "peivd",
    "meaning": "v. 铺( pave的过去式和过去分词 ); 为…铺平道路"
  },
  "paver": {
    "phonetic": "'peivә",
    "meaning": "n. 铺路工, 铺设人, 铺筑材料, 铺设材料, 铺路机"
  },
  "pawed": {
    "phonetic": "",
    "meaning": "vt. 用爪抓（paw的过去式与过去分词形式）"
  },
  "payee": {
    "phonetic": "pei'i:",
    "meaning": "n. 收款人, 领款人；[经] 受款人, 收款人"
  },
  "payer": {
    "phonetic": "'peiә",
    "meaning": "n. 支付者, 付款人；[经] 付款人"
  },
  "peace": {
    "phonetic": "pi:s",
    "meaning": "n. 和平, 和约, 治安, 和睦, 安宁, 静寂；vi. 安静下来, 不作声"
  },
  "peach": {
    "phonetic": "pi:tʃ",
    "meaning": "n. 桃子, 桃树, 桃色, 美人儿, 极好的事物；vt. 告发；vi. 告密, 检举"
  },
  "pearl": {
    "phonetic": "pә:l",
    "meaning": "n. 珍珠, 珠灰色, 杰出者, 珍贵之物；vt. 用珍珠镶, 使成珠状；vi. 成珠子状, 采珍珠, 用珍珠做"
  },
  "pecan": {
    "phonetic": "pi'kæn",
    "meaning": "n. 美洲山核桃(树)"
  },
  "pedal": {
    "phonetic": "'pedl",
    "meaning": "n. 踏板, 脚蹬子；a. 脚的, 脚踏的；vt. 用脚踏动；vi. 踩踏板, 骑车"
  },
  "peeve": {
    "phonetic": "pi:v",
    "meaning": "v. (使)气恼, (使)焦躁, (使)忿怒；n. 麻烦的事物, 怨恨, 生气, 触怒"
  },
  "penal": {
    "phonetic": "'pi:nl",
    "meaning": "a. 有关处罚的, 刑的, 刑罚的, 刑法上的, (课税)繁重的；[法] 刑事的, 刑法的, 受刑罚的"
  },
  "pence": {
    "phonetic": "pens",
    "meaning": "pl. (非正式)copper便士, (美)分, 分币"
  },
  "penne": {
    "phonetic": "'pennei",
    "meaning": "n. 通心粉；管形面点, 管状面"
  },
  "penny": {
    "phonetic": "'peni",
    "meaning": "n. 便士, 一分, 小钱, 点滴；[经] 便士"
  },
  "peony": {
    "phonetic": "'pi:әni",
    "meaning": "n. 牡丹(花), 芍药(花)"
  },
  "peppy": {
    "phonetic": "'pepi",
    "meaning": "a. 精神充沛的, 活泼的, 起动快的"
  },
  "perch": {
    "phonetic": "pә:tʃ",
    "meaning": "n. 栖木, 高位, 杆, 河鲈；v. (使)栖息, 就位, 位于, (使)暂歇"
  },
  "peril": {
    "phonetic": "'peril",
    "meaning": "n. 危险, 冒...之险, 险境, 险因；vt. 置...于险境, 冒险, 危及"
  },
  "perky": {
    "phonetic": "'pә:ki",
    "meaning": "a. 得意洋洋的, 快活的, 敏捷的, 美观的, 傲慢的, 神气的"
  },
  "pesky": {
    "phonetic": "'peski",
    "meaning": "a. 麻烦的, 恼人的, 棘手的, 讨厌的"
  },
  "pesto": {
    "phonetic": "'pestәj",
    "meaning": "n. <美>[食](浇在面条或通心粉等上的)香蒜沙司,香蒜酱"
  },
  "petal": {
    "phonetic": "'petәl",
    "meaning": "n. 花瓣；[医] 花瓣"
  },
  "peter": {
    "phonetic": "'pi:tә",
    "meaning": "vi. 逐渐消失, 逐渐减少"
  },
  "petit": {
    "phonetic": "pә'ti:, 'peti",
    "meaning": "[法] 小的, 轻的"
  },
  "petri": {
    "phonetic": "pɛtrə",
    "meaning": "abbr. petroleum 石油"
  },
  "petty": {
    "phonetic": "'peti",
    "meaning": "a. 琐碎的, 小规模的, 小气的, 委琐的；[经] 小额的, 微小的, 小规模的"
  },
  "phase": {
    "phonetic": "feiz",
    "meaning": "n. 时期, 局面, 方面, 位相, 相, 阶段；vt. 使调整相位, 使定相, 使一致, 逐步执行, 实行；[计] 阶段"
  },
  "phish": {
    "phonetic": "",
    "meaning": "v. 网络钓鱼"
  },
  "phone": {
    "phonetic": "fәun",
    "meaning": "n. 电话, 受话器, 耳机；vt. 打电话给；vi. 打电话"
  },
  "phony": {
    "phonetic": "'fәuni",
    "meaning": "n. 假货, 假冒者, 赝品；a. 伪造的, 假的, 不可信的, 华而不实的"
  },
  "photo": {
    "phonetic": "'fәutәu",
    "meaning": "n. 相片, 照片, 逼真的描绘；v. 照相；a. 照相的, 摄影用的, 详细记录的, 逼真的, 酷似的"
  },
  "piano": {
    "phonetic": "pi'ɑ:nәu",
    "meaning": "n. 钢琴"
  },
  "picky": {
    "phonetic": "'piki",
    "meaning": "a. 吹毛求疵的, 挑剔的, 找麻烦的"
  },
  "piece": {
    "phonetic": "pi:s",
    "meaning": "n. 块, 片, 篇, 碎片, 部分, 部件, 标准量；vt. 修补, 修理, 拼合, 接线头；vi. 吃零食"
  },
  "piety": {
    "phonetic": "'paiәti",
    "meaning": "n. 虔诚, 孝敬, 虔诚的行为"
  },
  "piggy": {
    "phonetic": "'pigi",
    "meaning": "n. 小猪；a. 贪心的, 似猪的, 邋遢的"
  },
  "piked": {
    "phonetic": "",
    "meaning": "a. 尖的"
  },
  "piker": {
    "phonetic": "'paikә",
    "meaning": "n. 胆小鬼, 缩手缩脚的人, 小气鬼"
  },
  "pilaf": {
    "phonetic": "pi'lɑ:f",
    "meaning": "n. 肉饭(由大米加鱼或肉及调料煮成)"
  },
  "piled": {
    "phonetic": "",
    "meaning": "a. 有细毛的"
  },
  "pilot": {
    "phonetic": "'pailәt",
    "meaning": "n. 飞行员, 领航员, 航船者, 导向器, 驾驶仪, 向导, 领导人；vt. 领航, 驾驶, 引导, 试用；a. 引导的, 控制的, 试点的；[计] 引导"
  },
  "pinch": {
    "phonetic": "pintʃ",
    "meaning": "n. 捏, 拧, 撮, 少量, 收缩, 挤压, 夹痛, 苦恼, 逮捕, 指控, 匮乏, 紧急关头；vt. 捏, 拧, 掐, 挤压, 修剪, 使困苦, 使萎缩, 节制, 少量加入, 逮捕, 勒索；vi. 收缩, 节省, 挤压, 引起苦恼"
  },
  "pined": {
    "phonetic": "",
    "meaning": "vi. 憔悴（pine的过去式与过去分词形式）"
  },
  "piney": {
    "phonetic": "'paini",
    "meaning": "a. 似松的, 松树般茂盛的"
  },
  "pinky": {
    "phonetic": "'piŋki",
    "meaning": "a. 带淡红色的, 比较激进的"
  },
  "pinot": {
    "phonetic": "pi'nәu",
    "meaning": "加州葡萄"
  },
  "pinto": {
    "phonetic": "'pintәu",
    "meaning": "a. 黑白花斑的, 杂色的；n. 花马, 菜豆"
  },
  "pinup": {
    "phonetic": "'pinʌp",
    "meaning": "a. 钉在壁上的, 适宜钉在壁上装饰的, 迷人的；n. 钉在壁上的东西"
  },
  "pious": {
    "phonetic": "'paiәs",
    "meaning": "a. 虔诚的, 敬神的, 尽责的, 可嘉的, 不可能实现的"
  },
  "piped": {
    "phonetic": "paipt",
    "meaning": "a. 酒醉的"
  },
  "piper": {
    "phonetic": "'paipә",
    "meaning": "n. 吹笛者, 风笛手, 管乐器吹奏者, 管道安装工, 幼鸽"
  },
  "pipet": {
    "phonetic": "pi'pet",
    "meaning": "n. 吸量管, 吸移管；[化] 吸移管"
  },
  "pique": {
    "phonetic": "pi:k",
    "meaning": "n. 赌气, 愤怒, 不快, 凹凸织物；vt. 伤害...自尊心, 激怒, 刺激, 引起兴趣, 使兴奋"
  },
  "piste": {
    "phonetic": "pi:st",
    "meaning": "n. 滑雪道"
  },
  "pitch": {
    "phonetic": "pitʃ",
    "meaning": "n. 程度, 坡度, 顶点, 前倾, 倾斜, 投掷, 音高, 螺距, 节距, 摊位, 树脂, 沥青；vt. 投, 掷, 向前倾跌, 扎营, 竭力推销, 为...定调, 定位于, 用沥青涂；vi. 搭帐篷, 投掷, 向前跌, 猛然摔倒, 坠落, 倾斜；[计] 孔距"
  },
  "pithy": {
    "phonetic": "'piθi",
    "meaning": "a. 有髓的, 由髓组成的, 简洁有力的"
  },
  "pivot": {
    "phonetic": "'pivәt",
    "meaning": "n. 枢轴, 支点, 旋转运动, 中枢, 关键人物；a. 枢轴的, (如)在枢轴上转动的；vi. 在枢轴上转动, 随着转移；vt. 装枢轴于, 以...为中心旋转；[计] 程序员交互验证和编制工具, 数据透视表"
  },
  "pixel": {
    "phonetic": "'piksәl",
    "meaning": "n. 像素；[计] 象素"
  },
  "pixie": {
    "phonetic": "'piksi",
    "meaning": "n. 妖精, 喜欢恶作剧的精灵, 小鬼；a. 淘气的, 调皮捣蛋的, 恶作剧的"
  },
  "pizza": {
    "phonetic": "'pi:tsә",
    "meaning": "n. 比萨饼"
  },
  "place": {
    "phonetic": "pleis",
    "meaning": "n. 地方, 地点, 位置, 住所, 座位, 地位, 处境, 特权, 空间, 余地, 职务, 位；vt. 放置, 寄予, 认出, 评定, 任命；vi. 名次列前"
  },
  "plaid": {
    "phonetic": "plæd",
    "meaning": "n. 格子花呢披风, 格子花呢, 格子图案"
  },
  "plain": {
    "phonetic": "plein",
    "meaning": "n. 平原, 草原, 朴实无华的东西, 无格式；a. 简单的, 明白的, 平常的, 不好看的, 朴素的, 清晰的, 普通的, 平坦的, 十足的；adv. 清楚地, 显然地；[计] 无格式"
  },
  "plait": {
    "phonetic": "pleit",
    "meaning": "n. 褶, 辫子, 麦秆条带；vt. 打褶, 编织, 把...编成辫"
  },
  "plane": {
    "phonetic": "plein",
    "meaning": "n. 平面, 扁平物, 机翼, 飞机, 水准, 地位；a. 平的, 平面的；vt. 将...刨平, 刨平, 掠过水面；vi. 翱翔, 乘飞机旅行, 刨掉"
  },
  "plank": {
    "phonetic": "plæŋk",
    "meaning": "n. 厚木板, 支架, 木板制品, 冲浪板, 救急物, 政纲条目；vt. 在...上铺板, 撂下, 立即付款"
  },
  "plant": {
    "phonetic": "plænt. plɑ:nt",
    "meaning": "n. 植物, 作物, 工厂, 树枝, 生长, 设施, 成套设备；vt. 种植, 栽培, 播种, 培养, 安置, 殖民于, 使位于；vi. 种植"
  },
  "plasm": {
    "phonetic": "plæzm",
    "meaning": "[医] 浆, 血浆, 原生质, 原浆"
  },
  "plate": {
    "phonetic": "pleit",
    "meaning": "n. 碟, 盘子, 盆中物, 金属板, 图版, 金银餐具, 印版, 金属牌(照)；vt. 镀金, 电镀, 用金属板固定, 给...装钢板, 为...制印版"
  },
  "plaza": {
    "phonetic": "'plɑ:zә",
    "meaning": "n. 广场, 市场, 购物区"
  },
  "plead": {
    "phonetic": "pli:d",
    "meaning": "vi. 辩护, 恳求；vt. 为...辩护, 提出...借口, 托称, 恳求"
  },
  "pleat": {
    "phonetic": "pli:t",
    "meaning": "n. 褶, 褶状物；vt. 打褶, 把...编成辫"
  },
  "plebe": {
    "phonetic": "pli:b",
    "meaning": "n. (军官学校)新生, 平民"
  },
  "plied": {
    "phonetic": "plaɪd",
    "meaning": "v. 使用（工具）( ply的过去式和过去分词 ); 经常供应（食物、饮料）; 固定往来; 经营生意"
  },
  "plier": {
    "phonetic": "'plaiә(r)",
    "meaning": "n. 钳子(如老虎钳,手钳,扁嘴钳等),镊子"
  },
  "plink": {
    "phonetic": "pliŋk",
    "meaning": "v. (使)发出叮当声；n. 叮当声"
  },
  "plonk": {
    "phonetic": "plɔŋk",
    "meaning": "n. (英)廉价酒, 扑通声, 叮当声；adv. 扑通一声地；vt. 用力地放下；[计] 扔垃圾"
  },
  "pluck": {
    "phonetic": "plʌk",
    "meaning": "n. 勇气, 猛拉, 动物内脏；vt. 摘, 猛拉, 拔, 拉, 扯, 采；vi. 拉, 拽"
  },
  "plumb": {
    "phonetic": "plʌm",
    "meaning": "n. 铅锤, 垂直；a. 垂直的；vt. 使垂直, 探测；vi. 成垂直"
  },
  "plume": {
    "phonetic": "plu:m",
    "meaning": "n. 羽毛, 羽毛装饰, 羽状的；vt. 用羽毛装饰, 整理羽毛, 使成羽毛状"
  },
  "plump": {
    "phonetic": "plʌmp",
    "meaning": "a. 圆胖的, 丰满的, 直接下落的, 直率的；vt. 突然放下, 支持, 使丰满, 使鼓起；vi. 扑通落下, 投票赞成, 变丰满, 鼓起；adv. 沉重地, 突然地, 直截了当地"
  },
  "plunk": {
    "phonetic": "plʌŋk",
    "meaning": "vt. 使发扑通声, 沉重地坠落；vi. 发扑通声, 支持；n. 使劲投掷, 扑通声, 扑通落下, 一美元；adv. 发出扑通声, 恰好"
  },
  "plush": {
    "phonetic": "plʌʃ",
    "meaning": "n. 长毛绒, 长毛绒裤；a. 长毛绒制的, 豪华的"
  },
  "poach": {
    "phonetic": "pәutʃ",
    "meaning": "vt. 水煮(蛋), 偷猎, 侵入, 窃取；vi. 偷猎, 陷入泥中"
  },
  "poesy": {
    "phonetic": "'pәuizi",
    "meaning": "n. 诗, 诗歌, 韵文, 诗才, 作诗法"
  },
  "point": {
    "phonetic": "pɒint",
    "meaning": "n. 点, 小数点, 标点, 地点, 要点, 特点, 尖端, 分数, 得分, 穴位；vt. 弄尖, 强调, 指出, 加标点于, 瞄准；vi. 指, 指向, 表明"
  },
  "poise": {
    "phonetic": "pɒiz",
    "meaning": "n. 平衡, 均衡, 姿势, 镇静, 安静, 砝码；vt. 使平衡, 使悬着, 保持...姿势；vi. 平衡, 悬着, 准备好"
  },
  "poked": {
    "phonetic": "pəukt",
    "meaning": "v. 伸出( poke的过去式和过去分词 ); 戳出; 拨弄; 与（某人）性交"
  },
  "poker": {
    "phonetic": "'pәukә",
    "meaning": "n. 戳的人, 拨火棍, 纸牌戏；vt. 烙制"
  },
  "pokey": {
    "phonetic": "'pәuki",
    "meaning": "n. 监狱；a. 迟钝的, 狭小的, 破旧的, 单调的"
  },
  "polar": {
    "phonetic": "'pәulә",
    "meaning": "a. 两极的, 极地的, 正好相反的, 极性的；n. 极线, 极面"
  },
  "poled": {
    "phonetic": "'pəʊld",
    "meaning": "vt.& vi. 用篙撑船, 摆船（pole的过去式与过去分词形式）"
  },
  "polio": {
    "phonetic": "",
    "meaning": "n. 脊髓灰质炎, 小儿麻痹症；[医] 脊髓灰质炎"
  },
  "polis": {
    "phonetic": "'pәulis",
    "meaning": "n. 城邦"
  },
  "polka": {
    "phonetic": "'pәulkә",
    "meaning": "n. 波尔卡舞, 女用紧身短上衣"
  },
  "polyp": {
    "phonetic": "'pɒlip",
    "meaning": "n. 息肉, 水螅虫；[医] 息肉"
  },
  "pooch": {
    "phonetic": "pu:tʃ",
    "meaning": "n. 狗, 杂种狗"
  },
  "poofy": {
    "phonetic": "'pjfi, 'pu:-",
    "meaning": "a. <俚>(男子)脂粉气的, 搞同性恋的"
  },
  "poppy": {
    "phonetic": "'pɒpi",
    "meaning": "n. 罂粟；[医] 罂粟"
  },
  "popup": {
    "phonetic": "",
    "meaning": "[电] 跃上型"
  },
  "porch": {
    "phonetic": "pɒ:tʃ",
    "meaning": "n. 门廊, 走廊"
  },
  "pored": {
    "phonetic": "",
    "meaning": "a. 有孔的"
  },
  "porky": {
    "phonetic": "'pɒ:ki",
    "meaning": "a. 猪肉的, 肥胖的"
  },
  "posed": {
    "phonetic": "",
    "meaning": "v. 主张；摆姿势；装模作样；形成（pose的过去分词）"
  },
  "poser": {
    "phonetic": "'pәuzә",
    "meaning": "n. 装腔作势者, 难题"
  },
  "posit": {
    "phonetic": "'pɒzit",
    "meaning": "vt. 假设, 安置, 布置"
  },
  "posse": {
    "phonetic": "'pɒsi",
    "meaning": "n. 一队, 一团, 地方武装团队；[法] 可能性"
  },
  "potty": {
    "phonetic": "'pɒti",
    "meaning": "a. 微小的, 不足道的；n. 便壶"
  },
  "pouch": {
    "phonetic": "pautʃ",
    "meaning": "n. 小袋, 小包, 眼袋, 邮袋, 育儿袋；vt. 装...入袋中, 使成袋状；vi. 成袋状"
  },
  "pound": {
    "phonetic": "paund",
    "meaning": "n. 磅, 英镑, 重击, 鱼塘, 拘留所, 兽栏；vt. 强烈打击, 捣烂, 监禁, 关入栏内；vi. 连续重击, 苦干"
  },
  "pouty": {
    "phonetic": "'pauti",
    "meaning": "a. 生气的, 鼓起的"
  },
  "power": {
    "phonetic": "'pauә",
    "meaning": "n. 力, 体力, 力量, 势力, 动力, 权力, 强国, 乘方, 强度, 幂, 功率；vt. 使...有力量, 供以动力, 激励；[计] 乘幂; DOS外部命令:能控制许多电池电源计算机上的电源管理特性"
  },
  "prank": {
    "phonetic": "præŋk",
    "meaning": "n. 开玩笑, 恶作剧, 戏谑；vt. 盛装, 装饰, 打扮；vi. 炫耀自己"
  },
  "prawn": {
    "phonetic": "prɒ:n",
    "meaning": "n. 明虾, 对虾；vi. 捕虾"
  },
  "preen": {
    "phonetic": "pri:n",
    "meaning": "vt. 用嘴整理, 打扮, 使得意；vi. 打扮漂亮, 感到得意"
  },
  "press": {
    "phonetic": "pres",
    "meaning": "n. 压, 揿, 按, 人群, 印刷机, 压力, 出版社, 记者, 报刊, 新闻舆论, 紧迫；vt. 压, 压榨, 紧抱, 逼迫, 推进, 强迫征募, 催逼；vi. 压, 重压, 催促, 拥挤, 奋力前进, 受压"
  },
  "price": {
    "phonetic": "prais",
    "meaning": "n. 价格, 代价, 价值；vt. 定...的价格"
  },
  "prick": {
    "phonetic": "prik",
    "meaning": "vt. 刺, 戳, 刺痛, 使竖起；vi. 刺, 竖起；n. 扎, 一刺, 刺痛；a. 竖起的"
  },
  "pricy": {
    "phonetic": "'praisi",
    "meaning": "a. 昂贵的, 价格高的"
  },
  "pride": {
    "phonetic": "praid",
    "meaning": "n. 骄傲, 自尊心, 自豪, 精华, 勇气；vt. 以...自豪"
  },
  "pried": {
    "phonetic": "praɪd",
    "meaning": "v. 打听, 刺探（他人的私事）( pry的过去式和过去分词 ); 撬开"
  },
  "prima": {
    "phonetic": "'pri:mә",
    "meaning": "a. 第一的, 主要的"
  },
  "prime": {
    "phonetic": "praim",
    "meaning": "n. 最佳部分, 初期, 全盛期；a. 主要的, 最初的, 根本的；v. 加油启动, 灌注, 填装"
  },
  "primo": {
    "phonetic": "'pri:mәu",
    "meaning": "a. 第一的；首先的"
  },
  "primp": {
    "phonetic": "primp",
    "meaning": "v. 打扮, 装饰"
  },
  "print": {
    "phonetic": "print",
    "meaning": "n. 打印, 版, 印刷物, 痕迹, 印刷业, 印刷字体, 图片, 印花布, 印章；v. 打印, 印刷, 铭记, 留印记于, 用印刷体写；[计] DOS外部命令:在打印机上打印文件, 可一边打印文件一边执行其他工作"
  },
  "prion": {
    "phonetic": "ˈpri:ɒn",
    "meaning": "n. 感染性蛋白质, 普列昂; 锯鹱"
  },
  "prior": {
    "phonetic": "'praiә",
    "meaning": "a. 更重要的, 较早的, 在先的；n. 小隐修院院长, 大隐修院副院长"
  },
  "prism": {
    "phonetic": "'prizm",
    "meaning": "n. 棱镜, 棱柱；[化] 棱镜"
  },
  "priss": {
    "phonetic": "pris",
    "meaning": "n. 娇女孩(或女子), 娇气的人, 脂粉气的男子"
  },
  "privy": {
    "phonetic": "'privi",
    "meaning": "a. 个人的, 私人的, 秘密的, 隐蔽的；n. 有利害关系的人, 当事人, 厕所"
  },
  "prize": {
    "phonetic": "praiz",
    "meaning": "n. 奖赏, 奖金, 奖品, 战利品, 捕获；a. 得奖的；vt. 珍视, 估价, 捕获, 撬, 撬动"
  },
  "probe": {
    "phonetic": "prәub",
    "meaning": "n. 探索, 调查, 探针, 探测器；v. 用探针探测, 调查, 探索"
  },
  "prole": {
    "phonetic": "prәul",
    "meaning": "n. 无产者"
  },
  "promo": {
    "phonetic": "'prәumәu",
    "meaning": "n. 商品广告；商品推销"
  },
  "prone": {
    "phonetic": "prәun",
    "meaning": "a. 俯伏的, 面向下的, 有...倾向的；[医] 旋前的, 伏的, 俯的"
  },
  "prong": {
    "phonetic": "prɒŋ",
    "meaning": "n. 叉状物, 耙子；vt. 刺, 贯穿, 翻掘"
  },
  "proof": {
    "phonetic": "pru:f",
    "meaning": "n. 证据, 证明, 试验, 检验, 考验；a. 不能透入的, 证明用的, 防...的, 耐...的；vt. 检验, 试验, 校对, 使不被穿透；[计] 审稿"
  },
  "prose": {
    "phonetic": "prәuz",
    "meaning": "n. 散文；v. 写散文；a. 散文的, 平凡的"
  },
  "proto": {
    "phonetic": "",
    "meaning": "[计] 原型, 样机, 典型"
  },
  "proud": {
    "phonetic": "praud",
    "meaning": "a. 骄傲的, 自大的, 自豪的, 辉煌的, 壮丽的"
  },
  "prove": {
    "phonetic": "pru:v",
    "meaning": "vt. 证明, 查验, 检验, 勘探, 显示；vi. 证明是"
  },
  "prowl": {
    "phonetic": "praul",
    "meaning": "n. 潜行, 徘徊, 悄悄踱步；vi. 潜行以觅食, 徘徊；vt. 徘徊"
  },
  "proxy": {
    "phonetic": "'prɒksi",
    "meaning": "n. 代理, 代理人, 委托书；[经] 代理人, 代表权, 授权书"
  },
  "prude": {
    "phonetic": "pru:d",
    "meaning": "n. 拘守礼仪的人, 故作正经的人"
  },
  "prune": {
    "phonetic": "pru:n",
    "meaning": "n. 洋李, 李子干, 深紫红色, 傻瓜；vt. 修剪, 砍掉, 删除；vi. 删除, 删节"
  },
  "psalm": {
    "phonetic": "sɑ:m",
    "meaning": "n. 圣诗, 圣歌, 诗篇；vt. 唱(圣歌)"
  },
  "pshaw": {
    "phonetic": "ʃɒ:",
    "meaning": "interj. 啐(表示不耐烦、轻蔑), 哼；n. 啐声, 哼声；v. 发啐声"
  },
  "psych": {
    "phonetic": "saik",
    "meaning": "vt. 精神分析治疗, 使作好心理准备"
  },
  "psyop": {
    "phonetic": "'sai,ɔp",
    "meaning": "[美军]心理战行动"
  },
  "pubic": {
    "phonetic": "'pju:bik",
    "meaning": "a. 阴部的, 耻骨的；[医] 耻骨的"
  },
  "pubis": {
    "phonetic": "'pju:bis",
    "meaning": "n. 耻骨；[医] 耻骨"
  },
  "pudge": {
    "phonetic": "pʌdʒ",
    "meaning": "n. 矮胖的人, 短而粗的东西"
  },
  "pudgy": {
    "phonetic": "'pʌdʒi",
    "meaning": "a. 矮胖的"
  },
  "puffy": {
    "phonetic": "'pʌfi",
    "meaning": "a. 胀大的, 肥胖的, 喘气的, 一阵阵吹的；[医] 虚肿的, 浮肿的"
  },
  "puked": {
    "phonetic": "pju:kt",
    "meaning": "v. 呕吐( puke的过去式和过去分词 )"
  },
  "pulpy": {
    "phonetic": "'pʌlpi",
    "meaning": "a. 果肉状的, 纸浆状的, 泥状的；[医] 髓样的, 软的"
  },
  "pulse": {
    "phonetic": "pʌls",
    "meaning": "n. 脉冲, 脉搏, 情绪, 意向, 拍子, 豆类；vi. 跳动, 脉跳；vt. 使跳动, 用脉冲调制；[计] 脉冲"
  },
  "punch": {
    "phonetic": "pʌntʃ",
    "meaning": "n. 打洞器, 钻孔机, 冲压机, 冲床, 潘趣酒；vt. 以拳重击, 开洞, 冲压；vi. 用拳猛击"
  },
  "punky": {
    "phonetic": "'pʌŋkɪ",
    "meaning": "a. 含火绒（或朽木）的; 松软的; 有弹性的; 闷烧的"
  },
  "punny": {
    "phonetic": "'pʌni",
    "meaning": "a. 一语双关的"
  },
  "pupae": {
    "phonetic": "'pju:pi:",
    "meaning": "pl. 蛹"
  },
  "pupil": {
    "phonetic": "'pju:pl",
    "meaning": "n. 学生, 门生, 未成年人, 瞳孔；[医] 瞳孔"
  },
  "puppy": {
    "phonetic": "'pʌpi",
    "meaning": "n. 小狗, 小动物, 自负的年轻人"
  },
  "puree": {
    "phonetic": "'pjjәrei",
    "meaning": "n. 菜泥, 果泥, 酱, 浓汤；vt. 把...制成浓汤/酱"
  },
  "purer": {
    "phonetic": "",
    "meaning": "n. 提纯器；a. 更纯的；更洁净的（pure的比较级）"
  },
  "purge": {
    "phonetic": "pә:dʒ",
    "meaning": "n. 净化, 清除, 泻药；v. (使)净化, 清除, (使)通便；[计] 服务器文件删除实用程序"
  },
  "purse": {
    "phonetic": "pә:s",
    "meaning": "n. 钱包, 小钱袋, 金钱, 募捐款, 囊状物；v. 缩拢, 皱起"
  },
  "pushy": {
    "phonetic": "'puʃi",
    "meaning": "a. 粗鲁的, 固执己见的, 好胜而爱出风头的"
  },
  "putty": {
    "phonetic": "'pʌti",
    "meaning": "n. 油灰, 淡灰色, 氧化锡；vt. 用油灰填塞"
  },
  "pwned": {
    "phonetic": "",
    "meaning": ""
  },
  "pygmy": {
    "phonetic": "'pigmi",
    "meaning": "n. 矮人, 侏儒；a. 矮小的"
  },
  "pylon": {
    "phonetic": "'pailɒn",
    "meaning": "n. 标塔, 路标塔；[医] 暂用假肢"
  },
  "quack": {
    "phonetic": "kwæk",
    "meaning": "n. 鸭叫声, 冒牌医生, 冒充内行之人；a. 冒牌医生的；v. 嘎嘎叫, 当冒牌医生, 夸大广告"
  },
  "quaff": {
    "phonetic": "kwæf",
    "meaning": "v. 狂饮, 大口地喝；n. 大口喝下的酒, 痛饮"
  },
  "quail": {
    "phonetic": "kweil",
    "meaning": "n. 鹌鹑；vi. 胆怯, 畏缩"
  },
  "quake": {
    "phonetic": "kweik",
    "meaning": "vi. 颤抖, 地震；n. 颤抖, 地震"
  },
  "qualm": {
    "phonetic": "kwɒ:m",
    "meaning": "n. 晕眩, 不安, 疑虑；[法] 疑虑, 不安, 内疚"
  },
  "quant": {
    "phonetic": "kwænt",
    "meaning": "n. 篙；v. 用篙撑"
  },
  "quark": {
    "phonetic": "kwɑ:k",
    "meaning": "n. 夸克；[化] 夸克"
  },
  "quart": {
    "phonetic": "kwɒ:t",
    "meaning": "n. 夸脱；[医] 夸脱(四分之一加仑)"
  },
  "quash": {
    "phonetic": "kwɒʃ",
    "meaning": "vt. 撤销, 平息, 镇压；[法] 撤销, 废止, 宣布无效"
  },
  "quasi": {
    "phonetic": "'kwɑ:zi:",
    "meaning": "a. 类似的, 准的；[经] 半, 准; 类似的"
  },
  "queen": {
    "phonetic": "'kwi:n",
    "meaning": "n. 王后, 女王；vt. 立为女王；vi. 做女王"
  },
  "queer": {
    "phonetic": "kwiә",
    "meaning": "n. 怪人, 同性恋者；a. 奇怪的, 不舒服的, 可疑的；vt. 搞糟"
  },
  "quell": {
    "phonetic": "kwel",
    "meaning": "vt. 压制, 平息, 减轻"
  },
  "query": {
    "phonetic": "'kwiәri",
    "meaning": "n. 疑问, 疑问号, 质问, 查询；v. 询问, 质问；[计] 查询"
  },
  "quest": {
    "phonetic": "kwest",
    "meaning": "n. 探索, 寻求, 调查；v. 寻找, 找, 追寻猎物"
  },
  "queue": {
    "phonetic": "kju:",
    "meaning": "n. 辫子, 一队人, 队列；vt. 使排队, 将...梳成辫子；vi. 排队；[计] 队列"
  },
  "quick": {
    "phonetic": "kwik",
    "meaning": "a. 快的, 迅速的, 敏捷的, 灵敏的, 急速的；adv. 快；n. 新长出的肉, 要害, 核心, 感觉敏锐部位"
  },
  "quiet": {
    "phonetic": "'kwaiәt",
    "meaning": "n. 安静, 闲适, 平静；a. 安静的, 静止的, 寂静的, 朴素的, 从容的, 暗中的；vi. 平静下来；vt. 使平静, 使平息, 使安心, 安慰"
  },
  "quill": {
    "phonetic": "kwil",
    "meaning": "n. 羽根, 大翎毛, 羽毛笔；vt. 刺穿"
  },
  "quilt": {
    "phonetic": "kwilt",
    "meaning": "n. 棉被；vt. 加软衬料后缝制, 东拼西凑地编；vi. 缝被子"
  },
  "quirk": {
    "phonetic": "kwә:k",
    "meaning": "n. 古怪举动, 俏皮话, 急转"
  },
  "quite": {
    "phonetic": "kwait",
    "meaning": "adv. 相当, 完全, 十分"
  },
  "quota": {
    "phonetic": "'kwәutә",
    "meaning": "n. 配额, 限额；[化] 定额"
  },
  "quote": {
    "phonetic": "kwәut",
    "meaning": "n. 引用；vt. 引述, 举证, 报(价)；vi. 引用"
  },
  "quoth": {
    "phonetic": "kwәuθ",
    "meaning": "vt. [古]说"
  },
  "quran": {
    "phonetic": "kj'rɑ:n, -'ræn",
    "meaning": "n. (伊斯兰教)可兰经"
  },
  "rabbi": {
    "phonetic": "'ræbai",
    "meaning": "n. 拉比(犹太教圣职人员), 大师(对犹太学者的尊称)；[法] 犹太教的法学博士, 老师, 犹太教教士"
  },
  "rabid": {
    "phonetic": "'ræbid",
    "meaning": "a. 猛烈的, 热烈的, 急进的, 狂怒的, 偏激的, 疯狂的；[医] 狂犬病的, 咬病的"
  },
  "raced": {
    "phonetic": "",
    "meaning": "vt.& vi. 和…比速度, （使）参加比赛（race的过去式与过去分词形式）"
  },
  "racer": {
    "phonetic": "'reisә",
    "meaning": "n. 比赛者, 游蛇属黑蛇"
  },
  "radar": {
    "phonetic": "'reidә",
    "meaning": "n. 雷达, 无线电探测器；[计] 雷达图"
  },
  "radii": {
    "phonetic": "'reidiai",
    "meaning": "pl. 半径；[医] 半径, 辐射线(解)"
  },
  "radio": {
    "phonetic": "'reidiәu",
    "meaning": "n. 无线电, 收音机, 无线电报, 无线电广播, 无线电台；v. 用无线电发送"
  },
  "radon": {
    "phonetic": "'reidɒn",
    "meaning": "n. 氡；[化] 氡Rn"
  },
  "raged": {
    "phonetic": "",
    "meaning": "vi. 大发脾气, 动怒（rage的过去式与过去分词形式）"
  },
  "rainy": {
    "phonetic": "'reini",
    "meaning": "a. 下雨的, 多雨的"
  },
  "raise": {
    "phonetic": "reiz",
    "meaning": "n. 上升, 高地, 增高；vt. 升起, 举起, 唤起, 提高, 使出现, 使复活, 提出, 筹集, 饲养"
  },
  "rajah": {
    "phonetic": "'rɑ:dʒә",
    "meaning": "n. 印度王公, 统治者"
  },
  "raked": {
    "phonetic": "reɪkt",
    "meaning": "v. 搜索( rake的过去式和过去分词 ); 以耙子耙平（泥土等）; 用耙子把…耙在一起; （翻阅旧记录、文件等以）搜寻事实等"
  },
  "rally": {
    "phonetic": "'ræli",
    "meaning": "n. 重振旗鼓, 集合, 群众集会, 跌停回升；v. 重整旗鼓, 集合, 恢复精神, 团结, 挖苦, 嘲笑"
  },
  "ralph": {
    "phonetic": "reif, rælf",
    "meaning": "n. 拉尔夫（男子名）"
  },
  "ramen": {
    "phonetic": "'rɑːmen",
    "meaning": "n. 拉面；面条"
  },
  "ranch": {
    "phonetic": "ræntʃ. rɑ:ntʃ",
    "meaning": "n. 大牧场；v. 经营牧场"
  },
  "randy": {
    "phonetic": "'rændi",
    "meaning": "a. 喧闹的, 大声的, 好色的；n. 粗鲁悍妇, 莽汉"
  },
  "range": {
    "phonetic": "'reindʒ",
    "meaning": "n. 排, 行, 山脉, 范围, 行列, 射程；vt. 排列, 归类于, 使并列, 放牧；vi. 平行, 延伸, 漫游；[计] 量程; 范围; 域; 距离"
  },
  "rangy": {
    "phonetic": "'reindʒi",
    "meaning": "a. 适于远行的, 广阔的, 四肢修长的"
  },
  "rapid": {
    "phonetic": "'ræpid",
    "meaning": "a. 迅速的, 飞快的, 急促的, 陡的；n. 急流"
  },
  "rarer": {
    "phonetic": "",
    "meaning": "a. 更稀罕的；更珍贵的（rare的比较级）"
  },
  "raspy": {
    "phonetic": "'ræspi",
    "meaning": "a. 刺耳的, 粗糙的, 易怒的"
  },
  "rated": {
    "phonetic": "'reitid",
    "meaning": "[电] 额定的"
  },
  "rater": {
    "phonetic": "'reitә",
    "meaning": "n. 定价人"
  },
  "ratio": {
    "phonetic": "'reiʃәu",
    "meaning": "n. 比, 比率；[医] 比, 比率, 比例"
  },
  "ratty": {
    "phonetic": "'ræti",
    "meaning": "a. 像老鼠的, 鼠臭的, 破烂的, 易怒的"
  },
  "raved": {
    "phonetic": "reivd",
    "meaning": "v. 胡言乱语( rave的过去式和过去分词 ); 愤怒地说; 咆哮; 痴心地说"
  },
  "raven": {
    "phonetic": "'reivn",
    "meaning": "n. 渡鸦, 掠夺；a. 乌黑的；v. 掠夺, 狼吞虎咽"
  },
  "raver": {
    "phonetic": "'reivә(r)",
    "meaning": "n. 说胡话的人, 社交场常客"
  },
  "rayon": {
    "phonetic": "'reiɒn",
    "meaning": "n. 人造丝；[化] 人造纤维; 人造丝"
  },
  "razed": {
    "phonetic": "reɪzd",
    "meaning": "v. 彻底摧毁, 将…夷为平地( raze的过去式和过去分词 )"
  },
  "razor": {
    "phonetic": "'reizә",
    "meaning": "n. 剃刀；vt. 剃"
  },
  "reach": {
    "phonetic": "ri:tʃ",
    "meaning": "n. 伸出, 延伸, 区域, 范围, 流域, 岬；vt. 到达, 达到, 伸出, 延伸, 影响；vi. 达到, 延伸, 伸出手, 传到"
  },
  "react": {
    "phonetic": "ri'ækt",
    "meaning": "vi. 起反应, 起作用, 反攻；[医] 应答, 发生反应"
  },
  "ready": {
    "phonetic": "'redi",
    "meaning": "n. 预备好的状态, 现款；a. 准备好的, 备用的, 可以使用的；adv. 预先, 迅速；vt. 使准备好"
  },
  "realm": {
    "phonetic": "relm",
    "meaning": "n. 王国, 领土, 领域；[计] 领域"
  },
  "rearm": {
    "phonetic": "ri:'ɑ:m",
    "meaning": "v. 重整军备, 重新武装"
  },
  "rebar": {
    "phonetic": "ri'bɑ:",
    "meaning": "钢筋, 螺纹钢筋"
  },
  "rebel": {
    "phonetic": "'rebl",
    "meaning": "n. 叛徒, 反叛者；vi. 造反, 反抗, 抵抗, 反感；a. 造反的, 反抗的"
  },
  "rebid": {
    "phonetic": "'rebɪd",
    "meaning": "v. 再叫牌, 第二次叫牌"
  },
  "rebus": {
    "phonetic": "'ri:bәs",
    "meaning": "n. 谜, 画谜"
  },
  "rebut": {
    "phonetic": "ri'bʌt",
    "meaning": "vi. 反驳；vt. 辩驳, 反驳, 揭露"
  },
  "recap": {
    "phonetic": "ri:'kæp",
    "meaning": "vt. 翻新胎面；n. 翻新的轮胎"
  },
  "recon": {
    "phonetic": "'ri:kɒn",
    "meaning": "n. 侦察, 交换子；[计] 追溯转换"
  },
  "recur": {
    "phonetic": "ri'kә:",
    "meaning": "vi. 复发, 回到, 重现, 再来, 诉诸, 采用, 循环"
  },
  "recut": {
    "phonetic": "reɪ'kʌt",
    "meaning": "v. 再切, 重切"
  },
  "redid": {
    "phonetic": "ri:'did",
    "meaning": "vbl.再做, 重做(redo的过去式)"
  },
  "redux": {
    "phonetic": "ri:'dʌks",
    "meaning": "a. 回来的, 回家的"
  },
  "reedy": {
    "phonetic": "'ri:di",
    "meaning": "a. 芦苇丛生的, 芦苇做的, 芦苇状的"
  },
  "refer": {
    "phonetic": "ri'fә:",
    "meaning": "vt. 提交, 归诸于, 把...提交, 使求助于；vi. 提到, 涉及, 查阅, 查询, 咨询"
  },
  "refit": {
    "phonetic": ".ri:'fit",
    "meaning": "v. 整修, 改装；n. 整修, 改装"
  },
  "regal": {
    "phonetic": "'ri:gl",
    "meaning": "a. 帝王的, 适于帝王的"
  },
  "rehab": {
    "phonetic": "'ri:hæb",
    "meaning": "n. 修复（等于rehabilitation）"
  },
  "reify": {
    "phonetic": "'ri:ifai",
    "meaning": "vt. 使具体化, 使人为物"
  },
  "reign": {
    "phonetic": "rein",
    "meaning": "v. 为王，为君；当政；统治；n. 为王，为君；当政；统治"
  },
  "reiki": {
    "phonetic": "",
    "meaning": "灵气疗法（通过触摸向人体内输送能量）"
  },
  "relax": {
    "phonetic": "ri'læks",
    "meaning": "vi. 放松, 松懈, 松弛, 变从容, 休息, 休养；vt. 使松弛, 缓和, 使松懈, 使休息"
  },
  "relay": {
    "phonetic": "'ri:lei",
    "meaning": "n. 驿马, 替班, 中继, 接力；vt. 分程传递, 转播, 使接替；vi. 接力传送, 转播"
  },
  "relic": {
    "phonetic": "'relik",
    "meaning": "n. 遗物, 遗迹, 纪念物, 遗风, 残留物"
  },
  "remap": {
    "phonetic": "'ri:,mæp",
    "meaning": "[计] 再交换, 再变换"
  },
  "remit": {
    "phonetic": "ri'mit",
    "meaning": "vt. 宽恕, 赦免, 免除, 汇出, 缓解, 减轻, 把...提交, 使恢复原状, 推迟；vi. 缓解, 汇款；n. 移交的事物"
  },
  "remix": {
    "phonetic": "ri:'miks",
    "meaning": "vt. 使再混合；再搅拌；重新合成（乐曲等）"
  },
  "renal": {
    "phonetic": "'ri:nl",
    "meaning": "a. 肾脏的, 肾的；[医] 肾的"
  },
  "renew": {
    "phonetic": "ri'nju:",
    "meaning": "vt. 使更新, 使恢复, 复兴, 修补, 补充, 继续, 重订, 重申, 续借；vi. 更新, 重新开始"
  },
  "repay": {
    "phonetic": "ri'pei",
    "meaning": "v. 偿还, 报答, 报复"
  },
  "repel": {
    "phonetic": "ri'pel",
    "meaning": "vt. 逐退, 抵制, 使厌恶, 抗御；vi. 使厌恶, 相互排斥"
  },
  "reply": {
    "phonetic": "ri'plai",
    "meaning": "n. 答复, 回答, 答辩；vi. 答复, 回答, 回击, 反响, 答辩；vt. 回答；[计] 答复"
  },
  "reran": {
    "phonetic": "ˌri:ˈræn",
    "meaning": "v. 再播放( rerun的过去式 ); 重新开动, 重新进行"
  },
  "rerun": {
    "phonetic": "ri:'rʌn",
    "meaning": "n. 重新开动, 再度上演；vt. 重新开动, 再度上演；[计] 再运行; 重新运行"
  },
  "resaw": {
    "phonetic": "re'zɔ:",
    "meaning": "再锯, 解锯"
  },
  "reset": {
    "phonetic": ".ri:'set",
    "meaning": "n. 重新设定, 重新组合, 重排版；vt. 重新设定, 重置, 重新组合；vi. 重置, 清零；[计] 重置, 清零"
  },
  "resin": {
    "phonetic": "'rezin",
    "meaning": "n. 树脂；vt. 涂树脂于"
  },
  "retch": {
    "phonetic": "retʃ",
    "meaning": "vi. 作呕, 反胃；vt. 呕吐；n. 反胃, 呕吐声"
  },
  "retie": {
    "phonetic": "rɪ'tɑɪ",
    "meaning": "重捆; 重绑; 重扎; 重系"
  },
  "retro": {
    "phonetic": "'retrәu",
    "meaning": "n. 制动火箭, 减速火箭；（服装式样等）重新流行"
  },
  "retry": {
    "phonetic": ".ri:'trai",
    "meaning": "vt. 再试, 再审；[计] 重发; 重试"
  },
  "reuse": {
    "phonetic": "ri:'ju:z",
    "meaning": "vt. 再使用；n. 重新使用"
  },
  "revel": {
    "phonetic": "'revl",
    "meaning": "n. 作乐, 狂欢；vi. 狂欢作乐, 陶醉, 着迷；vt. 耗费"
  },
  "revue": {
    "phonetic": "ri'vju:",
    "meaning": "n. 时事剧, 活报剧"
  },
  "rewon": {
    "phonetic": "",
    "meaning": "再赢, 赢回( rewin的过去式和过去分词 )"
  },
  "rheum": {
    "phonetic": "ru:m",
    "meaning": "n. 发炎性分泌物, 鼻粘膜炎, 感冒, 稀粘液, 大黄；[医] 稀粘液"
  },
  "rhino": {
    "phonetic": "'rainәu",
    "meaning": "n. 钱, 现金, 犀牛"
  },
  "rhyme": {
    "phonetic": "raim",
    "meaning": "n. 韵, 押韵, 韵文；vi. 押韵；vt. 使押韵, 用韵诗表达"
  },
  "ricin": {
    "phonetic": "'raisin",
    "meaning": "n. 篦麻毒；[化] 蓖麻毒; 蓖麻子白蛋白"
  },
  "rider": {
    "phonetic": "'raidә",
    "meaning": "n. 骑手, (文件后的)附件, 扶手；[化] 游码"
  },
  "ridge": {
    "phonetic": "ridʒ",
    "meaning": "n. 脊, 山脊, 山脉；[医] 嵴, 脊, 棱线"
  },
  "rifle": {
    "phonetic": "'raifl",
    "meaning": "n. 来复枪, 步枪；vt. 用步枪射击, 抢夺；vi. (抱有不良意图)迅速翻查"
  },
  "right": {
    "phonetic": "rait",
    "meaning": "n. 权利, 右边, 正义, 右派, 公正；a. 正确的, 对的, 恰当的, 正常的, 正直的, 正面的, 右方的；adv. 正确地, 以有利结果, 一直, 直接, 向右；vt. 扶直, 整理, 纠正, 伸冤, 使昭雪；vi. 恢复平衡；[计] 右, 权利"
  },
  "rigid": {
    "phonetic": "'ridʒid",
    "meaning": "a. 坚硬的, 刚性的, 严格的, 精密的, 刻板的"
  },
  "rigor": {
    "phonetic": "'rigә",
    "meaning": "n. 严格, 严厉, 苛刻, 严酷, 严密, 精确；[医] 寒战, 强直, 僵硬"
  },
  "riled": {
    "phonetic": "raɪld",
    "meaning": "v. 惹恼, 激怒( rile的过去式和过去分词 )"
  },
  "rinse": {
    "phonetic": "rins",
    "meaning": "n. 清洗, 染发, 染发剂；vt. 以清水冲洗, 漱, 漂清；vi. 被漂净"
  },
  "ripen": {
    "phonetic": "'raipәn",
    "meaning": "vt. 使成熟；vi. 成熟"
  },
  "riper": {
    "phonetic": "raipə",
    "meaning": "a. 成熟的( ripe的比较级 ); 时机成熟的; 强烈的; 口味浓郁的"
  },
  "risen": {
    "phonetic": "'rizәn",
    "meaning": "a. 升起的, 复活的；rise的过去分词"
  },
  "riser": {
    "phonetic": "'raizә",
    "meaning": "n. 起床者, 叛徒, 起义者, 竖板；[化] 上升管"
  },
  "risky": {
    "phonetic": "'riski",
    "meaning": "a. 危险的"
  },
  "ritzy": {
    "phonetic": "'ritsi",
    "meaning": "a. 豪华的, 时髦的, 讲究的"
  },
  "rival": {
    "phonetic": "'raivl",
    "meaning": "n. 对手, 竞争者；a. 竞争的"
  },
  "riven": {
    "phonetic": "'rivәn",
    "meaning": "rive的过去分词"
  },
  "river": {
    "phonetic": "'rivә",
    "meaning": "n. 河, 江；[法] 河流, 江河, 内河"
  },
  "rivet": {
    "phonetic": "'rivit",
    "meaning": "n. 铆钉；vt. 用铆钉固定, 敲进去, 注目, 吸引住"
  },
  "roach": {
    "phonetic": "rәutʃ",
    "meaning": "n. 斜齿鳊；vt. 使成凹状"
  },
  "roast": {
    "phonetic": "rәust",
    "meaning": "n. 烤肉, 烘烤, 嘲笑；a. 烘烤的, 烤过的；vt. 烤, 炙, 烘焙, 嘲笑；vi. 烤, 炙, 烘焙"
  },
  "robed": {
    "phonetic": "rəʊb",
    "meaning": "n. 长袍, 礼服；制服；vi. 穿长袍；vt. 使穿长袍；n. (Robe)人名；(德、罗、塞)罗贝；(英、法)罗布"
  },
  "robin": {
    "phonetic": "'rɒbin",
    "meaning": "n. 旅鸫；[医] 刺槐毒素"
  },
  "robot": {
    "phonetic": "'rәubәt",
    "meaning": "n. 机械人, 自动机械, 机械般工作的人；[计] 机器人; 自动机"
  },
  "rocky": {
    "phonetic": "'rɒki",
    "meaning": "a. 岩石的, 多石的, 像岩石的, 无情的, 摇动的, 摇晃的"
  },
  "rodeo": {
    "phonetic": "rәu'deiәu",
    "meaning": "n. 竞技表演；[经] 牛市场"
  },
  "roger": {
    "phonetic": "'rɔdʒә",
    "meaning": "interj. 对!, 行!, 好!"
  },
  "rogue": {
    "phonetic": "rәug",
    "meaning": "n. 恶棍, 流氓, 小淘气；vt. 欺骗；vi. 游手好闲"
  },
  "roman": {
    "phonetic": "'rәumәn",
    "meaning": "n. 罗马人；a. 罗马人的, 罗马的"
  },
  "roomy": {
    "phonetic": "'ru:mi",
    "meaning": "a. 广阔的, 宽敞的, 宽大的"
  },
  "roost": {
    "phonetic": "ru:st",
    "meaning": "n. 栖木, 休息所, 群栖的禽鸟；vi. 栖息, 安歇；vt. 使栖息"
  },
  "roped": {
    "phonetic": "",
    "meaning": "vt. （用绳子）捆（rope的过去式与过去分词形式）"
  },
  "roper": {
    "phonetic": "'rәjpә(r)",
    "meaning": "n. 制绳者, <美>用索套捕牲口的牧人,诱人进入赌场者"
  },
  "rosin": {
    "phonetic": "'rɒzin",
    "meaning": "n. 松香, 松脂；vt. 用松香涂"
  },
  "rotor": {
    "phonetic": "'rәutә",
    "meaning": "n. 转子, 旋筒, 转动体；[化] 转鼓; 转轴"
  },
  "rouge": {
    "phonetic": "ru:ʒ",
    "meaning": "n. 口红, 胭脂；v. 擦口红"
  },
  "rough": {
    "phonetic": "rʌf",
    "meaning": "n. 粗糙的东西, 毛坯, 未加工品, 梗概, 草图, 暴徒, 艰难；a. 粗糙的, 粗暴的, 蓬乱的, 草率的, 大致的, 简陋的, 暴风雨的, 艰难的；vt. 使粗糙, 使不平, 使蓬乱, 粗制, 草拟, 粗暴对待, 对...动粗；vi. 变粗糙；adv. 粗糙地, 粗暴地"
  },
  "round": {
    "phonetic": "raund",
    "meaning": "n. 圆, 圆形物, 巡回, 循环, 一轮, 一回合, 一局, 范围, 轮唱；a. 圆的, 球形的, 丰满的, 肥胖的, 完全的, 大概的, 完美的, 圆润的；prep. 围着, 附近, 绕过, 在...周围；adv. 围绕着, 在周围, 迂回地, 挨个, 朝反方向；vt. 弄圆, 使成圆形, 绕行, 完成, 围捕, 把...四舍五入；vi. 变圆, 发胖, 环行, 拐弯, 进展"
  },
  "rouse": {
    "phonetic": "rauz",
    "meaning": "n. 觉醒, 奋起, 干杯；vt. 唤醒, 鼓舞, 激动, 使振奋, 惊起；vi. 醒来, 奋起"
  },
  "route": {
    "phonetic": "ru:t",
    "meaning": "n. 路径, 途径, 路线；vt. 确定路线, 按规定路线发送；[计] 传递, 路由设定程序"
  },
  "roved": {
    "phonetic": "rəʊvd",
    "meaning": "v. 流浪( rove的过去式和过去分词 ); 漂泊; 徘徊; （指眼睛）环顾"
  },
  "rover": {
    "phonetic": "'rәuvә",
    "meaning": "n. 漂泊者, 流浪者, 海盗；[法] 流浪者, 海盗, 海盗船"
  },
  "rowdy": {
    "phonetic": "'raudi",
    "meaning": "n. 好吵闹的人；a. 吵闹的"
  },
  "rowed": {
    "phonetic": "rəud",
    "meaning": "v. 划船( row的过去式和过去分词 ); （用船）划运; 用…支桨划; 充当划手"
  },
  "rower": {
    "phonetic": "'rәuә",
    "meaning": "n. 桨手"
  },
  "royal": {
    "phonetic": "'rɒiәl",
    "meaning": "n. 王室, 皇族；a. 王室的, 皇家的, 盛大的, 庄严的"
  },
  "ruble": {
    "phonetic": "'ru:bl",
    "meaning": "n. 卢布(俄国货币)"
  },
  "ruddy": {
    "phonetic": "'rʌdi",
    "meaning": "a. 红的, 红润的；v. (使)变红"
  },
  "ruder": {
    "phonetic": "",
    "meaning": "n. (Ruder)人名；(英、德、瑞典)鲁德；a. 粗糙的；无礼的（rude的比较级）"
  },
  "rugby": {
    "phonetic": "'rʌ^bi",
    "meaning": "n. 橄榄球, 橄榄球赛"
  },
  "ruing": {
    "phonetic": "ru:ɪŋ",
    "meaning": "v. 对…感到后悔( rue的现在分词 ); 活羊拔毛"
  },
  "ruled": {
    "phonetic": "",
    "meaning": "a. 有横隔线的；有直线行的；受统治的"
  },
  "ruler": {
    "phonetic": "'ru:lә",
    "meaning": "n. 统治者, 管理者, 尺, 直尺；n. 划线板；[计] 标尺"
  },
  "rumba": {
    "phonetic": "'rʌmbә",
    "meaning": "n. 伦巴舞；vi. 跳伦巴舞"
  },
  "rummy": {
    "phonetic": "'rʌmi",
    "meaning": "a. 朗姆酒的, 奇妙的, 古怪的；n. 酒鬼, 拉米纸牌戏"
  },
  "rumor": {
    "phonetic": "'ru:mә",
    "meaning": "n. 谣言, 传闻；vt. 谣传"
  },
  "runny": {
    "phonetic": "'rʌni",
    "meaning": "a. 松软的, 水分过多的, 流鼻涕的"
  },
  "runup": {
    "phonetic": "",
    "meaning": "n. 迅速增大；上坡；起转"
  },
  "rupee": {
    "phonetic": "ru:'pi:",
    "meaning": "n. 卢比(印、巴等国货币单位)"
  },
  "rural": {
    "phonetic": "'ruәrәl",
    "meaning": "a. 乡下的, 田园的, 乡村风味的；[法] 农村的, 乡村的, 有关农业的"
  },
  "rusty": {
    "phonetic": "'rʌsti",
    "meaning": "a. 生锈的, 腐蚀的, 生疏的, 顽固的, 腐烂的；[医] 锈色的"
  },
  "saber": {
    "phonetic": "'seibә",
    "meaning": "n. 军刀, 骑兵；vt. 用马刀砍"
  },
  "sable": {
    "phonetic": "'seibl",
    "meaning": "n. 黑貂, 黑貂皮, 深褐色, 丧服；a. 黑貂皮的, 黑色的, 昏暗的"
  },
  "sabre": {
    "phonetic": "'seibә",
    "meaning": "n. 军刀, 骑兵；vt. 用马刀砍"
  },
  "sadly": {
    "phonetic": "'sædli",
    "meaning": "adv. 悲痛地, 悲惨地, 悲伤地, 说来遗憾"
  },
  "safer": {
    "phonetic": "",
    "meaning": "a. 更安全（safe的比较级）"
  },
  "saggy": {
    "phonetic": "'sægi",
    "meaning": "a. 松懈的, 下垂的"
  },
  "saint": {
    "phonetic": "seint",
    "meaning": "n. 圣徒, 圣人；a. 神圣的；[计] 自动积分程序符号"
  },
  "salad": {
    "phonetic": "'sælәd",
    "meaning": "n. 色拉"
  },
  "sally": {
    "phonetic": "'sæli",
    "meaning": "n. 突击, 出击, 远足；vi. 突击, 出击, 出发"
  },
  "salon": {
    "phonetic": "'sælɔ:ŋ",
    "meaning": "n. 大会客室, 大厅, 客厅, 交谊室, 沙龙, 美术展览馆, 画廊, 美容院, 发廊"
  },
  "salsa": {
    "phonetic": "'sɑ:lsә",
    "meaning": "n. 洋葱做的辣调味汁；萨尔萨舞曲"
  },
  "salty": {
    "phonetic": "'sɒ:lti",
    "meaning": "a. 有盐分的, 咸味浓的, 海洋的, 辛辣的, 有经验的"
  },
  "salve": {
    "phonetic": "sælv",
    "meaning": "n. 油膏, 药膏, 安慰, 奉承话；vt. 涂油膏于, 安慰, 缓和, 抢救, 打捞"
  },
  "salvo": {
    "phonetic": "'sælvәu",
    "meaning": "n. 保留条款, 遁辞, 保护手段, 齐射, 齐鸣；[法] 保留条款, 但书, 托辞"
  },
  "samba": {
    "phonetic": "'sæmbә",
    "meaning": "n. 桑巴舞；vi. 跳桑巴舞"
  },
  "samey": {
    "phonetic": "ˈseɪmi",
    "meaning": "a. <英><非正>单调乏味的, 无变化的"
  },
  "sandy": {
    "phonetic": "'sændi",
    "meaning": "a. 沙的, 沙地的, 多沙的"
  },
  "saner": {
    "phonetic": "seinə",
    "meaning": "a. 心智健全的( sane的比较级 ); 神志正常的; 明智的; 稳健的"
  },
  "sappy": {
    "phonetic": "'sæpi",
    "meaning": "a. 树液多的, 精力充沛的"
  },
  "sassy": {
    "phonetic": "'sæsi",
    "meaning": "a. 无礼的, 充满生气的, 时髦的"
  },
  "sated": {
    "phonetic": "ˈseɪtɪd",
    "meaning": "a. <正>厌腻的"
  },
  "satin": {
    "phonetic": "'sætin",
    "meaning": "n. 缎子；a. 绸缎做的, 缎子一般的, 光滑的"
  },
  "satyr": {
    "phonetic": "'sætә",
    "meaning": "n. 萨梯(森林之神), 好色之徒；[法] 色情狂者"
  },
  "sauce": {
    "phonetic": "sɒ:s",
    "meaning": "n. 酱油, 调味汁, 酱；vt. 给...调味, 使增加趣味"
  },
  "saucy": {
    "phonetic": "'sɒ:si",
    "meaning": "a. 莽撞的, 活泼的, 漂亮的"
  },
  "sauna": {
    "phonetic": "'saunә",
    "meaning": "n. 桑拿浴"
  },
  "saute": {
    "phonetic": "",
    "meaning": "n. 炒菜肴, 嫩煎的菜肴, 炸菜肴；vt. 炒, 嫩煎, 炸；a. 嫩煎的"
  },
  "saved": {
    "phonetic": "",
    "meaning": "a. 已保存的；获救的"
  },
  "saver": {
    "phonetic": "'seivә",
    "meaning": "n. 节省...的器具, 节约装置, 省俭的人；[化] 回收器; 收集器"
  },
  "savor": {
    "phonetic": "'seivә",
    "meaning": "n. 滋味, 气味, 食欲；vi. 有...的滋味；vt. 加调味品于, 使有风味, 尝到"
  },
  "savoy": {
    "phonetic": "sә'vɔi",
    "meaning": "n. [植]皱叶甘兰"
  },
  "savvy": {
    "phonetic": "'sævi",
    "meaning": "v. 理解, 领悟；n. 理解能力, 机智, 悟性"
  },
  "sawed": {
    "phonetic": "",
    "meaning": "saw的过去式和过去分词"
  },
  "scald": {
    "phonetic": "skɒ:ld",
    "meaning": "n. 烫伤, 烫洗；v. 烫伤, 烫洗"
  },
  "scale": {
    "phonetic": "skeil",
    "meaning": "n. 刻度, 衡量, 比例, 比例尺, 数值范围, 等级, 规模, 天平, 秤, 鳞, 积垢；vt. 依比例决定, 攀登, 测量, 绘制, 刮鳞, 使生垢, 过秤；vi. 剥落, 生水垢, 重量为, 攀登, 衡量；[计] 刻度"
  },
  "scalp": {
    "phonetic": "skælp",
    "meaning": "v. 剥头皮；n. 头皮, 战利品"
  },
  "scaly": {
    "phonetic": "'skeili",
    "meaning": "a. 有鳞的, 鳞状的, 覆有鳞片的, 积垢的, 积水垢的, 介壳虫蛀的；[医] 鳞状的, 有鳞屑的"
  },
  "scamp": {
    "phonetic": "skæmp",
    "meaning": "n. 流氓；vt. 草率地做"
  },
  "scant": {
    "phonetic": "skænt",
    "meaning": "a. 不充分的, 不足的；vt. 减少, 吝啬, 限制, 藐视, 忽略"
  },
  "scape": {
    "phonetic": "skeip",
    "meaning": "[医] 柄节(昆虫)"
  },
  "scare": {
    "phonetic": "skєә",
    "meaning": "n. 惊吓, 恐慌；vt. 惊吓, 使恐慌；vi. 受惊"
  },
  "scarf": {
    "phonetic": "skɑ:f",
    "meaning": "n. 围巾, 头巾, 领带, 领巾, 嵌接；vt. 用围巾围, 嵌接"
  },
  "scary": {
    "phonetic": "'skєәri",
    "meaning": "a. 容易受惊的, 胆小的, 提心吊胆的"
  },
  "scene": {
    "phonetic": "si:n",
    "meaning": "n. 场, 情景, 镜头, 发生地点, 道具, 布景, 景色；[化] 现场"
  },
  "scent": {
    "phonetic": "sent",
    "meaning": "n. 气味, 香味, 香水, 踪迹, 痕迹, 线索, 嗅觉；vt. 闻出, 嗅, 发觉, 使充满气味；vi. 嗅猎, 发出气味"
  },
  "schmo": {
    "phonetic": "ʃmәu",
    "meaning": "n. 笨人, 愚人"
  },
  "schwa": {
    "phonetic": "ʃwɑ:",
    "meaning": "n. 非重央元音"
  },
  "scion": {
    "phonetic": "'saiәn",
    "meaning": "n. 接穗, 子孙；[医] 嫩枝, 接穗"
  },
  "scoff": {
    "phonetic": "skɒf",
    "meaning": "n. 嘲笑, 愚弄, 笑柄, 食品；v. 嘲笑, 嘲弄, 贪吃, 狼吞虎咽地吃"
  },
  "scold": {
    "phonetic": "skәuld",
    "meaning": "n. 好骂街的人, 责骂；v. 责骂"
  },
  "scone": {
    "phonetic": "skәun",
    "meaning": "n. 烤饼"
  },
  "scoop": {
    "phonetic": "sku:p",
    "meaning": "n. 铲子, 勺子, 穴, 口, 独家新闻；vt. 汲取, 舀取, 挖空, 抢先报道"
  },
  "scoot": {
    "phonetic": "sku:t",
    "meaning": "vi. 快跑, 奔跑"
  },
  "scope": {
    "phonetic": "skәup",
    "meaning": "n. 范围, 机会, 广度, 眼界, 观察仪器, 导弹射程；[计] 作用域"
  },
  "score": {
    "phonetic": "skɒ:",
    "meaning": "n. 得分, 抓痕, 二十个, 刻痕, 帐目, 乐谱, 起跑线, 终点线, 大量；vt. 刻划, 划线, 获得, 评价, 把...记下；vi. 刻痕, 记分, 得分；[计] 得分"
  },
  "scorn": {
    "phonetic": "skɒ:n",
    "meaning": "n. 轻蔑, 藐视, 嘲笑, 被嘲弄的人；vt. 轻蔑, 不屑做"
  },
  "scour": {
    "phonetic": "'skauә",
    "meaning": "vt. 擦亮, 洗涤, 清洗, 冲刷成, 急速穿过；vi. 擦, 洗, 冲刷, 腹泻, 急速穿行；n. 擦, 洗, 腹泻, 洗涤剂"
  },
  "scout": {
    "phonetic": "skaut",
    "meaning": "n. 守候, 侦察, 搜索, 侦察员, 侦察机；vi. 守候, 侦察, 巡视, 嘲笑；vt. 侦察, 跟踪, 发现, 监视, 嘲弄"
  },
  "scowl": {
    "phonetic": "skaul",
    "meaning": "n. 愁容, 阴沉脸色；vi. 皱眉, 绷着脸；vt. 怒视"
  },
  "scram": {
    "phonetic": "skræm",
    "meaning": "n. 紧急刹车；vi. 快速离去"
  },
  "scrap": {
    "phonetic": "skræp",
    "meaning": "n. 碎片, 残余物, 些微, 片断, 铁屑, 吵架；vt. 扔弃, 敲碎, 拆毁；vi. 互相殴打；a. 零碎拼凑成的, 废弃的"
  },
  "scree": {
    "phonetic": "skri:",
    "meaning": "n. 山麓碎石, 岩屑堆"
  },
  "screw": {
    "phonetic": "skru:",
    "meaning": "n. 螺旋, 螺杆, 螺钉, 螺旋桨, 吝啬鬼；vt. 调节, 扭紧, 旋, 拧, 加强, 压榨, 勒索；vi. 转动, 旋, 拧"
  },
  "scrip": {
    "phonetic": "skrip",
    "meaning": "n. 便条, 纸条, 纸片；[经] 股票临时收据, 临时凭单, 代价券"
  },
  "scrod": {
    "phonetic": "skrɒd",
    "meaning": "n. 幼鳕"
  },
  "scrub": {
    "phonetic": "skrʌb",
    "meaning": "n. 用力擦洗, 矮树, 矮人, 渺小之物；vt. 用力擦洗, 擦掉, 摩擦；vi. 擦洗干净, 进行手臂消毒；a. 次等的, 矮小的, 非正规球队的, 临时凑合的"
  },
  "scrum": {
    "phonetic": "skrʌm",
    "meaning": "n. (橄榄球中)扭夺, 并列争球"
  },
  "scuba": {
    "phonetic": "'skju:bә",
    "meaning": "n. 自携式水中呼吸器"
  },
  "scuff": {
    "phonetic": "skʌf",
    "meaning": "vi. 拖着脚走, 磨损；vt. 拳打, 攻击, 用足尖触, 使磨损；n. 拖着脚走, 磨损, 家用平底拖鞋"
  },
  "scull": {
    "phonetic": "skʌl",
    "meaning": "n. 短桨, 尾橹；vt. 摇桨, 划；vi. 划船"
  },
  "seamy": {
    "phonetic": "'si:mi",
    "meaning": "a. 露出线缝的, 丑恶的"
  },
  "sedan": {
    "phonetic": "si'dæn",
    "meaning": "n. 轿车, 轿子"
  },
  "seder": {
    "phonetic": "'seidə",
    "meaning": "n. 逾越节家宴"
  },
  "sedge": {
    "phonetic": "sedʒ",
    "meaning": "n. 莎草, 蓑衣草"
  },
  "seedy": {
    "phonetic": "'si:di",
    "meaning": "a. 多种子的, 结籽的, 破烂的, 肮脏的"
  },
  "segue": {
    "phonetic": "'se^wei, 'sei^wei",
    "meaning": "n. [用作指示语][音]继续"
  },
  "seize": {
    "phonetic": "si:z",
    "meaning": "vt. 抓住, 逮捕, 俘获, 没收, 扣押, 掌握；vi. 突然抓住, 利用"
  },
  "sense": {
    "phonetic": "sens",
    "meaning": "n. 感应, 感觉, 感官, 意识, 观念, 情理, 知觉, 理智；vt. 感觉, 觉察, 检测；[计] 阅读; 检测"
  },
  "sepia": {
    "phonetic": "'si:pjә",
    "meaning": "n. 乌贼, 乌贼墨颜料, 深褐色, 乌贼汁；a. 乌贼墨色的, 使用乌贼墨颜料的"
  },
  "serif": {
    "phonetic": "'serif",
    "meaning": "n. 西文字体中的短细线, 衬线；[计] 衬线"
  },
  "serum": {
    "phonetic": "'siәrәm",
    "meaning": "n. 浆液, 血清, 乳清；[医] 血清; 浆液"
  },
  "serve": {
    "phonetic": "sә:v",
    "meaning": "vt. 可作...用, 服务, 经历, 招待, 供应, 送交, 对待；vi. 服务, 服役, 侍应, 适合, 有用, 开球；n. 发球, 轮到发球"
  },
  "setup": {
    "phonetic": "'setʌp",
    "meaning": "n. 装备, 组织, 计划, 机构, 调整, 设置；[计] 设置"
  },
  "seven": {
    "phonetic": "'sevn",
    "meaning": "num. 七, 七个"
  },
  "sever": {
    "phonetic": "'sevә",
    "meaning": "vt. 切断, 脱离, 分开, 使分离, 断绝, 中断；vi. 断, 裂开"
  },
  "sewed": {
    "phonetic": "",
    "meaning": "sew的过去式和过去分词"
  },
  "sewer": {
    "phonetic": "'su:ә",
    "meaning": "n. 下水道, 阴沟, 裁缝师；vt. 用下水道排, 铺设下水道于"
  },
  "shack": {
    "phonetic": "ʃæk",
    "meaning": "n. 陋屋, 棚屋；vi. 居住, 暂住"
  },
  "shade": {
    "phonetic": "ʃeid",
    "meaning": "n. 荫, 阴暗, 遮光物, 灯罩, 帘, 浓淡, 微量, 底纹；vi. 渐变；vt. 使阴暗, 使渐变, 遮蔽, 微减；[计] 底纹"
  },
  "shady": {
    "phonetic": "'ʃeidi",
    "meaning": "a. 荫凉的, 成荫的, 阴暗的, 隐蔽的；[法] 成问题的, 令人怀疑的"
  },
  "shaft": {
    "phonetic": "ʃæft",
    "meaning": "n. 轴, 箭杆, 矛, 矿井；vt. 装杆于, 利用"
  },
  "shake": {
    "phonetic": "ʃeik",
    "meaning": "n. 摇动, 震动；vt. 摇动, 动摇, 使震动, 挥舞；vi. 震动, 发抖, 动摇"
  },
  "shaky": {
    "phonetic": "'ʃeiki",
    "meaning": "a. 震动的, 摇晃的, 动摇的"
  },
  "shale": {
    "phonetic": "ʃeil",
    "meaning": "n. 页岩"
  },
  "shall": {
    "phonetic": "ʃæl",
    "meaning": "aux. 将"
  },
  "shalt": {
    "phonetic": "ʃælt;ʃәlt;ʃilt",
    "meaning": "vbl.shall的第二人称单数现在式"
  },
  "shame": {
    "phonetic": "ʃeim",
    "meaning": "n. 羞耻, 羞愧, 耻辱；vt. 使羞愧, 侮辱"
  },
  "shank": {
    "phonetic": "ʃæŋk",
    "meaning": "n. 胫, 腿骨, 杆, 柄；vt. 用铁球棒末端击球；vi. 花从病梗上枯萎脱落"
  },
  "shape": {
    "phonetic": "ʃeip",
    "meaning": "n. 形状, 形态, 外形, 形式, 身材；vt. 定形, 使成形, 塑造, 计划, 使符合；vi. 成形, 形成, 成长；[计] 形状"
  },
  "shard": {
    "phonetic": "ʃɑ:d",
    "meaning": "n. 陶瓷碎片, 鞘翅, 薄硬壳"
  },
  "share": {
    "phonetic": "ʃєә",
    "meaning": "n. 部分, 参与, 一份, 参股, 份额；vt. 均分, 分担, 分享, 分配, 共有；vi. 分享；[计] 共享; DOS外部命令:在网络或多工系统中提供文件共享；文件锁定及检测磁盘更动和对超过32MB硬盘分区的支持"
  },
  "shark": {
    "phonetic": "ʃɑ:k",
    "meaning": "n. 鲨鱼, 骗子；v. 诈骗"
  },
  "sharp": {
    "phonetic": "ʃɑ:p",
    "meaning": "n. 半升音调, 利刃, 骗子；a. 锋利的, 明显的, 敏锐的, 急剧的, 尖刻的, 严厉的, 刺耳的, 精明的；adv. 锐利地, 急速地"
  },
  "shave": {
    "phonetic": "ʃeiv",
    "meaning": "n. 修面, 刮胡子, 幸免, 剃刀；vt. 修面, 剃, 修剪, 掠过；vi. 刮脸, 勉强通过"
  },
  "shawl": {
    "phonetic": "ʃɒ:l",
    "meaning": "n. 披肩, 围巾；vt. 用披肩裹"
  },
  "sheaf": {
    "phonetic": "ʃi:f",
    "meaning": "n. 束, 捆, 扎；vt. 捆, 束"
  },
  "shear": {
    "phonetic": "ʃiә",
    "meaning": "n. 修剪, 剪下的东西, 大剪刀, 切变, 剪切机, 切；vt. 修剪, 割, 剥夺, 横越, 削剪；vi. 剪, 修剪, 剪羊毛, 切断"
  },
  "sheen": {
    "phonetic": "ʃi:n",
    "meaning": "n. 光辉, 光彩, 光泽；a. 光辉的, 发光的, 有光泽的；vi. 发出光泽"
  },
  "sheep": {
    "phonetic": "ʃi:p",
    "meaning": "n. 羊, 胆小者"
  },
  "sheer": {
    "phonetic": "ʃiә",
    "meaning": "a. 绝对的, 全然的, 纯粹的, 透明的, 峻峭的；vi. 偏转, 偏航；vt. 使急转向, 使偏航；adv. 完全, 全然, 峻峭；n. 偏航"
  },
  "sheet": {
    "phonetic": "ʃi:t",
    "meaning": "n. 床单, 张, 纸张, 印刷品, 裹尸布, 薄片；vt. 盖上被单, 遍布；vi. 大片落下；a. 片状的, 成薄片的；[计] 工作表"
  },
  "sheik": {
    "phonetic": "",
    "meaning": "n. 酋长, 王子, 村长, 族长, 教长, 导师, 有威信的丈夫"
  },
  "shelf": {
    "phonetic": "ʃelf",
    "meaning": "n. 架子, 搁板；[化] 架子"
  },
  "shell": {
    "phonetic": "ʃel",
    "meaning": "n. 贝壳, 壳, 外形, 炮弹；vt. 去壳, 脱落, 炮轰；vi. 剥落, 脱壳；[计] 外壳; DOS内部命令:指定命令行处理程序"
  },
  "shied": {
    "phonetic": "",
    "meaning": "v. （指马）惊退；后退；回避；厌恶（shy的过去分词形式）"
  },
  "shift": {
    "phonetic": "ʃift",
    "meaning": "n. 变化, 移动, 轮班, 手段, 应急办法, 移位；vt. 替换, 转移, 改变, 推卸, 变速；vi. 转换, 移动, 转变, 推托, 变速；[计] DOS内部命令:该命令可将批处理参数向左移动一个位置"
  },
  "shill": {
    "phonetic": "ʃil",
    "meaning": "n. 小贩的同伙, 赌棍的党羽"
  },
  "shine": {
    "phonetic": "ʃain",
    "meaning": "n. 光泽, 阳光；vt. 使发光；vi. 照耀, 发光, 发亮"
  },
  "shiny": {
    "phonetic": "'ʃaini",
    "meaning": "a. 有光泽的, 发光的, 辉煌的, 磨光的, 磨损的"
  },
  "shire": {
    "phonetic": "'ʃaiә",
    "meaning": "n. 郡"
  },
  "shirk": {
    "phonetic": "ʃә:k",
    "meaning": "vi. 溜掉, 逃避, 推卸；vt. 逃避"
  },
  "shirt": {
    "phonetic": "ʃә:t",
    "meaning": "n. 衬衫, 内衣, 汗衫"
  },
  "shiva": {
    "phonetic": "'ʃi:vә",
    "meaning": "n. 七日服丧期"
  },
  "shlep": {
    "phonetic": "ʃlep",
    "meaning": "v. & n. 拖; 拉; 无用的人; 废物"
  },
  "shlub": {
    "phonetic": "ʃlʌb",
    "meaning": "n. <美俚> = schlub"
  },
  "shoal": {
    "phonetic": "ʃәul",
    "meaning": "n. 浅水, 浅滩, 沙洲, 鱼群, 暗礁, 潜在危险；a. 浅的；vi. 鱼成群而游, 变浅；vt. 使变浅"
  },
  "shock": {
    "phonetic": "ʃɒk",
    "meaning": "n. 震动, 冲突, 震惊, 冲击, 突击, 禾束堆, 休克, 长毛狗；vt. 使震动, 使休克, 使受电击, 震惊得；vi. 震动, 吓人；a. 蓬乱浓密的"
  },
  "shoed": {
    "phonetic": "",
    "meaning": "shoe的过去式和过去分词"
  },
  "shone": {
    "phonetic": "ʃɔn",
    "meaning": "shine的过去式和过去分词"
  },
  "shook": {
    "phonetic": "ʃuk",
    "meaning": "shake的过去式"
  },
  "shoot": {
    "phonetic": "ʃu:t",
    "meaning": "n. 射击, 狩猎, 芽, 射伤, 发射, 发芽, 急流, 推力, 摄影, 急送, 滑运道, 浪费；vt. 射击, 射中, 损毁, 拍摄, 喷出, 投射, 挥出, 飞速行进, 挥霍, 给...注射；vi. 射出, 射击, 发出, 拍电影, 射门, 发芽"
  },
  "shore": {
    "phonetic": "ʃɒ:",
    "meaning": "n. 海岸, 海滨, 斜撑柱；vt. 把...送上岸, 支撑, 支持"
  },
  "shorn": {
    "phonetic": "ʃɔ:n",
    "meaning": "shear的过去分词"
  },
  "short": {
    "phonetic": "ʃɒ:t",
    "meaning": "a. 短的, 近的, 矮的, 短期的, 简短的, 少量的；adv. 简短地, 突然；n. 扼要, 短片, 缺乏；vt. 故意少给, 使短路"
  },
  "shout": {
    "phonetic": "ʃaut",
    "meaning": "n. 呼喊, 喊声；vi. 呼喊, 喊叫, 嚷；vt. 高喊"
  },
  "shove": {
    "phonetic": "ʃʌv",
    "meaning": "n. 推, 挤；vt. 推挤, 猛推, 强使；vi. 推"
  },
  "shown": {
    "phonetic": "ʃәun",
    "meaning": "show的过去分词"
  },
  "showy": {
    "phonetic": "'ʃәui",
    "meaning": "a. 艳丽的, 炫耀的"
  },
  "shred": {
    "phonetic": "ʃred",
    "meaning": "n. 碎布条, 细片, 少量；v. 撕碎"
  },
  "shrew": {
    "phonetic": "ʃru:",
    "meaning": "n. 泼妇；[法] 捍妇, 泼妇"
  },
  "shrub": {
    "phonetic": "ʃrʌb",
    "meaning": "n. 矮树, 灌木, 果汁甜酒"
  },
  "shrug": {
    "phonetic": "ʃrʌg",
    "meaning": "n. 耸肩；v. 耸肩"
  },
  "shuck": {
    "phonetic": "ʃʌk",
    "meaning": "n. 壳, 外皮, 牡蛎壳；v. 剥去, 脱去"
  },
  "shunt": {
    "phonetic": "ʃʌnt",
    "meaning": "vt. 使转轨, 使分流, 回避讨论, 推延；vi. 转向一边, 转轨, 往返；n. 转轨, 分流"
  },
  "shush": {
    "phonetic": "ʃʌʃ",
    "meaning": "interj. 嘘；n. 嘘声"
  },
  "shyly": {
    "phonetic": "",
    "meaning": "adv. 害羞地；羞怯地；胆怯地；小心地"
  },
  "sided": {
    "phonetic": "'saidid",
    "meaning": "a. 有边的, 有面的"
  },
  "sidle": {
    "phonetic": "'saidl",
    "meaning": "v. 横着走, 悄悄贴近, 侧身而行；n. 侧走, 挨近"
  },
  "siege": {
    "phonetic": "si:dʒ",
    "meaning": "n. 包围, 围攻, 再三的努力；vt. 包围, 围攻"
  },
  "sieve": {
    "phonetic": "siv",
    "meaning": "n. 筛子, 滤网；vt. 筛, 滤"
  },
  "sight": {
    "phonetic": "sait",
    "meaning": "n. 景观, 视力, 眼界, 阅读, 见解, 意见；vt. 看见, 瞄准；vi. 瞄准, 观看；a. 即席的, 见票即付的"
  },
  "sigma": {
    "phonetic": "'si^mә",
    "meaning": "[计] 求和；[医] σ(希腊文第十八个字母)"
  },
  "silky": {
    "phonetic": "'silki",
    "meaning": "a. 丝的, 柔滑的"
  },
  "silly": {
    "phonetic": "'sili",
    "meaning": "a. 愚蠢的, 糊涂的"
  },
  "silty": {
    "phonetic": "'silti",
    "meaning": "a. 淤泥的, 塞满了淤泥的"
  },
  "since": {
    "phonetic": "sins",
    "meaning": "prep. 自...以后, 自...以来；adv. 自那时以后；conj. 既然, 自...以后, 自...以来"
  },
  "sinew": {
    "phonetic": "'sinju:",
    "meaning": "n. 肌肉, 精力, 体力, 力量的源泉, 腱；vt. 赋予力量, 加强"
  },
  "singe": {
    "phonetic": "sindʒ",
    "meaning": "v. 烧焦, 烤焦"
  },
  "sinus": {
    "phonetic": "'sainәs",
    "meaning": "n. 窦, 静脉窦, 凹陷处"
  },
  "sired": {
    "phonetic": "saɪəd",
    "meaning": "v. 公畜( sire的过去式和过去分词 ); 陛下"
  },
  "siren": {
    "phonetic": "'saiәrin",
    "meaning": "n. 女海妖, 妖女, 警报器, 汽笛, 迷人的美女；a. 诱惑的；vi. 响着警报器前进"
  },
  "sissy": {
    "phonetic": "'sisi",
    "meaning": "n. 女孩子, 女人腔的男人, 胆小鬼；a. 女人腔的"
  },
  "sitar": {
    "phonetic": "si'tɑ:",
    "meaning": "n. 西他(印度弦乐器)"
  },
  "sited": {
    "phonetic": "",
    "meaning": "vt. 使坐落在（site的过去式与过去分词形式）"
  },
  "situp": {
    "phonetic": "",
    "meaning": "n. 仰卧起坐"
  },
  "sixth": {
    "phonetic": "siksθ",
    "meaning": "num. 第六, 六分之一"
  },
  "sixty": {
    "phonetic": "'siksti",
    "meaning": "num. 六十, 六十个"
  },
  "sized": {
    "phonetic": "'saizd",
    "meaning": "a. 依大小排列的, 依大小调整的, 型号的, ...尺码的"
  },
  "skate": {
    "phonetic": "skeit",
    "meaning": "n. 溜冰, 冰鞋；vi. 滑冰, 滑过"
  },
  "skeet": {
    "phonetic": "ski:t",
    "meaning": "n. 双向飞碟"
  },
  "skein": {
    "phonetic": "skein",
    "meaning": "n. 一束, 飞鸟群, 纠纷；[医] 染色质纽, 丝球; 线团, 线球"
  },
  "skied": {
    "phonetic": "s'kaɪd",
    "meaning": "v. 滑雪( ski的过去式和过去分词 )"
  },
  "skier": {
    "phonetic": "'ski:ә",
    "meaning": "n. 滑雪的人"
  },
  "skiff": {
    "phonetic": "skif",
    "meaning": "n. 小艇, 轻舟, 小型帆船"
  },
  "skill": {
    "phonetic": "'skil",
    "meaning": "n. 技术, 技巧, 技能, 熟练, 熟练工人；[化] 技能"
  },
  "skimp": {
    "phonetic": "skimp",
    "meaning": "vt. 少给, 克扣；vi. 吝啬；a. 少的, 不足的"
  },
  "skirt": {
    "phonetic": "skә:t",
    "meaning": "n. 裙子, 下摆, 边缘, 郊区；vt. 位于...边缘, 绕过, 回避；vi. 位于边缘"
  },
  "skulk": {
    "phonetic": "'skʌlk",
    "meaning": "vi. 偷偷隐躲, 偷懒"
  },
  "skull": {
    "phonetic": "skʌl",
    "meaning": "n. 头盖骨, 头脑, 好学生；[医] 头颅"
  },
  "skunk": {
    "phonetic": "skʌŋk",
    "meaning": "n. 臭鼬, 臭鼬皮, 讨厌鬼；vt. 使惨败, 欺骗"
  },
  "slack": {
    "phonetic": "slæk",
    "meaning": "n. 松弛, 松懈, 淡季, 闲散, 家常裤；a. 松弛的, 不流畅的, 疏忽的, 无力的, 呆滞的, 软弱的, 漏水的；adv. 马虎地, 缓慢地；vt. 放松, 使缓慢；vi. 松懈, 减弱, 松弛"
  },
  "slain": {
    "phonetic": "slein",
    "meaning": "slay的过去分词"
  },
  "slake": {
    "phonetic": "sleik",
    "meaning": "vt. 消除, 使清凉, 熄灭；[医] 消, 灭; 消和(石灰); 松, 缓和"
  },
  "slang": {
    "phonetic": "slæŋ",
    "meaning": "n. 俚语；v. 辱骂, 用俚语说"
  },
  "slant": {
    "phonetic": "slænt",
    "meaning": "n. 倾斜, 斜面, 观点, 偏见, 歪曲；a. 倾斜的；v. (使)倾斜"
  },
  "slash": {
    "phonetic": "slæʃ",
    "meaning": "v. 猛砍, 乱砍；n. 猛砍, 乱砍, 删减；[计] 斜线"
  },
  "slate": {
    "phonetic": "sleit",
    "meaning": "n. 板岩, 页岩, 提名名单, 人选, 记录, 石板；a. 石板色的；vt. 铺石板, 责骂, 痛打"
  },
  "sleek": {
    "phonetic": "sli:k",
    "meaning": "a. 光滑的, 油嘴滑舌的, 线条明快的, 圆滑的, 时髦的；vt. 使光滑, 掩盖；vi. 打扮漂亮, 滑动"
  },
  "sleep": {
    "phonetic": "sli:p",
    "meaning": "n. 睡眠, 静止, 昏迷, 麻木, 长眠, 冬眠；vi. 睡觉, 睡眠, 静止；vt. 睡"
  },
  "sleet": {
    "phonetic": "sli:t",
    "meaning": "n. 雨夹雪；vi. 下雨夹雪"
  },
  "slept": {
    "phonetic": "slept",
    "meaning": "sleep的过去式和过去分词"
  },
  "slice": {
    "phonetic": "slais",
    "meaning": "n. 薄的切片, 一部分, 菜刀；vt. 切成薄片, 切下；vi. 切；[计] 片"
  },
  "slick": {
    "phonetic": "slik",
    "meaning": "a. 光滑的, 熟练的, 聪明的, 华而不实的, 老套的, 陈腐的；adv. 灵活地, 聪明地；vt. 使光滑, 使漂亮；vi. 打扮整洁；n. 光滑平面, 平滑器, 修光工具"
  },
  "slide": {
    "phonetic": "slaid",
    "meaning": "n. 滑, 滑道, 山崩, 雪崩, 幻灯片；vt. 使滑动, 偷偷放入；vi. 滑动, 滑落, 不知不觉陷入, 偷偷地走"
  },
  "slime": {
    "phonetic": "slaim",
    "meaning": "n. 烂泥, 粘液；vt. 涂上泥；vi. 变粘滑"
  },
  "slimy": {
    "phonetic": "'slaimi",
    "meaning": "a. 泥的, 泥泞的, 粘糊糊的, 讨厌的"
  },
  "sling": {
    "phonetic": "sliŋ",
    "meaning": "n. 投石器, 抛掷, 吊索, 吊钩；vt. 用投石器投掷, 用吊钩吊上, 吊起"
  },
  "slink": {
    "phonetic": "sliŋk",
    "meaning": "vi. 鬼鬼祟祟地走, (动物)早产；vt. 早产；n. 鬼鬼祟祟的人, 早产的动物；a. 早产的"
  },
  "sloop": {
    "phonetic": "slu:p",
    "meaning": "n. 单桅帆船"
  },
  "slope": {
    "phonetic": "slәup",
    "meaning": "n. 倾斜, 斜坡, 斜率, 扛枪姿势；vt. 使倾斜, 弄斜, 扛；vi. 倾斜, 走, 逃走"
  },
  "slosh": {
    "phonetic": "slɒʃ",
    "meaning": "n. 泥泞, 溅泼声；v. 走泥泞路, 液体晃动, 溅, 泼"
  },
  "sloth": {
    "phonetic": "slәuθ",
    "meaning": "n. 怠惰, 懒惰"
  },
  "slump": {
    "phonetic": "slʌmp",
    "meaning": "n. 暴跌, 垂头弯腰的姿态；vi. 猛然掉落, 陷入, 衰落(经济等)"
  },
  "slung": {
    "phonetic": "slʌŋ",
    "meaning": "sling的过去式和过去分词"
  },
  "slunk": {
    "phonetic": "slʌŋk",
    "meaning": "slink的过去式和过去分词"
  },
  "slurp": {
    "phonetic": "slә:p",
    "meaning": "n. 吃的声音；v. 出声地吃(或喝)"
  },
  "slush": {
    "phonetic": "slʌʃ",
    "meaning": "n. 烂泥, 雪水, 无聊的言情内容, 胡说八道；vt. 溅湿, 灌泥浆于；vi. 在雪泥(或泥浆)中走"
  },
  "slyly": {
    "phonetic": "'slaili",
    "meaning": "adv. 狡猾地, 秘密地, 俏皮地, 偷偷地"
  },
  "smack": {
    "phonetic": "smæk",
    "meaning": "n. 风味, 滋味, 少量, 拍击声, 咂嘴声, 小渔船, 海洛因；vi. 有味道, 咂嘴, 发出拍击声；vt. 拍, 打, 掴, 咂, 出声地吻；adv. 啪地一声, 猛然"
  },
  "small": {
    "phonetic": "smɒ:l",
    "meaning": "a. 小的, 少的, 小型的, 低微的, 小气的, 细微的；adv. 些微地；n. 狭小部分"
  },
  "smarm": {
    "phonetic": "smɑ:m",
    "meaning": "vt. 使(头发)平滑, 阿谀, 说奉承话"
  },
  "smart": {
    "phonetic": "smɑ:t",
    "meaning": "a. 聪明的, 漂亮的, 刺痛的, 剧烈的, 敏捷的, 巧妙的, 伶俐的, 潇洒的；n. 刺痛, 痛苦；vi. 刺痛"
  },
  "smash": {
    "phonetic": "smæʃ",
    "meaning": "n. 打碎, 粉碎, 打碎时哗啦声, 猛击, 扣球, 杀球, 经营失败, 破产, 硬币, 假硬币；a. 非常轰动的, 了不起的；vt. 打碎, 粉碎, 击溃, 使破产, 使裂变, 使用假硬币；vi. 碎裂, 猛撞, 破产, 扣球, 杀球；adv. 轰隆一声, 哗啦一声"
  },
  "smear": {
    "phonetic": "smiә",
    "meaning": "vt. 涂, 擦上, 玷污, 把...擦模糊；vi. 被弄脏；n. 污点, 污迹, 污蔑"
  },
  "smell": {
    "phonetic": "smel",
    "meaning": "n. 味道, 气味, 嗅觉, 嗅, 臭味, 气息；vt. 闻, 探出, 察觉, 发出...的气味；vi. 嗅, 散发气味, 发臭"
  },
  "smelt": {
    "phonetic": "smelt",
    "meaning": "n. 胡瓜鱼；vt. 精炼, 熔炼；smell的过去式和过去分词"
  },
  "smile": {
    "phonetic": "smail",
    "meaning": "n. 微笑, 喜色, 笑容；vi. 微笑, 觉得好笑；vt. 微笑着表示"
  },
  "smirk": {
    "phonetic": "smә:k",
    "meaning": "vi. 傻笑, 假笑, 得意地笑；n. 傻笑, 假笑, 得意的笑"
  },
  "smite": {
    "phonetic": "smait",
    "meaning": "vt. 重击, 打, 击败, 毁灭, 侵袭, 打动；vi. 重击, 打；n. 重击, 打"
  },
  "smith": {
    "phonetic": "smiθ",
    "meaning": "n. 铁匠, 金属品工匠；[机] 锻造工, 上手"
  },
  "smock": {
    "phonetic": "smɒk",
    "meaning": "n. 工作服, 罩衫, 长罩衣；vt. 使穿上工作服, 缝制装饰用衣褶"
  },
  "smoke": {
    "phonetic": "smәuk",
    "meaning": "n. 烟, 雾气, 烟熏剂, 抽烟, 烟色；vi. 吸烟, 冒烟, 弥漫；vt. 以烟熏, 抽烟而导致..."
  },
  "smoky": {
    "phonetic": "'smәuki",
    "meaning": "a. 冒烟的, 满是烟的, 熏脏的, 烟灰色的"
  },
  "smote": {
    "phonetic": "smәut",
    "meaning": "smite的过去式和过去分词"
  },
  "snack": {
    "phonetic": "snæk",
    "meaning": "n. 小吃, 点心, 快餐；vi. 吃零食, 吃快餐"
  },
  "snafu": {
    "phonetic": "snæ'fu:",
    "meaning": "a. 一团槽的, 大混乱的；vt. 使混乱, 使一团槽；n. 混乱"
  },
  "snail": {
    "phonetic": "sneil",
    "meaning": "n. 蜗牛, 行动迟缓的人, 脑筋迟钝的人, 蜗形凸轮；vt. (蜗牛般)缓慢地打发(时间)；vi. 缓慢移动"
  },
  "snake": {
    "phonetic": "sneik",
    "meaning": "n. 蛇, 阴险的人；vi. 曲折行进；vt. 迂回, 拉, 急抽"
  },
  "snaky": {
    "phonetic": "'sneiki",
    "meaning": "a. 蛇的, 蛇一般的, 弯弯曲曲的, 阴险的, 多蛇的"
  },
  "snare": {
    "phonetic": "snєә",
    "meaning": "n. 陷阱, 诱惑, 圈套；vt. 以陷阱捕获, 诱惑"
  },
  "snarf": {
    "phonetic": "snɑ:f",
    "meaning": "vt. 很快地吃[或喝], 贪婪地吃[或喝]"
  },
  "snark": {
    "phonetic": "snɑ:k",
    "meaning": "n. 蛇鲨"
  },
  "snarl": {
    "phonetic": "snɑ:l",
    "meaning": "vi. 吼叫, 怒骂, 缠结；vt. 咆哮着说, 搞乱, 使缠结；n. 咆哮, 吼叫, 怒骂, 缠结, 混乱"
  },
  "sneak": {
    "phonetic": "sni:k",
    "meaning": "vi. 鬼鬼祟祟做事；vt. 偷偷地做；n. 鬼鬼祟祟的人, 偷偷摸摸的行为, 帆布胶底运动鞋；a. 暗中进行的"
  },
  "sneer": {
    "phonetic": "sniә",
    "meaning": "n. 冷笑, 嘲笑；vi. 嘲笑, 冷笑；vt. 嘲笑着说, 嘲笑得使"
  },
  "snide": {
    "phonetic": "snaid",
    "meaning": "n. 赝品, 假珠宝；a. 伪造的, 不诚实的, 卑鄙的, 险恶的"
  },
  "sniff": {
    "phonetic": "snif",
    "meaning": "n. 以鼻吸气, 嗅, 气息；vi. 嗅, 蔑视, 嗤之以鼻；vt. 闻, 用力吸, 发觉"
  },
  "snipe": {
    "phonetic": "snaip",
    "meaning": "n. 沙锥, 香烟屁股, 狙击, 街头流浪儿；vi. 猎鸟, 狙击, 诽谤；vt. 狙击"
  },
  "snoop": {
    "phonetic": "snu:p",
    "meaning": "vi. 调查, 窥探；n. 窥视行为, 爱管闲事的人, 私家侦探"
  },
  "snoot": {
    "phonetic": "snu:t",
    "meaning": "n. 鼻子, 脸, 鬼脸, 势利者"
  },
  "snore": {
    "phonetic": "snɒ:",
    "meaning": "n. 鼾声, 打鼾；vi. 打鼾；vt. 打鼾度过"
  },
  "snort": {
    "phonetic": "snɒ:t",
    "meaning": "vi. 喷着气弄响鼻子, 轻蔑地哼, 嘶嘶响着排气；vt. 哼着鼻子说, 喷出, 吸入(毒品)；n. 喷鼻息, (潜艇的)水下通气管"
  },
  "snout": {
    "phonetic": "snaut",
    "meaning": "n. 鼻口部, 鼻子, 口吻状物, 烟草"
  },
  "snowy": {
    "phonetic": "'snәui",
    "meaning": "a. 多雪的, 雪的, 被雪所覆盖着的, 下雪的"
  },
  "snuck": {
    "phonetic": "snʌk",
    "meaning": "<方>sneak的过去式和过去分词"
  },
  "snuff": {
    "phonetic": "snʌf",
    "meaning": "n. 烛花, 用鼻吸气, 嗅, 闻, 鼻烟, 气味；vt. 剪烛花, 掐灭, 扼杀, 消灭, 用鼻吸, 嗅出, 闻出；vi. 嗅, 闻"
  },
  "soapy": {
    "phonetic": "'sәupi",
    "meaning": "a. 涂着肥皂的, 谄媚的, 圆滑的"
  },
  "sober": {
    "phonetic": "'sәubә",
    "meaning": "a. 未醉的, 稳重的, 节制的, 严肃的, 不夸大的, 合理的, 朴素的；vt. 使醒酒, 使严肃；vi. 从醉里醒来, 变严肃"
  },
  "softy": {
    "phonetic": "'sɒfti",
    "meaning": "n. 傻子, 多愁善感的人"
  },
  "soggy": {
    "phonetic": "'sɒgi",
    "meaning": "a. 浸水的, 沉闷的；[化] 欠硫; 硫化不足"
  },
  "solar": {
    "phonetic": "'sәulә",
    "meaning": "a. 太阳的, 日光的, 源自太阳的；[医] 太阳的; 腹腔丛的"
  },
  "soled": {
    "phonetic": "",
    "meaning": "a. 底的"
  },
  "solid": {
    "phonetic": "'sɒlid",
    "meaning": "n. 固体；a. 坚硬的, 稳固的, 固体的, 实心的, 纯质的, 立体的, 立方的；[计] 原色"
  },
  "solve": {
    "phonetic": "sɒlv",
    "meaning": "vt. 解决, 付给, 溶解；vt. 求解；vi. 求解；[计] 求解"
  },
  "sonar": {
    "phonetic": "'sәunɑ:",
    "meaning": "n. 声纳；[计] 声纳"
  },
  "sonic": {
    "phonetic": "'sɒnik",
    "meaning": "a. 音波的, 音速的, 声音的；[电] 音波"
  },
  "sooth": {
    "phonetic": "su:θ",
    "meaning": "n. 真实；a. 真实的"
  },
  "sooty": {
    "phonetic": "'suti",
    "meaning": "a. 煤烟熏黑的, 乌黑的"
  },
  "soppy": {
    "phonetic": "'sɒpi",
    "meaning": "a. 浑身湿透的, 多雨的, 假情假义的"
  },
  "sorry": {
    "phonetic": "'sɒri",
    "meaning": "a. 难过的, 悲哀的, 遗憾的"
  },
  "sound": {
    "phonetic": "saund",
    "meaning": "n. 声音, 语音, 吵闹, 声调, 听力范围, 探条, 海峡；a. 健全的, 可靠的, 合理的, 健康的, 彻底的, 资金充实的；adv. 彻底地, 充分地；vi. 发出声音, 回响, 测深, 试探, 听起来；vt. 使发声, 宣告, 听诊, 测...深, 试探；[计] 声音"
  },
  "soupy": {
    "phonetic": "'su:pi",
    "meaning": "a. 汤汁一样的, 糊状的, 雾浓的"
  },
  "south": {
    "phonetic": "sauθ",
    "meaning": "n. 南方, 南；a. 南的, 向南的；adv. 在南方；vi. 转向南方"
  },
  "sowed": {
    "phonetic": "",
    "meaning": "sow的过去式和过去分词"
  },
  "sower": {
    "phonetic": "'sәuә",
    "meaning": "n. 播种者, 播种机, 四下传播的人"
  },
  "space": {
    "phonetic": "speis",
    "meaning": "n. 位置, 空间, 距离, 太空, 空白, 间隔, (期刊等的)篇幅；vt. 隔开, 分隔；vi. 留间隔；[计] 空白, 空格校验"
  },
  "spade": {
    "phonetic": "speid",
    "meaning": "n. 铲子, 锄, 铲刀, 黑桃；vt. 以锄掘, 把...弄实抹平；vi. 铲"
  },
  "spank": {
    "phonetic": "spæŋk",
    "meaning": "vt. 打, 拍击, 飞跑；vi. 飞跑；n. 拍打, 一巴掌"
  },
  "spare": {
    "phonetic": "spєә",
    "meaning": "n. 剩余, 备用品, 备件, 备用零件, 备用轮胎；a. 多余的, 备用的, 空闲的, 节约的, 瘦的；vi. 节约, 省掉, 宽恕；vt. 节约, 省用, 剩下, 饶恕, 赦免"
  },
  "spark": {
    "phonetic": "spɑ:k",
    "meaning": "n. 火花, 火星, 闪光, 无线电报务员, 瞬间放电, 活力, 朝气, 花花公子, 情郎；vi. 闪光, 发火花, 求婚；vt. 发动, 鼓舞, 使有朝气, 求婚"
  },
  "spasm": {
    "phonetic": "'spæzm",
    "meaning": "n. 痉挛, 抽搐, 发作；[医] 痉挛"
  },
  "spate": {
    "phonetic": "speit",
    "meaning": "n. 泛滥, 洪水, 大雨, 大量, 一阵"
  },
  "spawn": {
    "phonetic": "spɒ:n",
    "meaning": "n. (鱼)卵, 产物；vt. 产卵, 酿成, 大量生产；vi. 产卵, 大量生产"
  },
  "speak": {
    "phonetic": "spi:k",
    "meaning": "vi. 说, 说话, 演说, 发言；vt. 说, 讲, 说出"
  },
  "spear": {
    "phonetic": "spiә",
    "meaning": "n. 矛, 枪, 持矛者, 嫩枝；vt. 用矛刺；vi. 刺, 戳；a. 父系的"
  },
  "speck": {
    "phonetic": "spek",
    "meaning": "n. 斑点, 有斑点的东西, 污点, 缺点, 微粒, 肥肉；vt. 使有斑点"
  },
  "speed": {
    "phonetic": "spi:d",
    "meaning": "n. 速率, 速度, 迅速；vi. 加速, 超速, 快进；vt. 快速传送, 促进, 使加速；[计] 中央处理机速度设置程序"
  },
  "spell": {
    "phonetic": "spel",
    "meaning": "n. 符咒, 魅力, 轮值, 轮班, 工作时间, 一次发作；vt. 拼写, 拼成, 琢磨, 理解, 招致, 轮换, 迷住；vi. 轮换, 拼字"
  },
  "spelt": {
    "phonetic": "spelt",
    "meaning": "spell的过去式和过去分词；[医] 德国小麦"
  },
  "spend": {
    "phonetic": "spend",
    "meaning": "vt. 花费, 浪费, 度过, 消耗, 消磨；vi. 花费, 用尽"
  },
  "spent": {
    "phonetic": "spent",
    "meaning": "a. 用尽的, 精疲力竭的；spend的过去式和过去分词"
  },
  "sperm": {
    "phonetic": "spә:m",
    "meaning": "n. 精液, 精虫, 鲸油, 抹香鲸；[化] 鲸蜡油"
  },
  "spice": {
    "phonetic": "spais",
    "meaning": "n. 香料, 药料, 香气, 调味品, 情趣, 少许；vt. 加香料, 使添趣味"
  },
  "spicy": {
    "phonetic": "'spaisi",
    "meaning": "a. 香的, 多香料的, 辛辣的, 下流的"
  },
  "spied": {
    "phonetic": "spaɪd",
    "meaning": "v. 看见, 发现（ spy的过去式和过去分词 ）; 当间谍; 从事间谍活动; 搜集情报"
  },
  "spiel": {
    "phonetic": "'spi:l",
    "meaning": "n. 演说, 招揽生意的言辞, 电台广告稿；v. 高谈阔论, 演奏音乐"
  },
  "spiff": {
    "phonetic": "spif",
    "meaning": "<俚>vt.把…打扮整齐(up)"
  },
  "spike": {
    "phonetic": "spaik",
    "meaning": "n. 长钉, 鞋钉, 钉状物, 尖峰状物, 穗；vt. 以大钉钉牢, 用尖物刺穿, 阻止, 弃置不用；[计] 尖峰信号"
  },
  "spiky": {
    "phonetic": "'spaiki",
    "meaning": "a. 大钉一般的, 长而尖的, 钉满钉子的, 有穗的"
  },
  "spill": {
    "phonetic": "spil",
    "meaning": "n. 溢出, 溅出, 摔下, 溢出量, 木片, 小塞子；vt. 使溢出, 使散落, 洒, 使流出, 倒出, 使摔下；vi. 溢出, 涌流, 摔下"
  },
  "spilt": {
    "phonetic": "spilt",
    "meaning": "spill的过去式和过去分词"
  },
  "spine": {
    "phonetic": "spain",
    "meaning": "n. 背骨, 脊柱, 尖刺；[医] 脊柱; 棘, 刺; 马蹄嵴"
  },
  "spiny": {
    "phonetic": "'spaini",
    "meaning": "a. 多刺的, 尽是尖刺的, 尖刺状的, 麻烦的, 棘手的"
  },
  "spire": {
    "phonetic": "spaiә",
    "meaning": "n. 尖塔, 尖顶, 锥形体, 螺旋；vi. 突出, 耸立, 螺旋形上升；vt. 给...加塔尖"
  },
  "spite": {
    "phonetic": "spait",
    "meaning": "n. 恶意, 怨恨, 使人烦恼的事物；vt. 故意刁难, 欺侮"
  },
  "splat": {
    "phonetic": "splæt",
    "meaning": "n. 椅背纵板"
  },
  "splay": {
    "phonetic": "splei",
    "meaning": "vt. 展开, 张开, 使成八字形；vi. 伸展开；n. 展开；a. 八字形的, 倾斜的"
  },
  "split": {
    "phonetic": "split",
    "meaning": "n. 劈开, 裂片, 裂缝, 分裂, 派系, 派别, 柳条；a. 劈开的；vi. 分离, 分开, 裂开, 被劈开；vt. 劈开, 切开, 使分裂, 使分离；[计] 拆分"
  },
  "spoil": {
    "phonetic": "spɒil",
    "meaning": "n. 战利品, 赃物, 奖品, 变质, 次品；vt. 损坏, 破坏, 溺爱；vi. 腐坏, 掠夺"
  },
  "spoke": {
    "phonetic": "spәuk",
    "meaning": "n. 轮辐；vt. 装轮辐, 用刹车刹住；speak的过去式"
  },
  "spoof": {
    "phonetic": "spu:f",
    "meaning": "n. 幽默的讽刺诗文, 愚弄, 戏弄；v. 对...作幽默讽刺, 戏弄, 哄骗；a. 哄骗认的"
  },
  "spook": {
    "phonetic": "spu:k",
    "meaning": "n. 幽灵, 鬼；vt. 惊吓, 鬼怪般地出没；vi. 惊吓而逃窜, 受惊"
  },
  "spool": {
    "phonetic": "spu:l",
    "meaning": "n. 线轴, 缠线框；vt. 缠绕在线轴上, 缠绕；[计] 盘; 假脱机输入输出; 卷"
  },
  "spoon": {
    "phonetic": "spu:n",
    "meaning": "n. 匙, 调羹, 匙形工具；vt. 以匙舀起, 调情, 使成匙状"
  },
  "spore": {
    "phonetic": "spɒ:",
    "meaning": "n. 孢子；vi. 长孢子"
  },
  "sport": {
    "phonetic": "spɒ:t",
    "meaning": "n. 运动, 游戏, 娱乐, 消遣, 玩笑；a. 运动的, 户外穿戴的；vi. 游戏, 参加体育运动, 戏弄, 产生变种；vt. 炫耀, 使产生变种"
  },
  "spout": {
    "phonetic": "spaut",
    "meaning": "n. 喷口, 从喷口流出的水, 水落管, 水龙卷；vt. 喷出, 喷射, 滔滔不绝说出, 典押；vi. 喷射, 高谈阔论"
  },
  "spray": {
    "phonetic": "sprei",
    "meaning": "n. 水沫, 浪花, 水花, 喷雾, 喷雾器, 小树枝；vt. 喷雾, 扫射, 喷射；vi. 喷, 溅开"
  },
  "spree": {
    "phonetic": "spri:",
    "meaning": "n. 戏耍, 喧闹, 宴会, 狂饮；vi. 狂欢, 狂饮"
  },
  "sprig": {
    "phonetic": "sprig",
    "meaning": "n. 小树枝, 无头钉；vt. 用小树枝装饰, 用钉子钉上, 使蔓生"
  },
  "spume": {
    "phonetic": "spju:m",
    "meaning": "n. 泡沫；v. (使)起泡沫"
  },
  "spunk": {
    "phonetic": "spʌŋk",
    "meaning": "n. 精神, 勇气, 怒意, 引火柴"
  },
  "spurn": {
    "phonetic": "spә:n",
    "meaning": "n. 踢开, 拒斥；vt. 踢开, 冷落, 践踏, 唾弃；vi. 藐视, 摒弃"
  },
  "spurt": {
    "phonetic": "spә:t",
    "meaning": "n. 喷射, 冲刺；vt. 喷射；vi. 喷出, 迸发, 冲刺"
  },
  "squab": {
    "phonetic": "skwɒb",
    "meaning": "a. 尚未生毛的, 矮胖的, 刚孵出的；n. 雏鸟, 矮胖子；adv. 沉重地"
  },
  "squad": {
    "phonetic": "skwɒd",
    "meaning": "n. 班, 小队, 小集团；vt. 编成班"
  },
  "squat": {
    "phonetic": "skwɒt",
    "meaning": "n. 蹲, 窝；a. 蹲着的, 矮胖的；vi. 蹲下, 蹲坐, 蹲伏；vt. 使蹲下, 擅自占有"
  },
  "squib": {
    "phonetic": "skwib",
    "meaning": "n. 爆竹, 嘲讽, 讽刺文章；v. 放爆竹, 砰然爆开, 嘲弄"
  },
  "squid": {
    "phonetic": "skwid",
    "meaning": "n. 枪乌贼, 鱿鱼, 反潜水雷发射装置；[电] 超导量子干涉元件"
  },
  "stack": {
    "phonetic": "stæk",
    "meaning": "n. 堆叠, 堆, 大量, 书库, 枪架, 烟囱, 堆积, 存贮栈；vt. 堆积, 堆满, 暗中对...做手脚；vi. 堆起；[计] 堆积, 堆栈"
  },
  "staff": {
    "phonetic": "stɑ:f",
    "meaning": "n. 全体人员, 工作班子, 棍棒, 杆, 拐杖, 支柱, 权杖；a. 职员的, 雇员的, 参谋的；vt. 为...配备人员"
  },
  "stage": {
    "phonetic": "steidʒ",
    "meaning": "n. 阶段, 舞台, 场所, 戏剧, 站, 驿站, 级, 层, 脚手架；vt. 上演, 表演, 筹划；vi. 适于上演, 乘驿车旅行"
  },
  "staid": {
    "phonetic": "steid",
    "meaning": "a. 认真的, 沉着的, 固定的"
  },
  "stain": {
    "phonetic": "stein",
    "meaning": "n. 污染, 污点, 着色剂；vt. 沾染, 染污, 着色；vi. 变脏"
  },
  "stair": {
    "phonetic": "stєә",
    "meaning": "n. 梯级, 楼梯, 阶梯"
  },
  "stake": {
    "phonetic": "steik",
    "meaning": "n. 桩, 炮烙刑, 木柱, 赌注, 奖金；vt. 打桩, 用桩撑, 下赌注, 资助；vi. 打赌"
  },
  "stale": {
    "phonetic": "steil",
    "meaning": "n. 尿；a. 不新鲜的, 陈腐的, 疲惫的, 陈旧的；vt. 使变旧, 走味；vi. 变陈旧, 走味, 失时效, 撒尿"
  },
  "stalk": {
    "phonetic": "stɒ:k",
    "meaning": "n. 茎, 追踪, 高视阔步；vi. 悄悄靠近, 蹑手蹑脚地走近, 蔓延, 高视阔步；vt. 追踪, 搜索"
  },
  "stall": {
    "phonetic": "stɒ:l",
    "meaning": "n. 厩, 停车处, 牧师职位, 货摊, 托辞, 拖延；vt. 关入厩, 停顿, 推托, 支吾, 使陷于泥中；vi. 被关在厩内, 陷于泥中, 停止, 支吾"
  },
  "stamp": {
    "phonetic": "stæmp",
    "meaning": "n. 印, 邮票, 打印器, 戳子, 图章, 印花税票, 标志, 特征, 类型, 跺脚；vt. 盖章于, 顿足, 贴上邮票, 铭刻, 捣碎, 扑灭；vi. 捣碎, 跺脚"
  },
  "stand": {
    "phonetic": "stænd",
    "meaning": "n. 站立, 站住, 停顿, 讲台, 看台, 立场, 法院证人席；vi. 站, 立, 坐落, 停滞, 位于, 坚持, 维持原状；vt. 忍受, 使站立, 抵挡"
  },
  "stank": {
    "phonetic": "stæŋk",
    "meaning": "n. 池塘, 水沟, 小水坝；stink的过去式"
  },
  "staph": {
    "phonetic": "stæf",
    "meaning": "n. <口> = staphylococcus"
  },
  "stare": {
    "phonetic": "stєә",
    "meaning": "vi. 注视, 凝视, 瞪视, 显眼；vt. 盯；n. 凝视"
  },
  "stark": {
    "phonetic": "stɑ:k",
    "meaning": "a. 僵硬的, 完全的, 刻板的, 明显的, 荒凉的, 结实的；adv. 突出地, 简直, 全然"
  },
  "start": {
    "phonetic": "stɑ:t",
    "meaning": "n. 惊起, 出发, 开端, 起点, 吃惊, 有利条件；vi. 开始, 出发, 启动, 跳起, 吃惊, 出现, 松动, 脱落, 起价, 参赛；vt. 使惊起, 开动, 发动, 启动, 开始, 创办, 提议, 使松动, 使脱落, 起用；[计] 起始"
  },
  "stash": {
    "phonetic": "stæʃ",
    "meaning": "vt. 藏起来；n. 隐藏处, 隐藏物"
  },
  "state": {
    "phonetic": "steit",
    "meaning": "n. 州, 状态, 情形, 国家, 政府, 领土, 国务, 社会地位；a. 国家的, 正式的, 礼仪用的, 州的；vt. 说明, 陈述, 规定；[计] 状态"
  },
  "stave": {
    "phonetic": "steiv",
    "meaning": "n. 狭板, 梯级, 棍棒, 诗句；vt. 击穿, 弄破, 敲打, 赶走；vi. 穿孔, 破碎"
  },
  "stead": {
    "phonetic": "sted",
    "meaning": "n. 代替, 接替, 有利, 用处, 好处；vt. 对...有利"
  },
  "steak": {
    "phonetic": "steik",
    "meaning": "n. 牛排, 鱼排, 肉排"
  },
  "steal": {
    "phonetic": "sti:l",
    "meaning": "vt. 剽窃；偷偷地做；偷窃；vi. 窃取；偷偷地行动；[棒球]偷垒；n. [口]偷窃；便宜货；偷垒；[篮球]断球"
  },
  "steam": {
    "phonetic": "sti:m",
    "meaning": "n. 蒸汽, 精力；a. 蒸汽的；vi. 蒸发, 行驶, 发怒；vt. 蒸, 煮, 散发"
  },
  "steed": {
    "phonetic": "sti:d",
    "meaning": "n. 战马"
  },
  "steel": {
    "phonetic": "sti:l",
    "meaning": "n. 钢, 钢制品, 钢铁, 坚硬, 坚固；a. 钢的, 钢制的, 钢铁业的, 坚强的；vt. 使坚强, 钢化, 使冷酷"
  },
  "steep": {
    "phonetic": "sti:p",
    "meaning": "n. 浸渍, 悬崖；a. 险峻的, 陡峭的, 急剧升降的, 夸大的；v. 浸, 泡"
  },
  "steer": {
    "phonetic": "stiә",
    "meaning": "vt. 引导, 驾驶, 航行, 控制；vi. 驾驶, 掌舵, 行驶；n. 驾驶指示, 劝告"
  },
  "stein": {
    "phonetic": "stain",
    "meaning": "n. 啤酒杯"
  },
  "steno": {
    "phonetic": "'stenәu",
    "meaning": "n. 速记员, 速记, 速记法"
  },
  "stent": {
    "phonetic": "",
    "meaning": "[医] 斯滕特氏印模膏; 斯滕特氏印模; 移植片固定模"
  },
  "stern": {
    "phonetic": "stә:n",
    "meaning": "n. 尾部, 船尾, 臀；a. 严厉的, 严格的, 坚定的, 坚决的"
  },
  "stick": {
    "phonetic": "stik",
    "meaning": "n. 棍, 棒, 刺, 枯枝, 茎, 条状物；vt. 插进, 刺入, 钉住, 伸出, 粘贴, 停止；vi. 粘住, 停留, 坚持, 陷住, 伸出"
  },
  "stiff": {
    "phonetic": "stif",
    "meaning": "a. 坚硬的, 严厉的, 呆板的, 生硬的, 刚强的, 强烈的, 粘的, 稠的, 艰难的；n. 死尸, 醉鬼, 钞票；vt. 不肯付...小费"
  },
  "still": {
    "phonetic": "stil",
    "meaning": "n. 蒸馏室, 寂静, 剧照；v. 蒸馏, (使)平静, (使)静止；a. 静止的, 不动的, 静寂的, 不起泡的, 静物摄影的；adv. 仍然, 更, 静止地；conj. 然而, 但是"
  },
  "stilt": {
    "phonetic": "stilt",
    "meaning": "n. 高跷, 支柱, 脚柱"
  },
  "sting": {
    "phonetic": "stiŋ",
    "meaning": "n. 叮, 刺痛, 刺激, 讽刺；vt. 叮, 刺痛, 刺激, 使苦恼；vi. 叮, 刺痛"
  },
  "stink": {
    "phonetic": "stiŋk",
    "meaning": "n. 臭味, 臭气；vi. 发臭味, 名声臭；vt. 用臭味赶"
  },
  "stint": {
    "phonetic": "stint",
    "meaning": "vt. 节省, 限制, 停止；vi. 节约；n. 吝惜, 节约, 限额"
  },
  "stock": {
    "phonetic": "stɒk",
    "meaning": "n. 树干, 祖先, 血统, 原料, 备料, 库存, 牲畜, 股票, 股份, 保留剧目；a. 存货的, 常备的, 平凡的, 普通的, 股票的, 保留剧目的, 繁殖用的；vt. 装把手于, 进货, 备有, 放牧；vi. 出新芽, 备货, 囤积"
  },
  "stoic": {
    "phonetic": "'stәuik",
    "meaning": "a. 斯多葛派的, 禁欲主义的, 不以苦乐为意的, 坚忍的, 淡泊的；n. 斯多葛派学者, 画廊派的人, 禁欲主义者, 不介意苦乐的人, 高度自制的人"
  },
  "stoke": {
    "phonetic": "stәuk",
    "meaning": "v. 司炉, (使)大吃"
  },
  "stole": {
    "phonetic": "stәul",
    "meaning": "n. 女用披肩, 圣衣；steal的过去式"
  },
  "stomp": {
    "phonetic": "stɒmp",
    "meaning": "n. 跺脚；vt. 跺, 践踏；vi. 跺脚, 践踏"
  },
  "stone": {
    "phonetic": "stәun",
    "meaning": "n. 石头, 宝石, 果核, 纪念碑, 结石；vt. 投扔石子, 铺石头；a. 石的, 石制的, 完全的"
  },
  "stony": {
    "phonetic": "'stәuni",
    "meaning": "a. 多石的, 无情的"
  },
  "stood": {
    "phonetic": "stud",
    "meaning": "stand的过去式和过去分词"
  },
  "stool": {
    "phonetic": "stu:l",
    "meaning": "n. 凳子, 大便, 粪便, 厕所；vi. 长新枝；vt. 引诱, 诱捕"
  },
  "stoop": {
    "phonetic": "stu:p",
    "meaning": "n. 佝偻, 屈从, 弯腰；vi. 弯下, 屈从, 弯腰, 堕落；vt. 使屈从, 使弯曲"
  },
  "store": {
    "phonetic": "stɒ:",
    "meaning": "n. 商店, 贮藏, 仓库, 备用品, 存储器；vt. 储存, 贮藏, 供给；vi. 贮藏；a. 贮藏的, 现成的；[计] 存储器操作; 存储"
  },
  "stork": {
    "phonetic": "stɒ:k",
    "meaning": "n. 鹳"
  },
  "storm": {
    "phonetic": "stɒ:m",
    "meaning": "n. 暴风雨, 骚动, 风波, 风暴, 猛攻；vi. 起风, 猛冲, 怒吼；vt. 猛攻"
  },
  "story": {
    "phonetic": "'stɒ:ri",
    "meaning": "n. 故事, 小说, 传奇, 描述, 阅历, 经历, 层"
  },
  "stout": {
    "phonetic": "staut",
    "meaning": "a. 结实的；矮胖的；勇敢的；激烈的；n. 矮胖子；烈性啤酒"
  },
  "stove": {
    "phonetic": "stәuv",
    "meaning": "n. 火炉, 窑；vt. 用火炉烤；stave的过去式和过去分词"
  },
  "strap": {
    "phonetic": "stræp",
    "meaning": "n. 带, 皮带；vt. (用皮带)捆扎"
  },
  "straw": {
    "phonetic": "strɒ:",
    "meaning": "n. 稻草, 麦管, 吸管, 一文不值的东西, 草帽；a. 稻草的, 稻草色的, 琐碎的, 无价值的"
  },
  "stray": {
    "phonetic": "strei",
    "meaning": "n. 走失的家畜, 浪子；a. 迷途的, 偶然的；vi. 迷路, 彷徨, 流浪"
  },
  "strep": {
    "phonetic": "strep",
    "meaning": "a. 链球菌的"
  },
  "strew": {
    "phonetic": "stru:",
    "meaning": "vt. 散播, 撒满"
  },
  "strip": {
    "phonetic": "strip",
    "meaning": "n. 长条, 条状, 带, 脱衣舞；vt. 脱衣, 被剥去, 剥夺, 拆卸；vi. 脱衣服"
  },
  "strum": {
    "phonetic": "strʌm",
    "meaning": "n. 弹拨(声)；v. 漫不经心地弹, 漫不经心地奏"
  },
  "strut": {
    "phonetic": "strʌt",
    "meaning": "n. 高视阔步, 支柱, 压杆；vi. 趾高气扬地走, 肿胀；vt. 用支柱支撑, 炫耀"
  },
  "stuck": {
    "phonetic": "stʌk",
    "meaning": "stick的过去式和过去分词"
  },
  "study": {
    "phonetic": "'stʌdi",
    "meaning": "n. 学习, 研究, 学科, 论文, 求学, 书房, 试作；vt. 学习, 读书, 研究, 考虑, 计划；vi. 学习, 思索"
  },
  "stuff": {
    "phonetic": "stʌf",
    "meaning": "n. 原料, 要素, 东西, 材料, 素质, 织品, 废物, 废话；vt. 装填；vi. 狼吞虎咽"
  },
  "stump": {
    "phonetic": "stʌmp",
    "meaning": "n. 残株, 树桩, 烟蒂, 讲演台；vt. 砍断, 挑战, 难住；vi. 蹒跚而走"
  },
  "stung": {
    "phonetic": "stʌŋ",
    "meaning": "sting的过去式和过去分词"
  },
  "stunk": {
    "phonetic": "stʌŋk",
    "meaning": "stink的过去式和过去分词"
  },
  "stunt": {
    "phonetic": "stʌnt",
    "meaning": "n. 特技, 绝技, 花招, 噱头, 手腕, 发育不良；vt. 阻碍成长；vi. 表演特技"
  },
  "style": {
    "phonetic": "stail",
    "meaning": "n. 风格, 时尚, 文体, 风度, 字体, 类型；vt. 称呼, (根据新款式)设计, 使合潮流；n. 风格, 样式；[计] 风格, 样式"
  },
  "suave": {
    "phonetic": "swɑ:v",
    "meaning": "a. 柔和的, 温和的, 文雅的"
  },
  "sudsy": {
    "phonetic": "'sʌdzi",
    "meaning": "a. 肥皂一般的, 起着泡沫的"
  },
  "suede": {
    "phonetic": "sweid",
    "meaning": "n. 小山羊皮, 起毛皮革, 表面粗糙的软皮革, 麂皮；[机] 绒面革"
  },
  "sugar": {
    "phonetic": "'ʃugә",
    "meaning": "n. 糖, 糖块, 甜言蜜语；vt. 加糖于, 使甜蜜, 粉饰, 美化；vi. 制成糖"
  },
  "suing": {
    "phonetic": "",
    "meaning": "vbl. 控诉"
  },
  "suite": {
    "phonetic": "swi:t",
    "meaning": "n. 随员, 套房, (一)组, (一)套, 组曲, 继之而来的事；[电] 程序组"
  },
  "sulky": {
    "phonetic": "'sʌlki",
    "meaning": "a. 生气的, 阴沉的"
  },
  "sully": {
    "phonetic": "'sʌli",
    "meaning": "vt. 玷污, 弄脏；n. 污点, 脏污"
  },
  "sumac": {
    "phonetic": "'su:mæk, 'ʃu:-",
    "meaning": "[医] 漆树[属植物]"
  },
  "sunny": {
    "phonetic": "'sʌni",
    "meaning": "a. 阳光充足的, 乐观的, 快乐的, 像太阳的"
  },
  "sunup": {
    "phonetic": "'sʌnʌp",
    "meaning": "n. 日出"
  },
  "super": {
    "phonetic": "'sju:pә",
    "meaning": "n. 跑龙套角色, 冗员, 特级品, 特大号, 管理人；a. 上等的, 特大的, 超级的, 极好的, 十分的, 过分的；adv. 非常"
  },
  "surer": {
    "phonetic": "",
    "meaning": "a. 确信的；可靠的；必定的 (sure的变形)"
  },
  "surge": {
    "phonetic": "sә:dʒ",
    "meaning": "n. 巨涌, 汹涌, 澎湃；vi. 汹涌, 澎湃, 颠簸, 猛冲, 突然放松；vt. 使汹涌奔腾, 急放；[计] 电压尖峰"
  },
  "surly": {
    "phonetic": "'sә:li",
    "meaning": "a. 不和蔼的, 无礼的, 板面孔的, 阴沉的, 粗暴的, 乖戾的"
  },
  "sushi": {
    "phonetic": "'su:ʃi",
    "meaning": "n. 寿司（生鱼片冷饭团）"
  },
  "swain": {
    "phonetic": "swein",
    "meaning": "n. 乡村青年；情郎；求爱者"
  },
  "swale": {
    "phonetic": "sweil",
    "meaning": "n. 沼泽地, 低洼地；vt. 放火烧；vi. 烧焦"
  },
  "swami": {
    "phonetic": "'swɑ:mi",
    "meaning": "n. 偶像, 哲人"
  },
  "swamp": {
    "phonetic": "swɒmp",
    "meaning": "n. 沼泽, 进退两难的困境；vt. 淹没, 击溃, 清除, 使陷于沼泽；vi. 陷于沼泽, 淹没"
  },
  "swang": {
    "phonetic": "swæŋ",
    "meaning": "vbl.swing的过去式"
  },
  "swank": {
    "phonetic": "swæŋk",
    "meaning": "vi. 出风头, 炫耀；n. 出风头, 炫耀, 虚张声势, 优雅"
  },
  "swarm": {
    "phonetic": "swɒ:m",
    "meaning": "n. 群, 大群, 蜂群, 分蜂群；vi. 分群, 群集, 聚集一块, 云集, 攀；vt. 挤满, 爬, 攀"
  },
  "swash": {
    "phonetic": "swɒʃ",
    "meaning": "vi. 飞溅, 溅泼, 恐吓；vt. 泼, 冲洗；n. 泼水声, 吓唬, 虚张声势"
  },
  "swath": {
    "phonetic": "swɔ:θ",
    "meaning": "n. 刈幅, 刈下的一行草, 刈下的一行麦, 行, 一条, 条, 一行"
  },
  "swear": {
    "phonetic": "swєә",
    "meaning": "vt. 发誓, 咒骂, 使宣誓；vi. 发誓, 诅咒；n. 诅咒, 誓言"
  },
  "sweat": {
    "phonetic": "swet",
    "meaning": "n. 汗, 汗水, 水珠, 焦急；vi. 出汗, 渗出, 冒出水气, 结水珠, 烦恼, 懊恼；vt. 使出汗, 流出, 榨出, 使汗流浃背"
  },
  "sweep": {
    "phonetic": "swi:p",
    "meaning": "n. 扫除, 打扫, 肃清, 视野, 范围, 全胜；vt. 扫除, 掸去, 猛拉, 扫荡, 肃清, 冲走, 刮起, 环视, 掠过, 扫射；vi. 扫, 打扫, 袭击, 席卷, 扫视, 掠过"
  },
  "sweet": {
    "phonetic": "swi:t",
    "meaning": "n. 甜蜜, 糖果, 情人；a. 甜的, 芳香的, 悦耳的, 漂亮的, 和蔼的, 不咸的, 灵活的, 轻快的"
  },
  "swell": {
    "phonetic": "swel",
    "meaning": "n. 增大, 隆起的部分, 巨浪, 肿胀；a. 优秀的, 一流的；vi. 增大, 膨胀, 肿胀, 增强, 骄傲；vt. 使膨胀, 使增大, 使上涨, 使骄傲"
  },
  "swept": {
    "phonetic": "swept",
    "meaning": "sweep的过去式和过去分词"
  },
  "swift": {
    "phonetic": "swift",
    "meaning": "n. 褐雨燕, 快速爬行的小蜥蜴, 蝙蝠蛾, 大滚筒；a. 迅速的, 快的, 敏捷的, 立刻的；adv. 迅速地, 敏捷地"
  },
  "swill": {
    "phonetic": "swil",
    "meaning": "vt. 冲洗, 痛饮；vi. 大口地喝, 冲刷；n. 涮, 冲洗, 痛饮, 泔脚"
  },
  "swine": {
    "phonetic": "swain",
    "meaning": "n. 猪, 卑鄙的家伙"
  },
  "swing": {
    "phonetic": "swiŋ",
    "meaning": "n. 摇摆, 振幅, 音律, 节奏, 涨落, 秋千, 旋转, 行动自由；vi. 摇摆, 悬挂, 旋转, 大摇大摆地走, 转向；vt. 挥舞, 使旋转, 使转向, 悬挂, 吊运；a. 旋转的, 悬挂的, 强节奏爵士音乐的"
  },
  "swipe": {
    "phonetic": "swaip",
    "meaning": "n. 强打, 用力挥击, 尖刻的话, 碰擦, 起重杆；vt. 强打, 用力挥击, 偷"
  },
  "swirl": {
    "phonetic": "swә:l",
    "meaning": "n. 漩涡, 涡动；vt. 使成漩涡；vi. 打漩, 盘绕, 眩晕"
  },
  "swish": {
    "phonetic": "swiʃ",
    "meaning": "n. 嗖嗖声；vi. 发嗖嗖声, 嗖地挥动；vt. 嗖地挥动；a. 漂亮的, 时髦的"
  },
  "swoon": {
    "phonetic": "swu:n",
    "meaning": "n. 昏晕, 晕厥；vi. 昏晕, 着迷, 渐渐消失"
  },
  "swoop": {
    "phonetic": "swu:p",
    "meaning": "n. 俯冲, 攫取；vt. 抓取；vi. 猛扑, 突然袭击"
  },
  "sword": {
    "phonetic": "sɒ:d",
    "meaning": "n. 刀, 剑, 战争, 武力, 剑状物"
  },
  "swore": {
    "phonetic": "swɔ:, swɔә",
    "meaning": "swear的过去式；[法] 宣过誓的, 宣誓证明的, 决不改变的"
  },
  "sworn": {
    "phonetic": "swɒ:n",
    "meaning": "swear的过去分词"
  },
  "swung": {
    "phonetic": "swʌŋ",
    "meaning": "swing的过去式和过去分词"
  },
  "synch": {
    "phonetic": "siŋk",
    "meaning": "[计] 同步信号"
  },
  "synod": {
    "phonetic": "'sinәd",
    "meaning": "n. 教会会议, 会议"
  },
  "syrup": {
    "phonetic": "'sirәp",
    "meaning": "n. 糖浆, 果汁；[化] 糖浆剂"
  },
  "tabby": {
    "phonetic": "'tæbi",
    "meaning": "n. 平纹, 斑猫；vt. 使起波纹；a. 平纹组织的, 起波纹的"
  },
  "table": {
    "phonetic": "'teibl",
    "meaning": "n. 桌子, 餐桌, 工作台, 铭文, 表格, 表, 高原, 平地层；vt. 搁置, 嵌合, 制表, 把...列入议事日程；[计] 表格, 模拟运算表"
  },
  "taboo": {
    "phonetic": "tә'bu:",
    "meaning": "n. 禁忌, 禁止接近, 禁止使用；a. 禁忌的, 忌讳的；vt. 禁忌, 忌讳, 禁止"
  },
  "tacit": {
    "phonetic": "'tæsit",
    "meaning": "a. 沉默寡言的, 不苟言笑的, 缄默的"
  },
  "tacky": {
    "phonetic": "'tæki",
    "meaning": "a. 发粘的, 破烂的, 俗丽的"
  },
  "taffy": {
    "phonetic": "'tæfi",
    "meaning": "n. 太妃糖, 阿谀, 威尔士人"
  },
  "taint": {
    "phonetic": "teint",
    "meaning": "n. 污点, 耻辱, 感染；vt. 污染, 使腐败, 沾染, 腐蚀"
  },
  "taken": {
    "phonetic": "'teikәn",
    "meaning": "take的过去分词"
  },
  "taker": {
    "phonetic": "'teikә",
    "meaning": "n. 取者, 捕者, 接受者, 收取者；[法] 受者, 收票人, 接受打赌的人"
  },
  "talky": {
    "phonetic": "'tɒ:ki",
    "meaning": "a. 对话过多的"
  },
  "tally": {
    "phonetic": "'tæli",
    "meaning": "n. 符木, 记账, 得分, 比分, 计数器, 标签, 符合, 对应物；vt. 记录, 点数, 计算, 加标签于, 使符合；vi. 记帐, 符合, 吻合, 记分；[计] 计数"
  },
  "talon": {
    "phonetic": "'tælәn",
    "meaning": "n. 爪, 如爪的手, 魔爪, 爪饰；[医] 磨牙低尖"
  },
  "talus": {
    "phonetic": "'teilәs",
    "meaning": "n. 距骨, 踝, 斜面；[医] 距骨"
  },
  "tamed": {
    "phonetic": "teimd",
    "meaning": "v. （使）服从, 驯服( tame的过去式和过去分词 )"
  },
  "tamer": {
    "phonetic": "'teimә",
    "meaning": "n. 驯服手"
  },
  "tango": {
    "phonetic": "'tæŋgәu",
    "meaning": "n. 探戈舞, 探戈舞曲；vi. 跳探戈舞"
  },
  "tangy": {
    "phonetic": "'tæŋi",
    "meaning": "a. 有强烈盐味的, 气味刺鼻的, 有刺激性的"
  },
  "taped": {
    "phonetic": "",
    "meaning": "n. 录播, 压胶"
  },
  "taper": {
    "phonetic": "'teipә",
    "meaning": "n. 带子操作工, 小蜡烛, 尖细, 渐弱, 锥形, 尖塔；a. 尖细的, 分等级的；v. (使)一头逐渐变细, (使)逐渐减少"
  },
  "tapir": {
    "phonetic": "'teipә",
    "meaning": "n. 貘；[医] 貘"
  },
  "tardy": {
    "phonetic": "'tɑ:di",
    "meaning": "a. 慢的, 迟到的, 勉强的, 拖拉的, 迟的"
  },
  "tarot": {
    "phonetic": "'tærәut",
    "meaning": "n. (算命用的)有图纸牌"
  },
  "tarry": {
    "phonetic": "'tæri",
    "meaning": "vi. 耽搁, 逗留, 留住, 等候；n. 逗留；a. 涂了焦油的"
  },
  "taser": {
    "phonetic": "'teizə",
    "meaning": "n. 泰瑟枪（一种武器）"
  },
  "taste": {
    "phonetic": "teist",
    "meaning": "n. 味道, 品味, 味觉, 感受, 体验, 爱好, 审美, 少量；vt. 尝, 察觉...的味道, 体会；vi. 品尝, 察觉味道, 有某种味道"
  },
  "tasty": {
    "phonetic": "'teisti",
    "meaning": "a. 好吃的, 可口的"
  },
  "tater": {
    "phonetic": "'teitә",
    "meaning": "[口]=potato"
  },
  "tatty": {
    "phonetic": "'tæti",
    "meaning": "a. 穿破的, 粗糙的, 不值钱的"
  },
  "taunt": {
    "phonetic": "tɒ:nt",
    "meaning": "n. 辱骂, 嘲弄；vt. 嘲弄, 奚落；a. 很高的"
  },
  "taupe": {
    "phonetic": "tәup",
    "meaning": "n. 褐灰色"
  },
  "tawny": {
    "phonetic": "'tɒ:ni",
    "meaning": "a. 黄褐色的, 茶色的；n. 黄褐色"
  },
  "taxed": {
    "phonetic": "",
    "meaning": "vt. 使负重担（tax的过去式与过去分词形式）"
  },
  "teach": {
    "phonetic": "ti:tʃ",
    "meaning": "vt. 教, 讲授, 教导, 教育；vi. 教书, 教学, 可以教"
  },
  "teary": {
    "phonetic": "'tiәri",
    "meaning": "a. 哭泣的"
  },
  "tease": {
    "phonetic": "ti:z",
    "meaning": "n. 揶揄, 戏弄, 逗惹；vt. 戏弄, 取笑, 强求, 梳理, 使起毛"
  },
  "teddy": {
    "phonetic": "'tedi",
    "meaning": "n. 连衫衬裤；泰迪玩具熊"
  },
  "teeny": {
    "phonetic": "'ti:ni",
    "meaning": "a. 极小的, 小小的"
  },
  "teeth": {
    "phonetic": "ti:θ",
    "meaning": "pl. 牙齿；[医] 牙"
  },
  "telos": {
    "phonetic": "'telɔs",
    "meaning": "n. 终极,目的"
  },
  "tempo": {
    "phonetic": "'tempәu",
    "meaning": "n. 速度, 节奏, 进行速度, (棋的)一着"
  },
  "tempt": {
    "phonetic": "tempt",
    "meaning": "vt. 诱惑, 引诱, 引起...的兴趣, 吸引, 冒...风险"
  },
  "tenet": {
    "phonetic": "'tenit",
    "meaning": "n. 信条, 教义, 宗旨, 原则"
  },
  "tenor": {
    "phonetic": "'tenә",
    "meaning": "n. 稳定的进程, 思路, 要旨, 大意, 誊本, 票据的限期, 男高音；a. 男高音的"
  },
  "tense": {
    "phonetic": "tens",
    "meaning": "a. 紧张的, 拉紧的；v. (使)紧张, (使)拉紧；n. 时态"
  },
  "tenth": {
    "phonetic": "tenθ",
    "meaning": "num. 第十, 十分之一"
  },
  "tepee": {
    "phonetic": "'ti:pi:",
    "meaning": "n. (印地安人的)圆锥形帐篷"
  },
  "tepid": {
    "phonetic": "'tepid",
    "meaning": "a. 微温的, 温热的, 不太热烈的；[医] 微温的"
  },
  "terra": {
    "phonetic": "'terә",
    "meaning": "[医] 土, 土地"
  },
  "terry": {
    "phonetic": "'teri",
    "meaning": "n. 毛圈, 毛圈织物"
  },
  "terse": {
    "phonetic": "tә:s",
    "meaning": "a. 简洁的, 扼要的"
  },
  "testy": {
    "phonetic": "'testi",
    "meaning": "a. 易怒的, 暴躁的"
  },
  "tetra": {
    "phonetic": "'tetrә",
    "meaning": "n. 脂鲤"
  },
  "thank": {
    "phonetic": "θæŋk",
    "meaning": "n. 谢意, 感谢；vt. 谢谢, 感谢"
  },
  "theft": {
    "phonetic": "θeft",
    "meaning": "n. 盗窃, 失窃, 盗窃罪, 赃物；[法] 盗窃行为, 偷窃, 失窃"
  },
  "their": {
    "phonetic": "ðєә",
    "meaning": "pron. 他们的"
  },
  "theme": {
    "phonetic": "θi:m",
    "meaning": "n. 主题, 话题, 题目"
  },
  "there": {
    "phonetic": "ðєә",
    "meaning": "adv. 在那里"
  },
  "these": {
    "phonetic": "ði:z",
    "meaning": "pron. 这些"
  },
  "theta": {
    "phonetic": "'θeitә",
    "meaning": "n. 希腊字母的第八字"
  },
  "thick": {
    "phonetic": "θik",
    "meaning": "a. 厚的, 粗壮的, 浓的, 迟钝的, 浑浊的, 多雾的, 过分的, 口齿不清的；adv. 厚地, 密地, 浓浓地；n. 最浓处, 最厚处, 最密集处；[计] 暗, 粗线"
  },
  "thief": {
    "phonetic": "θi:f",
    "meaning": "n. 小偷, 贼；[化] 取样"
  },
  "thigh": {
    "phonetic": "θai",
    "meaning": "n. 大腿, 股；[医] 股, 大腿"
  },
  "thine": {
    "phonetic": "ðain",
    "meaning": "pron. 你的东西, 你的"
  },
  "thing": {
    "phonetic": "θiŋ",
    "meaning": "n. 事物, 东西, 物, 用品, 事, 事件, 情况, 行为, 特征"
  },
  "think": {
    "phonetic": "θiŋk",
    "meaning": "vt. 想, 考虑, 想起, 想像, 打算, 认为；vi. 思考, 料想；n. 想法；a. 思想的"
  },
  "third": {
    "phonetic": "θә:d",
    "meaning": "num. 第三, 三分之一；[机] 第三; 第三的"
  },
  "thong": {
    "phonetic": "θɒ:ŋ",
    "meaning": "vt. 装皮带, 用皮鞭打；n. 皮带, 皮鞭"
  },
  "thorn": {
    "phonetic": "θɒ:n",
    "meaning": "n. 刺, 棘, 荆棘"
  },
  "those": {
    "phonetic": "ðәuz",
    "meaning": "pron. 那些"
  },
  "three": {
    "phonetic": "θri:",
    "meaning": "num. 三, 三个"
  },
  "threw": {
    "phonetic": "θru:",
    "meaning": "throw的过去式"
  },
  "throb": {
    "phonetic": "θrɒb",
    "meaning": "n. 跳动, 搏动；vi. 博动, 抽动, 颤动"
  },
  "throw": {
    "phonetic": "θrәu",
    "meaning": "vt. 投, 掷, 抛, 发射, 摔下, 匆匆穿上(或脱下), 抛弃, 摆脱；vi. 丢, 掷, 抛；n. 投掷, 掷骰子, 冒险"
  },
  "thrum": {
    "phonetic": "θrʌm",
    "meaning": "n. 回丝, 花丝, 线头, 纱头, 乱弹；vt. 指弹, 敲打, 把绳毛夹杂于；vi. 乱弹, 轻敲"
  },
  "thumb": {
    "phonetic": "θʌm",
    "meaning": "n. 拇指；vt. 以拇指拨弄, 笨拙地摆弄, 用拇指翻旧, 迅速翻阅, 作搭车手势"
  },
  "thump": {
    "phonetic": "θʌmp",
    "meaning": "n. 重打, 重击声；v. 重打, 撞击, 痛打"
  },
  "thyme": {
    "phonetic": "taim",
    "meaning": "n. 百里香；[医] 百里香, 麝香草"
  },
  "tiara": {
    "phonetic": "ti'ɑ:rә",
    "meaning": "n. 冕状头饰"
  },
  "tibia": {
    "phonetic": "'tibiә",
    "meaning": "n. 胫骨, 胫节, 罗马古笛；[医] 胫骨"
  },
  "tidal": {
    "phonetic": "'taidl",
    "meaning": "a. 潮汐的, 受潮汐影响的"
  },
  "tided": {
    "phonetic": "",
    "meaning": "vt. 顺应潮水航行（tide的过去式与过去分词形式）"
  },
  "tiger": {
    "phonetic": "'taigә",
    "meaning": "n. 老虎, 虎, 凶暴的人"
  },
  "tight": {
    "phonetic": "tait",
    "meaning": "a. 紧的, 密封的, 吝啬的, 严厉的；adv. 紧紧地"
  },
  "tilde": {
    "phonetic": "'tildә",
    "meaning": "n. 波浪字符；加在西班牙语n字上的发音符号"
  },
  "tiled": {
    "phonetic": "taid",
    "meaning": "a. 用砖瓦覆盖的, 瓦状叠覆的；[计] 平铺的"
  },
  "timed": {
    "phonetic": "taimd",
    "meaning": "a. 时控的；定时的, 同步的"
  },
  "timer": {
    "phonetic": "'taimә",
    "meaning": "n. 计时员, 计时器；[计] 计时器"
  },
  "timid": {
    "phonetic": "'timid",
    "meaning": "a. 胆小的, 羞怯的"
  },
  "tinge": {
    "phonetic": "tindʒ",
    "meaning": "n. 色调, 色彩, 气味, 气息；vt. 染, 使带气息"
  },
  "tinny": {
    "phonetic": "'tini",
    "meaning": "a. 锡的, 含锡的, 像锡的"
  },
  "tipsy": {
    "phonetic": "'tipsi",
    "meaning": "a. 喝醉的, 倾斜的"
  },
  "tired": {
    "phonetic": "taiәd",
    "meaning": "a. 疲累的, 疲乏的, 厌倦的"
  },
  "titan": {
    "phonetic": "'taitn",
    "meaning": "n. 提坦, 太阳神, 巨人"
  },
  "titer": {
    "phonetic": "'taitә",
    "meaning": "n. 滴定度, 滴定量；[化] 滴定度"
  },
  "tithe": {
    "phonetic": "taið",
    "meaning": "n. 什一税, 十分之一, 小部分；vt. 课什一税；vi. 缴什一税"
  },
  "title": {
    "phonetic": "'taitl",
    "meaning": "n. 头衔, 名称, 标题, 书名, 扉页, 权利, 资格, 冠军, 字幕；vt. 授予头衔, 加标题于；[计] 标题"
  },
  "tizzy": {
    "phonetic": "'tizi",
    "meaning": "n. 万分惊讶"
  },
  "toady": {
    "phonetic": "'tәudi",
    "meaning": "n. 谄媚者, 马屁精；v. 谄媚, 拍马屁"
  },
  "toast": {
    "phonetic": "tәust",
    "meaning": "n. 吐司, 烤面包, 干杯；vt. 敬酒, 烤, 使暖和；vi. 烤, 烘"
  },
  "today": {
    "phonetic": "tә'dei",
    "meaning": "n. 今天, 当今, 现在；adv. 今天, 当今"
  },
  "toddy": {
    "phonetic": "'tɒdi",
    "meaning": "n. 棕榈汁, 棕榈酒；[医] 棕榈汁; 棕榈酒"
  },
  "token": {
    "phonetic": "'tәukәn",
    "meaning": "n. 表征, 记号, 代币；a. 象征的, 表意的；[计] 记号"
  },
  "tonal": {
    "phonetic": "'tәunl",
    "meaning": "a. 音调的, 色调的"
  },
  "toned": {
    "phonetic": "'tәund",
    "meaning": "a. 有声调的, 年久变色的"
  },
  "toner": {
    "phonetic": "'tәunә",
    "meaning": "n. 调色剂；[计] 增色剂; 色粉"
  },
  "toney": {
    "phonetic": "'tәjni",
    "meaning": "a. 高贵的,时髦的, Tony 托尼(男子名)"
  },
  "tonga": {
    "phonetic": "'tɔŋ^ә",
    "meaning": "[医] 雅司病"
  },
  "tonic": {
    "phonetic": "'tɒnik",
    "meaning": "n. 补药, (音乐)主调音或基音；a. 滋补的, 声调的, 使精神振作的"
  },
  "tooth": {
    "phonetic": "tu:θ",
    "meaning": "n. 牙齿, 齿状物, 爱好；vt. 装以齿, 将...切成齿状；vi. 啮合"
  },
  "topaz": {
    "phonetic": "'tәupæz",
    "meaning": "n. 黄晶, 黄玉, 南美蜂岛；[化] 黄玉"
  },
  "topic": {
    "phonetic": "'tɒpik",
    "meaning": "n. 主题, 论题, 话题"
  },
  "torah": {
    "phonetic": "'tәurә",
    "meaning": "n. 教导, 律法, <<旧约>>之首五卷；[法] 教训, 神论, 法律"
  },
  "torch": {
    "phonetic": "tɒ:tʃ",
    "meaning": "n. 火把, 启发之物；[化] 火炬"
  },
  "torso": {
    "phonetic": "'tɔ:sәu",
    "meaning": "n. 躯干, 裸体躯干雕像；[医] 躯干"
  },
  "torte": {
    "phonetic": "tɔ:t",
    "meaning": "n. 德国大蛋糕,果子奶油蛋糕"
  },
  "torus": {
    "phonetic": "'tɒ:rәs",
    "meaning": "n. 花托, 隆凸, 环面；[化] 螺绕环"
  },
  "total": {
    "phonetic": "'tәutl",
    "meaning": "a. 全体的, 总的, 全然的；vt. 计算...的总和, 共计为；vi. 合计；n. 总数, 全体, 合计；adv. 统统"
  },
  "toted": {
    "phonetic": "təutid",
    "meaning": "v. 手提, 背负, 携带( tote的过去式和过去分词 )"
  },
  "totem": {
    "phonetic": "'tәutәm",
    "meaning": "n. 图腾, 标志物, 崇拜物"
  },
  "touch": {
    "phonetic": "tʌtʃ",
    "meaning": "n. 触觉, 碰, 触, 机灵, 轻触, 格调, 少许, 缺点, 弹力；vt. 接触, 触摸, 触及, 使接触, 达到, 涉及, 影响到, 使轻度受害, 感动；vi. 触摸, 接近, 涉及, 提到"
  },
  "tough": {
    "phonetic": "tʌf",
    "meaning": "n. 恶棍；a. 强硬的, 艰苦的, 坚固的, 坚韧的, 粗暴的, 咬不动的"
  },
  "towed": {
    "phonetic": "təud",
    "meaning": "v. 拖, 拉, 拽( tow的过去式和过去分词 )"
  },
  "towel": {
    "phonetic": "'tauәl",
    "meaning": "n. 手巾, 毛巾；v. 擦干身子"
  },
  "tower": {
    "phonetic": "'tauә",
    "meaning": "n. 塔, 高楼, 堡垒；vi. 高耸, 翱翔"
  },
  "toxic": {
    "phonetic": "'tɒksik",
    "meaning": "a. 有毒的, 中毒的；[医] 中毒的, 毒物的"
  },
  "toxin": {
    "phonetic": "'tɒksin",
    "meaning": "n. 毒素；[化] 毒素"
  },
  "toyed": {
    "phonetic": "",
    "meaning": "(toy 的过去时) n. 玩具, 小玩艺儿, 小型的东西, 消遣；a. 供玩耍的, 作为玩具的；vi. 玩弄, 戏弄, 调情"
  },
  "trace": {
    "phonetic": "treis",
    "meaning": "n. 痕迹, 踪迹, 微量, 迹线, 缰绳；vt. 追踪, 回溯, 描绘；vi. 追溯, 沿路走"
  },
  "track": {
    "phonetic": "træk",
    "meaning": "n. 轨迹, 足迹, 径迹, 小道, 轨道, 磁轨, 途径；vt. 循路而行, 追踪, 通过, 用纤拉；vi. 追踪, 留下足迹, 沿轨道运行；[计] 跟踪"
  },
  "tract": {
    "phonetic": "trækt",
    "meaning": "n. 大片土地, 地带, 小册子；[医] 束, 道"
  },
  "trade": {
    "phonetic": "treid",
    "meaning": "n. 贸易, 商业, 交易, 生意, 职业, 顾客, 信风；vi. 进行交易, 做买卖, 经商, 对换, 购物；vt. 用...进行交换"
  },
  "trail": {
    "phonetic": "treil",
    "meaning": "n. 踪迹, 痕迹, 一串, 尾部, 小径, 持枪姿势；vt. 拖, 尾随, 追踪, 落后于, 开出路；vi. 拖曳, 垂下, 落后, 飘出, 蔓生"
  },
  "train": {
    "phonetic": "trein",
    "meaning": "n. 火车, 列车, 行列, 长队, 一连串的后果, 顺序；vt. 训练, 教育, 对准；vi. 受训练, 锻炼"
  },
  "trait": {
    "phonetic": "treit",
    "meaning": "n. 特征, 特性, 一笔, 少许"
  },
  "tramp": {
    "phonetic": "træmp",
    "meaning": "n. 坚实(或沉重)的脚步声, 流浪者；vi. 践踏, 重步行走, 步行, 流浪；vt. 走过, 踩"
  },
  "trans": {
    "phonetic": "",
    "meaning": "[电] transimitter的简写"
  },
  "trash": {
    "phonetic": "træʃ",
    "meaning": "n. 垃圾, 废物；vt. 丢弃"
  },
  "trawl": {
    "phonetic": "trɒ:l",
    "meaning": "n. 拖网；v. 用拖网捕鱼"
  },
  "tread": {
    "phonetic": "tred",
    "meaning": "n. 踏, 步态, 梯级, 交尾, 鞋底；vi. 踏, 行走, 交尾；vt. 踩, 踏, 践踏, 跳(舞)"
  },
  "treat": {
    "phonetic": "tri:t",
    "meaning": "n. 宴请, 款待；vt. 视为, 对待, 论述, 治疗, 款待；vi. 讨论, 谈判, 作东"
  },
  "treed": {
    "phonetic": "tri:d",
    "meaning": "育林的, 植树的"
  },
  "trend": {
    "phonetic": "trend",
    "meaning": "n. 趋势, 倾向, 走向；vi. 倾向, 转向；[计] 趋势"
  },
  "tress": {
    "phonetic": "tres",
    "meaning": "n. 一绺头发, 头发, 发辫"
  },
  "triad": {
    "phonetic": "'traiәd",
    "meaning": "n. 三个一组, 三件一组, 三和音；[计] 三元组"
  },
  "trial": {
    "phonetic": "'traiәl",
    "meaning": "n. 审判, 试验, 艰苦, 麻烦事, 考验；a. 审讯的, 试验性的"
  },
  "tribe": {
    "phonetic": "traib",
    "meaning": "n. 宗族, 部落, 一群人；[医] 族(生物分类)"
  },
  "trice": {
    "phonetic": "trais",
    "meaning": "vt. 吊起, 扯起并用绳缚住；n. 瞬间"
  },
  "trick": {
    "phonetic": "trik",
    "meaning": "n. 诡计, 欺诈, 谋略, 恶作剧, 习惯, 决窍；vt. 愚弄, 欺骗, 装饰；vi. 哄骗, 戏弄；a. 有决窍的, 特技的, 欺诈的, 漂亮的, 靠不住的"
  },
  "tried": {
    "phonetic": "traid",
    "meaning": "a. 试验过的, 可靠的；[法] 已经审讯的, 已经查验的"
  },
  "trike": {
    "phonetic": "traik",
    "meaning": "n. 三轮车"
  },
  "trill": {
    "phonetic": "tril",
    "meaning": "n. 颤声, 颤音, 啭鸣；vt. 用颤声说, 用颤音唱；vi. 发出颤音"
  },
  "tripe": {
    "phonetic": "traip",
    "meaning": "n. 肚子"
  },
  "trite": {
    "phonetic": "trait",
    "meaning": "a. 老一套的, 陈腐的, 用坏的"
  },
  "troll": {
    "phonetic": "trɒl",
    "meaning": "vi. 滚动, 参加轮唱, 曳绳钓鱼；vt. 使转动, 轮唱, 高唱, 用曳绳钓(鱼)；n. 转动, 轮唱, 钓绳"
  },
  "tromp": {
    "phonetic": "trɔmp",
    "meaning": "v. 践踏, 跺脚"
  },
  "troop": {
    "phonetic": "tru:p",
    "meaning": "n. 军队, 一群, 一队；vi. 群集, 结队, 成群而行"
  },
  "trope": {
    "phonetic": "trәup",
    "meaning": "n. 转义, 比喻"
  },
  "trout": {
    "phonetic": "traut",
    "meaning": "n. 鲑鱼"
  },
  "trove": {
    "phonetic": "trәuv",
    "meaning": "n. 发现物, 收藏品；[法] 发现物, 收藏物"
  },
  "truce": {
    "phonetic": "tru:s",
    "meaning": "n. 停战, 休战；vi. 停战, 休止；vt. 以休战结束"
  },
  "truck": {
    "phonetic": "trʌk",
    "meaning": "n. 卡车, 货车, 对...进行交易, 来往, 实物工资, (供应市场的)蔬菜, 废物, 废话；vt. 对...进行交易, 交往, 以卡车运输；vi. 驾驶卡车, 以物易物"
  },
  "truer": {
    "phonetic": "'tru:ә",
    "meaning": "a. 真的；确实的"
  },
  "truly": {
    "phonetic": "'tru:li",
    "meaning": "adv. 真实地, 不假"
  },
  "trump": {
    "phonetic": "trʌmp",
    "meaning": "n. 王牌, 法宝, 喇叭；vt. 打出王牌赢, 胜过；vi. 出王牌, 吹喇叭"
  },
  "trunk": {
    "phonetic": "trʌŋk",
    "meaning": "n. 树干, 干线, 躯干, 主干, 象鼻, 箱子；vt. 把...放入旅行箱内；a. 树干的, 躯干的, 干线的, 箱形的；[计] 中继线; 母线"
  },
  "truss": {
    "phonetic": "trʌs",
    "meaning": "vt. 捆绑；n. 捆, 束"
  },
  "trust": {
    "phonetic": "trʌst",
    "meaning": "n. 信任, 信赖, 相信, 受托, 职责, 信心, 托拉斯；a. 信托的, 托拉斯的；vt. 信赖, 信任, 相信, 盼望, 赊卖给；vi. 相信, 信赖, 依靠；[计] 委托, 信任"
  },
  "truth": {
    "phonetic": "tru:θ",
    "meaning": "n. 事实, 实情；[法] 真实, 真相, 事实"
  },
  "tryst": {
    "phonetic": "trist",
    "meaning": "n. 约会, 幽会；v. 约会"
  },
  "tubal": {
    "phonetic": "'tju:bl",
    "meaning": "a. 管的, 输卵管的；[医] 管的"
  },
  "tubby": {
    "phonetic": "'tʌbi",
    "meaning": "a. 桶状的, 肥胖的, 发钝音的"
  },
  "tubed": {
    "phonetic": "",
    "meaning": "vt. 把…装管（tube的过去式与过去分词形式）"
  },
  "tuber": {
    "phonetic": "'tju:bә",
    "meaning": "n. 块茎, 突起, 结节；[医] 结节; 块茎(植物)"
  },
  "tufty": {
    "phonetic": "'tʌfti",
    "meaning": "a. 簇生的, 多簇的, 丛生的"
  },
  "tulip": {
    "phonetic": "'tju:lip",
    "meaning": "n. 郁金香"
  },
  "tulle": {
    "phonetic": "tju:l",
    "meaning": "n. 薄纱"
  },
  "tummy": {
    "phonetic": "'tʌmi",
    "meaning": "n. 胃, 肚子"
  },
  "tumor": {
    "phonetic": "'tju:mә",
    "meaning": "n. 肿大, 肿块, 瘤, 赘生物, 肿瘤；[医] 瘤; 肿胀, 肿块"
  },
  "tuned": {
    "phonetic": "tju:nd",
    "meaning": "[计] 调谐的"
  },
  "tuner": {
    "phonetic": "'tju:nә",
    "meaning": "n. 调音师, 调音的人, 调节器；[电] 调谐器"
  },
  "tunic": {
    "phonetic": "'tju:nik",
    "meaning": "n. 束腰外衣；[医] 膜, 被膜"
  },
  "turbo": {
    "phonetic": "'tә:bәu",
    "meaning": "n. 涡轮增压器"
  },
  "tutor": {
    "phonetic": "'tju:tә",
    "meaning": "n. 家庭教师, 导师, 助教, 监护人；vt. 当...的教师, 教, 指导, 约束, 克制；vi. 当家庭教师, 受家庭教师的指导"
  },
  "twain": {
    "phonetic": "'twein",
    "meaning": "n. 二, 两, 一对"
  },
  "twang": {
    "phonetic": "twæŋ",
    "meaning": "n. 弦声, 砰然一声, 鼻音；vi. 砰然响, 发拨弦声, 带鼻音讲话；vt. 用鼻音讲, 使发拨弦声"
  },
  "tweak": {
    "phonetic": "twi:k",
    "meaning": "n. 拧, 扭, 焦急；vt. 扭, 开足马力"
  },
  "tweed": {
    "phonetic": "twi:d",
    "meaning": "n. (粗)花呢, 花呢服装"
  },
  "tween": {
    "phonetic": "twi:n",
    "meaning": "[医] 吐温(一类表面活性剂的商品名,聚氧乙烯山梨醇的脂肪酸脂)"
  },
  "tweet": {
    "phonetic": "twi:t",
    "meaning": "vi. 啁啾；n. 小鸟叫声"
  },
  "twerk": {
    "phonetic": "",
    "meaning": ""
  },
  "twerp": {
    "phonetic": "twә:p",
    "meaning": "n. 讨厌的家伙, 蠢人"
  },
  "twice": {
    "phonetic": "twais",
    "meaning": "adv. 两次, 两倍"
  },
  "twill": {
    "phonetic": "twil",
    "meaning": "n. 斜纹织物；vt. 把...织成斜纹"
  },
  "twine": {
    "phonetic": "twain",
    "meaning": "n. 合股线, 麻线, 搓；v. 搓, (使)交织, 编饰, (使)缠绕"
  },
  "twirl": {
    "phonetic": "twә:l",
    "meaning": "vt. (使)快速转动, 捻弄；n. 转动, 万能钥匙, 旋转的东西"
  },
  "twist": {
    "phonetic": "twist",
    "meaning": "n. 一扭, 扭曲, 曲折, 歪曲, 螺旋状, 新手法；vt. 拧, 扭, 捻, 编织, 使扭转, 缠绕, 盘绕, 歪曲, 使转动, 使苦恼, 使混乱, 使旋转；vi. 转向, 弯曲, 缠绕, 扭动, 呈螺旋形"
  },
  "twixt": {
    "phonetic": "twikst",
    "meaning": "prep. <诗>=between"
  },
  "tying": {
    "phonetic": "'taiiŋ",
    "meaning": "tie的现在分词"
  },
  "typed": {
    "phonetic": "",
    "meaning": "vt. 打字（type的过去式和过去分词）"
  },
  "udder": {
    "phonetic": "'ʌdә",
    "meaning": "n. (母牛等的)乳房；[医] 乳房(牛羊等)"
  },
  "ulcer": {
    "phonetic": "'ʌlsә",
    "meaning": "n. 溃疡, 腐烂物；[医] 溃疡"
  },
  "ulnar": {
    "phonetic": "'ʌlnә",
    "meaning": "a. 尺骨的；[医] 尺骨的, 尺侧的"
  },
  "ultra": {
    "phonetic": "'ʌltrә",
    "meaning": "a. 过分的, 极端的；n. 极端主义者, 过激论者, 急进论者"
  },
  "umber": {
    "phonetic": "'ʌmbә",
    "meaning": "n. 棕土, 棕土色；a. 棕色的, 棕土色的；vt. 涂红棕色于"
  },
  "umbra": {
    "phonetic": "'ʌmbrә",
    "meaning": "n. 阴影, 本影, 暗影；[化] 本影"
  },
  "unarm": {
    "phonetic": ".ʌn'ɑ:m",
    "meaning": "vt. 缴械；vi. 放下武器"
  },
  "unbag": {
    "phonetic": ",ʌn'bæ^",
    "meaning": "vt.把…从袋里倒(或取、放)出来"
  },
  "unbox": {
    "phonetic": ",ʌn'bɔks",
    "meaning": "vt.从箱子中取出"
  },
  "uncap": {
    "phonetic": ".ʌn'kæp",
    "meaning": "vt. 脱掉帽子, 打开盖；vi. 脱帽"
  },
  "uncle": {
    "phonetic": "ʌŋkl",
    "meaning": "n. 叔父, 伯父, 姨丈"
  },
  "uncut": {
    "phonetic": "'ʌn'kʌt",
    "meaning": "a. 未割的, 未修剪的, 未切的, 边未切齐的, 毛边的, 未削减的, 未缩略的"
  },
  "under": {
    "phonetic": "'ʌndә",
    "meaning": "prep. 在...之下, 低于；a. 下面的, 从属的；adv. 在下面"
  },
  "undid": {
    "phonetic": ".ʌn'did",
    "meaning": "undo的过去式"
  },
  "undue": {
    "phonetic": ".ʌn'dju:",
    "meaning": "a. 不适当的, 过度的, 未到期的；[经] 未到(支付)期的"
  },
  "unfed": {
    "phonetic": "'ʌn'fed",
    "meaning": "a. 得不到食物的, 没东西吃的, 得不到支持的"
  },
  "unfit": {
    "phonetic": ".ʌn'fit",
    "meaning": "a. 不适当的, 不胜任的, 不健康的；vt. 使不相宜, 使不合格"
  },
  "unhip": {
    "phonetic": "'ʌn'hip",
    "meaning": "a. 非赶时髦派的,不谙时髦的,不符合集团其他成员所遵循的习俗的"
  },
  "unify": {
    "phonetic": "'ju:nifai",
    "meaning": "v. 统一, 使成一体"
  },
  "union": {
    "phonetic": "'ju:njәn",
    "meaning": "n. 联盟, 联合, 结合, 工会；[化] 联合; 联管节; 活接头"
  },
  "unite": {
    "phonetic": "ju:'nait",
    "meaning": "vi. 联合, 接合, 混合；vt. 使联合, 统一, 使粘合, 使结合"
  },
  "unity": {
    "phonetic": "'ju:niti",
    "meaning": "n. 一致, 联合, 单一(性), 个体；[经] 统一"
  },
  "unlit": {
    "phonetic": "'ʌn'lit",
    "meaning": "a. 未点燃的, 无灯光的"
  },
  "unmet": {
    "phonetic": "ʌn'met",
    "meaning": "a. 未满足的,未相遇的,未应付的"
  },
  "unpin": {
    "phonetic": ".ʌn'pin",
    "meaning": "vt. 取下...上的别针, 拔掉闩"
  },
  "unsay": {
    "phonetic": ".ʌn'sei",
    "meaning": "vt. 取消, 撤回"
  },
  "unset": {
    "phonetic": "'ʌn'set",
    "meaning": "a. 未装配的, 未安装的, 未坚固的, (太阳)未落的；vt. 使松动, 使移动, 扰乱；[计] 复位, 置\"0\", 清除, 复原"
  },
  "untag": {
    "phonetic": "",
    "meaning": "abbr. United Nations Transition Assistance Group 联合国过渡协助组"
  },
  "untie": {
    "phonetic": ".ʌn'tai",
    "meaning": "vt. 解开；vi. 松开"
  },
  "until": {
    "phonetic": "әn'til",
    "meaning": "prep. 直到, 在...以前；conj. 直到...时, 在...以前"
  },
  "unwed": {
    "phonetic": ",ʌn'wed",
    "meaning": "a. 没有结婚的；未婚的"
  },
  "unzip": {
    "phonetic": ".ʌn'zip",
    "meaning": "vi. 拉开拉链；vt. 拉开"
  },
  "upend": {
    "phonetic": "ʌp'end",
    "meaning": "v. 颠倒, 倒放"
  },
  "upped": {
    "phonetic": "ʌpt",
    "meaning": "v. 站起身, 提高（价格等）( up的过去式和过去分词 ); 突然移动, 突然（做意想不到的事）"
  },
  "upper": {
    "phonetic": "'ʌpә",
    "meaning": "a. 上面的, 较高的, 上级的, 上院的, 穿在外面的, 北部的, 地表的, 后期的；n. 鞋帮, 上齿"
  },
  "upset": {
    "phonetic": "ʌp'set",
    "meaning": "a. 弄翻的, 混乱的, 心烦的；vt. 弄翻, 颠覆, 推翻, 打乱, 使不适, 使心烦；vi. 翻倒"
  },
  "urban": {
    "phonetic": "'ә:bәn",
    "meaning": "a. 都市的, 住在都市的, 习惯于都市的；[法] 城市的, 都市的, 市区的"
  },
  "urged": {
    "phonetic": "",
    "meaning": "vbl. 怂恿；催促"
  },
  "urine": {
    "phonetic": "'juәrin",
    "meaning": "n. 小便, 尿；[医] 尿"
  },
  "usage": {
    "phonetic": "'ju:sidʒ",
    "meaning": "n. 用法, 使用, 习惯, 惯用法, 习惯法；[经] 使用情况, 使用用途, 惯例"
  },
  "usher": {
    "phonetic": "'ʌʃә",
    "meaning": "n. 引座员, 招待员；vt. 引导, 招待；vi. 作招待员"
  },
  "using": {
    "phonetic": "",
    "meaning": "[计] 使用"
  },
  "usual": {
    "phonetic": "'ju:ʒuәl",
    "meaning": "a. 平常的, 通常的"
  },
  "usurp": {
    "phonetic": "ju:'zә:p",
    "meaning": "vt. 篡夺, 侵占, 夺取；vi. 篡夺, 侵占"
  },
  "usury": {
    "phonetic": "'ju:ʒuri",
    "meaning": "n. 高利贷；[经] 高利贷, 高利"
  },
  "utile": {
    "phonetic": "'ju:tail",
    "meaning": "a. 有用的；有益的"
  },
  "utter": {
    "phonetic": "'ʌtә",
    "meaning": "a. 全然的, 绝对的, 完全的；vt. 发出声音, 做声, 发表, 发射, 流通"
  },
  "uvula": {
    "phonetic": "'ju:vjulә",
    "meaning": "n. 悬雍垂, 小舌；[医] 悬雍垂"
  },
  "vague": {
    "phonetic": "veig",
    "meaning": "a. 含糊的, 不清楚的, 茫然的"
  },
  "valet": {
    "phonetic": "'vælit",
    "meaning": "n. 贴身男仆；vt. 伺候"
  },
  "valid": {
    "phonetic": "'vælid",
    "meaning": "a. 有确实根据的, 有法律效力的, 正当的, 正确的；[经] 有效的"
  },
  "valor": {
    "phonetic": "'vælә",
    "meaning": "n. 英勇, 刚勇, 勇猛"
  },
  "value": {
    "phonetic": "'vælju:",
    "meaning": "n. 价值, 价格, 购买力, 评价, 估价, 计算结果；vt. 评价, 估价, 重视；[计] 计算结果"
  },
  "valve": {
    "phonetic": "vælv",
    "meaning": "n. 活瓣, 阀, 活门；v. 装阀, 用阀调节"
  },
  "vampy": {
    "phonetic": "",
    "meaning": "吸血鬼风格的"
  },
  "vapid": {
    "phonetic": "'væpid",
    "meaning": "a. 乏味的, 走了气味的, 无生气的, 无趣味的"
  },
  "vapor": {
    "phonetic": "'veipә",
    "meaning": "n. 汽, 蒸气；vi. 蒸发；vt. 使蒸发"
  },
  "vault": {
    "phonetic": "vɒ:lt",
    "meaning": "n. 拱顶, 窖, 地下室, 撑竿跳, 穹窿；vt. 做成圆拱形, 撑竿跳过；vi. 成穹状弯曲, 跳跃"
  },
  "vaunt": {
    "phonetic": "vɒ:nt",
    "meaning": "v. 自夸；n. 自吹自擂"
  },
  "vegan": {
    "phonetic": "'vegәn",
    "meaning": "n. 严格的素食主义者；[医] 绝对素食者"
  },
  "veiny": {
    "phonetic": "'veini",
    "meaning": "a. 多静脉的, 有静脉的, 多脉纹的"
  },
  "veldt": {
    "phonetic": "velt",
    "meaning": "n. (南非洲的)草原"
  },
  "venal": {
    "phonetic": "'vi:nl",
    "meaning": "a. 可收买的, 贪污的, 用金钱买得的；[经] 贪污的"
  },
  "venom": {
    "phonetic": "'venәm",
    "meaning": "n. 毒液, 恶意；vt. 放毒, 使有毒"
  },
  "venue": {
    "phonetic": "'venju:",
    "meaning": "n. 犯罪地点, 审判地, 发生地点"
  },
  "verge": {
    "phonetic": "vә:dʒ",
    "meaning": "n. 边缘, 边界, 起始点；vi. 处在边缘, 接近, 下沉, 趋向"
  },
  "verse": {
    "phonetic": "vә:s",
    "meaning": "n. 诗, 韵文, 诗句；vt. 用诗表达；vi. 作诗"
  },
  "verso": {
    "phonetic": "'vә:sәu",
    "meaning": "n. 偶数页, 背面, 反面"
  },
  "verve": {
    "phonetic": "vә:v",
    "meaning": "n. 热情, 气魄, 神韵, 活力"
  },
  "vexed": {
    "phonetic": "vekst",
    "meaning": "a. 烦恼的, 焦急的, 生气的, 为难的, 恼怒的, 争论不休的"
  },
  "vicar": {
    "phonetic": "'vikә",
    "meaning": "n. 教区牧师, 教堂主持, 代理人；[法] 代表, 代理牧师, 代理主教"
  },
  "video": {
    "phonetic": "'vidiәu",
    "meaning": "n. 影像, 电视；a. 图像的, 电视的"
  },
  "vigil": {
    "phonetic": "'vidʒil",
    "meaning": "n. 警戒, 监视, 守夜；[医] 不眠, 警醒"
  },
  "vigor": {
    "phonetic": "'vigә",
    "meaning": "n. 精力, 活力"
  },
  "villa": {
    "phonetic": "'vilә",
    "meaning": "n. 别墅"
  },
  "vined": {
    "phonetic": "",
    "meaning": "vi. 形成藤蔓（vine的过去式与过去分词形式）"
  },
  "vinyl": {
    "phonetic": "'vainil",
    "meaning": "n. 乙烯基；[化] 乙烯基"
  },
  "viola": {
    "phonetic": "'vaiәlә",
    "meaning": "n. 中提琴"
  },
  "viper": {
    "phonetic": "'vaipә",
    "meaning": "n. 蝰蛇, 毒蛇, 毒如蛇蝎的人, 阴险的人；[医] 蝰蛇"
  },
  "viral": {
    "phonetic": "'vairәl",
    "meaning": "a. 病毒的, 病毒引起的；[医] 病毒的"
  },
  "virus": {
    "phonetic": "'vaiәrәs",
    "meaning": "n. 病毒, 滤过性病毒, 毒害；[化] 病毒"
  },
  "visit": {
    "phonetic": "'vizit",
    "meaning": "n. 拜访, 访问, 游览, 视察；vt. 拜访, 访问, 参观, 视察, 降临；vi. 访问, 参观, 闲谈"
  },
  "visor": {
    "phonetic": "'vaizә",
    "meaning": "n. 面甲, 帽舌, 面罩"
  },
  "vista": {
    "phonetic": "'vistә",
    "meaning": "n. 远景, 展望, 回想"
  },
  "vital": {
    "phonetic": "'vaitl",
    "meaning": "a. 生命的, 重要的, 充满活力的, 生死攸关的, 致命的；[医] 生命的, 生活的, 生活上必需的, 紧要的"
  },
  "vitro": {
    "phonetic": "",
    "meaning": "n. 在试管内"
  },
  "vivid": {
    "phonetic": "'vivid",
    "meaning": "a. 生动的, 鲜明的, 鲜艳的, 活泼的, 逼真的, 清晰的"
  },
  "vixen": {
    "phonetic": "'viksn",
    "meaning": "n. 雌狐, 悍妇, 泼妇；[法] 恶妇, 刁妇, 泼妇"
  },
  "vocal": {
    "phonetic": "'vәukl",
    "meaning": "a. 嗓音的, 声音的, 有声的, 歌唱的；n. 元音, 声乐作品"
  },
  "vodka": {
    "phonetic": "'vɒdkә",
    "meaning": "n. 伏特加酒；[化] 伏特加酒"
  },
  "vogue": {
    "phonetic": "vәug",
    "meaning": "n. 时尚, 时髦, 流行；a. 流行的, 时髦的"
  },
  "voice": {
    "phonetic": "vɒis",
    "meaning": "n. 声音, 嗓音, 嗓子, 愿望, 发言权, 表达, 喉舌, 语态；vt. 表达, 吐露, 调音"
  },
  "voila": {
    "phonetic": "",
    "meaning": "int. （法）瞧；可不是"
  },
  "vomit": {
    "phonetic": "'vɒmit",
    "meaning": "vt. 吐出, 呕吐；vi. 呕吐；n. 呕吐, 呕吐物, 催吐剂"
  },
  "voted": {
    "phonetic": "",
    "meaning": "表决的"
  },
  "voter": {
    "phonetic": "'vәutә",
    "meaning": "n. 选民, 投票人；[法] 选民, 选举人, 投票人"
  },
  "vouch": {
    "phonetic": "vautʃ",
    "meaning": "vi. 担保, 保证, 证明, 确定地说；vt. 担保, 证明, 断定, 传唤...出庭作证"
  },
  "vowed": {
    "phonetic": "",
    "meaning": "vt.& vi. 起誓, 发誓（vow的过去式与过去分词形式）"
  },
  "vowel": {
    "phonetic": "'vauәl",
    "meaning": "n. 元音；a. 元音的"
  },
  "vroom": {
    "phonetic": "vru:m, vrjm, vә'ru:m, -'rjm",
    "meaning": "n. , v.= varoom [拟声]"
  },
  "vying": {
    "phonetic": "'vaiiŋ",
    "meaning": "a. 竞争的；vie的现在分词"
  },
  "wacko": {
    "phonetic": "'wækәj",
    "meaning": "a. 古怪的, 发疯的"
  },
  "wacky": {
    "phonetic": "'wæki",
    "meaning": "a. 古怪的"
  },
  "waded": {
    "phonetic": "weidid",
    "meaning": "v. （从水、泥等）蹚, 走过, 跋( wade的过去式和过去分词 )"
  },
  "wader": {
    "phonetic": "'weidә",
    "meaning": "n. 涉水者, 涉禽, 高统防水长靴"
  },
  "wafer": {
    "phonetic": "'weifә",
    "meaning": "n. 薄酥饼, 圣饼, 晶片, 圆片, 干胶片；vt. 用干胶片封；[计] 圆片"
  },
  "waged": {
    "phonetic": "",
    "meaning": "a. 有职业的；有工作的；支付工资的"
  },
  "wager": {
    "phonetic": "'weidʒә",
    "meaning": "n. 赌注, 赌博, 赌物；vt. 下赌注, 向...保证；vi. 打赌"
  },
  "wagon": {
    "phonetic": "'wægәn",
    "meaning": "n. 四轮马车, 货车；[法] 囚车, 马车, 运货车"
  },
  "waist": {
    "phonetic": "weist",
    "meaning": "n. 腰部, 腰；[医] 腰"
  },
  "waive": {
    "phonetic": "weiv",
    "meaning": "vt. 不坚持要求, 放弃, 推迟考虑, 丢弃；[经] 放弃权利, 免除, 弃权人"
  },
  "waked": {
    "phonetic": "",
    "meaning": "wake的过去式和过去分词"
  },
  "waken": {
    "phonetic": "'weikn",
    "meaning": "vt. 唤醒, 使觉醒, 激发；vi. 觉醒, 醒来"
  },
  "waltz": {
    "phonetic": "wɒ:lts",
    "meaning": "n. 华尔兹舞, 圆舞曲；a. 华尔兹舞的, 圆舞曲的；vi. 跳华尔兹舞, 轻快地走动；vt. 与...跳华尔兹舞, 硬拖"
  },
  "waned": {
    "phonetic": "weɪnd",
    "meaning": "v. 衰落( wane的过去式和过去分词 ); （月）亏; 变小; 变暗淡"
  },
  "wanly": {
    "phonetic": "",
    "meaning": "adv. 苍白地；衰弱地；暗淡地"
  },
  "warty": {
    "phonetic": "'wɒ:ti",
    "meaning": "a. 有疣的, 多疣的, 似疣的；[医] 有疣的, 疣状的"
  },
  "waste": {
    "phonetic": "weist",
    "meaning": "n. 浪费, 废物, 损耗, 消耗, 荒地, 垃圾, 地面风化物；a. 废弃的, 荒芜的, 多余的；vt. 浪费, 消耗, 使荒芜；vi. 浪费, 消耗, 变消瘦"
  },
  "watch": {
    "phonetic": "wɒtʃ",
    "meaning": "n. 观察, 手表, 看守, 守护, 监视, 值班人；vt. 看, 注视, 照顾, 看守, 守护, 监视；vi. 观看, 注视, 守侯"
  },
  "water": {
    "phonetic": "'wɒ:tә",
    "meaning": "n. 水, 雨水, 海水, 水位, 水面, 流水；vt. 给...浇水, 供以水, 注入水, 使湿；vi. 流泪, 流口水, 加水；a. 水的, 水上的, 水生的, 含水的"
  },
  "waved": {
    "phonetic": "",
    "meaning": "a. 波浪形的, 起伏的"
  },
  "waver": {
    "phonetic": "'weivә",
    "meaning": "n. 动摇, 踌躇, 挥动者；vi. 摇摆, 颤抖, 摆动, 摇曳, 犹豫"
  },
  "waxed": {
    "phonetic": "'wæksid",
    "meaning": "a. 上过蜡的；防水的"
  },
  "waxen": {
    "phonetic": "'wæksn",
    "meaning": "a. 蜡的, 象蜡一样软的, 无生气的, 苍白的"
  },
  "weary": {
    "phonetic": "'wiәri",
    "meaning": "a. 疲倦的, 萎靡的, 厌倦的, 厌烦的；vt. 使疲倦, 使厌烦；vi. 疲乏, 生厌, 不耐烦"
  },
  "weave": {
    "phonetic": "wi:v",
    "meaning": "n. 编法, 织法, 编织式样；vt. 编织, 组合, 编排, 使迂回前进；vi. 纺织, 迂回行进"
  },
  "wedge": {
    "phonetic": "wedʒ",
    "meaning": "n. 楔子, 楔形物, 起因, 导致分裂的东西；vt. 楔住, 挤进, 楔入；vi. 楔入, 挤进"
  },
  "weedy": {
    "phonetic": "'wi:di",
    "meaning": "a. 尽是杂草的, 似杂草的, 瘦弱的, 蔓生的"
  },
  "weepy": {
    "phonetic": "'wi:pi",
    "meaning": "a. 要哭的, 眼泪汪汪的；n. 伤感的电影(或小说、戏剧等)"
  },
  "weigh": {
    "phonetic": "wei",
    "meaning": "vt. 称...重量, 衡量, 把...压弯, 考虑, 权衡, 起锚；vi. 称分量, 有意义, 重压, 起锚；n. 过秤, 称分量"
  },
  "weird": {
    "phonetic": "wiәd",
    "meaning": "a. 怪异的, 超自然的, 不可思议的；n. 命运, 预言, 符咒"
  },
  "whack": {
    "phonetic": "hwæk",
    "meaning": "vt. 猛击, 重打, 削减；vi. 重击；n. 重击, 重打"
  },
  "whale": {
    "phonetic": "hweil",
    "meaning": "n. 鲸；vi. 捕鲸；vt. 使惨败, 猛揍"
  },
  "wharf": {
    "phonetic": "hwɒ:f",
    "meaning": "n. 码头；vt. 卸在码头上, 靠码头；vi. 靠码头, 入坞"
  },
  "wheat": {
    "phonetic": "hwi:t",
    "meaning": "n. 小麦"
  },
  "wheel": {
    "phonetic": "hwi:l",
    "meaning": "n. 轮子, 车轮, 轮, 方向盘, 旋转, 机构, 重要人物；vt. 使旋转, 转动, 使转向；vi. 旋转, 转弯, 盘旋"
  },
  "whelp": {
    "phonetic": "hwelp",
    "meaning": "n. 小狗；v. 下崽"
  },
  "where": {
    "phonetic": "hwєә",
    "meaning": "adv. 在哪里；pron. 哪里；n. 地点"
  },
  "which": {
    "phonetic": "hwitʃ",
    "meaning": "pron. 哪一个, 那一个"
  },
  "whiff": {
    "phonetic": "hwif",
    "meaning": "n. 一吹, 一吸, 一阵, 一点点, 一口烟；vi. 轻轻地吹, 喷气, 三击不中出局, 垂钓；vt. 吹送, 喷出, 吸, 使三击不中出局"
  },
  "while": {
    "phonetic": "hwail",
    "meaning": "n. 一会儿, (一段)时间；conj. 当...的时候, 虽然；vt. 消磨"
  },
  "whine": {
    "phonetic": "hwain",
    "meaning": "n. 哀叫声, 嘎嘎声, 哀鸣；vi. 哭诉, 嘎嘎响, 发呜呜声；vt. 哀诉"
  },
  "whiny": {
    "phonetic": "'waini, 'hwaini",
    "meaning": "a. 好发牢骚的, 嘀咕不停的,烦躁的"
  },
  "whirl": {
    "phonetic": "hwә:l",
    "meaning": "n. 回旋, 旋转, 急走, 眩晕；vt. 使旋转, 使回旋, 卷走；vi. 回旋, 旋转, 急走, 发晕"
  },
  "whisk": {
    "phonetic": "hwisk",
    "meaning": "n. 掸, 扫帚, 毛掸子, 搅拌器, 拂；vt. 扫, 拂, 挥动, 迅速移动, 搅拌；vi. 飞奔"
  },
  "white": {
    "phonetic": "hwait",
    "meaning": "n. 白色, 洁白, 眼白, 白种人, 蛋白；a. 白色的, 纯洁的, 白种的, 苍白的, 空白的, 幸运的"
  },
  "whizz": {
    "phonetic": "hwiz",
    "meaning": "n. 飕飕声, 精明的人, 专家；v. (使)飕飕作声"
  },
  "whole": {
    "phonetic": "hәul",
    "meaning": "n. 全部, 全体, 整体, 完全之体系；a. 所有的, 完整的, 完全的, 纯粹的"
  },
  "whomp": {
    "phonetic": "hwɒmp",
    "meaning": "n. 撞击声；vi. 发撞击声；vt. 重击"
  },
  "whoop": {
    "phonetic": "hwu:p",
    "meaning": "n. 大叫, 呐喊, 一点点；vi. 叫喊, 鸣叫；vt. 高声说, 唤起"
  },
  "whorl": {
    "phonetic": "hwә:l",
    "meaning": "n. 轮生体, 螺层, 螺旋状物, 涡；vt. 使成涡漩"
  },
  "whose": {
    "phonetic": "hu:z",
    "meaning": "pron. 谁的"
  },
  "widen": {
    "phonetic": "'waidn",
    "meaning": "vt. 弄宽, 加宽, 扩大；vi. 变宽, 扩大"
  },
  "wider": {
    "phonetic": "",
    "meaning": "a. 宽的；广阔的（wide的比较级形式）"
  },
  "widow": {
    "phonetic": "'widәu",
    "meaning": "n. 寡妇, 孀妇；vt. 使成寡妇"
  },
  "width": {
    "phonetic": "widθ",
    "meaning": "n. 宽度, 宽广, 广博；[医] 宽度"
  },
  "wield": {
    "phonetic": "wi:ld",
    "meaning": "vt. 挥舞, 运用"
  },
  "wight": {
    "phonetic": "wait",
    "meaning": "n. 人类,人"
  },
  "wiled": {
    "phonetic": "",
    "meaning": "(wile 的过去时) n. 诡计, 狡猾；vt. 引诱, 诱骗, 消遣"
  },
  "willy": {
    "phonetic": "'wili",
    "meaning": "n. 阴茎；阳物；柳树（等于willow）"
  },
  "wimpy": {
    "phonetic": "'wimpi",
    "meaning": "a. <俚> = wimpish"
  },
  "wince": {
    "phonetic": "wins",
    "meaning": "n. 畏缩, 退避；vi. 畏缩, 退缩, 退避"
  },
  "winch": {
    "phonetic": "wintʃ",
    "meaning": "n. 曲柄, 绞车；vt. 用绞盘拉"
  },
  "windy": {
    "phonetic": "'windi",
    "meaning": "a. 多风的, 风强的, 腹胀的, 吹牛的"
  },
  "wined": {
    "phonetic": "",
    "meaning": "vt. 请…喝酒（wine的过去式与过去分词形式）"
  },
  "wiped": {
    "phonetic": "waipt",
    "meaning": "v. 擦( wipe的过去式和过去分词 ); 拭; 擦去; 拭去"
  },
  "wiper": {
    "phonetic": "'waipә",
    "meaning": "n. 揩擦的人, 刮水器, 接触电刷；[电] 接帚"
  },
  "wired": {
    "phonetic": "'waiәd",
    "meaning": "a. 以金属丝加强的, 接有电线的, 以铁丝围起的"
  },
  "wiser": {
    "phonetic": "",
    "meaning": "a. 贤明的；聪明的"
  },
  "wispy": {
    "phonetic": "'wispi",
    "meaning": "a. 小束状的, 细微的, 飘渺的"
  },
  "witch": {
    "phonetic": "witʃ",
    "meaning": "n. 巫婆, 女巫；vt. 施巫术, 迷惑"
  },
  "witty": {
    "phonetic": "'witi",
    "meaning": "a. 富于机智的, 诙谐的"
  },
  "woken": {
    "phonetic": "'wәukәn",
    "meaning": "wake的过去分词"
  },
  "woman": {
    "phonetic": "'wumәn",
    "meaning": "n. 女人, 妇女, 女仆；a. 女用的, 女性的, 妇女的；vt. 贬称...为女人, 使成女人腔"
  },
  "women": {
    "phonetic": "'wimin",
    "meaning": "pl. 女人"
  },
  "wonky": {
    "phonetic": "'wɒŋki",
    "meaning": "a. 不稳的, 摇晃的, 靠不住的"
  },
  "woody": {
    "phonetic": "'wudi",
    "meaning": "a. 多树木的, 木质的"
  },
  "wooed": {
    "phonetic": "wu:d",
    "meaning": "v. （向女子）求爱, 求婚( woo的过去式和过去分词 ); （尤用于报纸）争取得到…的支持"
  },
  "wooer": {
    "phonetic": "'wu:ә",
    "meaning": "n. 求婚者, 求爱者"
  },
  "wooly": {
    "phonetic": "'wuli",
    "meaning": "a. 长满羊毛的, 羊毛状的, 羊毛的, 毛茸茸的, 长满鬈发的, 模糊的；n. 毛线衣, 羊毛内衣"
  },
  "woozy": {
    "phonetic": "'wu:zi",
    "meaning": "a. 头昏眼花的, 虚弱的"
  },
  "wordy": {
    "phonetic": "'wә:di",
    "meaning": "a. 罗唆的, 口头的, 多言的"
  },
  "world": {
    "phonetic": "wә:ld",
    "meaning": "n. 世界, 地球, 宇宙, 万物, 世人, 人间, 领域, 世事, 世故, 社会生活, 大量；[法] 世界, 地球, 世人"
  },
  "wormy": {
    "phonetic": "'wә:mi",
    "meaning": "a. 有蛀虫的, 虫多的, 虫蛀的"
  },
  "worry": {
    "phonetic": "'wʌri",
    "meaning": "n. 担心, 烦恼, 忧虑, 苦恼, 撕咬；vt. 使烦恼, 使焦虑, 使苦恼, 困扰, 折磨, 撕咬；vi. 烦恼, 担心, 撕咬"
  },
  "worse": {
    "phonetic": "wә:s",
    "meaning": "n. 更坏的事, 更恶劣的事, 败局；a. 更坏的, 更恶劣的；adv. 更坏地, 更恶劣地"
  },
  "worst": {
    "phonetic": "wә:st",
    "meaning": "n. 最坏, 最坏的时候；a. 最坏的, 最恶劣的, 最不利的；adv. 最坏, 最糟"
  },
  "worth": {
    "phonetic": "wә:θ",
    "meaning": "n. 价值, 财产；a. 值...的, 值得的"
  },
  "would": {
    "phonetic": "wud",
    "meaning": "aux. 将, 愿意"
  },
  "wound": {
    "phonetic": "wu:nd",
    "meaning": "n. 创伤, 伤口, 伤疤, 伤害, 痛苦；vt. 伤害, 损害, 使受伤；vi. 打伤, 伤害；wind的过去式和过去分词"
  },
  "woven": {
    "phonetic": "'wәuvәn",
    "meaning": "weave的过去分词"
  },
  "wowed": {
    "phonetic": "waʊd",
    "meaning": "v. <俚>使惊叹, 使佩服( wow的过去式和过去分词 )"
  },
  "wrack": {
    "phonetic": "ræk",
    "meaning": "n. 漂积海草, 失事船只, 破坏；vt. 严重伤害"
  },
  "wrath": {
    "phonetic": "rɒ:θ",
    "meaning": "n. 愤怒, 激怒, 愤怒的举动, (自然现象等)严酷"
  },
  "wreak": {
    "phonetic": "ri:k",
    "meaning": "vt. 发泄(怒火), 报仇；[法] 报仇, 报复, 施"
  },
  "wreck": {
    "phonetic": "rek",
    "meaning": "n. 失事, 残骸, 破坏；vt. 使失事, 拆毁, 破坏；vi. (船)失事, 营救失事船只"
  },
  "wrest": {
    "phonetic": "rest",
    "meaning": "n. 扭, 拧；vt. 夺取, 猛扭, 歪曲, 费力取得"
  },
  "wring": {
    "phonetic": "riŋ",
    "meaning": "n. 扭绞, 拧, 挤；vt. 拧, 绞, 扭, 勒索, 折磨, 使痛苦；vi. 蠕动, 扭动, 绞, 扭, 感到痛苦"
  },
  "wrist": {
    "phonetic": "rist",
    "meaning": "n. 手腕, 腕关节；[医] 腕"
  },
  "write": {
    "phonetic": "rait",
    "meaning": "vt. 书写, 著述, 写, 写满, 写信给；vi. 写, 写字, 写信, 写作, 作曲；[计] 书写器"
  },
  "wrong": {
    "phonetic": "rɒŋ",
    "meaning": "a. 错误的, 不正当的, 失常的；adv. 错误地"
  },
  "wrote": {
    "phonetic": "rәut",
    "meaning": "write的过去式"
  },
  "wrung": {
    "phonetic": "r ʌŋ",
    "meaning": "wring的过去式和过去分词"
  },
  "wryly": {
    "phonetic": "raɪlɪ",
    "meaning": "adv. （面部表情）做鬼脸地, 苦笑地, 嘲讽地"
  },
  "wurst": {
    "phonetic": "wә:st",
    "meaning": "n. 香肠"
  },
  "xenon": {
    "phonetic": "'zenɒn",
    "meaning": "n. 氙；[化] 氙Xe"
  },
  "xerox": {
    "phonetic": "'ziәrɒks",
    "meaning": "v. 静电复印"
  },
  "yacht": {
    "phonetic": "jɒt",
    "meaning": "n. 快艇, 游艇；vi. 驾游艇, 乘游艇"
  },
  "yahoo": {
    "phonetic": "jә'hu:",
    "meaning": "n. 人面兽心的人, 乡愚, 粗汉"
  },
  "yappy": {
    "phonetic": "'jæpi",
    "meaning": "a. 喜欢叫嚷的,粗汉的"
  },
  "yearn": {
    "phonetic": "jә:n",
    "meaning": "vi. 渴望, 想念, 怀念, 同情"
  },
  "yeast": {
    "phonetic": "ji:st",
    "meaning": "n. 酵母；[化] 酵母"
  },
  "yield": {
    "phonetic": "ji:ld",
    "meaning": "n. 生产量, 投资收益；vt. 出产, 给予, 让出, 放弃, 使屈服；vi. 出产, 屈服, 投降, 倒塌"
  },
  "yodel": {
    "phonetic": "'jәudl",
    "meaning": "n. 真假嗓音反复变换的唱腔；v. 用真假嗓音反复变换地唱"
  },
  "yoked": {
    "phonetic": "'jəʊkt",
    "meaning": "vt. 结合（yoke的过去式形式）"
  },
  "yokel": {
    "phonetic": "'jәukәl",
    "meaning": "n. (贬)乡巴佬, 土包子, 乡下佬"
  },
  "young": {
    "phonetic": "jʌŋ",
    "meaning": "a. 年轻的, 无经验的, 朝气蓬勃的；n. 青年们, 幼小动物, 崽"
  },
  "youth": {
    "phonetic": "ju:θ",
    "meaning": "n. 年轻, 青年时代, 青年们, 青春；[法] 青年, 青年时期, 青春时期"
  },
  "yucca": {
    "phonetic": "'jʌkә",
    "meaning": "n. 丝兰；[医] 丝兰属"
  },
  "yucky": {
    "phonetic": "ˈjʌki",
    "meaning": "a. 令人讨厌的, 难以下咽的"
  },
  "yummy": {
    "phonetic": "'jʌmi",
    "meaning": "a. 美味的, 可口的, 赏心悦目的, 愉快的"
  },
  "zebra": {
    "phonetic": "'zi:brә",
    "meaning": "n. 斑马"
  },
  "zesty": {
    "phonetic": "'zesti",
    "meaning": "a. 强烈的兴趣, 热心, 热忱, 热情, 滋味, 风趣, 香味, 风味；vt. 给...加香味, 给...调味, 给...添风趣, 给...增兴趣"
  },
  "zilch": {
    "phonetic": "ziltʃ",
    "meaning": "n. 一无所有, 小人物, 无, 零"
  },
  "zippy": {
    "phonetic": "'zipi",
    "meaning": "a. 元气旺盛的, 敏捷的, 活泼的"
  },
  "zonal": {
    "phonetic": "'zәunl",
    "meaning": "a. 带的, 带状的, 形成地带的, 分区的；[医] 带的, 区的"
  },
  "zoned": {
    "phonetic": "zәund",
    "meaning": "a. 佩带象征处女的环带的, 划成区带的, 处女(般)的"
  },
  "zowie": {
    "phonetic": "'zaui",
    "meaning": "int. <美>好! 呦(表示激动,热情,赞叹等的感叹词)"
  }
}
