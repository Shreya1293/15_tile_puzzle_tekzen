from flask import Flask, render_template, redirect, request, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'thee'

#checks if the puzzle is solvable
def is_solvable(tile):
    #checks if the puzzle is solvable-> done by counting inversions
    inver=0
    for i in range(len(tile)):
        for j in range(i+1, len(tile)):
            if tile[i]>tile[j] and tile[i]!=0 and tile[j]!=0:
                inver+= 1
    return inver%2==0

def generate_solvable_puzzel():
    #shuffles the puzzel until a solvable set is found
    tiles=list(range(16))
    while True:
        random.shuffle(tiles)
        if is_solvable(tiles):
            return tiles

#routes to main page with the puzzle
@app.route("/",methods=["GET", "POST"])
def index():
    if "puzzle" not in session or "empty_index" not in session:
        session["puzzle"]=generate_solvable_puzzel()
        session["empty_index"]=session["puzzle"].index(0)#tracking the empty tile's position
    puzzel=session["puzzle"]
    empty_ind=session["empty_index"]
    msg=""
    if request.method=="POST":
        try:
            move_ind=int(request.form["move"])
        except (ValueError, KeyError):
            msg="Invalid move! Please try again."
            return render_template("index.html",puzzle=puzzel, message=msg)

        #check the move and update the puzzle if valid
        if is_valid_move(move_ind, empty_ind):
            puzzel[empty_ind],puzzel[move_ind]=puzzel[move_ind], puzzel[empty_ind]
            session["empty_index"]=move_ind
            if is_win(puzzel):
                msg="Congratulations!You solved the puzzle!!"
        else:
            msg="Invalid move!You can only move adjacent tiles"
        session["puzzle"]=puzzel
    return render_template("index.html",puzzle=puzzel,message=msg)

#check if a tile move is valid
def is_valid_move(ind, empty_ind):
    row,col=divmod(ind,4)
    emp_row,emp_col=divmod(empty_ind,4)
    return abs(row-emp_row) +abs(col-emp_col)==1

#check if the puzzle is solved
def is_win(puzzel):
    return puzzel==list(range(1,16))+[0]

#reset the puzzle
@app.route("/reset")
def reset():
    session.clear()
    session["puzzle"]=generate_solvable_puzzel()
    session["empty_index"]=session["puzzle"].index(0)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
