## Steps to set up the project:

### Step 1:
Go to the directory in which you want to clone the project.

```console
cd path\to\your\directory
```

### Step 2:
Clone the github repository to the directory.

```console
git clone https://github.com/MaharajaAlex/cli.git
```

### Step 3:
Change directory to the github repository.

```console
cd cli
```

### Step 4:
Open VS Code in that location.

### Step 5:
Activate the virtual environment.

```console
virtualenv\Scripts\Activate.ps1
```

### Step 6:
Install necessary python modules and packages.

```console
pip install -r requirements.txt
```

### Step 7:
Edit files as necessary. Do no change anything in `virtualenv` directory.

### Step 8:
After you have completed making all changes, open up terminal and make sure you are in the `cli` directory and the `virtualenv` is activated.

### Step 9:
Make new branch.

```console
git checkout -b very-short-name-specifying-change-in-brief
```

### Step 10:
Add and Commit your changes.

```console
git add .
git commit -m "Some message briefly explaining your changes"
```

### Step 11:
Push your changes to your repository.

```console
git push origin very-short-name-specifying-change-in-brief #basically the branch you created in step 9
```

### Step 12:
Go to the link provided by the terminal and create a pull reauest and wait for someone to approve it.
