"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for entry in items:
        key = str(entry) if not isinstance(entry,str) else entry
        if key in frequencies: 
            frequencies[key] = frequencies[key]+1
        else:
            frequencies[key] = 1
 
  
    
    return frequencies
