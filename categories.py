historical_pirates = {
    r'(b[kl]ack.{0,20}beard|teach)', r'henry.{0,10}morgan', r'[cz]h[ie]ng (y?i )?(sao|shih)', 'bartholomew roberts',
    r'anne.{0,10}bonny', 'mary read', r'calico.{0,10}jack', r'(captain|william).{0,10}kid', r'francis.{0,10}drake',
    'peter easton', r'red.{0,10}beard', 'radio caroline', r'captain.{0,10}morgan',
    r'red.{0,10}beard', 'john paul jones', 'bootstrap bill',
    'barbarossa', 'piet pieterszoon hein',
    r'henry [ea]very', 'ben hornigold', 'black bart',
    'grace o\'malley', r'gr[aá]inne mhaol', r'charles.{0,10}vane', 'barbaroja', 'stede bonnet',
    r'st.rtebec?ker', 'queen emeraldas', r'l.?olonnais', 'condor', r'pont[eé]n',
    'jean lafitte', r'jack.{0,10}rackham', 'barbossa', r'piet.{0,10}hein', r'bel?lamy', 'harlock', r'jolly rod?ger', 'roque brasiliano', 'jack birdy',
    'howell davis', r'(catherine hagerty|charlotte badger)', r'amaro pargo', r'(i am the captain now|captain phillips|abduwali muse)', 'sayyida',
    'edward low', 'black sam', 'kanhoji angre', 'cheung po tsai', 'hayrettin', 'bartolomé sharp', 'john quelch',
}

digital_pirates = {
    'van der sar', 'ernesto van der sar', 'empress', 'yify',
    'alexandra elbakyan', r'(gottfrid|svartholm|anakata)',
    r'(swartz?|schwarz)', 'dvdjon', 'dvdfab', 'libgen', 'dolphin team',
    'dodi', 'ulbricht', 'db0',
    'what.cd', 'codex', 'r2r', 'linuxrulez', r'm[0o]nkrus', 'cpy',
    'xatab', 'rarbg', 'justchill.tv', 'skidrow', 'cs.rin', 'voksi',
    'passthepopcorn.me', 'brewster kahle', r'(fredrik neij|tiamo)', 'john draper',
    r'mitnic?k', r'kim ?dot ?com', 'sparks', 'ytcracker',
    'mutahar', 'pompey pirates', 'medway boys', 'og frostwire', 'birungueta', 'sciresm', 'gary bowser', 'saurik',
    'axxo', 'aphex twin', 'vimm lair', r'pirate ?(party|byran)', 'rick falkvinge', r'(pirate.{0,10}bay|tpb)', r'fi[rt][ -]?(bit)? ?girl', 
    'artem vaulin', 'torrentfreak', 'fairlight', 'iso hunt',
    r'(raz[oe]r|1911)', 'thefloW', r'(freemediaheckyeah|fmhy)',
    'duke lupus', 'elite', 'team qtz', 'free stuff', r'anna.{0,20}archiv', 'slipstream', 'holopirates',
    'phrozen', 'openmedia', 'limewire', 'team v.r', 'riley testut', 'bunch of bandits', 'mobilism',
    'jc141', 'johncena141', 'core team', 'qxr', 'lz129hindenburg', r'(isak gerson|kopimism)', 'flwwhtbrt',
    'nyaa', 'elamigos', 'seedbox', 'conspir4cy', 'selfh.st', 'gary lake', 'devkitpro', 'apprentice harper', r'(tgx|torrentgalaxy)', 
    'socraticbliss3', r'solid_?squad', 'byxatab',
    'massgravel', r'sci[ -]hub', 'patrick breyer', 'gentleman pirate', 'rutracker', r'(quincy larson|freecodecamp)',
    'ilcorsaronero', 'diakov', 'emuparadise', 'bjthedj', 'megusta media', 'arion kurtaj', r'library ?genesis', 'bram cohen',
    r'seed.{0,10}ratio', 'audiobookbay', r'[rc]/piracy', 'debrid', 'anadius', 'animepahe', 'fmovies', 'steamdeckpirates', 'snahp', 'jack rhysider',
    'demonoid', 'paradox', '1337x.to', 'framestor', r'\brune\b', 'goldberg', 'MKDEV', 'oink.me', 'PMEDIA',
    'pilimi', r'(petr harmáček|harmy)', 'wiki group', 'daniel j. bernstein', 'dauphong', 'netrunner',
    
}

