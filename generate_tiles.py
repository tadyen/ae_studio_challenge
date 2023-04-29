#!/usr/bin/env python

import numpy as np

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
SLASHES_RULE = (3, 2, 2)

class Block():
    def __init__(self):
        self.tile_order = TILE_ORDER
        self.block = INIT_BLOCK
        self.filled_rule = FILLED_RULE
        self.slashes_rule = SLASHES_RULE
        self.sequence_index = 0
        self.apply_tile_vals()
        return
    
    def apply_tile_vals(self):
        self.tile_vals = np.zeros((3,2), dtype=int)
        self.tile_vals += self.block["FILLED"] * TILE_STATES["FILLED"]["VALUE"]
        self.tile_vals += self.block["SLASHED"] * TILE_STATES["SLASHED"]["VALUE"]
        return
    
    def print_block(self):
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
        printable = "\n".join([x.strip() for x in printable.splitlines()])
        print(printable)
        
if __name__ == "__main__":
    myblock = Block()
    myblock.apply_tile_vals()
    myblock.print_block()