### Library

Library Management System

### DOCUMENTATION ------------------

### 1. Book Management

A custom DocType - Book allows performing CRUD operations with the required fields as shown below.
![Book](book.png)
The system automatically tracks available stock of books based on number of books issued currently and validates that the total quantity of books 
must not be lower than books currently issued as shown below.
![Transaction 1](transaction1.png)
![Updated Qty](updatedqty.png)
![Qty Error](qtyerror.png)

### 2. Members Management

A custom DocType - Member allows performing CRUD operations with the required fields as shown below.
![Member](member.png)
Validation for outstanding debt to be not more than 500
![Max Debt](maxdebt.png)

### 3. Transactions Management

A custom DocType - Transaction allows members to issue and return books as shown below.
![Transaction](transaction.png)
It auto-updates book stocks as shown earlier and performs various validations like -

Insufficient quantity 
![Insufficient Qty](insufficientqty.png)
Book not issued before return
![Not Issued](notissued.png)

Rent fees is charged per day that the book is issued by using a daily scheduled job. Daily rent is set in a single DocType as shown below.
![Daily Rent](dailyrent.png)
The scheduler checks all books that are currently issued and not yet returned and updates the outstanding debt of the corresponding members
daily. Below is the scheduler log for this function.
![Scheduler](scheduler.png)
After succesful run, outstanding debt of members is updated as shown below.
![New Debt](newdebt.png)

### 4. Search Functionality

The system allows searching for books by title or author name as shown below
![Search One](search1.png)
![Search Two](search2.png)
![Search Three](search3.png)

### 5. Data Import Integration

A custom API endpoint allows importing book data in bulk without any page limits as shown below.
![API Call](apicall.png)
The above api call results in 30 records of the following data being imported into the Book DocType
![Imported](imported.png)
