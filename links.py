import os
import subprocess
import sys
import shutil
from typing import List, Dict

def check_dependencies() -> bool:
    """Check if required system commands (figlet, toilet) are installed."""
    dependencies = ["figlet", "toilet"]
    missing = []
    
    for dep in dependencies:
        
        if shutil.which(dep) is None:
            missing.append(dep)
    
    if missing:
        print(f"\033[31mWarning: Missing dependencies: {', '.join(missing)}")
        print("ASCII art will be skipped. Install figlet and toilet for enhanced output.")
        print("On Windows, you can install them via WSL or download Windows binaries.")
        print("Continuing with plain text output...\033[0m")
        print(" ")
        print(" ")
        return False
    return True

def clear_screen() -> None:
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def display_ascii_art(text: str, command: str = "figlet", font: str = None) -> None:
    """Display ASCII art using figlet or toilet with optional font."""
    if not shutil.which(command):
        print(f"\033[33m{text}\033[0m")  
        return
    try:
        cmd = [command, text]
        if font:
            cmd.extend(["-f", font])
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print(f"\033[33m{text}\033[0m")  

def print_colored(text: str, color_code: str) -> None:
    """Print text in the specified ANSI color."""
    
    if os.name == "nt":
        os.system("color")  
    print(f"\033[{color_code}m{text}\033[0m")

