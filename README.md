## Quality Development starter pack

This repository has been created to give a python template project which includes pytest instructions.

### Install requirements

Use pip or pip3 to install the dev requirements for the software testing:

```bash
pip install -r requirements_dev.txt
```

### 1️⃣ How to start

Fork this repository and clone your fork into your machine using:
```bash
git clone git@github.com:USERNAME/qd-starter-pack.git
```

enter to your project directory using:
```bash
cd qd-starter-pack
```

---

### 2️⃣ How to make a branch

To create a new `branch` from the main repository and work on a specific exercise (ex. `ex1.py`) you can use the following commands:
```bash
git checkout main

git checkout -b new-branch-name
```

---

### 3️⃣ How to make a commit

From this step you can edit your `ex1.py` and make some commits using:
```bash
git add exercises/ex1.py

git commit -m 'feat: description'
```
Use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) when you write a commit description.

---

### 4️⃣ How to make a PR

Push the commits into GitHub using:
```bash
git push -u origin new-branch-name
```

Afterward, it is possible to create a Pull Request by going to your fork `https://github.com/USERNAME/git-course-exercises.git` clicking on "create Pull Request" or going to the right section "Pull Request" -> "New Pull Request".

If you want to work on another `ex1.py`, go to step 2️⃣.

---

Use git wisely.


<!-- ### Software Testing

How to run properly the tests with the related html report:

```bash
$ pytest --cov src tests/ --cov-report=html
``` -->

### Clean code
Check [this article](https://testdriven.io/blog/clean-code-python/) to understand how to write "clean code" in python.

### Contributing

Feel free to improve this README with any other detail, if you do it, I'll be grateful.
