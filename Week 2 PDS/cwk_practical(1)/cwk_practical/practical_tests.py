
def tests_version():
     return( "7th Oct, 2020")

TESTS = {
  "number_of_vowels": [
      ("How many vowels?",   4, 1),
      ("Sooo many vowels!",  6, 1),
      ("XXXX",               0, 1)
      ],
   
   "number_of_distinct_vowels": [
     ("Hello World",        2, 1),
      ("Sooo many vowels!", 3, 1),
      ("XXXX",              0, 1),
      ("Eutopia",           5, 1)
    ],

"anagrams": [
      ( ("listen","silent"), True,  1),
      ( ("Listen","Silent"), True,  1),
      ( ("this","that"), False, 1),
      ( ("this","This"), False, 1),
    ],

   "is_palindrome": [
      ("Abba", True,  1),  
      ("Python", False, 1),  
      ( "Rotator", True,  1), 
      ( "Was it a cat I saw?", True, 1),
    ],

  "find_all_anagrams": [
        ("cheese", [], 1 ),
        ( "Python", ['phyton', 'typhon'], 1),
        ("Listen!", [], 1 ),
        ( "SeaBird", ['abiders', 'braised', 'darbies', 'sidebar'], 1),  
      ],
    
   "find_palindromes_of_length": [
       ( 7, ['deified', 'halalah', 'reifier', 'repaper', 'reviver', 'rotator', 'sememes'], 1 ),
       ( 10, [], 1 ),
      ],

  "password_strength": [
       ( "brandon123",   "MEDIUM",  1 ),
       ("hello",   "WEAK",  1 ),
       ( "secret99",   "WEAK",     1 ),
       ( "Secret999!",   "MEDIUM",   1 ),  
       ( "7Kings8all9Pies!",  "STRONG",   1 ),
    ]

}


def do_tests( function ):
    max_marks = 0
    marks = 0
    function_name = function.__name__
    print("\nRunning tests for :", function_name )
    tests = TESTS[function_name]
 
    for test in tests:
        (test_input, test_answer, test_marks) = test
        max_marks += test_marks
        
        if type(test_input) == tuple:
            print( " * {}{}".format(function_name, test_input.__repr__() ))
        else:
            print( " * {}({})".format(function_name, test_input.__repr__() ))

        if not type(test_input) == tuple:
           test_input = (test_input,)

        result = function(*test_input)

        print("    returned:", result.__repr__() , ", expected: ", test_answer.__repr__())

        # Handle case where answer may be a list in any order
        # by sorting both the result and the answer.
        if ( type(test_answer) == tuple and test_answer[0] == "any_order"
             and type(result) == list 
           ):
           result.sort()
           test_answer = test_answer[1]
           test_answer.sort() 

        if result == test_answer:
           print("    Correct.")
           marks += test_marks
        else:
           print("    Incorrect.")
    print( " Number of tests passed: {}/{}".format(marks, max_marks) ) 
        







