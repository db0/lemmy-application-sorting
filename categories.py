historical_pirates = {
    r'(black.{0,20}beard|teach)', r'henry.{0,10}morgan', r'[cz]h[ie]ng (y?i )?(sao|shih)', 'bartholomew roberts',
    r'anne.{0,10}bonny', 'mary read', r'calico.{0,10}jack', r'captain.{0,10}kidd', r'francis.{0,10}drake',
    'peter easton', r'red.{0,10}beard', 'radio caroline', r'captain.{0,10}morgan',
    r'red.{0,10}beard', 'john paul jones', 'bootstrap bill',
    'barbarossa', 'piet pieterszoon hein',
    'henry avery', 'ben hornigold', r'william.{0,10}kidd', 'black bart',
    'grace o\'malley', r'gr[aá]inne mhaol', r'charles.{0,10}vane', 'barbaroja', 'stede bonnet',
    r'st.rtebec?ker', 'queen emeraldas', r'l.?olonnais', 'condor', r'pont[eé]n',
    'jean lafitte', r'jack.{0,10}rackham', 'barbossa', r'piet.{0,10}hein', r'bel?lamy', 'harlock', r'jolly rod?ger', 'roque brasiliano', 'jack birdy'
}

digital_pirates = {
    r'arrr?s',
    'itstoggle', 'torrenting', 'archive.org',
    'van der sar', 'ernesto van der sar', 'empress', 'yify',
    'alexandra elbakyan', r'(gottfrid|svartholm|anakata)',
    r'(swartz?|schwarz)', 'dvdjon', 'dvdfab', 'libgen', 'dolphin team', 'sonarr', 'radarr',
    'dodi', 'ulbricht', 'db0',
    'what.cd', 'codex', 'r2r', 'linuxrulez', 'megathread', r'm[0o]nkrus', 'cpy',
    'xatab', 'rarbg', 'justchill.tv', 'skidrow', 'cs.rin', 'voksi',
    'passthepopcorn.me', 'brewster kahle', r'(fredrik neij|tiamo)', 'john draper',
    'napster', r'mitnic?k', r'kim ?dot ?com', 'sparks', 'ytcracker', 'qbittorrent', 'soulseek',
    'mutahar', 'pompey pirates', 'medway boys', 'og frostwire', 'birungueta', 'sciresm', 'gary bowser', 'saurik',
    'axxo', 'aphex twin', 'vimm lair', 'pirate party', 'rick falkvinge', r'(pirate.{0,10}bay|tpb)', r'fi[rt][ -]?(bit)? ?girl', 
    'artem vaulin', 'jellyfin', 'torrentfreak', 'fairlight', 'iso hunt',
    'razor', 'thefloW', r'(z.? ?library|z-?lib)', r'(freemediaheckyeah|fmhy)',
    'duke lupus', 'elite', 'team qtz', 'free stuff', r'anna.{0,20}archive', 'slipstream', 'holopirates', 'warez',
    'phrozen', 'openmedia', 'kazaa', 'limewire', 'team v.r', 'riley testut', 'bunch of bandits', 'mobilism',
    'jc141', 'johncena141', 'core team', 'qxr', 'lz129hindenburg', 'hydra launcher', r'(isak gerson|kopimism)', 'flwwhtbrt',
    'nyaa', 'elamigos', 'seedbox', 'conspir4cy', 'selfh.st', 'gary lake', 'devkitpro', 'apprentice harper', r'(tgx|torrentgalaxy)', 'socraticbliss3', 'solid_?squad', 'massgravel', r'sci[ -]hub', 'patrick breyer'
}

