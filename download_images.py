import os
import time
import requests

urls = {
    "Menu_ZA_0001": "https://archives.bulbagarden.net/media/upload/7/7f/Menu_ZA_0001.png",
    "Menu_ZA_0002": "https://archives.bulbagarden.net/media/upload/d/d0/Menu_ZA_0002.png",
    "Menu_ZA_0003": "https://archives.bulbagarden.net/media/upload/5/5f/Menu_ZA_0003.png",
    "Menu_ZA_0004": "https://archives.bulbagarden.net/media/upload/8/8f/Menu_ZA_0004.png",
    "Menu_ZA_0005": "https://archives.bulbagarden.net/media/upload/7/74/Menu_ZA_0005.png",
    "Menu_ZA_0006": "https://archives.bulbagarden.net/media/upload/2/27/Menu_ZA_0006.png",
    "Menu_ZA_0007": "https://archives.bulbagarden.net/media/upload/d/d1/Menu_ZA_0007.png",
    "Menu_ZA_0008": "https://archives.bulbagarden.net/media/upload/8/8c/Menu_ZA_0008.png",
    "Menu_ZA_0009": "https://archives.bulbagarden.net/media/upload/6/6d/Menu_ZA_0009.png",
    "Menu_ZA_0013": "https://archives.bulbagarden.net/media/upload/a/ab/Menu_ZA_0013.png",
    "Menu_ZA_0014": "https://archives.bulbagarden.net/media/upload/9/98/Menu_ZA_0014.png",
    "Menu_ZA_0015": "https://archives.bulbagarden.net/media/upload/e/e5/Menu_ZA_0015.png",
    "Menu_ZA_0016": "https://archives.bulbagarden.net/media/upload/0/03/Menu_ZA_0016.png",
    "Menu_ZA_0017": "https://archives.bulbagarden.net/media/upload/b/b7/Menu_ZA_0017.png",
    "Menu_ZA_0018": "https://archives.bulbagarden.net/media/upload/4/49/Menu_ZA_0018.png",
    "Menu_ZA_0023": "https://archives.bulbagarden.net/media/upload/4/4e/Menu_ZA_0023.png",
    "Menu_ZA_0024": "https://archives.bulbagarden.net/media/upload/f/f6/Menu_ZA_0024.png",
    "Menu_ZA_0025": "https://archives.bulbagarden.net/media/upload/e/e9/Menu_ZA_0025.png",
    "Menu_ZA_0026": "https://archives.bulbagarden.net/media/upload/3/35/Menu_ZA_0026.png",
    "Menu_ZA_0035": "https://archives.bulbagarden.net/media/upload/3/3a/Menu_ZA_0035.png",
    "Menu_ZA_0036": "https://archives.bulbagarden.net/media/upload/6/61/Menu_ZA_0036.png",
    "Menu_ZA_0063": "https://archives.bulbagarden.net/media/upload/3/38/Menu_ZA_0063.png",
    "Menu_ZA_0064": "https://archives.bulbagarden.net/media/upload/2/27/Menu_ZA_0064.png",
    "Menu_ZA_0065": "https://archives.bulbagarden.net/media/upload/6/61/Menu_ZA_0065.png",
    "Menu_ZA_0066": "https://archives.bulbagarden.net/media/upload/a/ae/Menu_ZA_0066.png",
    "Menu_ZA_0067": "https://archives.bulbagarden.net/media/upload/b/bd/Menu_ZA_0067.png",
    "Menu_ZA_0068": "https://archives.bulbagarden.net/media/upload/e/e4/Menu_ZA_0068.png",
    "Menu_ZA_0069": "https://archives.bulbagarden.net/media/upload/1/17/Menu_ZA_0069.png",
    "Menu_ZA_0070": "https://archives.bulbagarden.net/media/upload/5/5e/Menu_ZA_0070.png",
    "Menu_ZA_0071": "https://archives.bulbagarden.net/media/upload/b/b4/Menu_ZA_0071.png",
    "Menu_ZA_0079": "https://archives.bulbagarden.net/media/upload/4/4d/Menu_ZA_0079.png",
    "Menu_ZA_0080": "https://archives.bulbagarden.net/media/upload/5/55/Menu_ZA_0080.png",
    "Menu_ZA_0092": "https://archives.bulbagarden.net/media/upload/b/b5/Menu_ZA_0092.png",
    "Menu_ZA_0093": "https://archives.bulbagarden.net/media/upload/d/db/Menu_ZA_0093.png",
    "Menu_ZA_0094": "https://archives.bulbagarden.net/media/upload/d/dc/Menu_ZA_0094.png",
    "Menu_ZA_0095": "https://archives.bulbagarden.net/media/upload/e/ef/Menu_ZA_0095.png",
    "Menu_ZA_0115": "https://archives.bulbagarden.net/media/upload/e/e1/Menu_ZA_0115.png",
    "Menu_ZA_0120": "https://archives.bulbagarden.net/media/upload/2/2b/Menu_ZA_0120.png",
    "Menu_ZA_0121": "https://archives.bulbagarden.net/media/upload/2/2a/Menu_ZA_0121.png",
    "Menu_ZA_0123": "https://archives.bulbagarden.net/media/upload/4/47/Menu_ZA_0123.png",
    "Menu_ZA_0127": "https://archives.bulbagarden.net/media/upload/5/56/Menu_ZA_0127.png",
    "Menu_ZA_0129": "https://archives.bulbagarden.net/media/upload/d/d7/Menu_ZA_0129.png",
    "Menu_ZA_0130": "https://archives.bulbagarden.net/media/upload/7/7e/Menu_ZA_0130.png",
    "Menu_ZA_0133": "https://archives.bulbagarden.net/media/upload/5/51/Menu_ZA_0133.png",
    "Menu_ZA_0134": "https://archives.bulbagarden.net/media/upload/f/fe/Menu_ZA_0134.png",
    "Menu_ZA_0135": "https://archives.bulbagarden.net/media/upload/3/35/Menu_ZA_0135.png",
    "Menu_ZA_0136": "https://archives.bulbagarden.net/media/upload/a/a9/Menu_ZA_0136.png",
    "Menu_ZA_0142": "https://archives.bulbagarden.net/media/upload/6/69/Menu_ZA_0142.png",
    "Menu_ZA_0147": "https://archives.bulbagarden.net/media/upload/b/b3/Menu_ZA_0147.png",
    "Menu_ZA_0148": "https://archives.bulbagarden.net/media/upload/0/0f/Menu_ZA_0148.png",
    "Menu_ZA_0149": "https://archives.bulbagarden.net/media/upload/c/cb/Menu_ZA_0149.png",
    "Menu_ZA_0150": "https://archives.bulbagarden.net/media/upload/e/e4/Menu_ZA_0150.png",
    "Menu_ZA_0152": "https://archives.bulbagarden.net/media/upload/3/34/Menu_ZA_0152.png",
    "Menu_ZA_0153": "https://archives.bulbagarden.net/media/upload/f/fe/Menu_ZA_0153.png",
    "Menu_ZA_0154": "https://archives.bulbagarden.net/media/upload/5/55/Menu_ZA_0154.png",
    "Menu_ZA_0158": "https://archives.bulbagarden.net/media/upload/b/b4/Menu_ZA_0158.png",
    "Menu_ZA_0159": "https://archives.bulbagarden.net/media/upload/3/39/Menu_ZA_0159.png",
    "Menu_ZA_0160": "https://archives.bulbagarden.net/media/upload/8/84/Menu_ZA_0160.png",
    "Menu_ZA_0167": "https://archives.bulbagarden.net/media/upload/9/9c/Menu_ZA_0167.png",
    "Menu_ZA_0168": "https://archives.bulbagarden.net/media/upload/7/78/Menu_ZA_0168.png",
    "Menu_ZA_0172": "https://archives.bulbagarden.net/media/upload/2/22/Menu_ZA_0172.png",
    "Menu_ZA_0173": "https://archives.bulbagarden.net/media/upload/c/c8/Menu_ZA_0173.png",
    "Menu_ZA_0179": "https://archives.bulbagarden.net/media/upload/7/71/Menu_ZA_0179.png",
    "Menu_ZA_0180": "https://archives.bulbagarden.net/media/upload/e/e7/Menu_ZA_0180.png",
    "Menu_ZA_0181": "https://archives.bulbagarden.net/media/upload/b/bd/Menu_ZA_0181.png",
    "Menu_ZA_0196": "https://archives.bulbagarden.net/media/upload/8/81/Menu_ZA_0196.png",
    "Menu_ZA_0197": "https://archives.bulbagarden.net/media/upload/e/e6/Menu_ZA_0197.png",
    "Menu_ZA_0199": "https://archives.bulbagarden.net/media/upload/e/e1/Menu_ZA_0199.png",
    "Menu_ZA_0208": "https://archives.bulbagarden.net/media/upload/b/b4/Menu_ZA_0208.png",
    "Menu_ZA_0212": "https://archives.bulbagarden.net/media/upload/f/f8/Menu_ZA_0212.png",
    "Menu_ZA_0214": "https://archives.bulbagarden.net/media/upload/b/bf/Menu_ZA_0214.png",
    "Menu_ZA_0225": "https://archives.bulbagarden.net/media/upload/5/55/Menu_ZA_0225.png",
    "Menu_ZA_0227": "https://archives.bulbagarden.net/media/upload/1/15/Menu_ZA_0227.png",
    "Menu_ZA_0228": "https://archives.bulbagarden.net/media/upload/d/d4/Menu_ZA_0228.png",
    "Menu_ZA_0229": "https://archives.bulbagarden.net/media/upload/c/cf/Menu_ZA_0229.png",
    "Menu_ZA_0246": "https://archives.bulbagarden.net/media/upload/a/a9/Menu_ZA_0246.png",
    "Menu_ZA_0247": "https://archives.bulbagarden.net/media/upload/a/ae/Menu_ZA_0247.png",
    "Menu_ZA_0248": "https://archives.bulbagarden.net/media/upload/7/75/Menu_ZA_0248.png",
    "Menu_ZA_0280": "https://archives.bulbagarden.net/media/upload/8/8c/Menu_ZA_0280.png",
    "Menu_ZA_0281": "https://archives.bulbagarden.net/media/upload/8/89/Menu_ZA_0281.png",
    "Menu_ZA_0282": "https://archives.bulbagarden.net/media/upload/2/2d/Menu_ZA_0282.png",
    "Menu_ZA_0302": "https://archives.bulbagarden.net/media/upload/9/93/Menu_ZA_0302.png",
    "Menu_ZA_0303": "https://archives.bulbagarden.net/media/upload/c/c4/Menu_ZA_0303.png",
    "Menu_ZA_0304": "https://archives.bulbagarden.net/media/upload/5/55/Menu_ZA_0304.png",
    "Menu_ZA_0305": "https://archives.bulbagarden.net/media/upload/1/14/Menu_ZA_0305.png",
    "Menu_ZA_0306": "https://archives.bulbagarden.net/media/upload/0/01/Menu_ZA_0306.png",
    "Menu_ZA_0307": "https://archives.bulbagarden.net/media/upload/2/26/Menu_ZA_0307.png",
    "Menu_ZA_0308": "https://archives.bulbagarden.net/media/upload/3/3c/Menu_ZA_0308.png",
    "Menu_ZA_0309": "https://archives.bulbagarden.net/media/upload/d/dc/Menu_ZA_0309.png",
    "Menu_ZA_0310": "https://archives.bulbagarden.net/media/upload/c/c8/Menu_ZA_0310.png",
    "Menu_ZA_0315": "https://archives.bulbagarden.net/media/upload/b/b0/Menu_ZA_0315.png",
    "Menu_ZA_0318": "https://archives.bulbagarden.net/media/upload/c/c5/Menu_ZA_0318.png",
    "Menu_ZA_0319": "https://archives.bulbagarden.net/media/upload/2/26/Menu_ZA_0319.png",
    "Menu_ZA_0322": "https://archives.bulbagarden.net/media/upload/6/63/Menu_ZA_0322.png",
    "Menu_ZA_0323": "https://archives.bulbagarden.net/media/upload/4/43/Menu_ZA_0323.png",
    "Menu_ZA_0333": "https://archives.bulbagarden.net/media/upload/5/5b/Menu_ZA_0333.png",
    "Menu_ZA_0334": "https://archives.bulbagarden.net/media/upload/9/98/Menu_ZA_0334.png",
    "Menu_ZA_0353": "https://archives.bulbagarden.net/media/upload/4/41/Menu_ZA_0353.png",
    "Menu_ZA_0354": "https://archives.bulbagarden.net/media/upload/a/a5/Menu_ZA_0354.png",
    "Menu_ZA_0359": "https://archives.bulbagarden.net/media/upload/a/ab/Menu_ZA_0359.png",
    "Menu_ZA_0361": "https://archives.bulbagarden.net/media/upload/d/dd/Menu_ZA_0361.png",
    "Menu_ZA_0362": "https://archives.bulbagarden.net/media/upload/a/a4/Menu_ZA_0362.png",
    "Menu_ZA_0371": "https://archives.bulbagarden.net/media/upload/7/75/Menu_ZA_0371.png",
    "Menu_ZA_0372": "https://archives.bulbagarden.net/media/upload/5/54/Menu_ZA_0372.png",
    "Menu_ZA_0373": "https://archives.bulbagarden.net/media/upload/a/af/Menu_ZA_0373.png",
    "Menu_ZA_0374": "https://archives.bulbagarden.net/media/upload/d/d0/Menu_ZA_0374.png",
    "Menu_ZA_0375": "https://archives.bulbagarden.net/media/upload/8/83/Menu_ZA_0375.png",
    "Menu_ZA_0376": "https://archives.bulbagarden.net/media/upload/3/3d/Menu_ZA_0376.png",
    "Menu_ZA_0406": "https://archives.bulbagarden.net/media/upload/6/67/Menu_ZA_0406.png",
    "Menu_ZA_0407": "https://archives.bulbagarden.net/media/upload/8/8a/Menu_ZA_0407.png",
    "Menu_ZA_0427": "https://archives.bulbagarden.net/media/upload/3/36/Menu_ZA_0427.png",
    "Menu_ZA_0428": "https://archives.bulbagarden.net/media/upload/7/73/Menu_ZA_0428.png",
    "Menu_ZA_0443": "https://archives.bulbagarden.net/media/upload/b/b5/Menu_ZA_0443.png",
    "Menu_ZA_0444": "https://archives.bulbagarden.net/media/upload/0/07/Menu_ZA_0444.png",
    "Menu_ZA_0445": "https://archives.bulbagarden.net/media/upload/d/d7/Menu_ZA_0445.png",
    "Menu_ZA_0447": "https://archives.bulbagarden.net/media/upload/8/83/Menu_ZA_0447.png",
    "Menu_ZA_0448": "https://archives.bulbagarden.net/media/upload/5/56/Menu_ZA_0448.png",

    # This one is weird — it's a "thumb" format.  
    # I kept the original last part as filename key.
    "Menu_ZA_0449_thumb": "https://archives.bulbagarden.net/media/upload/thumb/b/bb/Menu_ZA_0449.png/180px-Menu_ZA_0449.png",

    "Menu_ZA_0450": "https://archives.bulbagarden.net/media/upload/1/15/Menu_ZA_0450.png",
    "Menu_ZA_0459": "https://archives.bulbagarden.net/media/upload/1/1e/Menu_ZA_0459.png",
    "Menu_ZA_0460": "https://archives.bulbagarden.net/media/upload/7/7d/Menu_ZA_0460.png",
    "Menu_ZA_0470": "https://archives.bulbagarden.net/media/upload/1/19/Menu_ZA_0470.png",
    "Menu_ZA_0471": "https://archives.bulbagarden.net/media/upload/5/50/Menu_ZA_0471.png",
    "Menu_ZA_0475": "https://archives.bulbagarden.net/media/upload/d/d0/Menu_ZA_0475.png",
    "Menu_ZA_0478": "https://archives.bulbagarden.net/media/upload/c/c6/Menu_ZA_0478.png",
    "Menu_ZA_0498": "https://archives.bulbagarden.net/media/upload/8/8a/Menu_ZA_0498.png",
    "Menu_ZA_0499": "https://archives.bulbagarden.net/media/upload/9/94/Menu_ZA_0499.png",
    "Menu_ZA_0500": "https://archives.bulbagarden.net/media/upload/9/91/Menu_ZA_0500.png",
    "Menu_ZA_0504": "https://archives.bulbagarden.net/media/upload/7/72/Menu_ZA_0504.png",
    "Menu_ZA_0505": "https://archives.bulbagarden.net/media/upload/9/9c/Menu_ZA_0505.png",
    "Menu_ZA_0511": "https://archives.bulbagarden.net/media/upload/6/63/Menu_ZA_0511.png",
    "Menu_ZA_0512": "https://archives.bulbagarden.net/media/upload/5/58/Menu_ZA_0512.png",
    "Menu_ZA_0513": "https://archives.bulbagarden.net/media/upload/5/5c/Menu_ZA_0513.png",
    "Menu_ZA_0514": "https://archives.bulbagarden.net/media/upload/e/e9/Menu_ZA_0514.png",
    "Menu_ZA_0515": "https://archives.bulbagarden.net/media/upload/9/95/Menu_ZA_0515.png",
    "Menu_ZA_0516": "https://archives.bulbagarden.net/media/upload/e/e6/Menu_ZA_0516.png",
    "Menu_ZA_0529": "https://archives.bulbagarden.net/media/upload/d/dc/Menu_ZA_0529.png",
    "Menu_ZA_0530": "https://archives.bulbagarden.net/media/upload/1/1c/Menu_ZA_0530.png",
    "Menu_ZA_0531": "https://archives.bulbagarden.net/media/upload/a/ad/Menu_ZA_0531.png",
    "Menu_ZA_0543": "https://archives.bulbagarden.net/media/upload/4/4d/Menu_ZA_0543.png",
    "Menu_ZA_0544": "https://archives.bulbagarden.net/media/upload/3/32/Menu_ZA_0544.png",
    "Menu_ZA_0545": "https://archives.bulbagarden.net/media/upload/f/f0/Menu_ZA_0545.png",
    "Menu_ZA_0551": "https://archives.bulbagarden.net/media/upload/b/b7/Menu_ZA_0551.png",
    "Menu_ZA_0552": "https://archives.bulbagarden.net/media/upload/8/82/Menu_ZA_0552.png",
    "Menu_ZA_0553": "https://archives.bulbagarden.net/media/upload/1/17/Menu_ZA_0553.png",
    "Menu_ZA_0559": "https://archives.bulbagarden.net/media/upload/6/6b/Menu_ZA_0559.png",
    "Menu_ZA_0560": "https://archives.bulbagarden.net/media/upload/9/9e/Menu_ZA_0560.png",
    "Menu_ZA_0568": "https://archives.bulbagarden.net/media/upload/9/99/Menu_ZA_0568.png",
    "Menu_ZA_0569": "https://archives.bulbagarden.net/media/upload/5/5e/Menu_ZA_0569.png",
    "Menu_ZA_0582": "https://archives.bulbagarden.net/media/upload/7/70/Menu_ZA_0582.png",
    "Menu_ZA_0583": "https://archives.bulbagarden.net/media/upload/d/d5/Menu_ZA_0583.png",
    "Menu_ZA_0584": "https://archives.bulbagarden.net/media/upload/d/de/Menu_ZA_0584.png",
    "Menu_ZA_0587": "https://archives.bulbagarden.net/media/upload/4/48/Menu_ZA_0587.png",
    "Menu_ZA_0602": "https://archives.bulbagarden.net/media/upload/d/df/Menu_ZA_0602.png",
    "Menu_ZA_0603": "https://archives.bulbagarden.net/media/upload/9/9c/Menu_ZA_0603.png",
    "Menu_ZA_0604": "https://archives.bulbagarden.net/media/upload/b/be/Menu_ZA_0604.png",
    "Menu_ZA_0607": "https://archives.bulbagarden.net/media/upload/8/85/Menu_ZA_0607.png",
    "Menu_ZA_0608": "https://archives.bulbagarden.net/media/upload/6/64/Menu_ZA_0608.png",
    "Menu_ZA_0609": "https://archives.bulbagarden.net/media/upload/f/fa/Menu_ZA_0609.png",
    "Menu_ZA_0618": "https://archives.bulbagarden.net/media/upload/4/4b/Menu_ZA_0618.png",
    "Menu_ZA_0650": "https://archives.bulbagarden.net/media/upload/a/a5/Menu_ZA_0650.png",
    "Menu_ZA_0651": "https://archives.bulbagarden.net/media/upload/7/7a/Menu_ZA_0651.png",
    "Menu_ZA_0652": "https://archives.bulbagarden.net/media/upload/e/e5/Menu_ZA_0652.png",
    "Menu_ZA_0653": "https://archives.bulbagarden.net/media/upload/f/f4/Menu_ZA_0653.png",
    "Menu_ZA_0654": "https://archives.bulbagarden.net/media/upload/2/2b/Menu_ZA_0654.png",
    "Menu_ZA_0655": "https://archives.bulbagarden.net/media/upload/8/83/Menu_ZA_0655.png",
    "Menu_ZA_0656": "https://archives.bulbagarden.net/media/upload/a/aa/Menu_ZA_0656.png",
    "Menu_ZA_0657": "https://archives.bulbagarden.net/media/upload/d/d4/Menu_ZA_0657.png",
    "Menu_ZA_0658": "https://archives.bulbagarden.net/media/upload/0/04/Menu_ZA_0658.png",
    "Menu_ZA_0659": "https://archives.bulbagarden.net/media/upload/4/4d/Menu_ZA_0659.png",
    "Menu_ZA_0660": "https://archives.bulbagarden.net/media/upload/5/5c/Menu_ZA_0660.png",
    "Menu_ZA_0661": "https://archives.bulbagarden.net/media/upload/a/a8/Menu_ZA_0661.png",
    "Menu_ZA_0662": "https://archives.bulbagarden.net/media/upload/8/85/Menu_ZA_0662.png",
    "Menu_ZA_0663": "https://archives.bulbagarden.net/media/upload/3/39/Menu_ZA_0663.png",
    "Menu_ZA_0664": "https://archives.bulbagarden.net/media/upload/d/d5/Menu_ZA_0664.png",
    "Menu_ZA_0665": "https://archives.bulbagarden.net/media/upload/2/24/Menu_ZA_0665.png",
    "Menu_ZA_0666": "https://archives.bulbagarden.net/media/upload/3/3c/Menu_ZA_0666.png",
    "Menu_ZA_0667": "https://archives.bulbagarden.net/media/upload/5/5b/Menu_ZA_0667.png",
    "Menu_ZA_0668": "https://archives.bulbagarden.net/media/upload/d/d7/Menu_ZA_0668.png",
    "Menu_ZA_0669": "https://archives.bulbagarden.net/media/upload/8/8b/Menu_ZA_0669.png",
    "Menu_ZA_0670": "https://archives.bulbagarden.net/media/upload/c/c7/Menu_ZA_0670.png",
    "Menu_ZA_0671": "https://archives.bulbagarden.net/media/upload/c/cd/Menu_ZA_0671.png",
    "Menu_ZA_0672": "https://archives.bulbagarden.net/media/upload/2/22/Menu_ZA_0672.png",
    "Menu_ZA_0673": "https://archives.bulbagarden.net/media/upload/7/7c/Menu_ZA_0673.png",
    "Menu_ZA_0674": "https://archives.bulbagarden.net/media/upload/d/df/Menu_ZA_0674.png",
    "Menu_ZA_0675": "https://archives.bulbagarden.net/media/upload/1/13/Menu_ZA_0675.png",
    "Menu_ZA_0676": "https://archives.bulbagarden.net/media/upload/0/0a/Menu_ZA_0676.png",
    "Menu_ZA_0677": "https://archives.bulbagarden.net/media/upload/1/19/Menu_ZA_0677.png",
    "Menu_ZA_0678": "https://archives.bulbagarden.net/media/upload/4/45/Menu_ZA_0678.png",
    "Menu_ZA_0679": "https://archives.bulbagarden.net/media/upload/e/ed/Menu_ZA_0679.png",
    "Menu_ZA_0680": "https://archives.bulbagarden.net/media/upload/5/54/Menu_ZA_0680.png",
    "Menu_ZA_0681": "https://archives.bulbagarden.net/media/upload/8/85/Menu_ZA_0681.png",
    "Menu_ZA_0682": "https://archives.bulbagarden.net/media/upload/2/20/Menu_ZA_0682.png",
    "Menu_ZA_0683": "https://archives.bulbagarden.net/media/upload/0/0b/Menu_ZA_0683.png",
    "Menu_ZA_0684": "https://archives.bulbagarden.net/media/upload/2/2b/Menu_ZA_0684.png",
    "Menu_ZA_0685": "https://archives.bulbagarden.net/media/upload/1/15/Menu_ZA_0685.png",
    "Menu_ZA_0686": "https://archives.bulbagarden.net/media/upload/d/d1/Menu_ZA_0686.png",
    "Menu_ZA_0687": "https://archives.bulbagarden.net/media/upload/9/94/Menu_ZA_0687.png",
    "Menu_ZA_0688": "https://archives.bulbagarden.net/media/upload/e/ec/Menu_ZA_0688.png",
    "Menu_ZA_0689": "https://archives.bulbagarden.net/media/upload/4/42/Menu_ZA_0689.png",
    "Menu_ZA_0690": "https://archives.bulbagarden.net/media/upload/5/5f/Menu_ZA_0690.png",
    "Menu_ZA_0691": "https://archives.bulbagarden.net/media/upload/f/fb/Menu_ZA_0691.png",
    "Menu_ZA_0692": "https://archives.bulbagarden.net/media/upload/a/a5/Menu_ZA_0692.png",
    "Menu_ZA_0693": "https://archives.bulbagarden.net/media/upload/c/ca/Menu_ZA_0693.png",
    "Menu_ZA_0694": "https://archives.bulbagarden.net/media/upload/2/2f/Menu_ZA_0694.png",
    "Menu_ZA_0695": "https://archives.bulbagarden.net/media/upload/4/4d/Menu_ZA_0695.png",
    "Menu_ZA_0696": "https://archives.bulbagarden.net/media/upload/a/a3/Menu_ZA_0696.png",
    "Menu_ZA_0697": "https://archives.bulbagarden.net/media/upload/c/c2/Menu_ZA_0697.png",
    "Menu_ZA_0698": "https://archives.bulbagarden.net/media/upload/d/dd/Menu_ZA_0698.png",
    "Menu_ZA_0699": "https://archives.bulbagarden.net/media/upload/e/e0/Menu_ZA_0699.png",
    "Menu_ZA_0700": "https://archives.bulbagarden.net/media/upload/2/2c/Menu_ZA_0700.png",
    "Menu_ZA_0701": "https://archives.bulbagarden.net/media/upload/f/f4/Menu_ZA_0701.png",
    "Menu_ZA_0702": "https://archives.bulbagarden.net/media/upload/e/ea/Menu_ZA_0702.png",
    "Menu_ZA_0703": "https://archives.bulbagarden.net/media/upload/f/f4/Menu_ZA_0703.png",
    "Menu_ZA_0704": "https://archives.bulbagarden.net/media/upload/3/3b/Menu_ZA_0704.png",
    "Menu_ZA_0705": "https://archives.bulbagarden.net/media/upload/e/e3/Menu_ZA_0705.png",
    "Menu_ZA_0706": "https://archives.bulbagarden.net/media/upload/3/37/Menu_ZA_0706.png",
    "Menu_ZA_0707": "https://archives.bulbagarden.net/media/upload/2/2a/Menu_ZA_0707.png",
    "Menu_ZA_0708": "https://archives.bulbagarden.net/media/upload/4/4d/Menu_ZA_0708.png",
    "Menu_ZA_0709": "https://archives.bulbagarden.net/media/upload/9/92/Menu_ZA_0709.png",
    "Menu_ZA_0710": "https://archives.bulbagarden.net/media/upload/1/1b/Menu_ZA_0710.png",
    "Menu_ZA_0711": "https://archives.bulbagarden.net/media/upload/5/5f/Menu_ZA_0711.png",
    "Menu_ZA_0712": "https://archives.bulbagarden.net/media/upload/8/89/Menu_ZA_0712.png",
    "Menu_ZA_0713": "https://archives.bulbagarden.net/media/upload/b/b8/Menu_ZA_0713.png",
    "Menu_ZA_0714": "https://archives.bulbagarden.net/media/upload/8/85/Menu_ZA_0714.png",
    "Menu_ZA_0715": "https://archives.bulbagarden.net/media/upload/d/db/Menu_ZA_0715.png",
    "Menu_ZA_0716": "https://archives.bulbagarden.net/media/upload/8/8c/Menu_ZA_0716.png",
    "Menu_ZA_0717": "https://archives.bulbagarden.net/media/upload/d/d0/Menu_ZA_0717.png",
    "Menu_ZA_0718": "https://archives.bulbagarden.net/media/upload/0/00/Menu_ZA_0718.png",
    "Menu_ZA_0719": "https://archives.bulbagarden.net/media/upload/5/5a/Menu_ZA_0719.png",
    "Menu_ZA_0720": "https://archives.bulbagarden.net/media/upload/a/a7/Menu_ZA_0720.png",
    "Menu_ZA_0721": "https://archives.bulbagarden.net/media/upload/d/d4/Menu_ZA_0721.png",
    "Menu_ZA_0780": "https://archives.bulbagarden.net/media/upload/b/be/Menu_ZA_0780.png",
    "Menu_ZA_0870": "https://archives.bulbagarden.net/media/upload/7/7d/Menu_ZA_0870.png",
    "Menu_ZA_9999": "https://archives.bulbagarden.net/media/upload/3/3f/Menu_ZA_9999.png"
}

# Folder where images are saved
save_dir = "menu_images"
os.makedirs(save_dir, exist_ok=True)

# User-Agent so Bulbagarden doesn't block the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

# Function to download with retries
def download_with_retry(name, url, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=12)

            # Success
            if response.status_code == 200:
                file_path = os.path.join(save_dir, f"{name}.png")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"✔ Saved: {name}")
                return True

            else:
                print(f"✖ {name} failed (HTTP {response.status_code})")

        except Exception as e:
            print(f"⚠ Error on attempt {attempt} for {name}: {e}")

        # Wait before retrying
        print(f"⟳ Retrying in {delay} seconds...")
        time.sleep(delay)

    print(f"❌ Failed permanently: {name}")
    return False


# -------------------------------
# MAIN DOWNLOAD LOOP
# -------------------------------

print(f"Saving images to: {save_dir}/\n")

for name, url in urls.items():
    print(f"Downloading {name}…")
    download_with_retry(name, url)
    time.sleep(1)  # throttle to avoid rate-limits

print("\n🎉 Done! All images attempted.")
