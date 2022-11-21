from rest_framework.views import APIView
from rest_framework.response import Response


"""Create APIView class"""
class HelloWorldApiView(APIView):
    """Test API View"""


    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_api_view=[
        'Uses HTTP methods as function',
        'Is similar to a traditional Django view',
        'Gives you the most control over the application logic',
        'Is mapped manually to urls'
        ]

        """Response needs to contain either list or dictionary. We will be passing dictionary here"""
        """It converts Response object to json"""
        return Response({'message':'Hello','an_api_view':an_api_view})
