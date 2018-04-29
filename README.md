# DiscoLib
Discord bot library 


## Over events

Ik had een begin gemaakt aan het parsen van events, maar mischien moeten we het niet op deze manier doen, maar de boel parsen en dan een relevantere dispatch maken

bv: de message_update returned een incompleet message object met enkel de veranderingen erin, mischien moeten wij dan een call maken naar een event functie die een oude en nieuwe returned oid.

De gebruiker moet zich niet bezig moeten houden met ID's etc om bij de juiste objecten te komen dit moet de Discord class doen en de relevante objects returnen ipv een kaal event object met rauwe data. 

MAW we moeten het hier nog ff over hebben en zodoende ga ik er atm niet mee verder, want ik denk dat dit de verkeerde aanpak is.