"""
Author: Ishaan Gupta (29735491)

In this assignment we create a Python module to implement some
basic family tree software, where users can look up various relationships
that exist in the database, as well as merging two family tree databases
that may contain overlapping information.

Functions 1-5 are due in Part 1 of the assignment. Functions
for 6 and 7 are due in Part 2.

We represent each entry in a family tree database as a list of three
strings [name, father, mother], where name is a person's name, father
is the name of their father, and mother is the name of their mother.
Where a particular relationship is unknown, the value None is used.
For example:

>>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Huey Duck', None, 'Della Duck'],
...           ['Dewey Duck', None, 'Della Duck'],
...           ['Louie Duck', None, 'Della Duck']]

For more information see the function documentation below and the
assignment sheet.

"""

# Part 1 (due Week 6) #

def person_index(person, family):
    """ Returns the index of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family) as specified above.
    Output: The index value of the person's entry in the family tree, or None if they have no entry.

    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> person_index('Dewey Duck', duck_tree)
    5
    >>> person_index('Fergus McDuck', duck_tree)


    This is a list processing problem that seeks to identify the index (row) of a person in a family tree database. The
    main challenge is to find a way to loop through the first column (representing the named person) in all the rows
    of the database. Importantly, the function should return nothing in the event the person is not found in the
    database.

    First, I created a rows variable that stores the total number of rows in the database, which is used to loop through
    the family tree database. Second, to determine the index (row) of the person, I chose to implement a for loop that
    iterates through each row (i) in the 1st column (indexed at 0) of the database. Importantly, the range function
    allows the for loop to iterate through the sequence of elements in the rows. On the condition the person matches the
    element in the database (i.e. boolean expression evalutes to true), the index variable is re-assigned to an integer.
    In the event the condition is not met, the function returns the original index variable that was assigned to no
    object (i.e. None).

    """
    index = None # 0
    rows = len(family) # 0
    for i in range(rows): # n+1
        if family[i][0] == person: # n
            index = i # 0
    return index # 0


def father(person, family):
    """ Returns the father of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family) as specified above.
    Output: The name of person's father, or None if the information is not in the database.

    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> father('Della Duck', duck_tree)
    'Quackmore Duck'
    >>> father('Huey Duck', duck_tree)

    >>> father('Daffy Duck', duck_tree)
    

    This is a list processing problem that seeks to identify the father of a person in a family tree database. The
    challenge is that the index (row) representing the set of relationships between the person, father and mother
    is unknown, thereby making it difficult to deduce the father of the person. In order to identify the father of the
    person, we implement the person_index function to identify the index of the person, and from the given row
    deduce the father of the person as listed in the second column. Importantly, the function should return nothing in
    the event the person is not found in the database.

    To determine the index (row) of the person, we enter the paramaters of the person_index function (person and family)
    and assign the index variable to the object (i.e. either an integer or None). On the condition the index is an
    integer (i.e. boolean expression evalutes to true), the function finds the father at the indentified index (row)
    in the 2nd column (indexed at 1) of the database and assigns the object to a dad variable.
    In the event the index is not an integer (i.e. boolean expression evaluates to false), the dad variable is assigned
    no object (i.e. None). The object of the dad variable is then returned.
    
    """
    index = person_index(person, family) # 2n+1
    if type(index) is int: # 1
        dad = family[index][1]
    else: # 1
        dad = None # 0
    return dad # 0


def mother(person, family):
    """ Returns the mother of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family) as specified above.
    Output: The name of person's mother, or None if the information is not in the database.

    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> mother('Hortense McDuck', duck_tree)
    'Downy ODrake'
    >>> mother('Fergus McDuck', duck_tree)

    >>> mother('Daffy Duck', duck_tree)

    
    This is a list processing problem that seeks to identify the mother of a person in a family tree database. The
    challenge is that the index (row) representing the set of relationships between the person, father and mother
    is unknown, thereby making it difficult to deduce the mother of the person. In order to identify the mother of the
    person, we implement the person_index function to identify the index of the person, and from the given row
    deduce the mother of the person as listed in the third column. Importantly, the function should return nothing in
    the event the person is not found in the database.

    To determine the index (row) of the person, we enter the paramaters of the person_index function (person and family)
    and assign the index variable to the object (i.e. either an integer or None). On the condition the index is an
    integer (i.e. boolean expression evalutes to true), the function finds the mother at the indentified index (row)
    in the 3rd column (indexed at 2) of the database and assigns the object to a mum variable.
    In the event the index is not an integer (i.e. boolean expression evaluates to false), the mum variable is assigned
    no object (i.e. None). The object of the mum variable is then returned.
    
    """
    index = person_index(person, family) # 2n+1
    if type(index) is int: # 1
        mum = family[index][2]
    else: # 1
        mum = None # 0
    return mum # 0


