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
        letter_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        
        try:
            selection = input("\nEnter a piece to move: ")
            selection = ''.join(c for c in selection if c.isalnum())
            selection = list(selection)
            
            if len(selection) != 2:
                raise ValueError("The position must be two digits, ")
            
            if selection[0] in letter_to_index.keys():
                selection[0] = letter_to_index[selection[0]]
            elif selection[0].isdigit():
                selection[0] = int(selection[0])
            else:
                raise ValueError("Column input invalid, ")
            
            if not selection[1].isdigit():
                raise ValueError("Row must be a digit, ")
            selection[1] = int(selection[1])
            
            if selection[0] not in range(8):
                raise ValueError("Column input invalid, ")
            if selection[1] not in range(8):
                raise ValueError("Row input invalid, ")
                
        except ValueError as e:
            return None, f"{e}please try again"
        except KeyError as e:
            return f"{e}please try again"
        
        return selection