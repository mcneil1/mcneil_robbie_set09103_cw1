from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
	return "Home page"

@app.route("/genre/")
def genre():
	return render_template('genre.html')
	

@app.route("/hip_hop/")
def artist():
	return "Artist page"

@app.route("/house/")
def album():
	return "Album page"

@app.route("/RnB/")
def rnb():
	return "Genre page"

@app.route("/indie_rock/")
def date():
	return "Release date page"

@app.route("/hip_hop/brockhampton/iridescence/")
def iridescence():
	album='iridescence'
	artist='BROCKHAMPTON'
	date='21/09/2108'
	cover='https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Brockhampton_Iridescence.jpg/220px-Brockhampton_Iridescence.jpg'
	review='BROCKHAMPTON are back with their fourth studio album "iridescence", their first full length LP since 2017s SATURATION trilogy and the departure of founding member Ameer Vann.\n Iridescence features some gorgeous production value in comparison to some of their earlier work, this is no doubt due to the fact that iridescence was recorded at Abbey Road following their European tour this summer. As any BROCKHAMPTON fan will expect there is a variety of tracks on this album, some songs such as BERLIN feature loud, crunchy basslines with over the top lyrics, while other songs such as TONYA feature beautiful piano melodies and verses from the members. This album also talks about important topics like self-harm, depression and coming to terms with your sexuality. iridescence has some stand-out performances - particularly Joba who once again shows that he is the most versatile member of the group. Other stand out performances come from Merlyn who felt under utilised on past projects and Bearface who no longer feels forgotten and gets a lot more time in the spotlight this time round, he also shows some growth in terms of his material as he seems to be stepping into the rapping along with his other members. With that in mind other members don\'t feature as prominently as I would have liked such as Matt Champion who is one of the more technical and impressive lyricists within the band. Kevin Abstract also seems to have taken a step back on this album. iridescence marks a new trilogy for BROCKHAMPTON and boasts new sounds and ideas from the members, even if they don\'t always land.\n This album impresses me, especially once you learn that it was recorded in 10 days. BROCKHAMPTON show thier usual heart and spirit but in a slightly new way and it  is a step in the right direction for the boyband after their rollercoaster of a year, and hopefully the band can improve upon their new formula on the second and third installments of the Best Years of Our Lives trilogy.'
	rating='86/100'
	tracks=['NEW ORLEANS','THUG LIFE','BERLIN','SOMETHING ABOUT HIM','WHERE THE CASH AT','WEIGHT','DISTRICT','LOOPHOLE','TAPE','J\'OUVERT','HONEY','VIVID','SAN MARCOS','TONYA','FABRIC']
	length='48:49'
	label='RCA'
	genre='Hip Hop'
	return render_template('album.html',album=album,artist=artist,genre=genre ,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)


@app.route("/house/daft_punk/alive/")
def alive():
	album='Alive (2007)'
	artist='Daft Punk'
	date='19/11/2007'
	cover='https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Daft_Punk_Alive_2007.JPG/220px-Daft_Punk_Alive_2007.JPG'
	rating='78/100'
	length='74:04'
	label='Virgin'
	tracks=['Robot Rock / Oh Yeah','Touch It / Technologic','Television Rules the Nation / Crescendolls','Too Long / Steam Machine','Around the World / Harder, Better, Faster, Stronger','Burnin\' / Too Long','Face to Face / Short Circuit','One More Time / Aerodynamic','Aerodynamic Beats / Forget Around the World','The Prime Time of Your Life / The Brainwasher / Rollin\' & Scratchin\' / Alive','Da Funk / Daftendirekt','Superheroes / Human After All / Rock\'n Roll']
	review='Daft Punk deliver one of the most iconic and unforgettable live albums of all time with Alive(2007). No dance artist is more well known and influential than Daft Punk, they boast a massive library of hit songs that even the most casual fans can sing and bop around to, but Alive is much more than just a dance album. The French duo manage to seamlessly blend a massive 26 songs into one continuous mashup. The sound of the crowd mixed with pumping bass lines, steady drumbeats and unforgettable lyrics make this one of Daft Punk\'s most memorable listens that you can revisit to time and time again. Old classics that you thought you knew get a breath of fresh air in Alive and each song is mixed and used flawlessly. Simply put that if you like to dance you will like this album, the old tracks make Alive a classic but the way they\'re used throughout the double LP make it abrand new experience as well. Daft Punk\,s Alive is dance music at it\'s very best.'
	genre='House, French House'
	return render_template('album.html',album=album,genre=genre, artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)
	
