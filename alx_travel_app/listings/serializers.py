from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Converts Listing model instances to JSON format for API responses.
    """
    class Meta:
        model = Listing
        # '__all__' includes all fields from the Listing model automatically.
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Converts Booking model instances to JSON format.
    """
    class Meta:
        model = Booking
        # Includes all fields from the Booking model.
        fields = '__all__'
