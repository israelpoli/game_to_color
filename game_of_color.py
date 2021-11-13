from colored import fg, bg, attr
import random

class Game():

    def __init__(self,board=None):

        self.colors=['%s  %s' % (bg(196), attr(0)),'%s  %s' % (bg(2), attr(0)),'%s  %s' % (bg(4), attr(0)),'%s  %s' % (bg(11), attr(0))]
        if board==None:
            self.board = self.game_board()
        else:
            self.board=board
        self.index_for_paint=[(0,0)]
        self.stack=[]


    def game_board(self):
        board=[]
        for i in range(18):
            tmp=[]
            for j in range(18):
                color=random.choice(self.colors)
                tmp.append(color)

            board.append(tmp)
        return board

    def print_board(self):

        for i in range(18):
            for j in range(18):
                print(self.board[i][j],end='')
            print('')

    def paint(self,color):

        for i in self.index_for_paint:

            self.board[i[0]][i[1]]=color


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

    def convert_to_color(self,color):

        if color=='r':
            return ('%s  %s' % (bg(196), attr(0)))
        if color=='y':
            return ('%s  %s' % (bg(11), attr(0)))
        if color=='b':
            return ('%s  %s' % (bg(4), attr(0)))
        if color=='g':
            return ('%s  %s' % (bg(2), attr(0)))

    def win_los(self):
        check=self.board[0][0]
        for i in range(18):
            for j in range(18):
                if self.board[i][j]!=check:
                    return False

        return True


    def __call__(self):

        count=1
        while count<=21:
            self.print_board()
            color=self.convert_to_color(input(f" Step {count} \n color>>"))
            if color not in self.colors:
                continue
            self.paint(color)
            self.add_indexes(color)
            if self.win_los()==True:
                self.print_board()
                print('you win')
                return
            count+=1
        if self.win_los()==False:
            self.print_board()
            print('you lose')
            return
        self.print_board()
        print('you win')

game=Game()
game()
