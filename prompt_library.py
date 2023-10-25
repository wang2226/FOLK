cot_decompose_with_answer = """
Please tell me the necessary questions that need to be answered in order to verify the following claim:

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.
>>>>>>
Followup Question: Where is Howard Hospital located?
Answer: Howard Hospital is located in Washington D.C.
Followup Question: Where is Providence Hospital located? 
Answer: Providence Hospital is located in Washington D.C.
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.
>>>>>>
Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Answer: The Super Aguri Honda SA07 is the car that has participated at the Formula 1 World Championship in 2007. The car was designed by Peter McCool.
Followup Question: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
Answer: Yes. Takuma Sato drove the Super Aguri Honda SA07 during the 20078 Formula One season.
------
Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.
>>>>>>
Followup Question: When did Sumo wrestler Toyozakura Toshiaki ended his career?
Answer: Toyozakura was one of 23 wrestlers found guilty of fixing the result of bouts after an investigation by the Japan Sumo Association, and he was forced to retire in April 2011.
Followup Question: What is Toyozakura Toshiaki's occupation?
Answer: Toyozakura Toshiaki is a former sumo wrestler from Hiroshima, Japan.
Followup Question: Did Sumo wrestler Toyozakura Toshiaki committed match-fixing?
Answer: In the end, 23 wrestlers in total were judged guilty of match-fixing and all were expelled.
------
Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.
>>>>>>
Followup Question: When was Alfredo Cornejo Cuevas born?
Answer: Alfredo Cornejo Cuevas (June 6, 1933 to August 15, 2021) was a Chilean boxer,
Followup Question: Did Alfredo Cornejo Cuevas win the gold metal in the welterweight division at the Pan American Games in 1959?
Answer: Alfredo Cornejo Cuevas (June 6, 1933 to August 15, 2021) was a Chilean boxer, who won the gold medal in the welterweight division at the 1959 Pan American Games
Followup Question: Where was The Pan American Games in 1959 held?
Answer: Sixty years ago, the third Pan American Games were held in Chicago from August 27 to September 7.
Followup Question: Did Alfredo Cornejo Cuevas win the world amateur welterweight title in Mexico City?
Answer: In the same year he also won the world amateur welterweight title in Mexico City.
------
Claim: %s
>>>>>>
"""

cot_decompose = """
Please tell me the necessary questions that need to be answered in order to verify the following claim:

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.
>>>>>>
Followup Question: Where is Howard Hospital located?
Followup Question: Where is Providence Hospital located? 
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.
>>>>>>
Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Followup Question: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
------
Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.
>>>>>>
Followup Question: When did Sumo wrestler Toyozakura Toshiaki ended his career?
Followup Question: What is Toyozakura Toshiaki's occupation?
Followup Question: Did Sumo wrestler Toyozakura Toshiaki committed match-fixing?
------
Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.
>>>>>>
Followup Question: When was Alfredo Cornejo Cuevas born?
Followup Question: Did Alfredo Cornejo Cuevas win the gold metal in the welterweight division at the Pan American Games in 1959?
Followup Question: Where was The Pan American Games in 1959 held?
Followup Question: Did Alfredo Cornejo Cuevas win the world amateur welterweight title in Mexico City?
------
Claim: %s
>>>>>>
"""

