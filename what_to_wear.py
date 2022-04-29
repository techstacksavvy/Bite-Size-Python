# Project: What to Wear

temperature_today = input("what's the weather for today? ")

if temperature_today >= '80 degrees':
    outfit = 'you should wear shorts and pack your sunglasses'
elif(temperature_today >= '60 degrees') and (temperature_today <= '79 degrees'):
    outfit = 'you should wear a light jacket'
else:
    outfit = 'you should wear a coat, scarf, hat and gloves'

# advice for the user
advice = f'Good morning! Today { outfit}.'

print(advice)
