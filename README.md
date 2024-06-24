<br/>
<div align="center">
  <a href="https://github.com/ibnaleem/snapscoretracker/releases">
    <img src="https://cdn.freebiesupply.com/logos/large/2x/snapchat-logo-png-transparent.png" alt="Logo" width="20%" height="20%">
  </a>
  
  <h2 align="center">SnapscoreTracker</h3>

  <p align="center">
    👻 A Snapscore tracker that reports various metrics such as time differences, score increases, snaps sent and received, snap rates per minute, hour, and day and much more 
    <br />
    <br />
    <a href="https://github.com/ibnaleem/snapscoretracker/issues">Report Bugs</a>
  </p>
</div>

---------------------------------------
| Date                | Time Difference          | Snapscore | Increase | Increase Difference | Snaps Sent | Number of Snaps Sent Since Last Time | Snaps Opened | Number of Snaps Opened Since Last Time | Number of People Snapped | Number of People Snapped Since Last Time | Snap Rate / min     | Snap Rate / hour        | Snap Rate / day      |
|---------------------|--------------------------|-----------|----------|---------------------|------------|---------------------------------------|--------------|-----------------------------------------|--------------------------|-----------------------------------------|----------------------|-------------------------|----------------------|
| 2024-06-13 18:46:00 |                          | 179396    | 0        |                     | 0          |                                       | 0            |                                         | 0                        |                                 |                      |                         |                      |
| 2024-06-13 18:50:00 | 4 minutes                | 179400    | 4        | 4.0                 | 2          | 2.0                                   | 2            | 2.0                                     | 2                        | 2.0                                   | 1.0                  |                         |                      |
| 2024-06-13 19:04:00 | 14 minutes               | 179405    | 5        | 1.0                 | 2          | 0.0                                   | 3            | -1.0                                    | 2                        | 0.0                                   | 0.3571428571428571    |                         |                      |
| 2024-06-14 14:29:00 | 19 hours, 25 minutes     | 179512    | 107      | 102.0               | 53         | 51.0                                  | 54           | 51.0                                    | 53                       | 51.0                                  | 0.0918454935622317    | 5.883347421808961       |                      |
| 2024-06-14 15:40:00 | 1 hours, 11 minutes      | 179514    | 2        | -105.0              | 1          | -52.0                                 | 1            | -51.0                                   | 1                        | -52.0                                 | 0.028169014084507     | 1.6901408450704225      |                      |
| 2024-06-14 15:46:00 | 6 minutes                | 179518    | 4        | 2.0                 | 2          | 1.0                                   | 2            | 1.0                                     | 2                        | 1.0                                   | 0.6666666666666666    |                         |                      |
| 2024-06-14 15:56:00 | 10 minutes               | 179523    | 5        | 1.0                 | 2          | 0.0                                   | 3            | -1.0                                    | 2                        | 0.0                                   | 0.5                  |                         |                      |
| 2024-06-14 16:08:00 | 12 minutes               | 179531    | 8        | 3.0                 | 4          | 2.0                                   | 4            | 3.0                                     | 4                        | 2.0                                   | 0.6666666666666666    |                         |                      |
| 2024-06-14 16:18:00 | 10 minutes               | 179534    | 3        | -5.0                | 1          | -3.0                                  | 2            | -4.0                                    | 1                        | -3.0                                 | 0.3                  |                         |                      |
| 2024-06-14 16:18:30 | 30 seconds               | 179537    | 3        | 0.0                 | 1          | 0.0                                   | 2            | 0.0                                     | 1                        | 0.0                                   |                      |                         |                      |
| 2024-06-14 16:52:00 | 33 minutes, 30 seconds   | 179543    | 6        | 3.0                 | 3          | 2.0                                   | 3            | 3.0                                     | 3                        | 2.0                                   | 0.2727272727272727    | 24.507042253521128      |                      |
| 2024-06-14 17:11:00 | 19 minutes               | 179549    | 6        | 0.0                 | 3          | 0.0                                   | 3            | 0.0                                     | 3                        | 0.0                                   | 0.3157894736842105    |                         |                      |
| 2024-06-14 17:18:00 | 7 minutes                | 179551    | 2        | -4.0                | 1          | -2.0                                  | 1            | -2.0                                    | 1                        | -2.0                                 | 0.2857142857142857    |                         |                      |
| 2024-06-14 17:28:00 | 10 minutes               | 179552    | 1        | -1.0                | 0          | -1.0                                  | 1            | -2.0                                    | 0                        | -1.0                                 | 0.1                  |                         |                      |
| 2024-06-14 18:10:00 | 42 minutes               | 179562    | 10       | 9.0                 | 5          | 5.0                                   | 5            | 6.0                                     | 5                        | 5.0                                   | 0.238095238095238     | 14.615384615384617      |                      |
| 2024-06-14 19:07:00 | 57 minutes               | 179564    | 2        | -8.0                | 1          | -4.0                                  | 1            | -4.0                                    | 1                        | -4.0                                 | 0.0350877192982456    |                         | 165.6986301369863    |