logic_decompose_with_answers = """
You are given a problem description and a claim. The task is to:
1) define all the predicates in the claim
2) parse the predicates into followup questions
3) answer the followup questions

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.
>>>>>>
Predicates:
Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Location(Providence Hospital, Washington D.C.) ::: Verify Providence Hospital is located in Washington, D.C.

Followup Question: Where is Howard Hospital located?
Answer: Howard Hospital is located in Washington D.C.
Followup Question: Where is Providence Hospital located? 
Answer: Providence Hospital is located in Washington D.C.
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.
>>>>>>
Predicates: 
Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
Drive(An IndyCar race driver, a Formula 1 car) ::: Verify an IndyCar driver drove a Formula 1 car.

Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Answer: The Super Aguri Honda SA07 is the car that has participated at the Formula 1 World Championship in 2007. The car was designed by Peter McCool.
Followup Question: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
Answer: Yes. Takuma Sato drove the Super Aguri Honda SA07 during the 20078 Formula One season.
------
Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead
>>>>>>
Predicates: 
Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.
Won(Colson Whitehead, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Colson Whitehead has won.

Followup Question: How many Pulitzer Prize did Thomas Loren Friedman win?
Answer: Friedman has won the Pulitzer Prize three times.
Followup Question: How many Pulitzer Prize did Colson Whitehead win?
Answer: Whitehead has won the Pulitzer Prize two times.
------
Claim: SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia.
>>>>>>
Predicates:
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) ::: Verify that SkyHigh Mount Dandenong is located on top of Mount Dandenong, Victoria, Australia.
Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) ::: Verify that SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.

Followup Question: Where is SkyHigh Mount Dandenong located?
Answer: SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia.
Followup Question: Was SkyHigh Mount Dandenong formerly known as Mount Dandenong Observatory? 
Answer: the name officially being changed from "Mount Dandenong Observatory" to the current "SkyHigh Mount Dandenong".
------
Claim: Shulin, a 33.1288 km (12.7911 sq mi) land located in New Taipei City, China, a country in East Asia, has a total population of 183,946 in December 2018.
>>>>>>
Predicates: 
Location(Shulin, New Taipei City, Chian) ::: Verify that Shulin is located in New Taipei City, China.
Population(Shulin, 183,946) ::: Verify that Shulin has a total population of 183,946 in December 2018.

Followup Question: Where is Shulin located?
Answer: Shulin is located in Taiwan. Shulin. Location within Taiwan ; Shulin is located in Taiwan. Shulin. Location within Taiwan ...
Followup Question: What is the population of Shulin?
Answer: Shulin has a total population of around 184,400.
------
Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.
>>>>>>
Predicates: 
Ending(Toyozakura Toshiaki, his career in 2011) ::: Verify that Toyozakura Toshiaki ended his career in 2011.
Occupation(Toyozakura Toshiaki, sumo wrestler) ::: Verify that Toyozakura Toshiaki is a sumo wrestler.
Commit(Toyozakura Toshiaki, match-fixing) ::: Verify that Toyozakura Toshiaki committed match-fixing.

Followup Question: When did Sumo wrestler Toyozakura Toshiaki ended his career?
Answer: Toyozakura was one of 23 wrestlers found guilty of fixing the result of bouts after an investigation by the Japan Sumo Association, and he was forced to retire in April 2011.
Followup Question: What is Toyozakura Toshiaki's occupation?
Answer: Toyozakura Toshiaki is a former sumo wrestler from Hiroshima, Japan.
Followup Question: Did Sumo wrestler Toyozakura Toshiaki committed match-fixing?
Answer: In the end, 23 wrestlers in total were judged guilty of match-fixing and all were expelled.
------
Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.
>>>>>>
Predicates: 
Born(Alfredo Cornejo Cuevas, June 6 1933) ::: Verify that Alfredo Cornejo Cuevas was born June 6 1933. 
Won(Alfredo Cornejo Cuevas, the gold metal in the welterweight division at the Pan American Games in 1959) ::: Verify that Alfredo Cornejo Cuevas won the gold metal in the welterweight division at the Pan American Games in 1959.
Held(The Pan American Games in 1959, Chicago United States) ::: Verify that The Pan American Games in 1959 was held in Chicago United States.
Won(Alfredo Cornejo Cuevas, the world amateur welterweight title in Mexico City).

Followup Question: When was Alfredo Cornejo Cuevas born?
Answer: Alfredo Cornejo Cuevas (June 6, 1933 to August 15, 2021) was a Chilean boxer,
Followup Question: Did Alfredo Cornejo Cuevas win the gold metal in the welterweight division at the Pan American Games in 1959?
Answer: Alfredo Cornejo Cuevas (June 6, 1933 to August 15, 2021) was a Chilean boxer, who won the gold medal in the welterweight division at the 1959 Pan American Games
Followup Question: Where was The Pan American Games in 1959 held?
Answer: Sixty years ago, the third Pan American Games were held in Chicago from August 27 to September 7.
Followup Question: Did Alfredo Cornejo Cuevas win the world amateur welterweight title in Mexico City?
Answer: In the same year he also won the world amateur welterweight title in Mexico City.
------
Claim: The birthplace of American engineer Alfred L.Rives is a plantation near Monticello, the primary residence of Thomas Jefferson.
>>>>>>
Predicates:
Birthplace(Alfred L. Rives, a plantation) ::: Verify The birthplace of American engineer Alfred L.Rives is a plantation
Primary residence(Thomas Jefferson, Monticello) ::: Verify Monticello, the primary residence of Thomas Jefferson. 
Near(a planation, Monticello) ::: Verify A plantation is near Monticello

Followup Question: Where is the birthplace of Alfred L. Rives? 
Answer:  The birthplace of Alfred L. Rives is Castle Hill in Virginia 
Followup Question: Where is the primary residence of Thomas Jefferson? 
Answer:  The primary residence of Thomas Jefferson is Monticello 
Followup Question: Is the birthplace of Alfred L. Rives near the residence of Thomas Jefferson? 
Answer:  Yes, Castle Hill is near Monticello.
------
Claim: %s
>>>>>>
"""

