from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        """
        {
            'basic_info': {
                'file_number': '2024-3337674-21', 
                'filing_date': '11/14/2024 3:57:03 PM', 
                'lapse_date': '11/15/2029 3:57:03 PM', 
                'status': 'A - Active'
            }, 
            'actions': [
                {'Action': 'Initial financing Statement', 'File Date': '11/14/2024 3:57:03 PM', 'Status': 'Active - Filed online'}
            ], 
            'names': [
                {'Name Role': 'DebtorEagle Buildings, LLC', 'Date Added': '11/14/2024 3:57:03 PM', 'Address': '1184 Hutchens RoadMurray KY 42071'}, 
                {'Name Role': 'Secured PartyThe Murray Bank', 'Date Added': '11/14/2024 3:57:03 PM', 'Address': '405 South 12th StreetMurray KY 42071'}, 
                {'Name Role': 'FilerThe Murray Bank', 'Date Added': '11/14/2024 3:57:03 PM', 'Address': '405 South 12th StreetMurray KY 42071'}
            ], 
            'collateral_description': {'date_filed': '11/14/2024 3:57:03 PM', 'description': 'ALL OF DEBTORS BUSINESS ASSETS INCLUDING BUT NOT LIMITED TO FURNITURE, FIXTURES, EQUIPMENT, INVENTORY, GENERAL INTANGIBLES, ACCOUNTS RECEIVABLE, ACCOUNTS, CHATTEL PAPER, DEPOSIT ACCOUNTS, LETTER OF CREDIT RIGHTS, PAYMENT INTANGIBLES, PROMISSORY NOTES, SOFTWARE, PATENTS, COPYRIGHTS, LICENSES, CUSTOMER LISTS, CONTRACTS, AND CONTRACT RIGHTS, WHETHER ANY OF THE FOREGOING IS OWNED NOW OR ACQUIRED LATER; ALL ACCESSIONS, ADDITIONS, REPLACEMENTS AND SUBSTITUTIONS RELATING TO ANY OF THE FOREGOING; ALL RECORDS OF ANY KIND RELATING TO ANY OF THE FOREGOING, ALL PROCEEDS WHETHER CASH OR NON-CASH, RELATING TO ANY OF THE FOREGOING (INCLUDING INSURANCE, GENERAL INTANGIBLES AND ACCOUNTS PROCEEDS)'}, 
            'images': [
                {'doc_type': 'UCC Filing - Initial financing Statement', 'link': '/uccscans/74/2024-3337674-21-2156229-U-20241114-pu.pdf', 'tiff_image': '', 'file_date': '11/14/2024 3:57:03 PM', 'pages': '1'}
            ]
        }
        """
        context = {'message': 'Welcome to the Home App!'}
        return render(request, 'home/index.html', context)