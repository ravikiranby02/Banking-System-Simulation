````markdown
# 📘 Student Report Card Generator

The **Student Report Card Generator** is a Python-based console application that helps manage students, their marks, and report cards. It is designed to simulate a simple school system for generating student performance reports.

---

## ✨ Features
- ➕ **Add Student Details** (Roll number, name, subjects, and marks)  
- 📄 **Generate Report Cards** for individual students or all students  
  - Shows marks for each subject  
  - Calculates average percentage  
  - Displays pass/fail status  
  - Assigns grade based on performance  
- 🏫 **Classroom Management**  
  - View all students in a class  
  - Calculate overall class average  
- ❌ Handles invalid inputs gracefully  

---

## 🛠️ How It Works
1. Run the program.  
2. Enter your classroom grade and section.  
3. Choose from the menu options:  
   - Add student details with marks for each subject.  
   - Generate report cards for students.  
   - View class list and class average.  
   - Exit the program.  

---

## 📊 Grading System
| Percentage | Grade |
|------------|-------|
| 90+        | A     |
| 80–89      | B+    |
| 70–79      | B     |
| 50–69      | C     |
| Below 50   | D     |

✅ A student **passes** if all subject marks are ≥ 35.

---

## 🚀 How to Run
1. Make sure you have **Python 3** installed.  
2. Save the script as `report_card.py`.  
3. Run in terminal or command prompt:
   ```bash
   python report_card.py
````

---

## 📌 Example

```
--- Student Report Card System ---
1. Add Student
2. Show Report Cards
3. ClassRoom
4. Exit
Enter your choice: 1
Enter Roll No: 1
Enter Name: Ravi
Enter subject name (or 'done' to finish): Math
Enter marks for Math: 85
Enter subject name (or 'done' to finish): Science
Enter marks for Science: 90
Enter subject name (or 'done' to finish): done
✅ Student Ravi added successfully.
```

---

## 🎯 Future Improvements

* Export report cards to **PDF/CSV**
* Add **student deletion** feature
* Store data in a **database** or file system
* Support for **multiple classrooms**

---

## 🧑‍💻 Author

👉 Do you also want me to add **badges** (like Python version, project status, etc.) at the top of the README to make it look more professional for GitHub?
```
