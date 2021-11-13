import random
import PySimpleGUI as sg
from utilities import lose,win

MAX_ROWS = MAX_COL = 18
QT_ENTER_KEY1 =  'special 16777220'
QT_ENTER_KEY2 =  'special 16777221'
class Gui_game_color():

    def __init__(self):

        self.layout =  [[[sg.Text('', size=(3, 1), key=(i,j), pad=(0,0),background_color=random.choice(['red','blue','yellow','green'])) for j in range(MAX_COL)] for i in range(MAX_ROWS)],
                  [sg.T(' '*5),sg.Button('red', button_color="red", size=(6,2)),sg.T(' '*5),sg.Button('blue', button_color="blue", size=(6,2)),sg.T(' '*5),sg.Button('yellow', button_color="yellow", size=(6,2)),
                   sg.T(' '*5),sg.Button('green', button_color="green", size=(6,2)),sg.T(' '*5),sg.Button('go back', button_color="orange", size=(6,2))]]
        self.board=[[self.layout[0][j][i].BackgroundColor for i in range(MAX_COL)]for j in range(MAX_ROWS)]
        self.index_for_paint = [(0, 0)]
        self.stack_for_go_back=[]
        self.stack = []
        self.color=['red','yellow','blue','green']
        self.window = sg.Window('Game of color', self.layout,return_keyboard_events=True)
        self.position = {'win': self.is_win, 'lose': self.is_lose}


    def draw(self,color):

        for i in self.index_for_paint:
            self.board[i[0]][i[1]] = color
            self.window[i[0],i[1]].update('', background_color=color)

    def add_indexes(self,color):

        self.stack=self.index_for_paint
        for i in self.index_for_paint:
            self.add_index(i,color)

        self.index_for_paint=self.stack

    def add_index(self,index,color):

            if index[0]!= 0:
                if self.board[index[0]-1][index[1]]==color and (index[0]-1,index[1]) not in self.stack:
                    self.stack.append((index[0]-1,index[1]))
                    self.add_index((index[0]-1,index[1]),color)

            if index[1]!=0:
                if self.board[index[0]][index[1]-1]==color and (index[0],index[1]-1) not in self.stack:
                    self.stack.append((index[0],index[1]-1))
                    self.add_index((index[0],index[1]-1), color)

            if index[1]!=17:

                 if self.board[index[0]][index[1]+1]==color and (index[0],index[1]+1) not in self.stack:

                    self.stack.append((index[0],index[1]+1))
                    self.add_index((index[0],index[1]+1), color)

            if index[0] != 17:
                if self.board[index[0]+1][index[1]]==color and (index[0]+1,index[1]) not in self.stack:
                    self.stack.append((index[0]+1,index[1]))
                    self.add_index((index[0]+1,index[1]),color)

    def is_lose(self):
        for i in range(MAX_ROWS):
            for j in range(MAX_COL):
                self.board[i][j] = 'red'
                self.window[i, j].update('', background_color='red')

        for i in lose:
            self.window[i].update('', background_color='black')
            self.board[i[0]][i[1]] = 'black'
        return

    def is_win(self):
        color = self.board[0][0]
        for i in range(MAX_ROWS):
            for j in range(MAX_COL):
                self.board[i][j] = color
                self.window[i, j].update('', background_color=color)

        for i in win:
            self.board[i[0]][i[1]] = 'black'
            self.window[i].update('', background_color='black')

    def lose_win(self,lose_or_win):
         self.position[lose_or_win]()

    def check_if_win(self):
        check=self.board[0][0]
        for i in range(18):
            for j in range(18):
                if self.board[i][j]!=check:
                    return False

        return True

    def for_go_back(self,color):
        tmp=[]
        for i in self.index_for_paint:
            tmp.append(i)
        self.stack_for_go_back.append((tmp,color))

    def go_back(self):
        if len(self.stack_for_go_back)==0:
            return
        previous_step=self.stack_for_go_back.pop(-1)
        self.index_for_paint,color=previous_step[0],previous_step[1]
        self.draw(color)
        # self.add_indexes(color)

    def play(self):

        count=1
        event=0
        while count<=21 and event not in (sg.WIN_CLOSED, 'Exit'):

            event, values = self.window.read()

            print(event)
            if event == "Down:40":
                print((event))
                self.go_back()
            elif event=='go back' :
                self.go_back()
                count-=1

            elif event in self.color:
                self.for_go_back(self.board[0][0])
                self.draw(event)
                self.add_indexes(event)
                if self.check_if_win()==True:
                    self.lose_win('win')
                    while event not in (sg.WIN_CLOSED, 'Exit'):
                        event, values = self.window.read()
                count+=1

        while event not in (sg.WIN_CLOSED, 'Exit'):

            if self.check_if_win() == True:
                self.lose_win('win')
            else:self.lose_win('lose')
            while event not in (sg.WIN_CLOSED, 'Exit'):
                event, values = self.window.read()

        self.window.close()

g=Gui_game_color()
g.play()


