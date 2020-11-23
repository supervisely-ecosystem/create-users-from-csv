<div align="center" markdown>

<img src="https://i.imgur.com/I3gDQn7.png"/>

# Create Users from CSV

<p align="center">

  <a href="#Overview">Overview</a> •
  <a href="#Preparation">Preparation</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a>
</p>

[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/remote-import)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/remote-import&counter=runs&label=runs&123)](https://supervise.ly)

</div>

## Overview

App creates users using public API and available only for admin users and users with admin permission.


## Preparation

1. Create a `.csv` file with usernames and passwords
2. `.csv` file must contain only 2 columns: user and password, all elements must be separated with `,`
3. Here's an example of how your `.csv` file should look like:
```
user,password
user1, 123aaa
user2, 321bbb
user3, 777ccc
user4, 444ttt
user5, 555555
```

4. Drag and drop this file into your supervisely team files
<img src="https://i.imgur.com/mgzaJTu.giff"/>

## How To Run 
**Step 1**: Add app to your team from Ecosystem if it is not there.

**Step 2**: Go to `Plugins & Apps` section in current team. And press `Get` button in front of application.

**Step 3**: Application will be added to `Current Team`->`PLugins & Apps` page.

**Step 4**: Go to `Current Team`->`Files` page, right-click on your .csv file and choose `Run App`->`Create users from CSV`.

**Step 5**: Click `Run` in the pop up menu.

**Note**: App shuts down automatically on finish. Or you can stop it manually from app settings page.
