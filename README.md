# python-security-log-analyzer
A beginner cybersecurity project for detecting suspicious login activity using Python
# Python Security Log Analyzer

## Project Overview
A beginner cybersecurity project that uses Python to analyse simulated authentication logs and detect repeated failed login attempts.

## Objectives
. Read and process security log files.
. Identify failed authentication attempts.
. Count failed logins by IP address.
. Generate alerts when repeated failures exceed a defined threshold.

## Technologies Used
- Python 3
- Visual Studio Code
- GitHub

## Detection Method
The program counts failed login attempts for each IP address and raises an alert when three or more failures are detected.

## Limitations
This is a basic educational detector. It does not currently use time windows, verify real attacks or process arbitrary log formats.

## Future Improvements
- Add time-based detection.
- Export results to CSV.
- Create incident investigation reports.
- Support real-world log formats using anonymised data.