logic_decompose = """
You are given a problem description and a claim. The task is to:
1) define all the predicates in the claim
2) parse the predicates into followup questions
3) answer the followup questions

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.
>>>>>>
Predicates:
Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Location(Providence Hospital, Washington D.C.) ::: Verify Providence Hospital is located in Washington, D.C.

Followup Question: Where is Howard Hospital located?
Followup Question: Where is Providence Hospital located? 
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.
>>>>>>
Predicates: 
Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
Drive(An IndyCar race driver, a Formula 1 car) ::: Verify an IndyCar driver drove a Formula 1 car.

Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Followup Question: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season?
------
Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead
>>>>>>
Predicates: 
Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.
Won(Colson Whitehead, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Colson Whitehead has won.

Followup Question: How many Pulitzer Prize did Thomas Loren Friedman win?
Followup Question: How many Pulitzer Prize did Colson Whitehead win?
------
Claim: SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia.
>>>>>>
Predicates:
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) ::: Verify that SkyHigh Mount Dandenong is located on top of Mount Dandenong, Victoria, Australia.
Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) ::: Verify that SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.

Followup Question: Where is SkyHigh Mount Dandenong located?
Followup Question: Was SkyHigh Mount Dandenong formerly known as Mount Dandenong Observatory? 
------
Claim: Shulin, a 33.1288 km (12.7911 sq mi) land located in New Taipei City, China, a country in East Asia, has a total population of 183,946 in December 2018.
>>>>>>
Predicates: 
Location(Shulin, New Taipei City, Chian) ::: Verify that Shulin is located in New Taipei City, China.
Population(Shulin, 183,946) ::: Verify that Shulin has a total population of 183,946 in December 2018.

Followup Question: Where is Shulin located?
Followup Question: What is the population of Shulin?
------
Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.
>>>>>>
Predicates: 
Ending(Toyozakura Toshiaki, his career in 2011) ::: Verify that Toyozakura Toshiaki ended his career in 2011.
Occupation(Toyozakura Toshiaki, sumo wrestler) ::: Verify that Toyozakura Toshiaki is a sumo wrestler.
Commit(Toyozakura Toshiaki, match-fixing) ::: Verify that Toyozakura Toshiaki committed match-fixing.

Followup Question: When did Sumo wrestler Toyozakura Toshiaki ended his career?
Followup Question: What is Toyozakura Toshiaki's occupation?
Followup Question: Did Sumo wrestler Toyozakura Toshiaki committed match-fixing?
------
Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.
>>>>>>
Predicates: 
Born(Alfredo Cornejo Cuevas, June 6 1933) ::: Verify that Alfredo Cornejo Cuevas was born June 6 1933. 
Won(Alfredo Cornejo Cuevas, the gold metal in the welterweight division at the Pan American Games in 1959) ::: Verify that Alfredo Cornejo Cuevas won the gold metal in the welterweight division at the Pan American Games in 1959.
Held(The Pan American Games in 1959, Chicago United States) ::: Verify that The Pan American Games in 1959 was held in Chicago United States.
Won(Alfredo Cornejo Cuevas, the world amateur welterweight title in Mexico City).

Followup Question: When was Alfredo Cornejo Cuevas born?
Followup Question: Did Alfredo Cornejo Cuevas win the gold metal in the welterweight division at the Pan American Games in 1959?
Followup Question: Where was The Pan American Games in 1959 held?
Followup Question: Did Alfredo Cornejo Cuevas win the world amateur welterweight title in Mexico City?
------
Claim: The birthplace of American engineer Alfred L.Rives is a plantation near Monticello, the primary residence of Thomas Jefferson.
>>>>>>
Predicates:
Birthplace(Alfred L. Rives, a plantation) ::: Verify The birthplace of American engineer Alfred L.Rives is a plantation
Primary residence(Thomas Jefferson, Monticello) ::: Verify Monticello, the primary residence of Thomas Jefferson. 
Near(a planation, Monticello) ::: Verify A plantation is near Monticello

Followup Question: Where is the birthplace of Alfred L. Rives? 
Followup Question: Where is the primary residence of Thomas Jefferson? 
Followup Question: Is the birthplace of Alfred L. Rives near the residence of Thomas Jefferson? 
------
Claim: %s
>>>>>>
"""

logic_decompose_old = """
You are given a problem description and a claim. The task is to:
1) define all the predicates in the claim
2) parse the predicates into followup questions
3) answer the followup questions

Claim: Howard University Hospital and Providence Hospital are both located in Washington, D.C.
>>>>>>
Predicates:
Location(Howard Hospital, Washington D.C.) # Verify Howard University Hospital is located in Washington, D.C.
Location(Providence Hospital, Washington D.C.) # Verify Providence Hospital is located in Washington, D.C.

Followup Question: Where is Howard Hospital located?
Followup Question: Where is Providence Hospital located? 
------
Claim: WWE Super Tuesday took place at an arena that currently goes by the name TD Garden.
>>>>>>
Predicates: 
Took place(WWE Super Tuesday, {an arena}) # Verify WWE Super Tuesday took place at {an arena}.
Known({an arena}, TD Garden) # Verify {an arena} currently goes by the name TD Garden.

Followup Question: Which arena the WWE Super Tuesday took place?
Followup Question: Does {an arena} currently goes by the name TD Garden?
------
Claim: An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season.
>>>>>>
Predicates: 
Designed(Peter McCool, {a Formula 1 car}) # Verify {a Formula 1 car} was designed by Peter McCool druing the 2007 Formula One season.
Drive(An IndyCar race driver, {a Formula 1 car}) # Verify An Indycar race driver drove {a Formula 1 car}.

Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season?
Followup Question: Did an IndyCar race driver drove {a Formula 1 car}?
------
Claim: Gina Bramhill was born in a village. The 2011 population of the area that includes this village was 167,446.
>>>>>>
Predicates: 
Born(Gina Bramhill, {a village}) # Verify Gina Bramhill was born in {a village}.
Population({a village}, 167, 446) # Verify the 2011 population of the area that includes this village was 167,446.

Followup Question: Which village was Gina Bramhill born in?
Followup Question: Was the 2011 population of the area that includes {a village} 167,446?
------
Claim: Don Ashley Turlington graduated from Saint Joseph's College, a private Catholic liberal arts college in Standish.
>>>>>>
Predicates: 
Graduate(Don Ashley Turlington, Saint Joseph's College) # Verify Ashley Turlington graduated from Saint Joseph's College.
Is(Saint Joseph's College, a private Catholic liberal arts college in Standish) # Verify Saint Joseph's College is a private Catholic liberal arts college in Standish

Followup Question: Did Don Ashley Turlington graduate from Saint Joseph's College?
Followup Question: Is Saint Joseph's College a private Catholic liberal arts college in Standish?
------
Claim: %s
>>>>>>
"""

