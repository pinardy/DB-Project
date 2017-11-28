import MySQLdb as mdb

con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")


with con:
    cur = con.cursor()

    #============= INSERT data ==============#

    insertBook = "INSERT INTO book (title, cover_format, num_pages, authors, publisher, year_publish, edition, ISBN10, ISBN13)" \
                 "VALUES " \
                 "('Database Management Systems: Evolution and Interoperation','hardcover',272,'Bhavani Thuraisingham'" \
                 ",'CRC Press',1997,1,'0849394937','9780849394935')," \
                 "('Database Management Systems: Design, Implementation, & Management','hardcover',784,'Carlos Coronel, Steven Morris'" \
                 ",'Course Technology',2014,11,'1285196147','9781285196145')," \
                 "('Database Management Systems: A Practical Approach to Design, Implementation, and Management (6th Edition)','hardcover',784,'Thomas Connolly, Carolyn Begg'" \
                 ",'Pearson',2014,6,'0132943263','9780132943260')," \
                 "('Database Management Systems: Design, Implementation, & Management','hardcover',791,'Carlos Coronel, Steven Morris'" \
                 ",'Course Technology',2016,12,'1305627482','9781305627482')," \
                 "('Database Design and Relational Theory: Normal Forms and All That Jazz (Theory in Practice)','hardcover',278,'C.J.Date'" \
                 ",'O Reilly Media',2012,1,'1449328016','9781449328016');"

    insertInventory = "INSERT INTO inventory (ISBN13, no_copies)" \
                      "VALUES " \
                      "('9780849394935',4)," \
                      "('9781285196145',3)," \
                      "('9780132943260',5)," \
                      "('9781305627482',10)," \
                      "('9781449328016',0);"

    insertPurchaseHistory = "INSERT INTO purchase_history (purchase_id, user_id, ISBN13, no_copies, order_date)" \
                            "VALUES " \
                            "(1, 1, '9780849394935', 1, '2017-11-24')," \
                            "(2, 1, '9781285196145', 1, '2017-11-24')," \
                            "(3, 1, '9780132943260', 1, '2017-11-24')," \
                            "(4, 2, '9781305627482', 1, '2017-11-24')," \
                            "(5, 3, '9780132943260', 1, '2017-11-24');"

    insertFeedback = ""

    insertRating = ""

    # Execution of cursor objects for schema
    try:
        cur.execute(insertBook)
        print("Inserted into book")
    except:
        pass

    try:
        cur.execute(insertInventory)
        print("Inserted into inventory")
    except:
        pass

    try:
        cur.execute(insertPurchaseHistory)
        print("Inserted into purchase_history")
    except:
        pass


    print("--- Execution of SQL successful ---")