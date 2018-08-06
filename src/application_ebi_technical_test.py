import sys
from client_api_ebi import *

class Application:

    def __init__(self):
        pass

    def close():
        """
        Function to exit the Application.
        """
        sys.exit()

    def get_name_by_accession():
        accession = input("Accession: ")
        return Api_client.get_name_by_accession(accession)

    def get_accessions_by_filter():
        attribute = input("Attribute: ")
        value = input("Value: ")
        return Api_client.get_accessions_by_filter(attribute, value)


    def get_examples_queries_results():
        given_accession = """
        Accession    |  Name
        SAMEA1507265 |  source GSM1000387 1
        SAMD00000328 |  SAMD00000328
        SAMEA1481290 |  source GSM898528 1
        """

        given_attribute_query = """
        Attribute    |  Value.        | Results
        organism     |  homo sapiens  | SAMN08025863, SAMN08025864
        organism     |  Homo Sapeins  | No samples found
        description title |  BioSample1 | SAMN08025863
        INSDC last update |           | SAMD00000001, SAMD00000006, SAMD00000007, SAMD00000008, SAMD00000009, SAMD00000010, SAMD00000011, SAMD00000012, SAMD00000014, SAMD00000021, SAMD00000325, SAMD00000326, SAMD00000327, SAMD00000328, SAMD00000330, SAMD00000331, SAMD00000332, SAMD00000333, SAMD00000334, SAMD00000341
        """

        print(given_accession, given_attribute_query)

    MENU_OPTIONS = {
        1: { 'title': 'Get total number of samples', 'function': Api_client.total_number_of_samples, 'response': 'Total number of samples: ' },
        2: { 'title': 'Get Name for an given Accession', 'function': get_name_by_accession, 'response': 'Name of the given accession: '},
        3: { 'title': 'Get Filtered Accessions for an given Attribute and Value', 'function': get_accessions_by_filter, 'response': 'Accessions: '},
        4: { 'title': 'Examples of such queries and results', 'function': get_examples_queries_results, 'response': ''},
        5: {'title':'Exit', 'function': close}
    }

    @classmethod
    def print_menu_options(cls):
        print('Choose a menu')
        # Print menu options
        for key, value in cls.MENU_OPTIONS.items():
            print(key, value.get('title'))

    @classmethod
    def get_selected_menu_item(cls):
        """
        :return a tuple, function_to_call and the text for print the response
        """
        # Read input from
        try:
            menu = int(input("Option: "))
            choosen_option = cls.MENU_OPTIONS.get(menu)
            function_to_call = choosen_option.get('function')
            response_text = choosen_option.get('response')
            return function_to_call, response_text
        except ValueError as e:
            raise Exception('Invalid Option. ')

    @classmethod
    def call_function_get_response(cls, function_to_call, response_text):
        result = function_to_call()
        print(response_text, result, '\n')


if __name__ == "__main__":
    while(True):
        try:
            Application.print_menu_options()
            function_to_call, response_text = Application.get_selected_menu_item()
            Application.call_function_get_response(function_to_call, response_text)
        except Exception as e:
            print('Error in API Client EBI, {} \n\r'.format(e))
