from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import decimal

class Command(BaseCommand):
    """
    Custom Django management command to seed the database with initial data.
    """
    help = 'Seeds the database with sample listings data for the ALX Travel App'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('Starting database seeding process...'))

        # Clear existing data to prevent duplicates on re-runs
        self.stdout.write('Deleting old data...')
        Listing.objects.all().delete()
        # Only delete non-superuser accounts to keep admin access
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write(self.style.SUCCESS('Old data deleted.'))
        self.stdout.write('Creating new data...')

        # Create a sample user to act as the owner of the listings
        try:
            # Use get_or_create to avoid errors if the user already exists
            owner, created = User.objects.get_or_create(
                username='property_owner',
                defaults={'first_name': 'Alex', 'last_name': 'Owner', 'email': 'owner@alx.com'}
            )
            if created:
                owner.set_password('securepassword123')
                owner.save()
                self.stdout.write(self.style.SUCCESS(f'Created sample user: {owner.username}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating owner user: {e}'))
            return


        # Sample listings data with a Nigerian context
        listings_data = [
            {
                'title': 'Luxury Lekki Apartment with Ocean View',
                'description': 'A stunning and modern apartment located in the heart of Lekki Phase 1. Enjoy breathtaking views of the Atlantic Ocean.',
                'address': '15 Admiralty Way, Lekki, Lagos, Nigeria',
                'price_per_night': decimal.Decimal('95000.00'),
                'bedrooms': 3,
                'bathrooms': 3,
                'owner': owner
            },
            {
                'title': 'Cozy Getaway in Ikeja GRA',
                'description': 'A quiet and serene bungalow perfect for a family vacation or a business trip. Close to the airport.',
                'address': '24 Oduduwa Crescent, Ikeja GRA, Lagos, Nigeria',
                'price_per_night': decimal.Decimal('60000.50'),
                'bedrooms': 2,
                'bathrooms': 2,
                'owner': owner
            },
            {
                'title': 'Modern Flat in Central Abuja',
                'description': 'Experience the capital city from this stylish and secure flat in Wuse 2. Ideal for professionals and tourists.',
                'address': '82 Adetokunbo Ademola Crescent, Wuse 2, Abuja, Nigeria',
                'price_per_night': decimal.Decimal('75000.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'owner': owner
            },
            {
                'title': 'Historic Calabar Villa',
                'description': 'Stay in a beautifully restored colonial villa near the Calabar Museum. A unique cultural experience.',
                'address': '19 Eyoma Street, Calabar, Cross River, Nigeria',
                'price_per_night': decimal.Decimal('45000.00'),
                'bedrooms': 4,
                'bathrooms': 3,
                'owner': owner
            }
        ]

        # Create Listing objects in the database
        for data in listings_data:
            try:
                listing = Listing.objects.create(**data)
                self.stdout.write(self.style.SUCCESS(f'Successfully created listing: "{listing.title}"'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating listing "{data["title"]}": {e}'))


        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
