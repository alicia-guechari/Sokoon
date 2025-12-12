from rest_framework import generics, permissions
from .models import DailyPositiveCard
from .serializers import *
# from rest_framework.renderers import JSONRenderer

class DailyPositiveCardListCreateView(generics.ListCreateAPIView):
    queryset = DailyPositiveCard.objects.all()
    serializer_class = DailyPositiveCardSerializer
    # permission_classes = [permissions.IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
        

class DailyPositiveCardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyPositiveCard.objects.all()
    serializer_class = DailyPositiveCardSerializer
    permission_classes = [permissions.IsAdminUser]

class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class JournalListCreateView(generics.ListCreateAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class JournalRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(student=self.request.user)