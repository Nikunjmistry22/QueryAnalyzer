# QueryAnalyzer

QueryAnalyzer is a GUI that is used to analyze your query in graph format. It is basically used to understand what is going on in the backend when you run a postgresql query. This helps us to get a better understanding of whether the query is optimized or not.

Requirements for this GUI are:
1. You should have a PostgreSQL database.
2. You should have Python 3.6+ version installed.

Steps to use the GUI:
1. Fill in the data: hostname, username, database, and password for connection.
2. Write your query in the query input box. If your query is correct syntax-wise, and the table/columns names are appropriate and present in your database, this will generate a graph about all the scans/execution/buckets/execution time/planning time.
3. The graph is developed with the help of NetworkX and Matplotlib.pyplot with GUI interface Tkinter.

To see the implementation video, click on the following link:
[Video Link](https://drive.google.com/file/d/1FdfWVQdcd-N4ul-0o9QhFNNe5Mb03m11/view?usp=sharing)

To download the GUI app, click on the following link:
[Google Drive](https://drive.google.com/file/d/1wp1i-zIHn44rGZmNCrkxLDFZ9f4u_qd6/view?usp=sharing) or use <a href="https://minhaskamal.github.io/DownGit/#/home">DownGit</a> to download QueryAnalyzer.exe from the dist folder of this GitHub repo.
