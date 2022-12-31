import random
## OWAIS ABUHAMMAD 
board = [[" " for x in range(8)] for y in range(8)] 
piece_list = ["R", "N", "B", "Q", "P"]
 
 
def place_kings(brd):  ## evaluate  one king for each color
	while True:
		row_white, col_white, row_black, col_black = random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7)
		diff_list = [abs(row_white - row_black),  abs(col_white - col_black)]
		if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):    ## to check the two kings are not adjecent
			brd[row_white][col_white], brd[row_black][col_black] = "K", "k"
			break
 
def populate_board(brd, wp, bp):    ## to distribute the pieces on the board
	for x in range(2):
		if x == 0:  ## for the white pieces
			piece_amount = wp
			pieces = piece_list
		else:
			piece_amount = bp  ## for the blackk pices
			pieces = [s.lower() for s in piece_list] 
		while piece_amount != 0:
			piece_row, piece_col = random.randint(0, 7), random.randint(0, 7) ##select random position
			piece = random.choice(pieces)     ## choose random piece
			if brd[piece_row][piece_col] == " " and place_pawn(piece, piece_row) == False and validity(brd,piece)==True: ##check if the place is empty
				brd[piece_row][piece_col] = piece                                                                    ##place_pawn and validity
				piece_amount -= 1                                                                                    ## is described  under
 

    
'''  to restrict pawn position '''
def place_pawn(pc, pr):
	if pc == "P" and pr == 0:                     
		return True
	elif pc == "p" and pr == 7:
		return True
	return False

''' to restrict pairs of pieces'''
def validity(brd,piece):
    num = [row.count(piece) for row in brd] ##this return the number of a specifc piece in each row
    s = 0      
    for i in num:                    ## num is a list  s for summation of the list
        s+=i
    if piece=='p' or piece =='P':    ## the Pawn has no resrict 
        return True
    elif  s<2 and piece !='q' and piece !='Q': ## if the piece is not queen  we can only place 2 of it
        return True
   
    elif s<1 and (piece =='q' or piece =='Q'):  ## we can only have one queen for each Black and White
        return True
    else:
        return False

    
def score(board):        ## Scoring Points described in the text file 
    Wscore,Bscore = 0,0
    W_Bouns,B_Bouns = 0,0
    W_knight,W_rook,W_queen,W_Bishop=0,0,0,0
    B_knight,B_rook,B_queen,B_Bishop=0,0,0,0
    for x in board:
        for j in x:
            if j =='P':
                Wscore+=1
            if j =='N':
                Wscore+=3
                W_knight+=1
            if j =='R':
                Wscore+=5
                W_rook+=1
            if j =='B':
                Wscore+=3
                W_Bishop+=1
            if j =='Q':
                Wscore+=9
            if j =='p':
                Bscore+=1
            if j =='n':
                Bscore+=3
                B_knight+=1
            if j =='r':
                Bscore+=5
                B_rook+=1
            if j =='b':
                Bscore+=3
                B_Bishop+=1
            if j =='q':
                Bscore+=9
    if (W_knight==1 or W_knight==2) and (W_rook==1 or W_rook==2):
        W_Bouns+=7.5
    if (W_knight==1 or W_knight==2) and (W_Bishop==1 or W_Bishop==2):
        W_Bouns+=7.5
    if (W_rook==1 or W_rook==2) and (W_Bishop==1 or W_Bishop==2):
        W_Bouns+=8
    if (W_rook==1 or W_rook==2) and (W_Bishop==1 or W_Bishop==2) and (W_knight==1 or W_knight==2):
        W_Bouns+=10

        
    if(W_rook==2):
        W_Bouns +=3.5
    if W_knight ==2:
        W_Bouns +=3.5
    if W_Bishop ==2:
        W_Bouns +=3.5

    if (B_knight==1 or B_knight==2) and (B_rook==1 or B_rook==2):
        B_Bouns+=7.5
    if (B_knight==1 or B_knight==2) and (B_Bishop==1 or B_Bishop==2):
        B_Bouns+=7.5
    if (B_rook==1 or B_rook==2) and (B_Bishop==1 or B_Bishop==2):
        B_Bouns+=8
    if (B_rook==1 or B_rook==2) and (B_Bishop==1 or B_Bishop==2) and (B_knight==1 or B_knight==2):
        B_Bouns+=10

        
    if(B_rook==2):
        B_Bouns +=3.5
    if B_knight ==2:
        B_Bouns +=3.5
    if B_Bishop ==2:
        B_Bouns +=3.5

        
    ##print('score is  white: ',Wscore+W_Bouns," Black: ",Bscore+B_Bouns,' W_Bouns: ',W_Bouns,"B_Bouns",B_Bouns)

    print('\nWhite score: ',Wscore+W_Bouns,'  Black score:  ',Bscore+B_Bouns)

    if (Wscore+W_Bouns)>(Bscore+B_Bouns):
        print("White is more close to Win...")
    elif(Bscore+B_Bouns)>(Wscore+W_Bouns):
        print("Black is more close to Win...")
    elif(Wscore+W_Bouns)==(Bscore+B_Bouns):
        print('Tie.....')

        
def main():
	piece_amount_white, piece_amount_black = random.randint(0, 15), random.randint(0, 15)  
	place_kings(board)
	populate_board(board, piece_amount_white, piece_amount_black)
	for piece in board:
		print(piece)
	score(board)
	
	

 

main()
