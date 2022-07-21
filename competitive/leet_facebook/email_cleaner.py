import re

html_string = "Lorem ipsum dolor sit amet, some.email@mydomain.com consectetur " \
              "adipisicing elit, anotheremail@somedomain.com sed do eiusmod tempor " \
              "incididunt ut labore 01234 567 891 et dolore +341234 567891 magna aliqua. " \
              "012 345 6789 Ut enim http://www.somedomain.comad minim www.somedoma.com veniam, " \
              "quis somedomain.com nostrud exercitation http://somedomain.com ullamco laboris nisi " \
              "ut aliquip ex ea commodo consequat."

emailRegex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

mo = emailRegex.match(html_string)