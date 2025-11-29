import sys

if len(sys.argv) != 5:
    print("Usage: python event.py <event_name> <venue> <date> <organiser_name>")
    sys.exit(1)
    
    event_name = sys.argv[1]
    venue = sys.argv[2]
    date = sys.argv[3]
    organiser_name = sys.argv[4]    
else:
    print(" ")
    event_name = "Birthday"
    venue = "Hubli"
    date = "1/12/2025"
    organiser_name = "Keerti"

    print("Event Name: ", event_name)
    print("Venue: ", venue)
    print("Date: ", date)
    print("Organiser Name: ", organiser_name)

