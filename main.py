class Crewmate:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.can_do_task = True
        self.can_sabotage = False
        self.can_vent = False
    
    def sabotage(self):
        if self.can_sabotage:
            print(f'{self.name} ruined the ship!')
        else:
            print('You are not the impostor, stop playing games!')
    
    def vent(self):
        if self.can_vent:
            print(f'you vented.')
        else:
            print('why would you do that?')
    
    def do_task(self):
        if self.can_sabotage and self.can_vent:
            print('you have to fake your tasks!')
        else:
            print('complete your tasks to win.')


class Impostor:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.can_do_task = False
        self.can_sabotage = True
        self.can_vent = True
    
    def sabotage(self):
        if self.can_sabotage:
            print(f'{self.name} ruined the ship!')
        else:
            print('You are not the impostor, stop playing games!')
    
    def vent(self):
        if self.can_vent:
            print(f'you vented.')
        else:
            print('why would you do that?')
    
    def do_task(self):
        if self.can_sabotage and self.can_vent:
            print('you have to fake your tasks!')
        else:
            print('complete your tasks to win.')


t1 = Crewmate('XANDÃO', 'Azul')

t1.sabotage()
t1.vent()
t1.do_task()

i1 = Impostor('PAXTEL', 'Verde')

i1.sabotage()
i1.vent()
i1.do_task()