direct_aggregate = """
Please verify the following claim and provide explanations:

Claim: The woman the story behind Girl Crazy is credited to is older than Ted Kotcheff.
>>>>>>
This claim is: [NOT_SUPPORTED]
Here are the reasons: The woman behind the story Girl Crazy is Hampton Del Ruth, who was born on September 7, 1879.
Ted Kotcheff was born on April 7, 1931. Hapmpton Del Ruth is not older than Ted Kotcheff.
------
Claim: A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area.
>>>>>>
This claim is: [NOT_SUPPORTED]
Here are the reasons: Madison Square Garden is the home to New York Rangers and New York Islanders. Both are popular in the New York metropolitan area.
Madison Square Garden has a capacity of 19,500, not 70,0000.
------
Claim: The writer of the song Girl Talk and Park So-yeon have both been members of a girl group.
>>>>>>
This claim is: [SUPPORTED]
Here are the reasons: Tionne Watkins is the writer of the song Girl Talk. She was a member of the girl-group TLC.
Park So-yeon is part of a girl group. Therefore, both Tioone Watkins and Park So-yeon have been members of a girl group.
------
Claim: Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany.
>>>>>>
This claim is: [SUPPORTED]
Here are the reasons: Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Frankfurt is in the German state of Hesse and the fifth-largest city in Germany.
------
Claim: %s
>>>>>>
"""

cot_aggregate = """
Answer the following SUPPORTED / NOT_SUPPORTED questions:

Is it true that The woman the story behind Girl Crazy is credited to is older than Ted Kotcheff. ?
Let's think step by step.

Girl Crazy 's story is credited to Hampton Del Ruth.
Hampton Del Ruth was born on September 7 , 1879.
Ted Kotcheff was born on April 7 , 1931.
>>>>>>
Therefore , the answer is: [NOT_SUPPORTED]
Here are the reasons: The woman behind the story Girl Crazy is Hampton Del Ruth, who was born on September 7, 1879.
Ted Kotcheff was born on April 7, 1931. Hapmpton Del Ruth is not older than Ted Kotcheff.
------
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area. ?
Let's think step by step.

Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League.
Madison Square Garden has a capacity of 19.500.
The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
>>>>>>
Therefore, the answer is: [NOT_SUPPORTED]
Here are the reasons: Madison Square Garden is the home to New York Rangers and New York Islanders. Both are popular in the New York metropolitan area.
Madison Square Garden has a capacity of 19,500, not 70,0000.
------
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group. ?
Let's think step by step.

Tionne Watkins is the writer of the song Girl Talk.
Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
Therefore, the answer is: [SUPPORTED]
Here are the reasons: Tionne Watkins is the writer of the song Girl Talk. She was a member of the girl-group TLC.
Park So-yeon is part of a girl group. Therefore, both Tioone Watkins and Park So-yeon have been members of a girl group.
------
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany. ?
Let's think step by step.

Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Frankfurt is in the German state of Hesse.
Frankfurt is the fifth-largest city in Germany.
>>>>>>
Therefore, the answer is: [SUPPORTED]
Here are the reasons: Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Frankfurt is in the German state of Hesse and the fifth-largest city in Germany.
------
Is it true that %s?
Let's think step by step:

%s
>>>>>>
"""

self_ask_aggregate = """
Given a question and a context, provide a SUPPORTED or NOT_SUPPORTED and explain why.

Question: 
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group. ?

Context:
Who is the writer of the song Girl Talk? Tionne Watkins is the writer of the song Girl Talk.
Is Park So-yeon a member of a girl group? Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Is the writer of the song Girl Talk a member of a girl group? Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
The claim is [SUPPORTED]. Here are the reasons, Tionne Watkins is the writer of the song Girl Talk, and she fame in the early 1990s as a member of the girl-group TLC.
Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area. ?

Context:
Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
The claim is [NOT_SUPPORTED]. Here are the reasons, Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League.
and the New York Islanders are a professional ice hockey team based in Elmont, New York. Madison Square Garden has a capacity of 19.500, not 70,000.
------
Question: 
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany. ?

Context:
Where was Werner Gunter Jaff\u00e9 Fellner born? Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Which state is Frankfurt in? Frankfurt is in the German state of Hesse.
>>>>>>
The claim is [SUPPORTED]. Here are the reasons, Werner Gunter JafFf\u00e9 Fellner was born in Frankfurt and Frankfurt is in the German state of Hesse.
------
Question:
Is it true that The American lyricist Tom Jones,  born in 1928, co-authored the screenplay for the musical film The Fantastics. ?

Context:
When was Tom Jones born? Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
What is Tome Jones nationality? Sir Thomas Jones Woodward OBE is a Welsh singer. 
Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
>>>>>>
The claim is [NOT_SUPPORTED]. Here are the reasons, Sir Thomas Jones Woodward OBE is a Welsh singer and Tome Jones co-authored the musical film The Fantastics,
but Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940. Thomas Jones is British, not American.
------
Question: Is it true that %s?

Context: 
%s
>>>>>>
"""


