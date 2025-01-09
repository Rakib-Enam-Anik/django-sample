from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class UploadedImageListCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        images = UploadedImage.objects.all()
        serializer = UploadedImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


