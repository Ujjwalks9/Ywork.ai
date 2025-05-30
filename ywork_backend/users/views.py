
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse


@login_required
def google_auth_success(request):
    return JsonResponse({
        "message": "Welcome, session user!",
        "username": request.user.username
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])  # authenticated via session or JWT
def get_token_for_logged_in_user(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    return Response({
        "username": user.username,
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        "message": "Welcome API user!",
        "username": user.username
    })