logic_aggregate_old_1 = """
Given a question and a context, provide a Yes or No answer and explain why.

Question: 
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group.?

Context:
Write(the writer, the song Girl Talk) ::: Verify that the writer of the song Girl Talk
Member(Park So-yeon, a girl group) ::: Verify that Park So-yeon is a memeber of a girl group
Member(the writer, a girl group) ::: Verify that the writer of the song Girl Talk is a member of a gril group

Who is the writer of the song Girl Talk? Tionne Watkins is the writer of the song Girl Talk.
Is Park So-yeon a member of a girl group? Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Is the writer of the song Girl Talk a member of a girl group? Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
Answer:
Write(the writer, the song Girl Talk) is True because Tionne Watkins is the writer of the song Girl Talk.
Member(Park So-yeon, a girl group) is True because Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Member(the writer, a girl group) is True because Watkins rose to fame in the early 1990s as a member of the girl-group TLC
Write(the writer, the song Girl Talk) && Member(Park So-yeon, a girl group) && Member(the writer, a girl group) is True.
So the answer is: Yes.
Therefore, the claim is [SUPPORTED].
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area.?

Context:
Home(a hocky team, Madison Square Garden) ::: Verify that a hockey team calls Madison Square Garden its home.
Capacity(Madison Square Garden, 70,000) ::: Verify that Madison Square Garden has capacity of 70,000.
Popular(New York Islanders, New York Metropolitan area) ::: Verify that New York Islanders are popular in the New York metropolitan area.

Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
Answer:
Home(a hocky team, Madison Square Garden) is True because Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
Capacity(Madison Square Garden, 70,000) is False because Madison Square Garden has a capacity of 19.500.
Popular(New York Islanders, New York Metropolitan area) is True because The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
Home(a hocky team, Madison Square Garden) && Capacity(Madison Square Garden, 70,000) && Popular(New York Islanders, New York Metropolitan area) is False.
So the answer is: No.
Therefore, the claim is [NOT_SUPPORTED].
------
Question: 
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany.?

Context:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt)
State(Frankfurt, the German state of Hesse)

Where was Werner Gunter Jaff\u00e9 Fellner born? Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Which state is Frankfurt in? Frankfurt is in the German state of Hesse.
>>>>>>
Answer:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) is True because Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
State(Frankfurt, the German state of Hesse) is True because Frankfurt is in the German state of Hesse.
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) && State(Frankfurt, the German state of Hesse) is True.
So the answer is: Yes.
Therefore, the claim is [SUPPORTED].
------
Question:
Is it true that The American lyricist Tom Jones,  born in 1928, co-authored the screenplay for the musical film The Fantastics.?

Context:
Born(Tom Jones, 1928)
Nationality(Tom Jones, American)
Co-author(Tome Jones, the musical film The Fantastics)

When was Tom Jones born? Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
What is Tome Jones nationality? Sir Thomas Jones Woodward OBE is a Welsh singer. 
Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
>>>>>>
Answer:
Born(Tom Jones, 1928) is False because Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
Nationality(Tom Jones, American) is False because Sir Thomas Jones Woodward OBE is a Welsh singer. 
Co-author(Tome Jones, the musical film The Fantastics) is True because Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
Born(Tom Jones, 1928) && Nationality(Tom Jones, American) && Co-author(Tome Jones, the musical film The Fantastics) is False.
So the answer is: No.
Therefore, the claim is [NOT_SUPPORTED].
------
Question: Is it true that %s?

Context: 
%s
>>>>>>
"""

