# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)
   
Title("Dark Web Links")

try:
    links = {
        "Search Engine": {
            "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
            "Danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
            "Sentor": "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/",
            "Hidden Answers": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/",
            "riseup searx": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",
        },
        "Bitcoin Anonymity": {
            "Dark Mixer": "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/",
            "Mixabit": "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/",
            "EasyCoin": "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/",
            "Onionwallet": "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/",
            "VirginBitcoin": "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/",
            "Cryptostamps": "http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/",
        },
        "DDoS": {
            "Stresser": "http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/",
        },
        "Torrents": {
            "The Pirate Bay": "http://uj3wazyk5kz5rzs.onion/",
            "1337x": "http://1337xwlc2c8sf3d7.onion/",
        },
        "Social Media": {
            "Foxy": "http://foxy6vayr5g5hwwx.onion/",
        },
        "Wikis": {
            "Hidden Wiki": "http://wikitjerrta4qgz4.onion/",
            "Deep Web Wiki": "http://wikicbtbf7rgjjbqe.onion/",
        },
        "Educational": {
            "EDU": "http://edu.onion/",
        },
    }

    def format_links(links):
        display_link = ""
        
        for category, sites in links.items():
            display_link += "\n" + MainColor2(category) + "\n"
            
            def add_sites(prefix, sites_dict):
                nonlocal display_link
                for i, (site, url) in enumerate(sites_dict.items()):
                    if isinstance(url, dict):
                        display_link += f"{prefix}├─ {red + site}\n"
                        add_sites(prefix + "│   ", url)
                    else:
                        if i == len(sites_dict) - 1:
                            display_link += f"{prefix}└─ {red + site}: {white + url}" + "\n"
                        else:
                            display_link += f"{prefix}├─ {red + site}: {white + url}" + "\n"
            
            add_sites("", sites)
        
        return display_link

    formatted_links = format_links(links)
    Slow(tor_banner + MainColor(formatted_links))
    Continue()
    Reset()
except Exception as e:
    Error(e)
