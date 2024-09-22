# Book Recommendation System in Python

This book recommendation system is a web app which allows users to select a book they have read and receive suggestions for other books they may like to use.
The system leverages collaborative filtering and clustering to create groups of books that are most likely to be read after each other.

Collaborative filtering is a technique which uses both information about items (in this case books) and users to guess what a user might like. The logic is as follows:
if user A likes book A and user B is similar to user A then user B should like book A also. In this project we use a more simplified version of this, using user ratings of books to create book vectors. Books that are similarly rated will be closer together in this vector space and therefore be recommended if a user likes another book in the same cluster.

Click here to try it out! https://recommendation-system-4f7119a43a05.herokuapp.com/

![image](https://github.com/user-attachments/assets/b322b0a2-197d-47b5-bf75-748e0b37dbeb)