@app.route("/RnB/frank_ocean/channel_orange/")
def orange():
	album="Channel Orange"
	artist="Frank Ocean"
	date="10/07/2012"
	cover="https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Channel_ORANGE.jpg/220px-Channel_ORANGE.jpg"
	rating="92"
	length="62:18"
	label="Def Jam"
	tracks=['Start','Thinkin\' Bout You','Fertilizer','Sierra Leone','Sweet Life','Not Just Money','Super Rich Kids ft. Earl Sweatshirt','Pilot Jones','Crack Rock','Pyramids','Lost','White ft. John Mayer','Monks','Bad Religion','Pink Matter ft Andre 3000','Forrest Gump','End']
	genre='R&B, Neo Soul'
	review="Odd Future member Frank Ocean\'s debut solo album, Channel Orange, is about love and life in Los Angeles. Frank Ocean has brought an unconventional musical style to this album, which describes a relationship which he had with a man and is full with emotional, tender and engrossing lyrics over almost sampleless beats across a wide range of styles and influences. The Album is beautiful, and by the end of the record, wich sits at just over an hour long, you'll want to listen to it again and again. The album is great in terms of music production and lyrical production and has excellent replay value. And despite some faults Frank Ocean really shines on Channel Orange, making him one to look out for in the future. Is this album perfect? No, every album has its ups and downs, but Channel Orange proves that Frank Ocean is one of the most exciting artists out in the world today. He is not afraid to talk about the stigmas that he may be subject to in his life - his bisexuality for example - and is taking R&B to heights which it has not reached in years. I'm excited to see what this artist brings to the table in the future, as he has shown here that he doesn't need to be a part of odd future to have a voice,  but for now Channel Orange is a suitable LP to keep your R&B needs at bay." 
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)
	
@app.route("/house/jamie_xx/in_colour/")
def in_colour():
	album="In Colour"
	artist="Jamie xx"
	date="29/05/2015"
	cover="http://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Jamie_xx_-_In_Colour.png/220px-Jamie_xx_-_In_Colour.png"
	rating="87/100"
	length="43:44"
	label="Young Turks"
	tracks=['Gosh','Sleep Sound','SeeSaw ft. Romy','Obvs','Just Saying','Stranger in a Room ft. Oliver Sim','Hold Tight','Loud Places ft. Romy','I Know There\'s Gonna Be (Good Times) ft. Young Thug and Popcaan','The Rest Is Noise','Girl']
	genre="House, Electronica, Rave, Folktronica, UK Garage"
	review="The xx producer and band member Jamie xx's debut solo LP, In Colour, may have taken almost a decade to produce, but you can see why when you give it a listen. In Colour is rich, complex and dazzlingly fluid, listening to it is a pleasure. Jaime brings the excellent sound production that we know and love from his work in the xx and puts it on full display, each song sounds different and unique in its own right, but you'll want to dance to all of them. This album isn't too over the top, the beats are simplistic but beautifully layered with outstanding build-ups that make the final product so enjoyable to listen to. Stand out songs include Loud Places which features Romy, Jaime\'s bandmate from the xx, and the opening track Gosh which features some of the strangest and surreal beats on the album. Overall this album is excellent, listening to each track back-to-back is as enjoyable everytime, In Colour shows what makes one of Jamie xx one of the best producers in dance right now."
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)
	
@app.route("/hip_hop/kids_see_ghosts/kids_see_ghosts/")
def KSG():
	album="Kids See Ghosts"
	artist="Kids See Ghosts"
	date="08/06/2018"
	cover="https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Kids_See_Ghost_Cover.jpg/220px-Kids_See_Ghost_Cover.jpg"
	rating="84/100"
	length="23:53"
	label="Def Jam"
	tracks=['Feel The Love ft. Pusha T','Fire','4th Dimention ft. Louis Prima','Freeee (Ghost Twon, Pt. 2) ft. Ty Dolla Sign','Reborn','Kids See Ghosts ft. Yasiin Bey','Cudi Montage']
	genre='Hip Hop, Psychodelic'
	review='Earlier this year Kanye West dropped his latest solo album \'ye\', and went on to recieve widespread acclaim. Now, Kanye has teamed up with rapper Kid Cudi to form the new hip hop duo \'Kids See Ghosts\'. With only 7 tracks and reaching a total runtime of less than 25 minutes Kids See Ghosts debut self-titled album makes a point to keep things to the point. Some may argue that there isn\'t enough content on this album, and I admit I was also left wanting more after listening to it, but the reason that this album stick out so much is because all 7 tracks are superb. Each song is perfect length and doesn\'t overstay its welcome. Kanye West and Cudi are on top form on this project which is always welcome. Once again Kanye\'s impressive producing skills show through and the album also includes some welcome features such as Ty Dolla Sign and Pusha T. There is a clear psychodelic influence on this album which gives the album a somewhat mellow vibe at times. Kids See Ghosts is definitely one of 2018\'s best hip hop albums, the flow of the album rapid and break-neck at times but each song stands out so much that you forgive the short run time of this excellent album. Hopefully Kanye West can continue his success with his upcoming album \'Yandi\', his third highly anticipated album of the year.'
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)

