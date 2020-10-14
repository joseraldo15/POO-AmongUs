class Crewmate:
    
    def _init_(self, name, color, do_task, sabotage, vent):
        self.name = name
        self.color = color
        self.do_task = True
        self.sabotage = False
        self.vent = False
    
    def sabotage(self):
        if self.sabotage:
            print(f'{self.name} ruined the ship!')
        else:
            print('You are not the impostor, stop playing games!')
    
    def vent(self):
        if self.vent:
            print(f'you vented.')
        else:
            print('why would you do that?')
    
    def do_task(self):
        if self.sabotage and self.vent:
            print('you have to fake your tasks!')
        else:
            print('complete your tasks to win.')


class Impostor:

    def _init_(self, name, color, do_task, sabotage, vent):
        self.name = name
        self.color = color
        self.do_task = False
        self.sabotage = True
        self.vent = True
    
    def sabotage(self):
        if self.sabotage:
            print(f'{self.name} ruined the ship!')
        else:
            print('You are not the impostor, stop playing games!')
    
    def vent(self):
        if self.vent:
            print(f'you vented.')
        else:
            print('why would you do that?')
    
    def do_task(self):
        if self.sabotage and self.vent:
            print('you have to fake your tasks!')
        else:
            print('complete your tasks to win.')
