"""
function is_ransome_note
"""

def is_ransome_note(note,megazine):

    for ch in note.lower():

        if ch not in megazine.lower():
            print(False)
            break

    else:
        print(True)

is_ransome_note("Hen","chicKen")