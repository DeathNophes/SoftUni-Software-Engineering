heroes = {}
n = int(input())
for _ in range(n):
    name, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)
    heroes[name] = {'HP': HP, 'MP': MP}

command = input()
while command != 'End':
    command = command.split(' - ')
    name = command[1]

    if 'CastSpell' in command:
        MP_needed = int(command[2])
        spell = command[3]
        if heroes[name]['MP'] >= MP_needed:
            heroes[name]['MP'] -= MP_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif 'TakeDamage' in command:
        damage = int(command[2])
        attacker = command[3]
        heroes[name]['HP'] -= damage
        if heroes[name]['HP'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]

    elif 'Recharge' in command:
        amount = int(command[2])
        if heroes[name]['MP'] + amount <= 200:
            heroes[name]['MP'] += amount
            print(f"{name} recharged for {amount} MP!")
        else:
            diff = 200 - heroes[name]['MP']
            heroes[name]['MP'] = 200
            print(f"{name} recharged for {diff} MP!")

    elif 'Heal' in command:
        amount = int(command[2])
        if heroes[name]['HP'] + amount <= 100:
            heroes[name]['HP'] += amount
            print(f"{name} healed for {amount} HP!")
        else:
            diff = 100 - heroes[name]['HP']
            heroes[name]['HP'] = 100
            print(f"{name} healed for {diff} HP!")

    command = input()

for hero in heroes.keys():
    print(hero)
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")