# SQL_CaseStudy_Paintings_Projects.
## About Dataset
### This project aims to explore the SQL Case Study Paintings to understand and analyze the datasets. SQL Case study dataset obtained from <u>(https://www.kaggle.com/datasets/mexwell/famous-paintings)</u> and then upload it to a PostgreSQL database using Python. 
### There were 8 tables namely artist, canvas_size, image_link, museum_hours, museum, product_size, subject, work. We use a simple Python script to upload data from CSV files to PostgreSQL database tables. We then use SQL queries to answer over 20 problems related to the famous paintings dataset and then practice basic to intermediate SQL problems.

## Code
### Python script for loading dataset into database.
See load_files.py file
### Objective
 The objective of this project are as follows:
1)To understand the popular painting styles used by artists
 2) Which artist has the most number of paintings placed in different museums all over the world.
 3) Analyse the working hours of museums
 4)To know the popular museums based on the number of paintings they hold.
 5) To understand the various canvas size most artist use and their cost.
 6) To know the top artist based on the sales price of their paintings

## $ To achieve the above objective following questions have to be answered:
 1) Fetch all the paintings which are not displayed on any museums?
 2) Are there museums without any paintings?
 3) How many paintings have an asking price of more than their regular price? 
 4) Identify the paintings whose asking price is less than 50% of its regular price
 5) Which canvas size costs the most?
 6) Delete duplicate records from work, product_size, subject and image_link tables
 7) Identify the museums with invalid city information in the given dataset
 8) Museum_Hours table has 1 invalid entry. Identify it and remove it.
 9) Fetch the top 10 most famous painting subject
 10) Identify the museums which are open on both Sunday and Monday. Display museum name, city.
 11) How many museums are open every single day?
 12) Which are the top 5 most popular museum? (Popularity is defined based on most no of paintings in a museum)
 13) Who are the top 5 most popular artist? (Popularity is defined based on most no of paintings done by an artist)
 14) Display the 3 least popular canva sizes
 15) Which museum is open for the longest during a day. Dispay museum name, state and hours open and which day?
 16) Which museum has the most no of most popular painting style?
 17) Identify the artists whose paintings are displayed in multiple countries
 18) Display the country and the city with most no of museums. Output 2 seperate columns to mention the city and country. If there are multiple value, seperate them with comma.
 19) Identify the artist and the museum where the most expensive and least expensive painting is placed. Display the artist name, sale_price, painting name, museum name, museum city and canvas label
 20) Which country has the 5th highest no of paintings?
 21) Which are the 3 most popular and 3 least popular painting styles?
 22) Which artist has the most no of Portraits paintings outside USA?. Display artist name, no of paintings and the artist nationality.

### Database Design
![image](https://github.com/user-attachments/assets/0aa56756-647c-4a5d-942d-a98571d73dc2)
 
 I would like to thank @TechTFQ for the guidance.


