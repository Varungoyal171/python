# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:20:05 2020

@author varun
"""
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='x'
p2s='o'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
                
        if count==3:
            print(symbol,"won")
            return True
    return False
       
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
                
        if count==3:
            print(symbol,"won")
            return True
    return False 

def check_diagonals(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if r==c:
                if board[r][c]==symbol:
                    count+=1
                    
            if r+c==2:
                if board[r][c]==symbol:
                    count+=1
                    
        if count==3:
            print(symbol,"won")
            return True
    return False 
  
    
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
        


def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("enter row pos - 1 or 2 or 3 :"))
        col=int(input("enter column pos - 1 or 2 or 3 :"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=="-":
            break
        else:
            print("Invalid input.Please enter again")
    board[row-1][col-1]=symbol
    
def play():
    
    for turn in range(9):
        if(turn%2==0):
            print("turn of x ")
            place(p1s)
            if won(p1s):
                print(numpy.matrix(board))
                break
        else:
            print("turn of o ")
            place(p2s)
            if won(p2s):
                print(numpy.matrix(board))
                break
        if not(won(p1s)) and not(won(p2s)):
            print("draw")
            