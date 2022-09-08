from rest_framework import generics
from .models import Thing
from .serializers import ThingSerializerList, ThingSerializerDetails
from .permissions import IsCreator


class ThingList(generics.ListCreateAPIView):
    permission_classes = (IsCreator,)
    serializer_class = ThingSerializerList

    def get(self, request, *args, **kwargs):
        self.queryset = Thing.objects.filter(creator=request.user.id)
        return self.list(request, *args, **kwargs)


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreator,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializerDetails
