class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to represent 3x3 board
        self.current_winner = None #keep track of the winner


    def print_board(self):
        #this is just printing the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')

        
    @staticmethod
    def print_board_nums():
        #0|1|2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
    def empty_squares(self):
        return " " in self.board
    def num_empty_sqares(self):
        return self.board.count(" ")

    def make_move(self,square,letter):
        #if valid move, then make the move ( assign sqaure to letter )
        #then return true, id=f invalid return False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winnner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,sqaure,letter):
        #winner if 3 in a row anywhere.. we have to check all of these!
        #first let's check for the row 
        row_ind = sqaure//3
        row = 

def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_board_nums()
    letter = "X"#starting lettter
    #iterate while the game still has empty sqaures
    #( we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_sqaures():
        #get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter + "{} makes a move to the square".format(square))
                game.print_board()
                print("") #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
            #adter we made our move, we need to alternate letters
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
        


        if print_game:
            print("It's a tie!")

            

