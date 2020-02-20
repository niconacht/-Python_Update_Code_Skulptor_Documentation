"""Python Data Representation
Update syntax for print in CodeSkulptor Docs  (Python2 --> Python3)
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """
    update_line = ""
    comment = ""
    index = 0
    length_before = 0
    length_after = 0
    print_command = ""
    to_print = ""
    parentheses = ["(", ")"]
    counter = 0

    # If line is print statement,  insert parentheses
    if line.lstrip().startswith("print"):
        length = len(line.lstrip())
        for elem in line[:len(line) - length + 1]:
            if elem == " ":
                counter += 1

        line_list = line.split()
        for i in range(counter):
            line_list.insert(0, " ")

        print_index = line_list.index("print")

        for elem in line_list[0:print_index+1]:
            print_command += elem

        for elem in line_list[print_index+1:]:
            to_print += elem + " "

        to_print = to_print.rstrip()

      #exclude comments and  multiple whitespaces in lines from print statement
        if not "#" in to_print:
            line = "{}{}{}{}".format(print_command, parentheses[0], to_print, parentheses[1])
            return line

        elif "#" in to_print:
            index = to_print.index("#")
            comment = to_print[index:]
            to_print = to_print[:index]
            length_before = len(to_print)
            to_print = to_print.rstrip()
            length_after = len(to_print)
            comment = (" " * length_after) + comment

        line = "print{}{}{}{}{}".format(print_command, parentheses[0], to_print, parentheses[1], comment)
        return line

    else:
      return line


def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """
    updated_block = ""
    line_list = pre_block.split("\n")

    for line in line_list:
        new_line = update_line(line)+ "\n"
        #print(new_line)
        updated_block += (new_line)
        #print(updated_block)
    return updated_block


def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Proces the <pre> blocks in the loaded text to update print syntax)
    Write the update text to the file specified by the string output_file_name
    """

    # open file and read text in file as a string
    result_string = ""
    openfile = open(input_file_name, "rt")
    read_file = openfile.read()
    pre_blocks = read_file.split("</pre>")

    # split text in <pre> blocks and update using update_pre_block()
    for block in pre_blocks:

        block = block
        pre_index = block.find("<pre class='cm'>")
        rest_of_block = block[0:pre_index +16]
        block = block[pre_index + 16:]
        block = update_pre_block(block)
        block = block.replace("\n", "")
        result_string += rest_of_block + block +"</pre>"

    print(result_string)

    with open(output_file_name, "wt") as outfile:
        outfile = outfile.write(result_string)
        print(outfile)

#update_file("table.html", "table_updated.html")
#update_file("docs.html", "docs_updated.html")








    #

    #pre_blocks = re.findall(pattern, read_file)




    # Write the answer in the specified output file







# A couple of test files

#update_file("docs.html", "docs_updated.html")

# Import some code to check whether the computed files are correct
##import examples3_file_diff as file_diff
##file_diff.compare_files("table_updated.html", "table_updated_solution.html")
##file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same
