# 🐍 Day 10 – Maximum Subarray

## 📌 Overview

Day 10 focuses on the Maximum Subarray problem and introduces Kadane's Algorithm.

The goal is to find the contiguous subarray with the largest possible sum.

## 🎯 Problem Statement

Given an array of integers, find:

- The maximum possible subarray sum
- The subarray that produces that sum
- The starting index
- The ending index

## 💡 Example

Input:

[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Maximum subarray:

[4, -1, 2, 1]

Maximum sum:

6

Because:

4 + (-1) + 2 + 1 = 6

## 🧠 Kadane's Algorithm

The algorithm maintains a running sum called `current_sum`.

For every element, it decides whether to:

1. Continue the existing subarray
2. Start a new subarray

The algorithm also maintains `max_sum`, which stores the largest sum found so far.

## ⚡ Complexity

### Kadane's Algorithm

Time Complexity:

O(n)

Space Complexity:

O(1)

The array itself is provided as input, while only a few additional variables are used for processing.

## 🌍 Real-World Applications

Maximum subarray techniques can be useful when searching for the best continuous period in a sequence of data.

Examples include:

### Financial Analytics

Finding a continuous period with the highest cumulative gain or return.

### Website Analytics

Finding a continuous period with unusually high user activity.

### Sales Analytics

Finding the strongest consecutive period of sales performance.

### System Monitoring

Finding a continuous period where a performance metric shows the largest cumulative change.

## 🛠️ Technologies

- Python 3
- VS Code
- Git
- GitHub

## 📂 Project Structure

Day10-Maximum-Subarray/
│
├── day10_max_subarray.py
└── README.md

## 🚀 How to Run

Open the project in VS Code.

Run:

python day10_max_subarray.py

Example:

-2 1 -3 4 -1 2 1 -5 4

## 📤 GitHub Submission

git add day10_max_subarray.py README.md

git commit -m "Complete Day 10 maximum subarray"

git push

## 👨‍💻 Author

Akash

---

🐍 Python Mastery Sprint – Day 10