pirate_tools = {
    r'arrr?s?\b', r'(\bmas\b|microsoft activation script)', 'homebrew', 'revanced', 'archive.org', 'tokybo', 'antrenamer',
    'itstoggle', r'(torr?enting|bitt?orr?ent)', r'(qbitt?orr?ent|QBT)', 'jellyfin', 'soulseek', 'napster', 'megathread', 'winrar',
    r'(z.? ?library|z-?lib)', 'warez', 'kazaa', 'stremio', 'glftpd', 'torrentio', 'hydra launcher', 'mactheripper', r'mihon|tachiyomi', 'deluge',
    'iptv', r'\bi2p\b', 'internet archive',
     
}

foss_advocates = {
    r'(stall?man|\brms\b)', r'(linus|torvalds)',
    'theo de raadt', 'mental outlaw', 'kenny', 'lawrence lessig',
    r'ross?man', 'fabrice bellard',
    r'(peter sunde|brokep)', 'deviant ollam', 'shelby techtangents',
    'eff', 'snowden', 'noncompete',
    'phil zimmermann', 'behlendorf', 'doctorow', 'geohot',
    r'tim.{0,5}reilly', 'drew devault', 'ton roosendaal', 'peter zaitsev',
    'alan cox', 'tux', 'brewster kahle', r'(eric ?s? raymond|\besr\b)', 'christopher lydon',
    'chelsea manning', 'moxie marlinespike', 'baptiste', 'dolphin team',
    'aaron schwartz', 'chriss messina', 'greg kroah-hartman', 'george hotz', 'david heinemeier hansson', 'techlore',
    'george hotz', 'lefebvre', 'chainfire', 'jon maddog hall', r'jim(my|bo) wales', 'neil stephenson',
    'sam ruby', 'fumiama', 'carl richell', 'geoff knauth', 'manul laphroaig', 'the mentor', 'vignoli',
    'techtangents', r'terry (a. )?davis', 'crimew', 'db0', 'kovid goyal',
    'neal stephenson', 'level1techs', 'poettering', 'audrey tang', 'ossi', 'vladimir vuki',
    'bruce perens', 'limor fried', 'sindre sorhus', 'mitch kapor', 'maxer', 'eben moglen',
    'alexis kauffmann', 'ian murdock', 'trafotin', 'suckless', 'zaitzev', 'michael tiemann',
    'paul vixie', r'(cydia|jay freeman)', 'guido van rossum', r'jeremy soller', 'grady booch', 'john carmack', 'scott collins', 'igor pavlov',
    'coraline ada ehmke', r'(jake leslie davis|topiary)', 'dingledine', 'douglas engelbart', r'cedric m[oö]ssner', 'dillon', r'masnic?k', 'd4rken',
    'haidra', 'arvid norber', 'norwell', 'orcaslicer', 'paulus schoutsen', 'linietsky', 'ariel manzur', r'emulator.{0,20}near', 'junio hamano', 'jonas oberg',
    'bram cohen', 'jagielski', 'chris titus', 'dennis ritchie', 'ross scott', 'doug cutting', 'pliny', 'douglas rushkoff', 'Tim Wu', 'James Meese', 'Chris Messina',
    
}

fos_software = {
    'linux', 'firefox', 'github', 'lemmy', r'(vlc|videolan)', r'\bkde\b', 'blender',
    'melonds', r'\bgnu\b', 'marlin', 'dolphin', 'cyanogen', 'proton', r'\bTeX\b',
    'gimp', 'libretro', 'debian', 'ubuntu', 'python', r'\barch\b', 'gentoo', 'redox', r'\brust\b', r'\btor\b', 'openbsd', '7zip', 'edopro',
    r'(notesbook|\btuta\b)', 'aihorde', '\bxz\b', 'godot', r'\bgit\b', 'termux', 'krita', 'sabnzb', 'newpipe', 'aniyomi', 'proxmox', 'pihole',
    'lnreader', 'quicknovel', 'neovim', 'caddy', 'bookstack', 'universal blue', 'Zen Browser', 'Home Assistant', '2600', 'syncthing', 'librewolf',
    'GrapheneOS', 'Mihon', r'\bi2p\b', 'ffmpeg',
}

