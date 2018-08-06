import urllib3
import json


urllib3.disable_warnings()
https = urllib3.PoolManager()
main_url_ebi = 'https://www.ebi.ac.uk/biosamples/samples'


class Api_client:

    list_of_status = {
            200: 'The response was ok.',
            201: 'Resource was created',
            400: 'The request was malformed. Change the request',
            401: 'Unauthorized',
            403: 'Forbidden for this request',
            404: 'Resource not found',
            405: 'Method not allowed'
        }

    @classmethod
    def control_errors_from_request(cls, status):
        """
        Control de status errors requested made to EBI API
        """
        to_continue, return_result = True, None
        status = int(status)
        if status != 200:
            to_continue = False
        return_result = cls.list_of_status.get(status, 'Wrong Status')
        return to_continue, return_result


    @classmethod
    def get_method_client_method(cls, url_formed):
        """
        Reusable method GET
        :return tuple. if is ok the response. If the response is ok will return data as a Json
        otherwise will return the message according to Status code.
        """
        request_url = https.request('GET', url_formed)
        response_is_ok, response = cls.control_errors_from_request(request_url.status)
        if response_is_ok:
            response = json.loads(request_url.data.decode('utf-8'))
        return response_is_ok, response


    @classmethod
    def get_accessions_by_filter(cls, attribute, value):
        """
        : return the name of accession.
        : IF does not exist print the list_of_status text
        """
        # Transform the value and attribute.
        # If the value is full of spaces do not include the value in the URL
        attribute = attribute.replace(' ','+')
        value = value.replace(' ', '+') if not value.isspace() else None
        url_formed = main_url_ebi+'?filter=attr:{attribute}:{value}'.format(attribute=attribute, value=value ) if value else main_url_ebi+'?filter=attr:{attribute}'.format(attribute=attribute)
        response_is_ok, data = cls.get_method_client_method(url_formed)
        response = data
        if response_is_ok:
            _embedded = data.get('_embedded')
            if (_embedded is not None):
                samples = _embedded.get('samples')
                if samples is not None:
                    response = ''
                    for sample in samples:
                        response = response + sample.get('accession') + ', '
            else:
                response = ' No Samples found'

        return response


    @classmethod
    def get_name_by_accession(cls, accession):
        """
        : return the name of accession.
        : IF does not exist print the list_of_status text
        """
        url_formed = main_url_ebi+'/{accession}'.format(accession=accession)
        response_is_ok, data = cls.get_method_client_method(url_formed)
        response = data
        if response_is_ok:
            if (data.get('name') is not None):
                response = data.get('name')
        return response


    @classmethod
    def total_number_of_samples(cls):
        """
        :return -1 if any error, other case it is ok
        """
        url_formed = main_url_ebi
        response = -1
        response_is_ok, data = cls.get_method_client_method(url_formed)
        if response_is_ok:
            if (data.get('page') is not None) and (data.get('page').get('totalElements')):
                response = data.get('page').get('totalElements')
        return response
