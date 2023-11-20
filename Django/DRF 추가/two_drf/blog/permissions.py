from rest_framework import permissions

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     '''
#     인증되어있는지 확인하여 조회만 가능하게 하고, 작성자만 수정 및 삭제 가능하게 합니다.
#     R = 모두 허용 
#     C = 로그인 사용자 허용
#     UD = 작성자만 허용
#     '''
#     # has_permission이 True여야 has_object_permission을 호출
    



class IsAuthorOrReadOnly(permissions.BasePermission):
    # 인증이 되어있는지 확인하여 조회만 가능하게 하고, 작성자만 수정, 삭제가 가능하게 합니다.
    def has_permission(self, request, view):
        '''
        GET, HEAD, OPTIONS 요청은 인증 여부와 상관없이 항상 True를 리턴합니다.
        '''
        if request.user and request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj):
        '''
        GET, HEAD, OPTIONS 요청은 인증 여부와 상관없이 항상 True를 리턴합니다.
        그 외 요청(PUT, DELETE)에 대해서는 작성자에 한해서만 True를 리턴합니다.
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user