```
python3 main.py -h
usage: Snapscore Tracker [-h] -u USERNAME -s SNAPSCORE [-t TIME] [-a AVERAGE]

👻 A Snapscore tracker that reports various metrics such as time differences,
score increases, snaps sent and received, snap rates per minute, hour, and day
and much more.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Snapchat username to track
  -s SNAPSCORE, --snapscore SNAPSCORE
                        Snapscore to log
  -t TIME, --time TIME  The time you want to log the Snapscore in Y-m-d H:M:S
                        format. Example: 2024-06-15 12:00:00 will log the
                        Snapscore at 12:00:00 on June 15, 2024. If not
                        provided, the current time will be used. Use this
                        feature if you want to log the Snapscore at a specific
                        time. WARNING: Current time can be inaccurate by an
                        hour: 2024-06-15 12:00:00 will log the Snapscore at
                        11:00:00 on June 15, 2024. Using this parameter will
                        fix this issue.
  -a AVERAGE, --average AVERAGE
                        Calculate the mean of a column from the logs

Contribute: https://github.com/ibnaleem/snapscoretracker
```
## Installation
> 💡 [Install Python if you don't have it already](https://www.python.org/downloads/)
#### Clone this repository:
```
$ git clone https://github.com/ibnaleem/snapscoretracker.git
```
#### Install dependencies:
```
$ pip install -r requirements.txt
```
#### Create `/logs` directory:
```
$ mkdir logs
```
#### Create `{username}_logs.csv` file:
```
$ touch ibnaleem_logs.csv # replace {username} with the username of the Snapchat account you're tracking
```
#### Run the script
```
$ python3 main.py -u {username} -s {snapscore} -t {time in Y-m-d H:M:S format}
```
## Features
- `Date` - the date ***you*** logged the Snapscore
- `Time Difference` - the difference between the previous datetime and the new datetime (eg. a difference of 5 minutes will be reported if you log another snapscore 5 minutes later)
- `Snapscore` - the Snapscore
- `Increase` - the increase since the previous snapscore
- `Increase Difference` - the difference between the previous increase and the new increase (a negative increase implies the person is snapping fewer people than before)
- `Snaps Sent` - the number of Snaps sent
- `Number of Snaps Sent Since Last Time` - the difference between the previous `Snaps Sent` and the new `Snaps Sent` (a negative implies the person has sent fewer snaps than before)
- `Snaps Opened` - the number of Snaps opened
- `Number of Snaps Openeed Since Last Time` - the difference between the previous `Snaps Opened` and the new `Snaps Opened` (a negative implies the person has opened fewer snaps than before)
- `Number of People Snapped` - the number of people they've Snapped; equivalent to `Snaps Sent`
- `Number of People Snapped Since Last Time` - the difference between the previous `NoPSSLT` and the new `NoPSSLT` (a negative implies the person has talked to fewer people than before)
- `Snap rate / min` - the number of Snaps sent per minute
- `Snap rate / hour` - the number of Snaps sent per hour 
- `Snap rate / day` - the number of Snaps sent per day

> ⚠️ Only `Increase Difference`, `Number of Snaps Sent Since Last Time`, `Number of Snaps Opened Since Last Time`, `Number of People Snapped Since Last Time` can hold negative values; if any other column contains negative values, you've likely entered a Snapscore less than the previous (e.g entering 170,000 instead of 180,000)
<details close>
<summary>💡 Calculate Average of a column</summary>
<br>
  To calculate the mean value of a column, find the column name in the <code>.csv</code> file and append it to the <code>-a</code> or <code>--average</code> argument:
<pre>$ python3 main.py -u {username} -a Increase</pre>
You may need to wrap the column name in quotes (<code>""</code>) if it contains spaces:
<pre>$ python3 main.py -u {username} -a "Snap rate / min"</pre>
</br>
</details>

## Built With
- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Rich](https://github.com/Textualize/rich)
## LICENSE
This repository is under the [MIT License](https://github.com/ibnaleem/snapscoretracker/blob/main/LICENSE)
## Created By
[Ibn Aleem](https://www.linkedin.com/in/shaffan-aleem-b7a852255/)

## Contributing
I welcome contributions from the community and appreciate the time and effort put into making [SnapscoreTracker](https://github.com/ibnaleem/gnupg-discord) better. To contribute, please follow the guidelines and steps outlined below:

> Note: **_Your pull request will be closed if you do not specify the changes you've made._**

### Fork the Repository
Start by [forking this repository](https://github.com/ibnaleem/snapscoretracker/fork). You can do this by clicking on the ["Fork"](https://github.com/ibnaleem/snapscoretracker/fork) button located at the top right corner of the GitHub page. This will create a personal copy of the repository under your own GitHub account.

### Clone the Repository
Next, clone the forked repository to your local machine using the following command:
```bash
$ git clone https://github.com/yourusername/snapscoretracker.git
```
Navigate to the cloned directory:
```bash 
$ cd snapscoretracker
```
### Create a New Branch
Before making any changes, it's recommended to create a new branch. This ensures that your changes won't interfere with other contributions and keeps the main branch clean. Use the following command to create and switch to a new branch:
```bash
$ git checkout -b branch-name
```
### Make the Desired Changes
Now, you can proceed to make your desired changes to the project. Whether it's fixing bugs, adding new features, improving documentation, or optimising code, your efforts will be instrumental in enhancing the project.

### Commit and Push Changes
Once you have made the necessary changes, commit your work using the following commands:
```bash
$ git add .
$ git commit -m "Your commit message"
```
Push the changes to your forked repository:
```bash
$ git push origin branch-name
```
### Submit a Pull Request
Head over to the [original repository](https://github.com/ibnaleem/snapscoretracker) on GitHub and go to the ["Pull requests"](https://github.com/ibnaleem/snapscoretracker/pulls) tab.
1. Click on the "New pull request" button.
2. Select your forked repository and the branch containing your changes.
3. Provide a clear and informative title for your pull request, and use the description box to explain the modifications you have made. **_Your pull request will be closed if you do not specify the changes you've made._**
4. Finally, click on the "Create pull request" button to submit your changes.

## [PGP Fingerprint](https://github.com/ibnaleem/ibnaleem/blob/main/public_key.asc)
```
2024 7EC0 23F2 769E 6618  1C0F 581B 4A2A 862B BADE
```

![GitHub Opensource](https://img.shields.io/badge/open%20source-yes-orange) ![GitHub Maintained](https://img.shields.io/badge/maintained-yes-yellow) ![Last Commit](https://img.shields.io/github/last-commit/ibnaleem/snapscoretracker) ![Commit Activity](https://img.shields.io/github/commit-activity/w/ibnaleem/snapscoretracker) ![Issues](https://img.shields.io/github/issues/ibnaleem/snapscoretracker) ![Forks](https://img.shields.io/github/forks/ibnaleem/snapscoretracker)
