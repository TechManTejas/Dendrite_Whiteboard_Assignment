from rest_framework import viewsets, status
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Whiteboard
from .serializers import WhiteboardSerializer, InvitationSerializer

class WhiteboardViewSet(viewsets.ModelViewSet):
    serializer_class = WhiteboardSerializer

    def get_queryset(self):
        # Only return whiteboards created by the current user
        return Whiteboard.objects.filter(host=self.request.user)

    def perform_create(self, serializer):
        # Set the host (creator) of the whiteboard to the current user
        serializer.save(host=self.request.user)


class ClientWhiteboardViewSet(viewsets.ModelViewSet):
    serializer_class = WhiteboardSerializer

    def get_queryset(self):
        # Only return whiteboards where the current user is a client
        return Whiteboard.objects.filter(clients=self.request.user)
    

class InviteeWhiteboardViewSet(viewsets.ModelViewSet):
    serializer_class = WhiteboardSerializer

    def get_queryset(self):
        # Only return whiteboards where the current user is an invitee
        return Whiteboard.objects.filter(invitees=self.request.user)
    

class WhiteboardInvitationViewSet(viewsets.ViewSet):
    def send_invitation_email(self, email, whiteboard):
        # Implement the logic to send invitation email
        # You can use Django's email functionality or a third-party library like sendgrid

        # For example (replace with your email sending logic):
        subject = 'Invitation to collaborate on a whiteboard'
        message = f'You have been invited to collaborate on the whiteboard "{whiteboard.title}"'
        # send_mail(subject, message, 'your@gmail.com', [email])

    def create(self, request, whiteboard_id=None):
        whiteboard = Whiteboard.objects.get(pk=whiteboard_id)

        serializer = InvitationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        # Check if the user is already a client or invitee
        if email in whiteboard.clients.values_list('email', flat=True) or \
                email in whiteboard.invitees.values_list('email', flat=True):
            return Response({'detail': 'User is already a client or invitee.'}, status=status.HTTP_400_BAD_REQUEST)

        # Send invitation email
        self.send_invitation_email(email, whiteboard)

        # Update the invitees of the whiteboard
        whiteboard.invitees.add(User.objects.get(email=email))

        return Response({'detail': 'Invitation sent successfully.'}, status=status.HTTP_200_OK)