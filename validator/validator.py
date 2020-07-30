'''DNI and Dominican Cedula Validator version 0.0.1'''

import re

class Validator:

      def is_valid(self, document, numeration) ->bool:
          document = document.upper()

          if document=='DNI':
             if re.match('[0-9]{8}[A-Z]', numeration):
                return True   
             return False 

          elif document=='CEDULA':
             if re.match('[0-9]{11}', numeration):
                return True  
             return False

          return False 