logic_aggregate_old_2 = """
Given a question and a context, provide a Yes or No answer and explain why.

Question: 
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group.?

Context:
Write(the writer, the song Girl Talk) ::: Verify that the writer of the song Girl Talk
Member(Park So-yeon, a girl group) ::: Verify that Park So-yeon is a memeber of a girl group
Member(the writer, a girl group) ::: Verify that the writer of the song Girl Talk is a member of a gril group

Who is the writer of the song Girl Talk? Tionne Watkins is the writer of the song Girl Talk.
Is Park So-yeon a member of a girl group? Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Is the writer of the song Girl Talk a member of a girl group? Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
Answer:
Write(Tionne Watkins, the song Girl Talk) is True because Tionne Watkins is the writer of the song Girl Talk.
Member(Park So-yeon, a girl group) is True because Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Member(Tionne Watkins, a girl group) is True because Watkins rose to fame in the early 1990s as a member of the girl-group TLC
Write(Tionne Watkins, the song Girl Talk) && Member(Park So-yeon, a girl group) && Member(Tionne Watkins, a girl group) is True.
So the answer is: Yes.
Therefore, the claim is [SUPPORTED].
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area.?

Context:
Home(a hocky team, Madison Square Garden) ::: Verify that a hockey team calls Madison Square Garden its home.
Capacity(Madison Square Garden, 70,000) ::: Verify that Madison Square Garden has capacity of 70,000.
Popular(New York Islanders, New York Metropolitan area) ::: Verify that New York Islanders are popular in the New York metropolitan area.

Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
Answer:
Home(New York Rangers, Madison Square Garden) is True because Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
Capacity(Madison Square Garden, 70,000) is False because Madison Square Garden has a capacity of 19.500.
Popular(New York Islanders, New York Metropolitan area) is True because The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
Home(New York Rangers, Madison Square Garden) && Capacity(Madison Square Garden, 70,000) && Popular(New York Islanders, New York Metropolitan area) is False.
So the answer is: No.
Therefore, the claim is [NOT_SUPPORTED].
------
Question: 
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany.?

Context:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt)
State(Frankfurt, the German state of Hesse)

Where was Werner Gunter Jaff\u00e9 Fellner born? Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Which state is Frankfurt in? Frankfurt is in the German state of Hesse.
>>>>>>
Answer:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) is True because Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
State(Frankfurt, the German state of Hesse) is True because Frankfurt is in the German state of Hesse.
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) && State(Frankfurt, the German state of Hesse) is True.
So the answer is: Yes.
Therefore, the claim is [SUPPORTED].
------
Question:
Is it true that The American lyricist Tom Jones,  born in 1928, co-authored the screenplay for the musical film The Fantastics.?

Context:
Born(Tom Jones, 1928)
Nationality(Tom Jones, American)
Co-author(Tome Jones, the musical film The Fantastics)

When was Tom Jones born? Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
What is Tome Jones nationality? Sir Thomas Jones Woodward OBE is a Welsh singer. 
Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
>>>>>>
Answer:
Born(Tom Jones, 1928) is False because Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
Nationality(Tom Jones, American) is False because Sir Thomas Jones Woodward OBE is a Welsh singer. 
Co-author(Tome Jones, the musical film The Fantastics) is True because Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
Born(Tom Jones, 1928) && Nationality(Tom Jones, American) && Co-author(Tome Jones, the musical film The Fantastics) is False.
So the answer is: No.
Therefore, the claim is [NOT_SUPPORTED].
------
Question: Is it true that %s?

Context: 
%s
>>>>>>
"""

logic_aggregate = """
Given a question and a context, provide a [SUPPORTED] or [NOT_SUPPORTED] answer and explain why.

Question: 
Is it true that The writer of the song Girl Talk and Park So-yeon have both been members of a girl group.?

Context:
Write(the writer, the song Girl Talk) ::: Verify that the writer of the song Girl Talk
Member(Park So-yeon, a girl group) ::: Verify that Park So-yeon is a memeber of a girl group
Member(the writer, a girl group) ::: Verify that the writer of the song Girl Talk is a member of a gril group

Who is the writer of the song Girl Talk? Tionne Watkins is the writer of the song Girl Talk.
Is Park So-yeon a member of a girl group? Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Is the writer of the song Girl Talk a member of a girl group? Watkins rose to fame in the early 1990s as a member of the girl-group TLC
>>>>>>
Prediction:
Write(Tionne Watkins, the song Girl Talk) is True because Tionne Watkins is the writer of the song Girl Talk.
Member(Park So-yeon, a girl group) is True because Park Soyeon is a South Korean singer. She is a former member of the kids girl group I& Girls.
Member(Tionne Watkins, a girl group) is True because Watkins rose to fame in the early 1990s as a member of the girl-group TLC
Write(Tionne Watkins, the song Girl Talk) && Member(Park So-yeon, a girl group) && Member(Tionne Watkins, a girl group) is True.
The claim is [SUPPORTED].

Explanation:
Tionne Watkins, a member of the girl group TLC in the 1990s, is the writer of the song "Girl Talk." 
Park Soyeon, a South Korean singer, was formerly part of the girl group I& Girls. 
Therefore, both Watkins and Park Soyeon have been members of girl groups in their respective careers.
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area.?

Context:
Home(a hocky team, Madison Square Garden) ::: Verify that a hockey team calls Madison Square Garden its home.
Capacity(Madison Square Garden, 70,000) ::: Verify that Madison Square Garden has capacity of 70,000.
Popular(New York Islanders, New York Metropolitan area) ::: Verify that New York Islanders are popular in the New York metropolitan area.

Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
Prediction:
Home(New York Rangers, Madison Square Garden) is True because Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
Capacity(Madison Square Garden, 70,000) is False because Madison Square Garden has a capacity of 19.500.
Popular(New York Islanders, New York Metropolitan area) is True because The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
Home(New York Rangers, Madison Square Garden) && Capacity(Madison Square Garden, 70,000) && Popular(New York Islanders, New York Metropolitan area) is False.
The claim is [NOT_SUPPORTED].

Explanation:
The New York Rangers, along with the New York Islanders and the New Jersey Devils, are popular National Hockey League (NHL) teams in the New York metropolitan area. 
Madison Square Garden, a well-known venue in New York City, has a capacity of approximately 19,500, not 70,000.
------
Question: 
Is it true that Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt in the German state of Hesse and the fifth-largest city in Germany.?

Context:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt)
State(Frankfurt, the German state of Hesse)

Where was Werner Gunter Jaff\u00e9 Fellner born? Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
Which state is Frankfurt in? Frankfurt is in the German state of Hesse.
>>>>>>
Prediction:
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) is True because Werner Gunter Jaff\u00e9 Fellner was born in Frankfurt.
State(Frankfurt, the German state of Hesse) is True because Frankfurt is in the German state of Hesse.
Born(Werner Gunter Jaff\u00e9 Fellner, Frankfurt) && State(Frankfurt, the German state of Hesse) is True.
The claim is [SUPPORTED].

Explanation:
Werner Gunter Jaffé Fellner was born in Frankfurt, which is both in the German state of Hesse and the fifth-largest city in Germany.
------
Question:
Is it true that The American lyricist Tom Jones,  born in 1928, co-authored the screenplay for the musical film The Fantastics.?

Context:
Born(Tom Jones, 1928)
Nationality(Tom Jones, American)
Co-author(Tome Jones, the musical film The Fantastics)

When was Tom Jones born? Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
What is Tome Jones nationality? Sir Thomas Jones Woodward OBE is a Welsh singer. 
Who co-author the musical film The Fantastics? Tome Jones co-authored the musical film The Fantastics.
>>>>>>
Prediction:
Born(Tom Jones, 1928) is False because Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940
Nationality(Tom Jones, American) is False because Thomas Jones Woodward is a British singer. 
Co-author(Tome Jones, the musical film The Fantastics) is True because Tome Jones co-authored the musical film The Fantastics.
Born(Tom Jones, 1928) && Nationality(Tom Jones, American) && Co-author(Tome Jones, the musical film The Fantastics) is False.
The claim is [NOT_SUPPORTED].

Explanation:
Thomas Jones Woodward was born in Pontypridd, South Wales, Great Britain on June 7, 1940. He is a british singer.
Thomas Jones co-authored the musical film The Fantastics.
------
Question: Is it true that %s?

Context: 
%s
>>>>>>
"""