anarchists = {
    'chomsky', 'severino di giovanni', 'jacque ellul',
    r'(goldman|red emma)', 'kropotkin', 'bookchin', 'lucy parsons',
    'bakunin', r'gra[eb]ber', 'salvador segui', 'el noi del sucre',
    'gelderloos', 'tolstoy', 'alice nutter', 'jen angel', 'sergey nechayev',
    'margaret sanger', 'abbie hoffman', 'jaron lanier',
    'william powell', 'bhagat singh', 'juan carlos mechoso',
    'malatesta', r'slavoj [zž]i[zž]ek', 'mark fisher',
    'robert evans', r'no gods.? no masters', 'sid vicious',
    r'mah?[kc][hi]?no', 'marvin heemeyer', r'hunter.{0,10}thompson',
    'raul wallenberg', 'moore', 'durruti', r'(vendetta|\bV\b)',
    'jello biafra', 'pink panther gang', 'assange', 'voltairine',
    'laozi', 'greg graffin', 'proudhon', 'technoblade', 'banksy', 
    'leopold kohr', 'ricardo flores magon', 'eric hughes', r'thought ?slime',
    'louise michel', 'charlotte wilson', '[Öo]calan', 'landauer', r'james c. ?scott',
    r'utah.{0,10}phillips', r'katniss.{0,10}everdeen', 'crimew', 'db0', r'abbie.{0,10}hoffman',
    'wilhelm weitling', 'william goodwin', 'radowitzky', 'diogenes', 'woody guthrie.',
    'ken kesey', 'anti-?flag', 'black ?flag', 'dead kennedy', r'(ursula|guin)', 'co-op',
    'gramci', 'john zerzan', r'julio l.pez ch.vez', 'sacco', 'vanzetti', 'kate libby',
    'silvestre revueltas', 'ben reitman', r'bell.{0,10}hooks', 'maria lacerda de moura',
    r'iain.{0,10}banks', r'(pat the bunny|schneeweis)', 'zoe baker', 'andrewism', r'(danbert nobacon|chumbawamba)', 'lou watts',
    'phineas fisher', r'edward.{0,10}abbey', 'leslie fish', 'rudolf rocker', r'pussy ri[o0]t', 'pekka himanen',
    'albert camus', r'christiani?a', 'howard zinn', r'people.?s history of the (us|united)',
    r'sub.?media', 'oscar wilde', 'crocodilekin', 'gary snyder', 'vaillant', 'stirner',
    r'philip k\.? dick', 'lorax', 'spooner', 'shock doctrine', 'merchants of doubt',
    'margaret killjoy', r'protests.{0,10}portland', r'(mary harris jones|mother jones)', r'lorenzo kom.?boa', 'kim diaz holm', 
    r'marsha.{0,10}johnson', r'ram[oó]n de la sagra', 'carne ross', r'elis[ée]?e reclus', 'osvaldo bayer', 'wright mills', 'art young', 
    'daniel fraga', 'renzo novatore', 'peter lamborn wilson', 'william godwin', r'cnt.{0,5}fai', 'amir taaki', 
    r'beau of the fifth column|belle of the ranch', 'sam dolgoff', 'halim alrah', 'bellegarrigue',
    'ruth ellen kinna', ' jack white', 'grothendieck', r'oiticica', 'calheiros', 'johann most', 'benjamin tucker', 'vonnegut',
    'john brown', 'sex pistols', 'undernet', 'carl auge', 'mateo morral', 'franscisco ferrer', 'rache bartmoss', 'rio reiser',
    'crimethink', 'ettore mattei', 'mcanderson', 'giuseppe pinelli', r'(\bccc\b|chaos computer club)', 'slc punk', r'elise ottesen[- ]jensen',
    'sophie scholl', r'haymarket|chicago (anarchists|affair)', r'rick.{0,20}young ones', 'malcolm x', 'bertrand russel', 'erich mühsam', 'rise-up'
    r'(fat mike|\bnofx\b)', 'eugene debs', 'Gabriel Garcia Marquez', 'jane fonda', 'Ricardo Flores Magón', 'Lucio Urtubia', 'Benjamin Lay', 'Propagandhi',
}

