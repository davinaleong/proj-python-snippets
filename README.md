# 🐍 Python Code Snippets Collection

This repository contains assorted Python code snippets, projects, and notebooks for learning, experimentation, and sharing.

## 📦 Setup Instructions

Follow these steps to set up your local environment using **Anaconda** and **Jupyter Notebook**.

---

### 1️⃣ Install Anaconda

✅ Download Anaconda from the official website:
[https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

✅ Follow the installer instructions for your operating system (Windows, macOS, Linux).

✅ Confirm installation by running:

```bash
conda --version
```

---

### 2️⃣ Create a Conda Environment

✅ Open **Anaconda Prompt** (or your terminal) and create a new environment:

```bash
conda create --name python-snippets python=3.11
```

✅ Activate the environment:

```bash
conda activate python-snippets
```

---

### 3️⃣ Install Jupyter Notebook

✅ Inside the activated environment, install Jupyter:

```bash
conda install jupyter
```

---

### 4️⃣ Run Jupyter Notebook

✅ Launch Jupyter Notebook in the project folder:

```bash
jupyter notebook
```

✅ A browser window should open. You can now run or create `.ipynb` notebooks from this repo.

---

### 📂 Repo Structure

```
/python-snippets/
├── notebooks/
│   └── example.ipynb
├── scripts/
│   └── example.py
└── README.md
```

---

### 💡 Tips

- Use `conda deactivate` to exit the environment.
- Update packages with `conda update --all`.
- Share your environment setup using:

```bash
conda env export > environment.yml
```

and restore it with:

```bash
conda env create -f environment.yml
```
