import os
import django
from dotenv import load_dotenv
from django.conf import settings
from django.db import connection

# Load environment variables
load_dotenv()

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_shop_django.settings')
django.setup()

def get_database_tables():
    """Get all tables in the database using Django's ORM"""
    try:
        # Get all table names
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            print("\nTables in the database:")
            for (table_name,) in cursor:
                print(table_name)
    except Exception as e:
        print(f"\nError accessing database: {e}")

if __name__ == '__main__':
    get_database_tables()