def get_onion_links() -> List[Dict[str, str]]:
    """Return a categorized list of .onion links for educational purposes."""
    return [
        {
            "category": "Dark Web Directories",
            "links": [
                {"url": "http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/", "desc": "OnionLinks v3"},
                {"url": "http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/", "desc": "The Hidden Wiki"},
                {"url": "http://2jwcnprqbugvyi6ok2h2h7u26qc6j5wxm7feh3znlh2qu3h6hjld4kyd.onion/", "desc": "Another Hidden Wiki"},
                {"url": "http://jgwe5cjqdbyvudjqskaajbfibfewew4pndx52dye7ug3mt3jimmktkid.onion/", "desc": "Pug’s Ultimate Dark Web Guide"},
                {"url": "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page", "desc": "The Original Hidden Wiki"}
            ]
        },
        {
            "category": "Bitcoin Anonymity",
            "links": [
                {"url": "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/", "desc": "Dark Mixer – Anonymous Bitcoin Mixer"},
                {"url": "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/", "desc": "Mixabit – Bitcoin Mixer"},
                {"url": "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/", "desc": "EasyCoin – Bitcoin Wallet and Mixer"},
                {"url": "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/", "desc": "Onionwallet – Anonymous and Secure Bitcoin Wallet and Mixer"},
                {"url": "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/", "desc": "VirginBitcoins – Buy Freshly Mined Clean Bitcoins"}
            ]
        },
        {
            "category": "Drug Stores",
            "links": [
                {"url": "http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/", "desc": "DCdutchconnectionUK – The Dutch Connection for the UK"},
                {"url": "http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/", "desc": "DrChronic – Weed Straight from the Source"},
                {"url": "http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/", "desc": "TomAndJerry – Cocaine, Heroin, MDMA and LSD from NL"},
                {"url": "http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/", "desc": "420prime – Cannabis in Dispensary Quality from the UK"},
                {"url": "http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/", "desc": "Bitpharma – Biggest European .onion Drug Store"},
                {"url": "http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/", "desc": "EuCanna – First Class Cannabis"},
                {"url": "http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/", "desc": "Smokeables – Finest Organic Cannabis from the USA"},
                {"url": "http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/", "desc": "CannabisUK – UK Wholesale Cannabis Supplier"},
                {"url": "http://2ln3x7ru6psileh7il7jot2ufhol4o7nd54z663xonnnmmku4dgkx3ad.onion/", "desc": "Brainmagic – Best Darkweb Psychedelics"},
                {"url": "http://usmost4cbpesx552s2s4ti3c4nk2xgiu763vhcs3b4uc4ppp3zwnscyd.onion/", "desc": "NLGrowers – Coffee Shop Grade Cannabis from the Netherlands"},
                {"url": "http://xf2gry25d3tyxkiu2xlvczd3q7jl6yyhtpodevjugnxia2u665asozad.onion/", "desc": "Peoples Drug Store – The Darkweb’s Best Drug Supplier!"},
                {"url": "http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/", "desc": "DeDope – German Weed Store"}
            ]
        },
        {
            "category": "Commercial Links",
            "links": [
                {"url": "http://prjd5pmbug2cnfs67s3y65ods27vamswdaw2lnwf45ys3pjl55h2gwqd.onion/", "desc": "Dark Web Hackers for Hire"},
                {"url": "http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/", "desc": "AccMarket – Premium Paypal, Ebay and Bank Accounts"},
                {"url": "http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/", "desc": "Cardshop – USA CVV KNOWN BALANCE & Worldwide CC & CVV"},
                {"url": "http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/", "desc": "Darkmining – Bitcoin Mining with Stolen Electricity"},
                {"url": "http://jhi4v5rjly75ggha26cu2eeyfhwvgbde4w6d75vepwxt2zht5sqfhuqd.onion/", "desc": "Bitcoin Investment Trust – Earn 5-9% per Week!"},
                {"url": "http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/", "desc": "Mobile Store – Best Unlocked Cell Phones Vendor"},
                {"url": "http://vhlehwexxmbnvecbmsk4ormttdvhlhbnyabai4cithvizzaduf3gmayd.onion/", "desc": "Kamagra 4 Bitcoin – Like Viagra but Cheaper"},
                {"url": "http://ymvhtqya23wqpez63gyc3ke4svju3mqsby2awnhd3bk2e65izt7baqad.onion/", "desc": "OnionIdentityServices – Fake Passports and ID Cards for Bitcoin"},
                {"url": "http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/", "desc": "UK Guns and Ammo Store"},
                {"url": "http://lqcjo7esbfog5t4r4gyy7jurpzf6cavpfmc4vkal4k2g4ie66ao5mryd.onion/", "desc": "USfakeIDs – US Fake ID Store"},
                {"url": "http://qazkxav4zzmt5xwfw6my362jdwhzrcafz7qpd5kugfgx7z7il5lyb6ad.onion/", "desc": "Counterfeit USD – High Quality USD Counterfeits"},
                {"url": "http://gd5x24pjoan2pddc2fs6jlmnqbawq562d2qyk6ym4peu5ihzy6gd4jad.onion/", "desc": "USAcitizenship – Become a Citizen of the USA"},
                {"url": "http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/", "desc": "EuroGuns"},
                {"url": "http://okayd5ljzdv4gzrtiqlhtzjbflymfny2bxc2eacej3tamu2nyka7bxad.onion/", "desc": "Apples4Bitcoin – iPhones, iPads and More for Bitcoin"},
                {"url": "http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/", "desc": "UKpassports – Real UK Passports"},
                {"url": "http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/", "desc": "ccPal – PayPals, Ebays, CCs and More"},
                {"url": "http://kq4okz5kf4xosbsnvdr45uukjhbm4oameb6k6agjjsydycvflcewl4qd.onion/", "desc": "Rent-A-Hacker – Hire a Hacker for Bitcoin"},
                {"url": "http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/", "desc": "Webuybitcoins – Sell Your Bitcoins for Cash, Paypal, WU etc"},
                {"url": "http://odahix2ysdtqp4lgak4h2rsnd35dmkdx3ndzjbdhk3jiviqkljfjmnqd.onion/", "desc": "HQER – High Quality Euro Bill Counterfeits"}
            ]
        },
        {
            "category": "Other Resources",
            "links": [
                {"url": "http://danielas3rtn54uwmofdo3x2bsdifr47huasnmbgqzfrec5ubupvtpid.onion/", "desc": "DanielWin"},
                {"url": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/", "desc": "Hidden Answers"},
                {"url": "https://kcmykvkkt3umiyx4xouu3sjo6odz3rolqphy2i2bbdan33g3zrjfjgqd.onion/", "desc": "aboutMastodon"},
                {"url": "http://dhosting4xxoydyaivckq7tsmtgi4wfs3flpeyitekkmqwu4v4r46syd.onion/", "desc": "Daniels Hosting"},
                {"url": "http://cathug2kyi4ilneggumrenayhuhsvrgn6qv2y47bgeet42iivkpynqad.onion/", "desc": "Cathugger’s Site"},
                {"url": "http://zgeajoabenj2nac6k5cei5qy62iu5yun5gm2vjnxy65r3p3amzykwxqd.onion/", "desc": "Darkweb Blog"},
                {"url": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/", "desc": "Riseup Searx"},
                {"url": "http://45tbhx5prlejzjgn36nqaxqb6qnm73pbohuvqkpxz2zowh57bxqawkid.onion/", "desc": "Parckwart’s Website"},
                {"url": "http://sidignlwz2odjhgcfhbueinmr23v5bubq2x43dskcebh5sbd2qrxtkid.onion/", "desc": "SecureJabber"},
                {"url": "http://sik5nlgfc5qylnnsr57qrbm64zbdx6t4lreyhpon3ychmxmiem7tioad.onion/", "desc": "Qubes OS"},
                {"url": "http://dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion/", "desc": "Whonix"},
                {"url": "http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/", "desc": "OnionShare"},
                {"url": "http://nanochanqzaytwlydykbg5nxkgyjxk3zsrctxuoxdmbx5jbh2ydyprid.onion/", "desc": "NanoChan"},
                {"url": "http://picochanwvqfa2xsrfzlul4x4aqtog2eljll5qnj5iagpbhx2vmfqnid.onion/", "desc": "PicoChan"},
                {"url": "http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion/", "desc": "EndChan"},
                {"url": "http://dngtk6iydmpokbyyk3irqznceft3hze6q6rasrqlz46v7pq4klxnl4yd.onion/", "desc": "256Chan"},
                {"url": "http://cct5wy6mzgmft24xzw6zeaf55aaqmo6324gjlsghdhbiw5gdaaf4pkad.onion/", "desc": "Snopyta"},
                {"url": "http://wnrgozz3bmm33em4aln3lrbewf3ikxj7fwglqgla2tpdji4znjp7viqd.onion/", "desc": "VYempire.xyz"},
                {"url": "http://7sk2kov2xwx6cbc32phynrifegg6pklmzs7luwcggtzrnlsolxxuyfyd.onion/", "desc": "SystemLI.org"},
                {"url": "http://stormwayszuh4juycoy4kwoww5gvcu2c4tdtpkup667pdwe4qenzwayd.onion/", "desc": "CryptoStorm VPN"},
                {"url": "http://xdkriz6cn2avvcr2vks5lvvtmfojz2ohjzj4fhyuka55mvljeso2ztqd.onion/", "desc": "Cock.li"},
                {"url": "http://eludemailxhnqzfmxehy3bk5guyhlxbunfyhkcksv4gvx6d3wcf6smad.onion/", "desc": "Elude.in"},
                {"url": "http://lainwir3s4y5r7mqm3kurzpljyf77vty2hrrfkps6wm4nnnqzest4lqd.onion/", "desc": "qord11.net"},
                {"url": "http://cgjzkysxa4ru5rhrtr6rafckhexbisbtxwg2fg743cjumioysmirhdad.onion/", "desc": "Course Enigma"},
                {"url": "http://killnod2s77o3axkktdu52aqmmy4acisz2gicbhjm4xbvxa2zfftteyd.onion/", "desc": "Kill9"},
                {"url": "http://digdeep4orxw6psc33yxa2dgmuycj74zi6334xhxjlgppw6odvkzkiad.onion/", "desc": "DigDeeper"},
                {"url": "http://spywaredrcdg5krvjnukp3vbdwiqcv3zwbrcg6qh27kiwecm4qyfphid.onion/", "desc": "Spyware Watchdog"},
                {"url": "http://meynethaffeecapsvfphrcnfrx44w2nskgls2juwitibvqctk2plvhqd.onion/", "desc": "May Vane Day Studios"},
                {"url": "http://zsxjtsgzborzdllyp64c6pwnjz5eic76bsksbxzqefzogwcydnkjy3yd.onion/", "desc": "Shadow Wiki"},
                {"url": "http://g7ejphhubv5idbbu3hb3wawrs5adw7tkx7yjabnf65xtzztgg4hcsqqd.onion/", "desc": "Defcon"},
                {"url": "http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/", "desc": "Propublica"},
                {"url": "http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion/", "desc": "Darknetlive"},
                {"url": "http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion/", "desc": "KeyBase.IO"},
                {"url": "http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/", "desc": "CIA.GOV"},
                {"url": "http://archivebyd3rzt3ehjpm4c3bjkyxv3hjleiytnvxcn7x32psn2kxcuid.onion/", "desc": "Internet Archive"},
                {"url": "http://bible4u2lvhacg4b3to2e2veqpwmrc2c3tjf2wuuqiz332vlwmr4xbad.onion/", "desc": "Bible4u"},
                {"url": "http://kx5thpx2olielkihfyo4jgjqfb7zx7wxr3sd4xzt26ochei4m6f7tayd.onion/", "desc": "Imperial Library"},
                {"url": "http://nv3x2jozywh63fkohn5mwp2d73vasusjixn3im3ueof52fmbjsigw6ad.onion/", "desc": "Comic Books"}
            ]
        }
    ]

def main() -> None:
    """Main function to display the dark web links directory."""
    clear_screen()
    
    
    logox = """
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █▀█ █▀█   █▄░█ █▀▀ ▀█▀ █░█░█ █▀█ █▀█ █▄▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▄█ █▀▄   █░▀█ ██▄ ░█░ ▀▄▀▄▀ █▄█ █▀▄ █░█

© 2025 asankaxgit. All Rights Reserved. This tool and its associated code, 
documentation, and resources are the intellectual property of asankaxgit. 
Unauthorized reproduction, distribution, or modification of this tool is 
prohibited without explicit permission from the copyright holder."""
    print(logox)
    print("")
    
    
    disclaimer = """
    DISCLAIMER: This tool is provided strictly for EDUCATIONAL AND RESEARCH PURPOSES ONLY.
    Accessing or using dark web (.onion) links may involve legal, ethical, and security risks.
    Users are solely responsible for ensuring compliance with all applicable laws.
    The creators do not endorse or promote any illegal activities.
    Use Tor Browser to access .onion links and exercise caution to ensure safety.
    By using this tool, you agree to use it lawfully and assume all associated risks.
    """
    print_colored(disclaimer.strip(), "31")  
    print()
    
    
    check_dependencies()
    
    
    for category in get_onion_links():
        print_colored(f"{category['category'].upper()}:", "33")  
        for link in category['links']:
            print(f"{link['url']} – {link['desc']}")
        print()

if __name__ == "__main__":
    main()
