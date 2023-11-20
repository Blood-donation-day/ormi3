from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request):
    # request.user는 인증된 사용자의 정보를 담고 있습니다.
    print('request.user: ', request.user)
    print('request.data: ', request.data)
    print('request.auth: ', request.auth)
    print('request.authenticators: ', request.authenticators)
    print('request.content_type: ', request.content_type)
    
    content = {'message': f'반갑습니다!, {request.user}님!'}
    return Response(content)