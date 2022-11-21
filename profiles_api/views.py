from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

"""Create APIView class"""
class HelloWorldApiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializer

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


    def post(self, request):
        """Create a hello message with our name"""
        """First we will retreive the serializer first and pass in the data send by request object"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            """This retrieves the name field validatae by HelloSerializer class"""
            name=serializer.validated_data.get('name')
            """User f as prefix to add concat variables to a string in python"""
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request , pk=None):
        """Http put is used to update an entire object"""
        """pk=None signifies that there is no primary key needed to update"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        """like if we provide only few filds and not an entire object, it will update the given fields only"""
        return Response({'method':'PATCH'})


    def delete(self, request , pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})
