import collections

jedis = [
  {'name': 'Ahsoka Tano', 'lightsaber_color': 'green'},
  {'name': 'Anakin Skywalker', 'lightsaber_color': 'blue'},
  {'name': 'Anakin Solo', 'lightsaber_color': 'blue'},
  {'name': 'Ben Skywalker', 'lightsaber_color': 'blue'},
  {'name': 'Count Duku', 'lightsaber_color': 'red'},
  {'name': 'Darth Craidus', 'lightsaber_color': 'red'},
  {'name': 'Darth Maul', 'lightsaber_color': 'red'},
  {'name': 'Darth Vader', 'lightsaber_color': 'red'},
  {'name': 'Jacen Solo', 'lightsaber_color': 'green'},
  {'name': 'Ki-Adi-Mundi', 'lightsaber_color': 'blue'},
  {'name': 'Kit Fisto', 'lightsaber_color': 'green'},
  {'name': 'Luke Skywalker', 'lightsaber_color': 'green'},
  {'name': 'Obi-Wan Kenobi', 'lightsaber_color': 'blue'},
  {'name': 'Palpatine', 'lightsaber_color': 'red'},
  {'name': 'Plo-Koon', 'lightsaber_color': 'blue'},
  {'name': 'Qui-Gon Jinn', 'lightsaber_color': 'green'},
  {'name': 'Yoda', 'lightsaber_color': 'green'},
]

frequencies = collections.Counter(jedi['lightsaber_color'] for jedi in jedis)

print(frequencies)
# Counter({'blue': 6, 'green': 6, 'red': 5})
