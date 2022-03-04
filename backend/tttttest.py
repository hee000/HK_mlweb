# from flask import Flask, request, jsonify
# from flask_restx import Api, Resource
# from flask_cors import CORS #comment this on deployment
# from werkzeug.exceptions import BadRequest
# from werkzeug.datastructures import ImmutableMultiDict

# app = Flask(__name__)

# CORS(app) #comment this on deployment

# api = Api(app)


# @api.route('/i')
# class test(Resource):
#     def get(self):
#         return {"hello":"react"}



# if __name__=="__main__":
#     app.run(host="0.0.0.0", port="4000",debug=True, threaded=True)
    


from turtle import *


class Disc(Turtle):
    def __init__(self, n):  
        Turtle.__init__(self, shape="square", visible=False) 
        self.pu()                                            
        self.shapesize(1.5, n*1.5, 2)   # square-->rectangle 
        self.fillcolor(n/6., 0, 1-n/6.)                                 
        self.st()                                                       



class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x   

    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))       


def hanoi(n, from_, with_, to_):
    if n > 0:   
        hanoi(n-1, from_, to_, with_)                      
        to_.push(from_.pop())                              
        hanoi(n-1, with_, from_, to_)


def play():
    onkey(None,"space")
    clear()            
    try:               
        hanoi(6, t1, t2, t3)  
        write("press STOP button to exit",
        align="center", font=("Courier", 16, "bold"))
    except Terminator:         
        pass              # turtledemo user pressed STOP



def main():
    global t1, t2, t3 
    ht(); penup(); goto(0, -225)      # writer turtle                                      세미콜론 이용하여 한줄로 표시 #94
    t1 = Tower(-250)                                                  
    t2 = Tower(0)
    t3 = Tower(250)

    for i in range(6,0,-1):                                                                                  
        t1.push(Disc(i))                                                                                     

    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
        align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")                              
    listen()                                          
    return "EVENTLOOP"



msg = main()
print(msg)
mainloop()

