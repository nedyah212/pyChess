import time

class Utilities:
    
    @staticmethod
    def get_selection():
        letter_to_index = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}
        reverse_int_index = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
        
        try:
            selection = input("\nEnter a piece to move: ")
            selection = ''.join(c for c in selection if c.isalnum())
            
            if len(selection) != 2:
                raise ValueError("Input must be exactly 2 characters")
            
            result = [None, None]
            
            # First character - letter or digit
            if selection[0].isalpha():
                if selection[0].lower() not in letter_to_index:
                    raise ValueError("First character must be a-h")
                result[0] = letter_to_index[selection[0].lower()]
            
            elif selection[0].isdigit():
                num = int(selection[0])
                if num not in reverse_int_index:
                    raise ValueError("First digit must be 1-8")
                result[0] = reverse_int_index[num]
            else:
                raise ValueError("An unexpected error has occured")
            
            # Second character - must be digit
            if not selection[1].isdigit():
                raise ValueError("Second character must be a digit")
            
            num = int(selection[1])
            if num not in reverse_int_index:
                raise ValueError("Second digit must be 1-8")
            
            result[1] = reverse_int_index[num]
            
            return result, ""
            
        except ValueError as e:
            return [None, None], f"{e}, please try again"
        except KeyError as e:
            return [None, None], f"Invalid input: {e}, please try again"