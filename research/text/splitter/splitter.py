import enchant

locale = 'en_US'

dict = enchant.Dict(locale)

print(dict.check("Hello"))