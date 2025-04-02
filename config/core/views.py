from rest_framework.response import Response
from rest_framework import viewsets, status
from .utils import custom_api_response

class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet to apply custom response format to all API views.
    """

    def list(self, request, *args, **kwargs):
        """ Custom response for GET (list all objects) """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            return self.get_paginated_response(self.get_serializer(page, many=True).data)  # ✅ Serialize data

        serializer = self.get_serializer(queryset, many=True)  # ✅ Serialize data
        return custom_api_response(message="Data retrieved successfully", data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """ Custom response for GET (retrieve single object) """
        instance = self.get_object()
        serializer = self.get_serializer(instance)  # ✅ Serialize data
        return custom_api_response(message="Data retrieved successfully", data=serializer.data)

    def create(self, request, *args, **kwargs):
        """ Custom response for POST (create object) """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate input
        self.perform_create(serializer)  # Save object
        
        return custom_api_response(
            message="Created successfully",
            data=serializer.data,  # ✅ Ensure serialized data is returned
            status_code=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        """ Custom response for PUT/PATCH (update object) """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return custom_api_response(
            message="Updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """ Custom response for DELETE """
        super().destroy(request, *args, **kwargs)
        return custom_api_response(
            message="Deleted successfully",
            data=None,
            status_code=status.HTTP_204_NO_CONTENT
        )

    def get_paginated_response(self, data):
        """ Custom paginated response """
        return Response({
            "success": True,
            "message": "Data retrieved successfully",
            "count": self.paginator.page.paginator.count,
            "next": self.paginator.get_next_link(),
            "previous": self.paginator.get_previous_link(),
            "data": data  # ✅ Ensure serialized data is passed
        }, status=status.HTTP_200_OK)
