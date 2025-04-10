from bs4 import BeautifulSoup

# to get the home.html file -> need to know how to work with files

# open the file with read only format
with open('home.html', 'r') as html_file:
    content= html_file.read()
    # print(content)
    
    # create an instance oif beautiful soupo and set the parser and the document to be scrappeed
    soup=BeautifulSoup(content, 'lxml')
    #   soup is an instance, content is being parsed using 'lxml' parsing
    # print(soup.prettify())
    # now this soup contains the parsed content

    # tags=soup.find('h5')  searched and brings only the first matching tag
    courses=soup.find_all('h5')
    print(courses)
    # since we have a list we need to iterate only each element
    for course in courses:
        print(course.text)         # .text gives the text inside the tag


    print()
    # Now our task will be to print each courses with details

    course_card=soup.find_all('div', class_='card')
    # print(course_card)

    for x in course_card:
        name = x.h5.text
        price = x.a.text.split()[-1]

        # Syntax for Split Method : text.split('seperator')
        # if no seperator is given => Whitespaces

        print(f"course name : {name}")
        print(f"course price : {price}")

        # see course price is the last word in the string -> use 'split' method
