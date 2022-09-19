"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)

        for approach in results:
            row = []
            row.append(approach.time)
            row.append(approach.distance)
            row.append(approach.velocity)
            row.append(approach.neo.designation)
            row.append(approach.neo.name if approach.neo.name else '')
            row.append(approach.neo.diameter if approach.neo.diameter else '')
            row.append(approach.neo.hazardous)

            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    file_content = []

    for approach in results:
        approach_dict = approach.serialize()

        approach_dict['neo'] = approach.neo.serialize()
        file_content.append(approach_dict)

    with open(filename, 'w') as outfile:
        json.dump(file_content, outfile, indent=2)
