import csv
import io

# Allowed field names.
FIELD_NAMES = {'firstname', 'lastname', 'street', 'zip', 'city', 'image'}


def parse_contacts_csv(csv_string: str):
    """
    Parses CSV string and yields a dictionary for each record.
    """
    for row in csv.DictReader(io.StringIO(csv_string)):
        # Drop extra fields.
        yield {
            key: value
            for key, value in row.items()
            if key in FIELD_NAMES
        }