def children(person, family):
    """ Returns the children of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family) as specified above.
    Output: A list containing the names of all of person's children.
    
    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(children('Della Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> children('Donald Duck', duck_tree)
    []
    >>> sorted(children('Fergus McDuck', duck_tree))
    ['Hortense McDuck', 'Scrooge McDuck']
    >>> children('Donald Mallard', duck_tree)
    []

    This is a list processing problem that seeks to identify the children of a person within a family tree database.
    The challenge is that a person may have parents of their own in the database, so there needs to be a way of
    looping through the 2nd and 3rd columns to determine if the person is a father or mother, respectively. If the
    person is a parent, the approach would be obtain the index (row) or set of indices (rows) of the person, to then
    find the child or set of children of the parent as identified in the first column of the database. Importantly, if
    the person is not in the database, or the person is not a parent, the function should return an empty list.

    First, I created a rows variable and a columns variable that stores the total number of rows and columns of the
    database, which is used to loop through the database. Second, I created an indices variable and a kids variable and
    assigned each to an empty list. Accordingly, these lists are modified depending on whether the person is a parent
    or not. To determine if the person is a parent, I implemented a nested for loop that first iterates through the
    rows of the database (outer loop) before iterating through the columns of the database (inner loop). Importantly,
    the range function allows the for loop to iterate through the sequence of elements in the rows and columns. To note,
    the inner loop only needs to iterate through the 2nd (indexed at 1) and 3rd (indexed at 2) columns of the database
    as we want to determine if the person is a parent, hence why we specify the optional start and stop parameters of
    the range function as 1 and columns. For row (i) in column (j) of the database, if the element matches the person
    (i.e. boolean expression evalutes to true), then row i is appended to the indices list. Accordingly, using a for
    loop, we can iterate through the indices list and append the object to the kids list that corresponds to the kth
    index (row) in the first column (indexed at 0) of the database.
     
    """
    rows = len(family)
    columns = len(family[0])
    indices = []
    kids = []
    for i in range(rows):
        for j in range(1, columns):
            if family[i][j] == person:
                indices.append(i)
    for k in indices:
        kids.append(family[k][0])
    return kids


def grandparents(person, family):
    """ Returns the grandparents of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family) as specified above.
    Output: A list containing only the names of the grandparents of person that are stored in the database.
    
    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(grandparents('Scrooge McDuck', duck_tree))
    ['Dingus McDuck', 'Molly Mallard']
    >>> sorted(grandparents('Louie Duck', duck_tree))
    ['Hortense McDuck', 'Quackmore Duck']
    >>> grandparents('Fergus McDuck', duck_tree)
    []

    This is a list processing problem that seeks to identify the grandparents of a person in a family tree database.
    The first challenge is in establishing whether the person identifies as a child, which can be determined by looping
    through the 1st column of the database. In the event the person is a child, the next challenge is to identify
    whether the person has a father and mother. To determine the father and mother of the person, we can implement
    the father function and mother function, respectively.  Similarly, we can implement the father function and mother
    function to find the parents of the father and mother. This infers the person will have two sets of grandparents
    - one on the paternal side and one on the maternal side. So, the final challenge is in finding a way to
    concatenate the two sets of grandparents together into one list. Importantly, if the person is not in the database,
    the function should return an empty list. Moreover, if select parents or grandparents are unknown, the function
    should only return a list containing those grandparents in the database.

    First, I created a rows variable that stores the total number of rows in the database, which is used to loop through
    the database. Second, I created a g_parents variable assigned to an empty list. Accordingly, this list is
    modified depending on whether the person has grandparents on the paternal or maternal side. To determine if the
    person is a child, I implemented a for loop that iterates through each row (i) in the 1st column (indexed at 0) of
    the database. Importantly, the range function allows the for loop to iterate through the sequence of elements in the
    rows. On the condition the person matches the element in the database (i.e. boolean expression evalutes to true),
    the father and mother of the person can then be identified using the father and mother function. Note multiple
    assignment of the dad variable and mum variable to the outputs of the father function and mother function to avoid
    duplication of the function names. Similarly, using a for loop, we iterate through each row (i) in the 1st column
    (indexed at 0) of the database to check if the dad and mum identify as children in the database. In the event they
    do (i.e. boolean expression evaluates to true), the outputs of the father and mother function is then appended to
    the g_parents list. The g_parents list is then returned.

    """
    rows = len(family)
    g_parents = []
    for i in range(rows):
        if family[i][0] == person:
            dad, mum = father(person, family), mother(person, family)
    for i in range(rows):
        if family[i][0] == dad:
            g_parents.append(father(dad, family))
            g_parents.append(mother(dad, family))
    for i in range(rows):
        if family[i][0] == mum:
            g_parents.append(father(mum, family))
            g_parents.append(mother(mum, family))
    return g_parents


