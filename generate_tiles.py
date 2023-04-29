#!/usr/bin/env python

import numpy as np
import math
TILE_STATES = {
    "BLANK" : 
    {
        "VALUE" : 0,
        "PRINT" : "🔳"
    },
    "FILLED" : 
    {
        "VALUE" : 1,
        "PRINT" : "🟩"
    },
    "SLASHED" : 
    {
        "VALUE" : 2,
        "PRINT" : "❌"
    },
    "BOTH" : 
    {
        "VALUE" : 3,
        "PRINT" : "❎"
    }
}

TILE_ORDER = np.array([
    [5, 0],
    [4, 1],
    [3, 2],
])


INIT_BLOCK = {
    "FILLED" : 
    np.array([
        [0, 1],
        [0, 0],
        [0, 0],
    ]),
    "SLASHED" : 
    np.array([
        [0, 0],
        [1, 0],
        [0, 0],
    ])
}

FILLED_RULE = (1, 1, 2)
SLASHED_RULE = (3, 2, 2)

class Block():
    def __init__(self):
        self.tile_order = TILE_ORDER
        self.block = INIT_BLOCK
        self.filled_rule = FILLED_RULE
        self.slashed_rule = SLASHED_RULE
        self.sequence_index = 0
        self.apply_tile_vals()
        return
    
    def apply_tile_vals(self):
        self.tile_vals = np.zeros((3,2), dtype=int)
        self.tile_vals += self.block["FILLED"] * TILE_STATES["FILLED"]["VALUE"]
        self.tile_vals += self.block["SLASHED"] * TILE_STATES["SLASHED"]["VALUE"]
        return
    
    def print_block(self, console_out:bool = None):
        index = 0
        p: list[int] = [] # list of printables
        for row in self.tile_vals:
            for tile_val in row:
                printable = [ v["PRINT"] for k,v in TILE_STATES.items() if v["VALUE"] == tile_val ][0]
                p.append( printable )
        printable = f"""
        Block # {self.sequence_index}
        {p[0]} {p[1]}
        {p[2]} {p[3]}
        {p[4]} {p[5]}
        """
        # remove \n at start and end
        printable = printable.strip() 
        
        # remove spaces at start and end of each line
        printable = "\n".join([x.strip() for x in printable.splitlines()])
        
        if console_out != None and console_out:
            print(printable)
        return printable
                
    def sequence_step(self):
        filled_index = sum(sum( self.block["FILLED"] * self.tile_order ))
        filled_index += self.filled_rule[ self.sequence_index % len(self.filled_rule) ]
        filled_index = filled_index % np.inner( * np.shape(self.tile_order) )
        self.block["FILLED"] = self.block["FILLED"] * 0
        for row_num in range( np.shape(self.tile_order)[0] ):
            for col_num in range( np.shape(self.tile_order)[1] ):
                if filled_index == self.tile_order[row_num][col_num]:
                    self.block["FILLED"][row_num][col_num] = 1
        
        slashed_index = sum(sum( self.block["SLASHED"] * self.tile_order ))
        slashed_index += self.slashed_rule[ self.sequence_index % len(self.slashed_rule) ]
        slashed_index = slashed_index % np.inner( * np.shape(self.tile_order) )
        self.block["SLASHED"] = self.block["SLASHED"] * 0
        for row_num in range( np.shape(self.tile_order)[0] ):
            for col_num in range( np.shape(self.tile_order)[1] ):
                if slashed_index == self.tile_order[row_num][col_num]:
                    self.block["SLASHED"][row_num][col_num] = 1
        self.sequence_index += 1
        return
    
if __name__ == "__main__":
    myblock = Block()
    myblock.apply_tile_vals()
    myblock.print_block(True)
    for _ in range(11):
        myblock.sequence_step()
        myblock.apply_tile_vals()
        myblock.print_block(True)