logic_aggregate_old = """
Given a question and a context, provide a [SUPPORTED] or [NOT_SUPPORTED] answer and explain why.

Question: 
Is it true that Howard University Hospital and Providence Hospital are both located in Washington, D.C. ?

Context:
Location(Howard Hospital, Washington D.C.) ::: Verify Howard University Hospital is located in Washington, D.C.
Location(Providence Hospital, Washington D.C.) ::: Verify Providence Hospital is located in Washington, D.C.

Followup Question: Where is Howard Hospital located? Howard University Hospital is located at 2041 Georgia Avenue NW, Washington, DC.
Followup Question: Where is Providence Hospital located? Providence St. Vincent's Hospital located in Portland, Oregon.
>>>>>>
Prediction:
Location(Howard Hospital, Washington D.C.) is True because Howard University Hospital is located in Washington D.C.
Location(Providence Hospital, Washington D.C.) is False because Providence Hospital is located in Portland, Oregon.
Location(Howard Hospital, Washington D.C.) && Location(Providence Hospital, Washington D.C.) is False.
The claim is [NOT_SUPPORTED].

Explanation:
Howard University Hospital is located in Washington D.C.
Providence Hospital is located in Portland, Oregon.
Therefore, while Howard University Hospital is indeed located in Washington, D.C., Providence Hospital is not located there. 
Providence Hospital is actually located in Portland, Oregon.
------
Question:
Is it true that An IndyCar race driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season. ?

Context:
Designed(Peter McCool, a Formula 1 car) ::: Verify a Formula 1 car was designed by Peter McCool during the 2007 Formula One season.
Drive(An IndyCar race driver, a Formula 1 car) ::: Verify an IndyCar driver drove a Formula 1 car.

Followup Question: Which Formula 1 car was designed by Peter McCool during the 2007 Formula One season? The Super Aguri SA07 was designed by Peter McCool.
Followup Question: Did an IndyCar driver drove a Formula 1 car designed by Peter McCool during the 2007 Formula One season? The Super Aguri SA07 was Super Aguri F1's Formula One car for the 2007 Formula One season. It was designed by Peter McCool and was driven by Takuma Sato and ...
>>>>>>
Prediction:
Designed(Peter McCool, a Formula 1 car) is True because The Super Aguri SA07 was designed by Peter McCool.
Drive(An IndyCar race driver, a Formula 1 car) is True because The Super Aguri SA07 was Super Aguri F1's Formula One car for the 2007 Formula One season. It was designed by Peter McCool and was driven by Takuma Sato and ...
Designed(Peter McCool, a Formula 1 car) && Drive(An IndyCar race driver, a Formula 1 car) is True.
The claim is [SUPPORTED].

Explanation:
The Super Aguri SA07 was Super Aguri F1's Formula One car for the 2007 Formula One season. It was designed by Peter McCool and was driven by Takuma Sato.
Therefore, an IndyCar race driver, named Takuma Sato drove Super Aguri F1's Formula One car that was designed by Peter McCool.
------
Question:
Is it true that Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead. ?

Context:
Won(Thomas Loren Friedman, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Thomas Loren Friedman has won.
Won(Colson Whitehead, Pulitzer Prize) ::: Verify the number of Pulitzer Prizes Colson Whitehead has won.

Followup Question: How many Pulitzer Prize did Thomas Loren Friedman win? He is a three-time Pulitzer Prize winner who is a weekly columnist for The New York Times. 
Followup Question: How many Pulitzer Prize did Colson Whitehead win? Colson Whitehead has won two Pulitzer Prizes.
>>>>>>
Prediction:
Won(Thomas Loren Friedman, Pulitzer Prize) is True because Thomas Loren Friedman is a three-time Pulitzer Prize winner who is a weekly columnist for The New York Times. 
Won(Colson Whitehead, Pulitzer Prize) is True because Colson Whitehead win? Colson Whitehead has won two Pulitzer Prizes.
Won(Thomas Loren Friedman, Pulitzer Prize) && Won(Thomas Loren Friedman, Pulitzer Prize) is True.
The claim is [SUPPORTED].

Explanation:
Thomas Loren Friedman has won three Pulitzer Prizes. Colson Whitehead has won two Pulitzer Prizes.
Therefore Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead.
------
Question:
Is it true that SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia. ?

Context:
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) ::: Verify that SkyHigh Mount Dandenong is located on top of Mount Dandenong, Victoria, Australia.
Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) ::: Verify that SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.

Followup Question: Where is SkyHigh Mount Dandenong located? SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia.
Followup Question: Was SkyHigh Mount Dandenong formerly known as Mount Dandenong Observatory? the name officially being changed from "Mount Dandenong Observatory" to the current "SkyHigh Mount Dandenong".
>>>>>>
Prediction:
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) is True because SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia.
Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) is True because SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.
Location(SkyHigh Mount Dandenong, top of Mount Dandenong, Victoria, Australia) && Known(SkyHigh Mount Dandenong, Mount Dandenong Observatory) is True.
The claim is [SUPPORTED].

Explanation:
SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia and it is formerly known as Mount Dandenong Observatory.
------
Question:
Is it true that A hockey team calls the 70,000 capacity Madison Square Garden it's home. That team, along with the New York Islanders, and the New Jersey Devils NHL franchise, are popular in the New York metropolitan area. ?

Context:
Home(a hocky team, Madison Square Garden) ::: Verify that a hockey team calls Madison Square Garden its home.
Capacity(Madison Square Garden, 70,000) ::: Verify that Madison Square Garden has capacity of 70,000.
Popular(New York Islanders, New York Metropolitan area) ::: Verify that New York Islanders are popular in the New York metropolitan area.

Which hocky team calls Madison Square Garden Home? Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
What is the capacity of Madison Square Garden? Madison Square Garden has a capacity of 19.500.
Is New York Islanders popular in New York Metropolitan area? The New York Islanders are a professional ice hockey team based in Elmont, New York. ... 
>>>>>>
Prediction:
Home(New York Rangers, Madison Square Garden) is True because Madison Square Garden hosts approximately 320 events a year. It is the home to the New York Rangers of the National Hockey League
Capacity(Madison Square Garden, 70,000) is False because Madison Square Garden has a capacity of 19.500.
Popular(New York Islanders, New York Metropolitan area) is True because The New York Islanders are a professional ice hockey team based in Elmont, New York. ...
Home(New York Rangers, Madison Square Garden) && Capacity(Madison Square Garden, 70,000) && Popular(New York Islanders, New York Metropolitan area) is False.
The claim is [NOT_SUPPORTED].

Explanation:
The New York Rangers, along with the New York Islanders and the New Jersey Devils, are popular National Hockey League (NHL) teams in the New York metropolitan area. 
Madison Square Garden, a well-known venue in New York City, has a capacity of approximately 19,500 and serves as the home arena for the New York Rangers.
------
Question:
Is it true that Sumo wrestler Toyozakura Toshiaki did not commit match-fixing, ending his career in 2019 that started in 1989. ?

Context:
Ending(Toyozakura Toshiaki, his career in 2011) ::: Verify that Toyozakura Toshiaki ended his career in 2011.
Occupation(Toyozakura Toshiaki, sumo wrestler) ::: Verify that Toyozakura Toshiaki is a sumo wrestler.
Commit(Toyozakura Toshiaki, match-fixing) ::: Verify that Toyozakura Toshiaki committed match-fixing.

Followup Question: When did Sumo wrestler Toyozakura Toshiaki ended his career? Toyozakura Toshiaki was forced to retire in April 2011.
Followup Question: What is Toyozakura Toshiaki's occupation? Toyozakura Toshiaki is a former sumo wrestler from Hiroshima, Japan
Followup Question: Did Sumo wrestler Toyozakura Toshiaki committed match-fixing? After admitting his involvement in match-fixing, he retired from the sport in 2011 following an investigation by ...
>>>>>>
Prediction:
Ending(Toyozakura Toshiaki, his career in 2011) is False because Toyozakura Toshiaki was forced to retire in April 2011.
Occupation(Toyozakura Toshiaki, sumo wrestler) is True because Toyozakura Toshiaki was a former sumo wrestler.
Commit(Toyozakura Toshiaki, match-fixing) is False because Toyozakura Toshiaki admitted his involvement in match-fixing.
Ending(Toyozakura Toshiaki, his career in 2011) && Occupation(Toyozakura Toshiaki, sumo wrestler) && Commit(Toyozakura Toshiaki, match-fixing) is False.
The claim is [NOT_SUPPORTED].

Explanation:
Toyozakura Toshiaki is a former sumo wrestler, he was forced to retire in April 2011 after admitting his involvement in match-fixing.
Therefore, Toyozakura Toshiaki committed match-fixing, ending his career in 2011.
------
Question: Is it true that %s?

Context: 
%s
>>>>>>
"""
