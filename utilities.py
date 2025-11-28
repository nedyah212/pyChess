import time

class Utilities:
    
    @staticmethod
    def get_selection(move_to_pos = False):
        letter_to_index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        reverse_int_index = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7, 1: 8}
        
        if move_to_pos:
            msg = "\nEnter a location to move to: "
        else:
            msg = "\nEnter a piece to move: "

        try:
            selection = input(msg)
            selection = ''.join(c for c in selection if c.isalnum())
            
            if len(selection) != 2:
                raise ValueError("Input must be exactly 2 characters")
            
            result = [None, None]
            
            # First character - letter or digit
            if selection[0].isalpha():
                if selection[0].lower() not in letter_to_index:
                    raise ValueError("First character must be a-h")
                result[0] = letter_to_index[selection[0].lower()] - 1 
            
            elif selection[0].isdigit():
                num = int(selection[0])
                if num not in reverse_int_index:
                    raise ValueError("First digit must be 1-8")
                result[0] = num - 1 
            else:
                raise ValueError("An unexpected error has occured")
            
            # Second character - must be digit
            if not selection[1].isdigit():
                raise ValueError("Second character must be a digit")
            
            num = int(selection[1])
            if num not in reverse_int_index:
                raise ValueError("Second digit must be 1-8")
            
            result[1] = reverse_int_index[num] - 1
            
            return result, ""
            
        except ValueError as e:
            return [None, None], f"{e}, please try again"
        except KeyError as e:
            return [None, None], f"Invalid input: {e}, please try again"
