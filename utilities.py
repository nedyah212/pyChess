import time

class Utilities:
    
    @staticmethod
    def get_selection():
        """
        This method prompts the user for a position input via the terminal, this position 
        represents the position the user intends to select, or to move to. Input must be 2
        characters, either char(a-h),int(0-7) OR int(0-7), int(0-7). Non alphanumeric
        characters are sanitized.
        Args: 
            None
        Returns:
            list: [row, column] as integers OR error message string
        """
        letter_to_index = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}

        try:
            selection = input("\nEnter a piece to move: ")
            selection = ''.join(c for c in selection if c.isalnum())
            selection = list(selection)
            
            if selection is None:
                raise ValueError("The entry cannot be empty,")

            if len(selection) != 2:
                raise ValueError("Wrong amount of characters,")
            
            if selection[0] in letter_to_index.keys():
                selection[0] = letter_to_index[selection[0]]
            
            elif selection[0].isdigit():
                selection[0] = int(selection[0])
            
            else:
                raise ValueError("Entry is not valid,")
            
            if not selection[1].isdigit():
                raise ValueError("The second value must be a digit,")
            
            selection[1] = int(selection[1])
            
            if selection[0] not in range(8):
                raise ValueError("The first value must be a-h or 0-7,")
            
            if selection[1] not in range(8):
                raise ValueError("The second value must be 0-7,")
                
        except ValueError as e:
            selection = f"{e} please try again."
        except KeyError as e:
            selection = f"{e} please try again"
        
        return selection