foss_advocates = {
    r'(stall?man|rms)', r'(linus|torvalds)',
    'theo de raadt', 'mental outlaw', 'kenny', 'lawrence lessig',
    r'ross?man', 'fabrice bellard',
    'peter sunde', 'deviant ollam', 'shelby techtangents',
    'eff', 'snowden', 'noncompete',
    'phil zimmermann', 'behlendorf', 'doctorow', 'geohot',
    'tim o\'reilly', 'drew devault', 'ton roosendaal', 'peter zaitsev',
    'alan cox', 'tux', 'brewster kahle', r'(eric ?s? raymond|esr)', 'christopher lydon',
    'chelsea manning', 'moxie marlinespike', 'jean-baptiste kempf', 'dolphin team',
    'aaron schwartz', 'chriss messina', 'greg kroah-hartman', 'george hotz', 'david heinemeier hansson', 'techlore',
    'george hotz', 'lefebvre', 'chainfire', 'jon maddog hall', 'jimmy wales', 'neil stephenson',
    'sam ruby', 'fumiama', 'carl richell', 'geoff knauth', 'manul laphroaig', 'the mentor', 'vignoli',
    'techtangents', r'terry (a. )?davis', 'crimew', 'db0', 'kovid goyal',
    'neal stephenson', 'level1techs', 'poettering', 'audrey tang', 'ossi', 'vladimir vuki',
    'bruce perens', 'limor fried', 'sindre sorhus', 'mitch kapor', 'maxer', 'eben moglen',
    'alexis kauffmann', 'ian murdock', 'trafotin', 'suckless', 'zaitzev', 'michael tiemann',
    'paul vixie', r'(cydia|jay freeman)', 'guido van rossum', r'jeremy soller', 'grady booch', 'john carmack', 'scott collins', 'igor pavlov'
    
    
}

software = {
    'linux', 'firefox', 'github', 'lemmy', 'vlc', r'\bkde\b', 'blender',
    'melonds', r'\bgnu\b', 'marlin', 'dolphin', 'cyanogen', 'proton',
    'gimp', 'libretro', 'debian', 'ubuntu', 'python', r'\barch\b', 'gentoo', 'redox', r'\brust\b', r'\btor\b', 'openbsd', '7zip', 'edopro'
}

anarchists = {
    'chomsky', 'severino di giovanni', 'jacque ellul',
    r'(goldman|red emma)', 'kropotkin', 'bookchin', 'lucy parsons',
    'bakunin', 'graeber', 'salvador segui', 'el noi del sucre',
    'gelderloos', 'tolstoy', 'alice nutter', 'jen angel',
    'margaret sanger', 'abbie hoffman', 'jaron lanier',
    'william powell', 'bhagat singh', 'juan carlos mechoso',
    'malatesta', r'slavoj [zž]i[zž]ek', 'mark fisher',
    'robert evans', r'no gods.? no masters', 'sid vicious',
    r'mah?[kc][hi]?no', 'marvin heemeyer', r'hunter.{0,10}thompson',
    'raul wallenberg', 'alan moore', 'durruti', 'vendetta',
    'jello biafra', 'pink panther gang', 'assange', 'voltairine',
    'laozi', 'greg graffin', 'proudhon', 'technoblade', 'banksy', 'schneeweis', 
    'leopold kohr', 'ricardo flores magon', 'eric hughes', r'thought ?slime',
    'louise michel', 'charlotte wilson', 'ocalan', 'landauer', r'james c. ?scott',
    r'utah.{0,10}phillips', r'katniss.{0,10}everdeen', 'crimew', 'db0', r'abbie.{0,10}hoffman',
    'wilhelm weitling', 'william goodwin', 'radowitzky', 'diogenes', 'woody guthrie.',
    'ken kesey', 'anti-?flag', 'black ?flag', 'dead kennedy', r'(ursula|guin)', 'co-op',
    'gramci', 'john zerzan', r'julio l.pez ch.vez', 'sacco', 'vanzetti', 'kate libby',
    'silvestre revueltas', 'ben reitman', r'bell.{0,10}hooks', 'maria lacerda de moura',
    r'iain.{0,10}banks', 'pat the bunny', 'zoe baker', 'andrewism', r'(danbert nobacon|chumbawamba)', 'lou watts',
    'phineas fisher', r'edward.{0,10}abbey', 'leslie fish', 'rudolf rocker', r'pussy ri[o0]t', 'pekka himanen',
    'albert camus', r'christiani?a', 'howard zinn', r'people.?s history of the (us|united)',
    r'sub.?media', 'oscar wilde', 'crocodilekin', 'gary snyder', 'vaillant', 'stirner',
    r'philip k\.? dick', 'lorax', 'spooner', 'shock doctrine', 'merchants of doubt',
    'margaret killjoy', r'protests.{0,10}portland', r'(mary harris jones|mother jones)', r'lorenzo kom.?boa', 'kim diaz holm', r'marsha johnson', r'ram[oó]n de la sagra', 'carne ross', r'elis[ée]?e reclus', 'osvaldo bayer', 'wright mills', 'art young', 'daniel fraga', 'renzo novatore', 'peter lamborn wilson', 'william godwin', r'cnt.{0,5}fai', 'amir taaki', r'beau of the fifth column|belle of the ranch', 'sam dolgoff', 'halim alrah', 'bellegarrigue'
    

}

