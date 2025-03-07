## **VicBank - A Simple Banking System 🏦**  

### **📌 Overview**  
VicBank is a Python-based banking system that provides users with secure account management, transactions, and a user-friendly interface. The system allows users to:  
✅ Create and manage accounts  
✅ Deposit, withdraw, and transfer funds  
✅ Store user details in a JSON database  
✅ Implement unique ID and transaction PIN for security  


### **🚀 Features**  
🔹 **User Authentication** - Users must enter a unique ID and PIN to access their accounts.  
🔹 **Account Management** - Create and store account details in a JSON database.  
🔹 **Transactions** - Perform deposits, withdrawals, and transfers.  
🔹 **Error Handling** - Ensures smooth operation with input validation.  
🔹 **Secure Data Storage** - Stores user information in a JSON file.  

---

### **🛠️ Installation & Setup**  
1️⃣ **Clone the Repository:**  
bash
git clone https://github.com/Vic-Godwin/vicbank.git
cd vicbank

  
2️⃣ **Run the Program:**  
bash
python vicbank.py



### **📂 Project Structure**  

vicbank/
│── vicbank.py           # Main banking system script
│── vicbank_module.py    # Contains reusable banking functions
│── vicbank_database.json # Stores user data
│── README.md            # Project documentation


### **💡 Usage Guide**  
1️⃣ **Start the program** and enter your unique ID.  
2️⃣ **Authenticate with your transaction PIN.**  
3️⃣ Choose an action:  
   - 📥 Deposit  
   - 📤 Withdraw  
   - 🔄 Transfer funds  
   - 📑 View account details  


### **📝 Example Code Snippet**
```python
for account_detail in user_info:
    special_code = input("Please Enter unique ID to proceed: ")
    if special_code == account_detail['Unique ID']:
        print(f"Welcome {account_detail['name']}\n")
        break


### **🔧 Future Improvements**  
🚀 Implement a **Graphical User Interface (GUI)**  
🚀 Add **Automated Email/SMS Alerts**  
🚀 Introduce **Interest & Loan Features**  


### **📜 License**  
This project is open-source and available under the **MIT License**.  


### **💬 Contributions & Support**  
Feel free to contribute! Fork the repository, submit pull requests, or suggest improvements.  

For any issues, contact:  
📧 Email: vicgodwin95@gmail.com  
📌 GitHub Issues: [VicBank Issues](https://github.com/Vic-Godwin/vicbank/issues) 
