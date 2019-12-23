# A dic is a key value pair
studies = {'monday': '2hr', 'wednesday': '3hr', 'saturday': '4hr'}
print(studies)


def show(dic):
    # iterate over
    for day, duration in studies.items():
        print(f'On {day} I need to study {duration}')


show(studies)

# input to dic
days = {}

while True:
    day = input('Enter a day: ')
    hour = input('How many hours: ')
    days[day] = hour + 'hr'

    choice = input('Want to add more (y/n)? :')
    if choice == 'y':
        continue
    else:
        break

print('Your studies schedule is below.')
show(days)