fictional = {
    r'(spar?row|johnny depp|pirates.{0,10}car?ribb?ean)', 'luffy', r'(long )?john silver',
    'patchy', 'alestorm', 'borderlands', 'hondo ohnaka', 'steve the pirate', 'edward kenway',
    r'((captain)?.{0,10}hook|peter pan)', r'zero ?cool', 'belters',
    'lechuck', 'gaige', 'arsene lupin', 'lupin iii', r'(threepwood|guybrush)',
    r'blau ?b[aä]r', r'captain.{0,10}blood', 'chiching xi', 'pippi longstocking',
    'crunch', r'gary.{0,10}fung', 'judas', 'baba', r'dread ?pirate ?roberts?', 'hunter s. thompson', 'ishikawa goemon', 
    'orlando bloom', r'jack.{0,10}spparo', 'tony bennett', 'triad', r'pont[eé]n',
    'trafalgar d', r'davy.{0,10}jones', r'captain.{0,10}silver', 'captain sticky beard', 'long dong silver',
    'robin hood', 'spongebob', 'vallo', 'saltspite', 'bluebeard', r'(robbie rotten|lazytown)', 'the pirates of penzance', ' ridley the space pirate',
    r'(willem van der decken|flying dutchman)', 'zoro', r'white ?beard', 'buggy', 'sea of thieves', 'curse of oak island', r'jake.{0,10}never ?land',
    r'(captain mosey|flying spaghetti monster)', 'nightcrawler', 'Ace from Onepiece', 'Tress of the Emerald Sea'
}

other = {
    'bernie sanders', 'naomi klein', 'crazy frog', 'john oliver',
    'raoul wallenberg', 'o\'reilly', r'(the )?joker',
    'cereal killer', 'kate middleton', 'ted kaczynski',
    'ozzy osbourne', 'alice cooper', 'murray rothbard', 'christopher hitchens', 
    'andrew mccutcheon', 'milie gillet','tim curry', 'odesseiron', 'mangione', 'project mayhem',
    'raul duke', 'tomas de lezo', 'wozniak', 'kant', 'batman', 'elon musk', 'notch', 'kirk', 'emmanuel goldstein',
    'voltaire', 'dessalines', 'bryan reynolds', 'jakub polak', 'black hawk',
    r'[fp]h?antomas', 'foucalt', r'anon(ymo?us)?', 'kermit', 'ghandi', r'(satoshi|nakamoto)', 'fawkes', 'timothy leary',
    'openai', 'fixedfun1', "krishnamurthy", 'lina kahn', 'jesus', r'paul.{0,10}burchill', r'(gr[aá]inne|grace) (ní mháille|o.malley)', 
    'eiswuxe', 'neves', 'heart bound', 'piratesoftware', r'neo.{0,20}matrix', 'bob loblaw', 'privacy guides', r'(gabe newell|gaben)', 
    'antigone', 'dionysius the phocaean', 'the dark knight', 'max schrems', 'lauren mosenthal', 'buddha', r'mohamm[ae]d', 'john lennon',
    'emerson', 'luke smith', 'cosmo jarvis', 'thomas paine', 'nietzsche', 'katharina könig', r'(captain|james) cook', 'bart simpson', 'mozart',
    r'p[oa]ncho villa', 'david baker', 'andrew mccutchen', 'bitcoin', 'corbettreport.com', 'peter wilson', 'Shannon Larratt',
}

asd = {
  r'\basd\b', r'\baudhd\b', '♾️', r'I.+autistic', 'on the spectrum'
}
adhd = {
  r'\bau?dhd\b', '🦋'
}