@app.route("/indie_rock/the_strokes/is_this_it/")
def is_this_it():
	album="Is This It"
	artist="The Strokes"
	date="30/07/2001"
	rating="91/100"
	length="36:28"
	label="RCA"
	genre="Indie Rock, Garage Rock Revival, Post-Punk Revival"
	cover="https://upload.wikimedia.org/wikipedia/en/thumb/0/09/The_Strokes_-_Is_This_It_cover.png/220px-The_Strokes_-_Is_This_It_cover.png"
	tracks=['Is This It','The Modern Age','Some','Barely Legal','Someday','Alone, Together','Last Nite','Hard To Explain','New York City Cops','Trying Your Luck','Take It or Leave It']
	review="The Strokes now iconic debut album is a must have album to own for any Rock fan. Julian Casablancas brings a certain charms and swagger to each song, the basslines are catchy, the drums make you want to tap your feet, and yes the theme of sex, drugs and rock & roll may have been done in the past, but theres something about Is This It which makes it refreshing. This album also contains some essential songs for anybodies music library, Last Nite is a classic, you recognise it as soon as it comes on, and the lyrics are catchy, it's siimply impossible not to sing and dance to. This album just oozes charisma, if you like a single Strokes song then you'll love Is This It. And although the familair themes and formulaic structure of some of the songs make the album feel trite at times you can't deny that it isn't an excellent album thats gone on to inspire many of todays indie rock artists. If you haven't already given this classic a spin then you should definitely add it to your queue, you won't regret it."
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)

@app.route("/indie_rock/the_xx/xx/")
def xx():
	album='xx'
	artist='The xx'
	date='14/07/2009'
	rating='87/100'
	label='Young Turks'
	genre='Indie Rock, Indie Pop, Dream Pop'
	length="38:28"
	cover='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Xx_album_cover.svg/220px-Xx_album_cover.svg.png'
	tracks=['Intro','VCR','Crystalised','Islands','Heart Skipped a Beat','Fantasy','Shelter','Basic Space','Infinity','Night Time','Stars']
	review="South London band The xx's debut album xx features somber moments, fantastic production, moody vocals, twangy guitar strings, big basslines and heart-wrenching lyrics at times. The xx certainly have a sound that is their own and they know that, accross the album there is surprisingly little filler over the 11 tracks, every song feels perfectly realised and tells it's own story. A lot of the themes on this album revolve around struggling in love, and depicts the members talking about previous loves, letting go of ones you love, and still needing someone who no longer needs you. It's a message that's not new but one that everyone can get behind. The album starts off strong which is a fantastic opening track which perfectly sets the tone of the album, Intro doesn't even have any lyrics but its a song I find myself relistening to. Some of the dreamiest moments come from songs like \'Stars\' and \'Fantasy\' which gives us some of the strangest melodies on the project with quiet floaty beats over some fantastic guitar strings. xx is a listening experience from start to finish, it's an easy listening album, none of the music is offensive, it's just a relaxing, chilled out album thats easy to listen to and is one of 2009's best debut albums."
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)

@app.route("/RnB/childish_gambino/awaken_my_love/")
def awaken_my_love():
	album="Awaken, My Love!"
	artist="Childish Gambino"
	date="02/12/2016"
	rating="77/100"
	label="Glassnote"
	genre="R&B, Soul, Funk, Psychadelic"
	length="48:57"
	cover="https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Childish_Gambino_-_Awaken%2C_My_Love%21.png/220px-CHildish_Gambino_-_Awaken%2C_My_Love%21.png"
	tracks=['Me and Your Mama','Have Some Love','Boggieman','Zombies','Riot','Redbone','California','Terrified','Baby Boy','The Night Me and Your Momma Met','Stand Tall']
	review="Donald Glover, AKA Childish Gambino, makes an unexpected yet welcome transition into the world of R&B, Soul and Funk on his third album 'Awaken, My Love!'. Being compared to the likes on Prince on this album you quickly realise that this is not like Glovers' past two albums 'Camp' and 'Because the Internet' which are both deeply rooted in the hip-hop genre. Although his past albums did enjoy moderate success from critics and fans alike they did feel a bit stagnent and over the top at times. Here, on the other hand, Glover seems to fit in perfectly. The combination of Glovers fantastic vocal work mixed with dreamy, spacey, surreal background beats is almost heavenly at times. This makes for some very sweet and intimate moments on the album like on 'The Night Me and Your Momma Met' and the hit single 'Redbone' which seemed to take the world by storm, and for good reason. The song is one of Glovers best and shows how wide his vocal range is. Overall the album features great music production, even if the lyrics can feel lazy, tired and leave you wanting more, 'Awaken, My Love!' is still a very beautiful and dreamy album that truly shows that Donald Glover will seemingly succeed in every project he works on."
	return render_template('album.html',genre=genre,album=album,artist=artist,date=date,cover=cover,review=review,rating=rating,tracks=tracks,length=length,label=label)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

