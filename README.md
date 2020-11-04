# Application-to-support-COVID-19-management

## Details
The requirement for the final project was to develop a real time reporting application
for managing the patient and hospital status in the state of Kentucky. There were specifically
three functions required for the project viz. 1) Application Management Functions (MF1
and MF2), 2) Real Time Reporting functions (RTR1, RTR 2 and RTR3) and 3) Logic and
Operational Functions (OF1, OF 2 and OF3). Our team Team AXY has developed this
real time reporting application as per the requirement set for the project. We have used
Python Programming Language for the application and the choice of Database technology
is OrientDB which is a graph based DBMS.
We chose to go with the OrientDB because since we were looking to implement a
non-traditional database system for our project which required realtime reporting and faster
querying. Given that OrientDB offers working with the studio and vertices/edges, it makes
the patient and hospitals to be represented as vertex and the assignment between them
as edges. Furthermore since it supports key-value store and is a SQL-like query language,
OrientDB also offers simplicity in accessing the database all the while providing the adequacy
for complex applications like this project. In addition to that OrientDB also has full ACID
support along with concurrency and durability and furthermore its Python API pyorient is
much easier to implement.
We used two parallel processes using multiprocessing library viz. 1) rabbit process
that continuously listens to the patient record data that is being fed to the server; 2) sending
process is for the webserver and apis that provide the RTR and stores them to database and
it also includes the RealTime process that continuously updates the database system and
checks for the alerts based on the growth of number of cases according to zipcodes.

## Final Comments
After testing our application using the apis, we found that the application we have
developed, is performing very efficiently and elegant in handling and managing the flow of
patient data in real time. This could offer the solutions to assist in both the reporting
and management of healthcare in relation to the COVID-19 pandemic. Our application
also provides real-time reporting and alerting of case growth on zipcode basis and also
develops the statewide alert if at least five zipcodes are in alert state. In addition to that the
application also offers logic to route patients to appropriate facilities using proper apis, if
warranted, or determine if they should stay at home. It also provides methods to report on
both individual patient information and provides up-to-date information on hospital status,
such as available beds.