# Part 2: (due Week 11) #

def siblings(person, family):
    """ Returns the siblings of a person from a family tree database.

    Input: A person's name (person) and a family tree database (family)
           as specified above.
    Output: A list containing the names of all siblings, both half and full,
            of person that are stored in the database.
    
    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', None, 'Downy ODrake'],
    ...           ['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> siblings('Della Duck', duck_tree)
    ['Donald Duck']
    >>> sorted(siblings('Louie Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck']
    >>> siblings('Scrooge McDuck', duck_tree)
    ['Hortense McDuck']
    >>> siblings('Fergus McDuck', duck_tree)
    []
    >>> siblings('Daisy Duck', duck_tree)
    []
    
    This is a list processing problem that seeks to identify the siblings of a person in a family tree database.
    The first challenge is in establishing whether the person belongs to the family tree database, which can be
    determined by using the person_index function. Importantly, the siblings function should return an empty list in
    the event the person_index function returns no index. The next challenge is in diciphering the full- and half-
    siblings of the person. After determining the father and mother of the person using the father function and mother
    function, we can use if statements to distinguish the full and half siblings as we loop through the family tree
    database. Importantly, full siblings will have the same set of parents, whereas half siblings will only have one
    common parent either on the maternal or paternal side. Accordingly, the approach would be to utilise three if
    statements to check if the family member fits under one of three above categories. To note, the function should
    return an empty list in the event the person has no siblings in the database.

    First, I created a results (res) variable assigned to an empty list. Accordingly, this list is modified depending
    on whether any full or half siblings are found in the database. Next, I assigned three variables - index, dad and
    mum - to the results of the person_index, father and mother functions, respectively. Using an if statement,
    we evaluate the index variable to see if the person is within the database. If the index is of NoneType
    (i.e. Boolean expression is True), the function returns the res variable, otherwise it continues. Next, to
    determine if the person has any siblings, I implemented a for loop that iterates through each row (i) of the
    database. Importantly, the range function allows the for loop to iterate through the length of rows in the
    database. Then, I created three unique if statements and used the dad and mum variables to distinguish if the
    family member is a full or half sibling from the paternal or maternal side. If the family member in the ith row has
    the same dad in the father column (indexed at 1) and the same mum in the mother column (indexed at 2), the family
    member is a full sibling and is appended to the res list based on their unique position in the person column
    (indexed at 0) of the database. If the boolean expression evalutes to false, the function proceeds to determine
    if the family member is a half sibling from the maternal side in the next if statement. Following a nested
    if statement, the function first checks to see if the family member at the ith row has the same dad in the father
    column. If it doesn't (i.e. boolean expression evalutes to false), the function proceeds to check if the family
    member has the same mum in the mother column. Presuming the father of the family member is of NoneType, we
    would expect the mother of the family member to not be of NoneType as the database should have at the least
    information pertaining to one of their parents. Otherwise, the family member would cease to exist in the database
    since they would have no relation to anyone! Following the above logic, we check to see if mum is not of NoneType
    and whether the family member has the same mum in the mother column. If the boolean expression evaluates to True,
    the family member is a half sibling from the maternal side and is therefore appended to the res list based on their
    unique position in the person column. Applying the same logic, we can find whether any half siblings exist on the
    paternal side of the person in question. Finally, we use the in-built remove python function to remove the person
    from the res list as the person is also identified as a sibling. The res list is then returned.

    The time complexity of the siblings function is O(n) in the worst case. Firstly, The index, dad and mum variables
    all have n time complexity in the worst case (see three functions above for detailed analysis of the steps).
    Secondly, the for loop iterates through each row of the database through its entire length. In the very worst case,
    the function will run through each of the three if conditions. If this occurs, each if condition will have n time
    complexity. The boolean expression and append operation in the last if statement each has a constant time complexity
    of 1. Therefore, if the last condition is always reached, the boolean expression and append operation will each
    yield a time complexity of n. As n has highest order in the function, the siblings function has O(n) time
    complexity in the worst case.

    """
    res = []
    index, dad, mum = person_index(person, family), father(person, family), mother(person, family)
    if index is None:
        return res
    for i in range(len(family)):
        if family[i][1] == dad and family[i][2] == mum:
            res.append(family[i][0])
        elif family[i][1] != dad:
            if mum is not None and family[i][2] == mum:
                res.append(family[i][0])
        elif family[i][2] != mum:
            if dad is not None and family[i][1] == dad:
                res.append(family[i][0])
    res.remove(person)
    return res


