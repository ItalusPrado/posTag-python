from enum import Enum

class Label2(Enum):
    PCP = 'PCP',
    PDEN = 'PDEN',
    CUR = 'CUR',
    PREP = 'PREP',
    PREP__PROSUB = 'PREP+PROSUB',
    KS = 'KS',
    ADV_KS = 'ADV-KS',
    PREP__ADV = 'PREP+ADV',
    PRO_KS = 'PRO-KS',
    NUM = 'NUM',
    PROSUB = 'PROSUB',
    ADV = 'ADV',
    PROADJ = 'PROADJ',
    NPROP = 'NPROP',
    PU = 'PU',
    PROPESS = 'PROPESS',
    PREP__ART = 'PREP+ART',
    ADJ = 'ADJ',
    V = 'V',
    N = 'N',
    ART = 'ART',
    PREP__PROPESS = 'PREP+PROPESS',
    IN = 'IN',
    PREP__PRO_KS = 'PREP+PRO-KS',
    PREP__PROADJ = 'PREP+PROADJ',
    KC ='KC'

class Label(Enum):
    EMPTY = 'EMPTY',
    PCP = 'PCP',
    CUR = 'CUR',
    NONE = 'NONE'
    PREP = 'PREP',
    # PREP__PROSUB = 'PREP+PROSUB',
    # PREP__ADV = 'PREP+ADV',
    # PREP__ART = 'PREP+ART',
    # PREP__PRO_KS = 'PREP+PRO-KS',
    # PREP__PROADJ = 'PREP+PROADJ',
    # PREP__PROPESS = 'PREP+PROPESS',

    NUM = 'NUM',
    ADV = 'ADV',

    PRO = 'PRO',
    # PDEN = 'PDEN',
    # PROSUB = 'PROSUB',
    # PROADJ = 'PROADJ',
    # PRO_KS = 'PRO-KS',
    # PROPESS = 'PROPESS',

    PU = 'PU',
    # ADV_KS = 'ADV-KS',

    ADJ = 'ADJ',
    V = 'V',

    N = 'N',
    # NPROP = 'NPROP',

    ART = 'ART',
    IN = 'IN',

    K = 'K'
    # KC ='KC',
    # KS = 'KS',


