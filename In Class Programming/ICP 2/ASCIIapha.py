print("This program takes a name and returns the fist letter as ASCII Art")
inputString = input("Enter Your Name: ")
firstLetter = inputString[0].capitalize()
def letters_to_ascii(argument):
    switcher = {
        "A": """
   *
  * *
 *   *
*     *
*******
*     *
*     *
        """,
        "B": """
******
*     *
*     *
******
*     *
*     *
******
            """,
        "C": """
 *****
*     *
*
*
*
*     *
 *****
        """,
        "D": """
******
*     *
*     *
*     *
*     *
*     *
******
        """,
        "E": """
*******
*
*
*****
*
*
*******
        """,
        "F": """
*******
*
*
*****
*
*
*
""",
        "G": """
 *****
*     *
*
*  ****
*     *
*     *
 *****
        """,
        "H": """
*     *
*     *
*     *
*******
*     *
*     *
*     *
        """,
        "I": """
***
 *
 *
 *
 *
 *
***
""",
        "J": """

      #
      #
      #
      #
#     #
#     #
 #####
        """,
        "K": """
*    *
*   *
*  *
***
*  *
*   *
*    *
        """,
        "L": """
*
*
*
*
*
*
*******
""",
        "M": """
*     *
**   **
* * * *
*  *  *
*     *
*     *
*     *
        """,
        "N": """
*     *
**    *
* *   *
*  *  *
*   * *
*    **
*     *
        """,
        "O": """
*******
*     *
*     *
*     *
*     *
*     *
*******
        """,
        "P": """
******
*     *
*     *
******
*
*
*
        """,
        "Q": """
 *****
*     *
*     *
*     *
*   * *
*    *
 **** *
        """,
        "R": """
******
*     *
*     *
******
*   *
*    *
*     *
        """,
        "S": """
 *****
*     *
*
 *****
      *
*     *
 *****
        """,
        "T": """
*******
   *
   *
   *
   *
   *
   *
        """,
        "U": """
*     *
*     *
*     *
*     *
*     *
*     *
 *****
        """,
        "V": """
*     *
*     *
*     *
*     *
 *   *
  * *
   *
        """,
        "W": """
*     *
*  *  *
*  *  *
*  *  *
*  *  *
*  *  *
 ** **
        """,
        "X": """
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
        """,
        "Y": """
*     *
 *   *
  * *
   *
   *
   *
   *
        """,
        "Z": """
*******
     *
    *
   *
  *
 *
*******
        """
    }
    # Get the function from switcher dictionary
    response = switcher.get(argument, lambda: "Invalid first letter")
    print(response)
    # Execute the function
letters_to_ascii(firstLetter)