from copy import deepcopy

def combine_trees(f1, f2):
    """ Combines two family tree databases to create a new family tree database.

    Input: Two family tree databases, f1 and f2.
    Output: A new family tree database, sorted by name, that merges f1
        and f2 together, combining any duplicate entries, or None if
        there is some conflict that prevents them from being merged.
    
    For example:
    >>> duck_tree = [['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', None, 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> duck_tree2 = [['Scrooge McDuck', 'Fergus McDuck', None],
    ...           ['Matilda McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard']]
    >>> combine_trees(duck_tree,duck_tree2)
    [['Della Duck', 'Quackmore Duck', 'Hortense McDuck'], ['Dewey Duck', None, 'Della Duck'], ['Donald Duck', 'Quackmore Duck', 'Hortense McDuck'], ['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'], ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'], ['Huey Duck', None, 'Della Duck'], ['Louie Duck', None, 'Della Duck'], ['Matilda McDuck', 'Fergus McDuck', 'Downy ODrake'], ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake']]
    >>> combine_trees(duck_tree,[['Donald Duck','Scrooge McDuck','Hortense McDuck']])
    
    >>> grandparents('Scrooge McDuck', combine_trees(duck_tree,duck_tree2))
    ['Dingus McDuck', 'Molly Mallard']
    >>> duck_tree
    [['Donald Duck', 'Quackmore Duck', 'Hortense McDuck'], ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'], ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'], ['Scrooge McDuck', None, 'Downy ODrake'], ['Huey Duck', None, 'Della Duck'], ['Dewey Duck', None, 'Della Duck'], ['Louie Duck', None, 'Della Duck']]
    >>> duck_tree2
    [['Scrooge McDuck', 'Fergus McDuck', None], ['Matilda McDuck', 'Fergus McDuck', 'Downy ODrake'], ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'], ['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard']]

    This is a list processing challenge that seeks to combine two family tree databases together to create a new sorted
    family tree database. The first challenge is in finding a way to iterate through the list of elements in the person
    column (indexed at 0) in each database to determine if any common family members exist. The approach would be to
    sort both databases in alphabetical order. Once the databases are sorted, we can iteratively compare each of the
    elements in the two sorted databases to single out the common family members in the person column until one of the
    sorted databases reaches the end of the length of the database. If any common family members are found, the approach
    would be to append the set of relationships of the common family members to two empty lists from each of the sorted
    databases to later compare and process. Simultaneously, we need to remove the set of relationships from a copy of
    each of the sorted databases so no duplicate entries of the common family members exist when we add the copies and
    the processed relationships toegether to form the brand new database. The next challenge is in comparing the two
    new lists together. Since the two new lists will have the exact same alphabetical listing of common family members
    as per the person column, we can follow a similar approach and simultaneously iterate through each row (i) of the
    two lists to denote any similarities or differences in the parental information of each family member. Importantly,
    we want to maximise the amount of information available for the family member in question, whilst ensuring no
    conflicting information exists between the lists of the family member. This can be achieved by implementing various
    if conditions. Importantly, the function should return None if conflicting parental information is found between the
    two lists for the family member. Otherwise, if no conflicting information is found, the function should append the
    updated rows to a new list, which will be added to the two copies of the sorted databases to form the new database
    with the most complete information.

    First, I used the in-built sorted python function to re-order the f1 database and f2 database by alphabet (based
    on the first column). Then, I assigned two variables (a and b) to deep copies (built in python function from the
    copy module) of the the sorted f1 and f2 databases, respectively. Importantly, we need to use the deep copy function
    to create fully independent clones of the f1 and f2 databases. If any common family members are found in the person
    column (indexed at 0), the f1 and f2 databases will be unaffected as the function will only remove the row entries
    from the deep copies. Next, I created two variables (i and j) to iterate through the f1 and f2 databases and
    assigned a value of 0 to each. Then, I created three new variables - common1, common2 and update - and assigned
    each to an empty list. The common1 and common2 variables will be modified depending on whether any common family
    members are found in the person column between the two databases. Then, once the two variables have been processed
    and the maximum amount of information has been extracted for the common family member (explained further below),
    the row is updated and appended to the update list. In the next step, I implemented a while loop to iterate through
    the f1 and f2 databases. Whilst the i and j variables are less than the length of the databases, the while loop
    will iterate through the databases in the ith row (f1 database) and jth row (f2 database) of the to determine
    if any common family members exist in the person column (indexed at 0). Making use of multiple if statements,
    we first check to see if the family member in f1 is alphabetically smaller than that family member in f2. If true,
    1 is augmented to the i iteration variable. If false, the function then checks to see if the family member in f1 is
    alphabetically larger than the family member in f2. If true, 1 augmented to the j variable. Otherwise, if neither
    conditions are met, this indicates the family members from both databases are the same. Accordingly, 1 is augmented
    to both the iteration variables, and the ith and jth rows are appended to the common 1 and common2
    lists, respecitively. Meanwhile, the ith and jth rows are removed from the a and b deep copies, respectively.
    Once the common family members are collated in the common1 and common2 lists, the next step is to compare the
    two lists. Since the ith and jth rows were appended to the common1 and common2 lists at the exact same time,
    we can directly compare the lists row by row since they will both have the exact same family member in the person
    column (indexed at 0). In this instance, I implemented a for loop that iterates through each row (i) of the
    lists. Importantly, the range function allows the for loop to iterate through the length of rows of the two lists.
    If the ith and jth rows are the same, the ith row from the common1 list is appended to the update list. Otherwise,
    the function will run through the else statment and will check to see if one of five nested conditions have been
    satisfied. Each condition tests various instances of missing (i.e. NoneType) and non-missing data in the father
    column (indexed at 1) and mother column (indexed at 2) in the common1 and common2 lists, collating the maximum
    amount of data and appending the data as a new row entry to the update list. Importantly, if neither of the first
    four conditions are satisfied, this infers the existence of conflicting information in the father or mother columns
    of both lists. In such an event, the function returns nothing since databases with conflicting information cannot be
    combined together. Finally, the a, b and update lists are combined and returned in alphabetical order (once again
    using the in-built sorted function in python).

    The time complexity of the combine_trees function is O(nlogn) in the worst case. The in-built sorted python function
    that is used to sort the two databases and the combined database has a time complexity of nlogn. In all cases, each
    of the deep copies of the two databases will have n*m time complexity where n represents the rows and m represents
    the columns of a table. However, m is usually ignored by convention and therefore the deep copies each have a
    time complexity of n. In the worst case, the while loop will have a time complexity of n as it will only stop
    once one of the i or j iteration variables exceeds the length of their respective databases. In the very worst case,
    the function will run through each of the three if conditions. If this occurs, each if condition will have n time
    complexity. Each of the operations and the augmented assigned statements in the last if statement each has a
    constant time complexity of 1. Therefore, if the last condition is always reached (i.e. two databases are exactly
    the same), each of the operations and augmented assignment statements will yield a time complexity of n. The for
    loop iterates through each row of the database through its entire length. Therefore, the for loop has a time
    complexity of n. In the very worst case, the function will run through the if statement and the first four if
    conditions under the nested else statement. Each has a constant time complexity of 1, so each of the four conditions
    will have a time complexity of n as the for loop iterates through the common1 and common2 lists. If the fourth
    condition under the nested else statement is always satisfied, the append operation will also have a time
    complexity of n since it has a constant time complexity of 1 in each iteration. As nlogn is of higher order than
    n, the combine_trees function has a time complexity of O(nlogn) in the worst case.

    """
    f1, f2 = sorted(f1), sorted(f2)
    a, b = deepcopy(f1), deepcopy(f2)
    i, j = 0, 0
    common1, common2, update = [], [], []
    while i < len(f1) and j < len(f2):
        if f1[i][0] < f2[j][0]:
            i += 1
        elif f1[i][0] > f2[j][0]:
            j += 1
        else:
            common1.append(f1[i]), a.remove(f1[i])
            common2.append(f2[j]), b.remove(f2[j])
            i += 1
            j += 1
    for i in range(len(common1)):
        if common1[i] == common2[i]:
            update.append(common1[i])
        else:
            if common1[i][1] is None and common2[i][2] is None:
                update.append([common1[i][0], common2[i][1], common1[i][2]])
            elif common1[i][2] is None and common2[i][1] is None:
                update.append([common1[i][0], common1[i][1], common2[i][2]])
            elif (common1[i][1] is not None and common2[i][1] is None) or (common1[i][2] is not None and common2[i][2] is None):
                update.append(common1[i])
            elif (common1[i][1] is None and common2[i][1] is not None) or (common1[i][2] is None and common2[i][2] is not None):
                update.append(common2[i])
            else:
                return None
    return sorted(a + b + update)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
