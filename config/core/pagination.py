from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    Custom pagination that allows clients to set page_size via query params.
    """
    page_size_query_param = 'page_size'  # Allows the client to specify page size
    max_page_size = 100  # Prevents performance issues by limiting large requests

def get_paginated_response(self, data):
        return {
            "success": True,
            "message": "Data retrieved successfully",
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "data": data  # Instead of "results", we use "data"
        }