import os
from datetime import datetime

def count_frequencies(filename, date, ga_assigned, name,month_assigned):
    frequencies = {}
    total_count = 0

    # Read the input file and count frequencies
    with open(filename, 'r') as file:
        for line in file:
            number = line.split()[0]
            frequencies[number] = frequencies.get(number, 0) + 1
            total_count += 1

    # Format date
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%b %-d, %Y')

    # Calculate unregistered
    unregistered = ga_assigned - total_count

    # Ensure the reports directory exists
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Create report file path
    report_filename = os.path.join(reports_dir, f"{name}-{month_assigned}_report_{date}.txt")

    # Write the report
    with open(report_filename, 'w') as report:
        report.write(f"Report as of {formatted_date}\n\n")
        report.write(f"• GA Registered: {total_count}\n")
        report.write(f"• Unregistered: {unregistered}\n\n")
        report.write("Details of registered:\n\n")

        # Sort frequencies by count in descending order
        for number, count in sorted(frequencies.items(), key=lambda x: (-x[1], x[0])):
            report.write(f"• {number}: {count}\n")

# Example usage
count_frequencies('data.txt', '2025-02-16', 100, "Moha", "Jan")