fictional = {
    r'(sparrow|johnny depp|pirates.{0,10}car?ribb?ean)', 'luffy', r'(long )?john silver',
    'patchy', 'alestorm', 'borderlands', 'hondo ohnaka', 'steve the pirate', 'edward kenway',
    r'((captain)?.{0,10}hook|peter pan)', r'zero ?cool', 'belters',
    'lechuck', 'gaige', 'arsene lupin', 'lupin iii', 'threepwood',
    r'blau ?b[aä]r', r'captain.{0,10}blood', 'chiching xi', 'pippi longstocking',
    'crunch', r'gary.{0,10}fung', 'judas', 'baba', r'dread ?pirate ?roberts?', 'hunter s. thompson', 'ishikawa goemon', 
    'orlando bloom', r'jack.{0,10}spparo', 'tony bennett', 'triad', r'pont[eé]n',
    'trafalgar d', r'davy.{0,10}jones', r'captain.{0,10}silver', 'captain sticky beard', 'long dong silver',
    'robin hood', 'spongebob', 'vallo', 'saltspite', 'bluebeard', r'(robbie rotten|lazytown)', 'the pirates of penzance'
    
    
}
other = {
    'bernie sanders', 'naomi klein', 'crazy frog', 'john oliver',
    'raoul wallenberg', 'o\'reilly', 'the joker',
    'cereal killer', 'kate middleton', 'ted kaczynski',
    'ozzy osbourne', 'alice cooper', 'murray rothbard', 'christopher hitchens', 
    'andrew mccutcheon', 'milie gillet','tim curry', 'odesseiron', 'mangione', 'project mayhem',
    'raul duke', 'tomas de lezo', 'wozniak', 'kant', 'batman', 'elon musk', 'notch', 'kirk', 'emmanuel goldstein',
    'voltaire', 'dessalines', 'bryan reynolds', 'jakub polak', 'black hawk',
    r'[fp]h?antomas', 'foucalt', r'Anon(ymo?us)?', 'kermit', 'ghandi', r'(satoshi|nakamoto)', 'fawkes', 'timothy leary',
    'openai', 'fixedfun1', "krishnamurthy", 'lina kahn', 'jesus', r'paul.{0,10}burchill', r'(gráinne ní mháille|grace o.malley)', 'eiswuxe', 'neves', 'heart bound', 'piratesoftware', r'neo.{0,20}matrix', 'bob loblaw', 'privacy guides', r'(gabe newell|gaben)', 'antigone', 'dionysius the phocaean'
}

asd = {
  r'\basd\b', r'\baudhd\b', '♾️', r'I.+autistic',
}
adhd = {
  r'\bau?dhd\b', '🦋'
}