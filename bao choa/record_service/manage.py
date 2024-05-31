#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'record_service.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "record_service.settings")

    import django
    django.setup()

    # Override default port for runserver command
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "7000"
    runserver.default_addr = "192.168.0.103"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


 #http://192.168.0.103:7000/search_record/