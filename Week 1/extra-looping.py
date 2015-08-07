'''

Convert a string into a several lines, but with two caveats.
One if the string ends with a newline, then you return just that text.
Second, if the string is longer then a screen size, break up the string

Ex:

string = "L1\nL2\nLong Line\nL4"

text_to_array with screen size 5 -> outputs

["L1","L2","Long ","Line","L4"]



''


text_array = "Several Lines of text.\nThat we want to try and fit on to a certain size screen.\nSo we want to draw one line up until the new line, unless the length of the line is longer then the screen size, then we need to break that line up into items in that array"


def print_screen(array_lines):
    #print out the array
    pass

def text_to_array(text,screen_width):
    #takes text converts to array that then can be used by print screen
    pass


print_screen(text_to_array(text_array,30))

        



