1. **How do HTTP applications preserve the state of an application across multiple request-response cycles, especially concerning user authentication and session management.**

   HTTP is inherently stateless, meaning each request-response cycle is independent and the server retains no memory of previous interactions. To preserve application state across multiple requests, especially for user authentication and session management, web applications employ several mechanisms. 

   The primary technique is using cookies , which are small pieces of data stored in the user's browser and sent with every subsequent request to the same server. However, storing sensitive information directly in cookies poses security risks, so modern applications use session management. In this approach, the server generates a unique session identifier (session ID) stored in a cookie on the client side, while the actual session data—such as user authentication status, preferences, and temporary data—is stored securely on the server side, typically in a database or in-memory cache.  
     
   Django implements this through its built-in session framework. When a user logs in, Django creates a session, stores the session data in the database (by default), and sends a session ID cookie to the browser. On subsequent requests, Django reads the session ID from the cookie, retrieves the corresponding session data from the database, and makes it available to the application. This allows the application to "remember" the user across multiple page visits without exposing sensitive information.  
     
    Alternative approaches include token-based authentication (such as JWT \- JSON Web Tokens), commonly used in REST APIs, where encrypted tokens containing user information are sent with each request, eliminating the need for server-side session storage.  
     
2. **Investigate and document the procedures for performing Django database migrations to a server-based relational database like MariaDB.**  
     
   Migrating a Django application from SQLite to a server-based relational database like MariaDB involves several key steps to ensure data integrity and proper configuration. First, MariaDB must be installed on the server, and a dedicated database and user account should be created with appropriate privileges.   
     
   The command \`CREATE DATABASE myproject CHARACTER SET utf8mb4 COLLATE utf8mb4\_unicode\_ci;\` ensures proper character encoding for international text support. Second, the Python MySQL client library must be installed. Django requires either mysqlclient (recommended) or PyMySQL. This is installed via pip: pip install mysqlclient. On some systems, MySQL development headers may need to be installed first (e.g., sudo apt-get install python3-dev libmysqlclient-dev on Ubuntu). Third, Django's settings.py must be updated to configure the new database connection.  
   The \`DATABASES\` setting should be changed from SQLite configuration to: \`\`\`python DATABASES \= { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'database\_name', 'USER': 'database\_user', 'PASSWORD': 'secure\_password', 'HOST': 'localhost', 'PORT': '3306', } } \`\`\`   
     
   Finally, Django migrations are applied to create the database schema using python manage.py migrate. If migrating existing data, it should be dumped from SQLite using python manage.py dumpdata \> data.json, then loaded into MariaDB with python manage.py loaddata data.json after running migrations. This process ensures all tables, relationships, and data are properly transferred to the production database.  
     
   References  
     
1. Django Software Foundation (2025) \*Sessions\*. Django Documentation. Available at: https://docs.djangoproject.com/en/5.1/topics/http/sessions/ (Accessed: 30 January 2026).  
2. Django Software Foundation (2025) \*Databases\*. Django Documentation. Available at: https://docs.djangoproject.com/en/5.1/ref/databases/ (Accessed: 30 January 2026).  
3. MariaDB Foundation (2025) \*Getting Started with MariaDB\*. MariaDB Knowledge Base. Available at: https://mariadb.com/kb/en/getting-started-with-mariadb/ (Accessed: 31 January 2026).  
4. Myers, B. (2024) \*Understanding Sessions and Cookies\*. Real Python. Available at: https://realpython.com/django-sessions/ (Accessed: 31 January 2026).