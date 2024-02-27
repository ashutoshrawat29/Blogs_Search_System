from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seo import doc_, doc_feedback
@api_view(['GET', 'POST'])
def search_(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        print(request.data["entered_query"])
        
        return Response({"data":doc_(request.data["entered_query"])})
@api_view(['GET', 'POST'])
def feedback_(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        print(request.data["entered_query"])
        
        return Response({"data":doc_feedback(request.data["entered_query"],request.data["rel_ids"],request.data["nonrel_ids"],request.data["choice"])})
